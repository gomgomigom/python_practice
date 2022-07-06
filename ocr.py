import platform
from tempfile import TemporaryDirectory
from pathlib import Path
from tqdm import tqdm
from PIL import Image

import pytesseract
from wand.image import Image as wi

out_directory = Path("./ocr_test/")

PDF_file = Path(r"./pdf_hwp/대구지법 2007고합449.pdf")
print(PDF_file)

image_file_list = []
text_file = out_directory / Path("out_text.txt")
print(out_directory / Path("out_text.txt"))


def main():
    # with TemporaryDirectory() as tempdir:
    tempdir = "./ocr_test/"
    pdf_pages = wi(filename=PDF_file, resolution=300)
    pdfImage = pdf_pages.convert("jpeg")
    for page_enumeration, img in enumerate(tqdm(pdfImage.sequence), start=1):
        page = wi(image=img)
        file_name = f"{tempdir}/page_{page_enumeration:03}.jpg"
        page.save(filename=file_name)
        image_file_list.append(file_name)
    with open(text_file, "a") as output_file:
        for image_file in tqdm(image_file_list):
            text = str(
                (
                    pytesseract.image_to_string(
                        Image.open(image_file), lang="eng+kor"
                    )
                )
            )
            text = text.replace(r"-\n", "")
            output_file.write(text)


main()
