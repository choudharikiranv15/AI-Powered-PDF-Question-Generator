import fitz  # PyMuPDF
import os
import json

# --- SETUP ---
PDF_FILE = "IMO class 1 Maths Olympiad Sample Paper 1 for the year 2024-25.pdf"
IMAGE_OUTPUT_DIR = "extracted_images"
JSON_OUTPUT_FILE = "page_content_with_coords.json"

# Clean up old files
if os.path.exists(JSON_OUTPUT_FILE):
    os.remove(JSON_OUTPUT_FILE)
if not os.path.exists(IMAGE_OUTPUT_DIR):
    os.makedirs(IMAGE_OUTPUT_DIR)

# --- PDF PROCESSING with COORDINATES ---
try:
    doc = fitz.open(PDF_FILE)
    all_pages_data = []
    print(f"Starting advanced extraction from '{PDF_FILE}'...")

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)

        # 1. Text Extraction with coordinates
        # get_text("blocks") gives text chunks with their bounding boxes
        text_blocks = page.get_text("blocks")

        # 2. Image Extraction with coordinates
        page_images = []
        for img_index, img in enumerate(page.get_images(full=True)):
            xref = img[0]
            # Get the bounding box of the image
            rect = page.get_image_bbox(img)

            # Use get_pixmap for potentially better quality
            pix = fitz.Pixmap(doc, xref)
            if pix.n - pix.alpha < 4:  # this is GRAY or RGB
                pix.save(
                    f"{IMAGE_OUTPUT_DIR}/page_{page_num + 1}_img_{img_index}.png")
            else:  # CMYK: convert to RGB first
                pix_rgb = fitz.Pixmap(fitz.csRGB, pix)
                pix_rgb.save(
                    f"{IMAGE_OUTPUT_DIR}/page_{page_num + 1}_img_{img_index}.png")

            image_info = {
                "path": f"{IMAGE_OUTPUT_DIR}/page_{page_num + 1}_img_{img_index}.png",
                # [left, top, right, bottom]
                "bbox": [rect.x0, rect.y0, rect.x1, rect.y1]
            }
            page_images.append(image_info)

        # 3. Structured Output for the current page
        page_data = {
            "page_number": page_num + 1,
            "text_blocks": text_blocks,
            "images": page_images
        }
        all_pages_data.append(page_data)

        print(
            f"  - Page {page_num + 1}: Found {len(page_images)} images and {len(text_blocks)} text blocks.")

    doc.close()

    # --- JSON FILE CREATION ---
    with open(JSON_OUTPUT_FILE, 'w') as f:
        json.dump(all_pages_data, f, indent=4)

    print(f"\nSuccessfully created '{JSON_OUTPUT_FILE}' with coordinate data.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
