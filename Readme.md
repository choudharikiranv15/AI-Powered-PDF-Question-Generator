AI-Powered PDF Question Generator
Problem Statement
Educators and content creators often face the challenge of generating a large volume of practice questions from existing materials, such as educational PDFs. Manually creating new and varied questions from a static document is a time-consuming and repetitive task. This project aims to solve that problem by providing an intelligent tool that automates the question generation process, leveraging modern AI to create fresh, relevant questions from PDF content.

Project Overview
This project is a web-based application that analyzes educational PDF documents and uses a multimodal AI to generate new questions based on the document's content. The tool allows a user to upload a PDF, target a specific question number, and receive a new, AI-generated question based on the visual context of the page where the original question appears.

The final implementation is a single, self-contained index.html file that leverages modern web technologies to provide a seamless user experience directly in the browser. This approach bypasses the complexities and common errors associated with server-side PDF content extraction.

Key Features
Direct PDF Upload: Users can upload PDF files directly in the browser.

Intelligent Page Analysis: The application automatically finds the correct page associated with a user-specified question number.

AI-Powered Generation: It uses the Google Gemini 1.5 Flash model to understand the visual context of a PDF page and generate a new, relevant question.

Self-Contained & Serverless: The entire application runs in a single HTML file, requiring no backend or server setup.

Technologies Used
Frontend: HTML5, Tailwind CSS

JavaScript Libraries:

PDF.js (by Mozilla): For rendering PDF documents and their pages into images directly in the browser.

Google Gemini API (via fetch): To send page images and prompts to the gemini-1.5-flash model for analysis and question generation.

AI Model: Google Gemini 1.5 Flash

How It Works
The application follows a robust, modern workflow to ensure reliability and accuracy:

PDF Loading: The user uploads a PDF file and provides a Google AI API Key.

Page Identification: When the user enters a question number, the application uses PDF.js to search through the text content of each page to find which page that question is on.

Page-to-Image Rendering: Instead of trying to extract individual, often problematic, image and text objects, the application renders the entire identified page into a high-quality PNG image.

AI-Powered Analysis: This single page image is sent to the Gemini API along with a carefully crafted prompt. The prompt instructs the AI to locate the specified question number on the page image and generate a new question based on its context.

Display Results: The application displays both the original page image and the newly generated question, providing a complete and context-rich experience for the user.

This approach is highly effective because it delegates the complex task of parsing the visual layout to the powerful multimodal AI, solving the errors related to direct content extraction.

How to Run the Application
To run this project, you only need a modern web browser and the final HTML file.

Save the Code: Save the final application code as a single HTML file (e.g., index.html).

Get an API Key:

Go to Google AI Studio.

Create a new project and generate an API key.

Open the Application: Open the index.html file in a web browser (like Google Chrome, Firefox, or Edge).

Use the Interface:

Click "Choose File" to upload a PDF document.

Paste your Google AI API Key into the input field.

Enter a question number from the PDF into the designated field.

Click the "Generate with AI" button.

View the Result: The application will process the request and display the original PDF page and the newly generated question side-by-side.

![Alt Text](D:\kiran\Web developement\Task\Testline\assets\Screenshot 2025-07-21 200957.png)
![Alt Text](D:\kiran\Web developement\Task\Testline\assets\Screenshot 2025-07-21 201020.png)
![Alt Text](D:\kiran\Web developement\Task\Testline\assets\Screenshot 2025-07-21 201101.png)
![Alt Text](assets\Screenshot 2025-07-21 201122.png)
