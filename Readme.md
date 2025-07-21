# 📘 AI-Powered PDF Question Generator

## 🧠 Problem Statement

Educators and content creators often struggle to generate large volumes of practice questions from existing educational PDFs. Manually crafting these questions is time-consuming and repetitive.

This project aims to solve that problem by providing a **smart, AI-powered tool** that can automatically generate new, relevant questions based on the visual content of any given PDF page.

---

## 🚀 Project Overview

The **AI-Powered PDF Question Generator** is a **fully client-side, browser-based tool** that lets users:

- Upload an educational PDF.
- Enter a question number.
- Automatically generate a fresh AI-powered question based on that page's context.

The tool uses **Google Gemini 1.5 Flash**, a multimodal AI model, to analyze the **visual content of the page**, not just the text — solving the common problem of unreliable content extraction from PDFs.

---

## 🧩 Key Features

✅ Direct PDF upload in the browser  
✅ Automatically finds the page based on question number  
✅ AI-generated questions from full page image context  
✅ No server, backend, or deployment needed — works from a single HTML file  
✅ Uses PDF.js to render pages and Google Gemini for question generation

---

## 🛠️ Technologies Used

| Tech / Library              | Purpose                                                   |
| --------------------------- | --------------------------------------------------------- |
| **HTML5**, **Tailwind CSS** | Responsive, modern UI                                     |
| **JavaScript**              | Frontend logic and interactions                           |
| **PDF.js** (by Mozilla)     | PDF parsing and page rendering to image in-browser        |
| **Google Gemini 1.5 Flash** | Multimodal AI for image understanding and text generation |
| **fetch API**               | Communicate with Gemini API from browser                  |

---

## 🔄 How It Works

1. **Upload PDF**: User selects a PDF file from their device.
2. **Enter API Key**: User enters their Google Gemini API key.
3. **Locate Question Page**: The app finds which page contains the entered question number.
4. **Render Page Image**: That page is rendered into a high-quality PNG using PDF.js.
5. **AI Prompting**: The image is sent to Gemini with a custom prompt asking it to generate a new question.
6. **Display Result**: The original page and the new question are shown side-by-side.

> ✅ This process offloads complex parsing to Gemini AI, ensuring reliable, visually-aware results.

---

## 🧪 How to Run the Application

> 🖥️ **Requirements**: Any modern web browser (Chrome, Firefox, Edge)

1. **Download/Clone Repo**:  
   Clone or download this repository.

2. **Open the App**:  
   Open `index.html` in your browser.

3. **Generate API Key**:

   - Visit [Google AI Studio](https://makersuite.google.com/app)
   - Create a new project and get your **Gemini API Key**

4. **Use the Tool**:

   - Upload a PDF.
   - Paste your Gemini API key.
   - Enter a question number (e.g., `Q15`).
   - Click **"Generate with AI"**.

5. **View Output**:
   - You'll see the original page and a newly generated AI question based on its context.

---

## 📸 Screenshots

> _Screenshots of the application in action:_

### 🖼️ Interface Overview

![Interface Overview](assets/Screenshot%202025-07-21%20200957.png)

### 🔑 API Key and Upload

![API Key Input](assets/Screenshot%202025-07-21%20201020.png)

### 🔍 Page Detection

![Page Detection](assets/Screenshot%202025-07-21%20201101.png)

### 🧠 AI-Generated Question

![Generated Question](assets/Screenshot%202025-07-21%20201122.png)

---

## 📌 Final Notes

- This is a **100% frontend-only** solution — perfect for educators, creators, or students who want quick, AI-enhanced question generation without setup.
- Future upgrades may include export to DOCX/PDF, MCQ formatting, or image-based question generation across multiple pages.

---

## 📩 Feedback & Contributions

Contributions and suggestions are welcome!  
Feel free to submit an issue or open a pull request to enhance this tool.

---
