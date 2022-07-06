import pytesseract
from PIL import Image
from pdf2image import convert_from_path
from pathlib import Path
from tqdm import tqdm
import cv2
import time


file = Path("/Users/gom/Desktop/스크린샷 2022-07-06 10.37.32.png")
file_name = Path("./pdf_hwp/대구지법 2007고합449.pdf")
text = str(pytesseract.image_to_string(Image.open(file), lang="eng+kor"))

print(text)

# PDF_file = Path("./pdf_hwp/대구지법 2007고합449.pdf")
# convert_from_path(PDF_file, 500)[1].save("./ocr_test/out.jpg", "JPEG")
# pages = convert_from_path(PDF_file, 500)

# for i, page in enumerate(pages):
#     print(type(page))
#     page.save(f"./ocr_test/{i:02}.jpg", "JPEG")

from wand.image import Image as wi

pdf = wi(filename=file_name, resolution=500)
pdfImage = pdf.convert("jpeg")
for i, img in enumerate(pdfImage.sequence):
    page = wi(image=img)
    page.save(filename=f"./ocr_test/aaa{i:03}.jpg")

list = [1, 54, 5303]

for enumeration, number in enumerate(tqdm(list), start=1):
    print(enumeration, number)
    time.sleep(0.1)
