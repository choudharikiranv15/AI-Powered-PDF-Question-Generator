import google.generativeai as genai
import json
from PIL import Image
import os

# --- SETUP ---
# IMPORTANT: Replace with your actual API key
API_KEY = "AIzaSyBCaZkrTX_b2m73KFKD3LDjnf2hXoEF0iU"
STRUCTURED_JSON_FILE = "questions_final.json"
# Let's try Q19 (the trees) or 5 (bananas)
TARGET_QUESTION_NUMBER = int(input("Enter the question number: "))

# Configure the generative AI model
try:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    print(f"Error configuring AI model. Is your API Key correct? Error: {e}")
    exit()

# --- DATA LOADING ---
try:
    with open(STRUCTURED_JSON_FILE, 'r') as f:
        questions = json.load(f)
except FileNotFoundError:
    print(
        f"Error: The file '{STRUCTURED_JSON_FILE}' was not found. Did you run 'parse_questions.py' first?")
    exit()

# Find the target question from our JSON data
target_question = next(
    (q for q in questions if q['question_number'] == TARGET_QUESTION_NUMBER), None)

if not target_question:
    print(
        f"Error: Question #{TARGET_QUESTION_NUMBER} not found in the JSON file.")
    exit()

# --- IMPROVED IMAGE FINDING LOGIC ---
image_path = None
# Prioritize primary images first
if target_question.get("images"):
    image_path = target_question["images"][0]
# If no primary images, check for option images and grab the first one
elif target_question.get("option_images"):
    image_path = list(target_question["option_images"].values())[0]

if not image_path:
    print(
        f"Error: Question #{TARGET_QUESTION_NUMBER} does not have any associated image to analyze.")
    exit()

original_question = target_question['question_text']

print(
    f"Found target question #{TARGET_QUESTION_NUMBER}: '{original_question}'")
print(f"Using image: {image_path}")

try:
    img = Image.open(image_path)
except FileNotFoundError:
    print(f"Error: Image file not found at '{image_path}'")
    exit()

# The prompt tells the AI what to do.
prompt = f"""
You are an expert in creating educational material for 1st-grade students.
Based on the provided image, your task is to generate a new math question.

The original question for this image was: '{original_question}'

Create a completely new question that is different from the original but uses the same image. The question must be suitable for a 1st grader.
"""

# --- GENERATE NEW QUESTION ---
print("\nAsking the AI to generate a new question... 🤖")

try:
    response = model.generate_content([prompt, img])
    print("\n✅ AI-Generated Question:")
    print("---------------------------------")
    print(response.text)
    print("---------------------------------")

except Exception as e:
    print(f"\nAn error occurred while calling the AI model: {e}")
