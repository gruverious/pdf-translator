# 📄 PDF Translator (English → Tamil)

This project automatically extracts text from an input PDF, translates it into Tamil, and generates a new translated PDF while preserving the document structure.

---

## 🚀 Features

- 📥 Extracts text from PDF using PyMuPDF (fitz)
- 🔤 Automatically translates text to Tamil
- 📄 Generates a new translated PDF
- 🅰️ Uses Noto Serif Tamil font for proper Tamil rendering
- 🧱 Preserves layout using block-based text positioning
- 🔁 Retry mechanism for stable translation

---

## ⚙️ How It Works

1. Extracts text blocks (with positions) from the input PDF  
2. Cleans and processes the extracted text  
3. Translates each block using Google Translator  
4. Reconstructs the PDF with translated Tamil text  
5. Saves output as a new PDF  

---

## 📦 Installation

1. Clone the repository:

git clone https://github.com/your-username/pdf-translator.git  
cd pdf-translator  

2. Install dependencies:

pip install -r requirements.txt  

---

## ▶️ Usage

1. Place your PDF file in the project folder  
2. Rename it as:

input.pdf  

3. Run the script:

python translator.py  

4. Output:

- Translated file will be generated as:  
  translated.pdf  

---

## 📁 Project Structure

pdf-translator/  
│  
├── fonts/  
│   └── NotoSerifTamil-Regular.ttf  
│  
├── input.pdf  
├── translated.pdf  
├── translator.py  
├── requirements.txt  
├── README.md  
├── .gitignore  

---

## 🛠 Tech Stack

- Python  
- PyMuPDF (fitz) – PDF text extraction
- deep-translator – Translation engine
- reportlab – PDF generation 
- pillow – Image/font support 

---

## 🧠 Key Implementation Details

- Uses block-level extraction instead of plain text for better layout preservation  
- Implements retry logic for translation failures  
- Normalizes Unicode text for proper Tamil rendering  
- Handles multi-line wrapping using ReportLab utilities  
- Maintains spacing and page flow dynamically  

---

## Future Improvements

- Support multiple languages  
- Preserve exact formatting (tables, styles)  
- Add GUI  
- Deploy as a web application  
- Improve performance and translation speed
- Improve translation efficiency

---

## Author

Sivaraj kumar

---
