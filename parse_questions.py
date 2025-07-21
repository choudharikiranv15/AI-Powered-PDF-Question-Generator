import json
import re
import os

# --- SETUP ---
RAW_JSON_FILE = "page_content_with_coords.json"
FINAL_JSON_FILE = "questions_final.json"

# --- HELPER FUNCTION FOR COORDINATE MATCHING ---


def find_closest_image(question_bbox, image_list):
    """
    Finds the best image for a question based on vertical proximity.
    It looks for an image that is below the question text and closest to it.
    """
    q_x0, q_y0, q_x1, q_y1 = question_bbox
    best_image = None
    min_distance = float('inf')

    for image in image_list:
        img_x0, img_y0, img_x1, img_y1 = image['bbox']
        # Ensure the image is roughly below the question text
        if img_y0 > q_y0:
            vertical_distance = img_y0 - q_y1  # Distance from bottom of text to top of image
            if 0 <= vertical_distance < min_distance:
                min_distance = vertical_distance
                best_image = image['path']

    return best_image


# --- MAIN PARSING LOGIC ---
try:
    with open(RAW_JSON_FILE, 'r') as f:
        all_pages_data = json.load(f)

    all_questions = []

    print("Starting intelligent parsing using coordinates...")

    for page_data in all_pages_data:
        text_blocks = page_data["text_blocks"]
        page_images = page_data["images"]
        full_page_text = "".join([block[4] for block in text_blocks])

        # Find all question starting points
        question_starts = list(re.finditer(
            r'(^|\n)(\d{1,2}\.\s)', full_page_text))

        if not question_starts:
            continue

        for i, start_match in enumerate(question_starts):
            question_number = int(
                start_match.group(2).replace('.', '').strip())

            # Find the text block that contains this question number
            start_char_index = start_match.start()
            current_char_count = 0
            question_bbox = None
            for block in text_blocks:
                if current_char_count <= start_char_index < current_char_count + len(block[4]):
                    question_bbox = block[:4]
                    break
                current_char_count += len(block[4])

            if not question_bbox:
                continue

            # Define the text block for the current question
            start_index = start_match.end()
            end_index = question_starts[i+1].start() if i + \
                1 < len(question_starts) else len(full_page_text)
            question_content = full_page_text[start_index:end_index]

            # --- Extract Components ---
            question_text = question_content.strip().split('\n')[0]
            options_raw = re.findall(
                r'\[([A-D])\]\s*([^\n]*)', question_content)
            options = {opt[0]: opt[1].strip() for opt in options_raw}
            answer_match = re.search(r'Ans\s*\[([A-D])\]', question_content)
            answer = answer_match.group(1) if answer_match else "Not Found"

            # Use our new function to find the correct image
            closest_image = find_closest_image(question_bbox, page_images)

            # --- Assemble the final JSON object ---
            structured_question = {
                "question_number": question_number,
                "question_text": question_text,
                "images": [closest_image] if closest_image else [],
                "options": options,
                "option_images": {},  # This logic can be enhanced further if needed
                "answer": answer
            }
            all_questions.append(structured_question)
            print(
                f"  - Parsed Question #{question_number} and linked images by location.")

    all_questions.sort(key=lambda q: q['question_number'])

    with open(FINAL_JSON_FILE, 'w') as f:
        json.dump(all_questions, f, indent=4)

    print(
        f"\nSuccess! Final structured file '{FINAL_JSON_FILE}' created with accurate image links.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
