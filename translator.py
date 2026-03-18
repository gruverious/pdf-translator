import time 
import fitz
import unicodedata
from deep_translator import GoogleTranslator
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import simpleSplit

def extract_blocks(pdf_path):
    
    doc=fitz.open(pdf_path)
    pages=[]

    for page in doc:

        blocks=page.get_text("blocks")
        page_blocks=[]

        for block in blocks:

            x0,y0,x1,y1,text,*_ = block


            if text.strip():
                text=clean_text(text)
                page_blocks.append({
                    "x":x0,
                    "y":y0,
                    "text":text
                })
        
        pages.append(page_blocks)
    
    return pages

def clean_text(text):
    text=text.replace("\n/\n"," / ")
    text=text.replace("\n", " ")
    text=" ".join(text.split())

    return text

def safe_translate(text,retries=3,delay=2):
    for attempt in range(retries):
        try:
            result=GoogleTranslator(source="auto",target="ta").translate(text)
            if result and ("Error" in result or "<!DOCTYPE" in result):
                raise ValueError(f"Bad translation response : {result[:80]}")
            return unicodedata.normalize("NFC",result)
        except Exception as e:
            print(f" Retry {attempt+1} for block due to : {e}")
            time.sleep(delay*(attempt+1))
    return text

def translate_text(pages):

    translated_pages=[]

    for page in pages:

        translated_blocks=[]

        for block in page:

            translated=safe_translate(block["text"])
            time.sleep(0.3)

            translated_blocks.append({
                "x":block["x"],
                "y":block["y"],
                "text":translated

            })
            
        translated_pages.append(translated_blocks)
    
    return translated_pages

def create_pdf(pages,output_file):

    pdfmetrics.registerFont(TTFont('Tamil','fonts/NotoSerifTamil-Regular.ttf'))
    c=canvas.Canvas(output_file)
    font_size=12
    line_height=font_size*1.6
    margin_x=50
    margin_top=50

    for page in pages:
        page_height=c._pagesize[1]
        y=page_height-margin_top

        for block in page:
            text=block["text"]
            wrapped_lines=simpleSplit(text,"Tamil",font_size,500)

            block_height=len(wrapped_lines)*line_height
            if y-block_height < margin_top:
                c.showPage()
                y=page_height-margin_top

            textobject=c.beginText(margin_x,y)
            textobject.setFont("Tamil",font_size)
            textobject.setLeading(line_height)

            for line in wrapped_lines:
                textobject.textLine(line)

            c.drawText(textobject)
            y-=block_height+10
        c.showPage()
    c.save()





input_pdf = "input.pdf"
output_pdf = "translated.pdf"

pages = extract_blocks(input_pdf)
print("Text extracted")

translated_pages = translate_text(pages)
print("Translation done")

create_pdf(translated_pages, output_pdf)
print("PDF created")

print("Translation completed!")

