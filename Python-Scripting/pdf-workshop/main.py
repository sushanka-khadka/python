import os
import PyPDF2

def pdf_merger():
    merger= PyPDF2.PdfMerger()
    save_to = "./output/merged"
    os.makedirs(save_to, exist_ok=True)
    for file in os.listdir('./files'):
        merger.append(f"./files/{file}")
    merger.write(f'{save_to}/merged_files.pdf')


def pdf_appender():
    reader_read = PyPDF2.PdfReader('./files/wtr.pdf')
    reader_append = PyPDF2.PdfReader('./files/twopage.pdf')
    writer = PyPDF2.PdfWriter()
    save_to = "./output/appended"
    os.makedirs(save_to, exist_ok=True)
    for pg in reader_append.pages:
        writer.add_page(pg)
    for pg in reader_read.pages:
        writer.add_page(pg)
    with open(f"{save_to}/appended.pdf",mode='wb') as new_file:
        writer.write(new_file)

def add_watermark():
    save_to= "./output/with_watermark"
    os.makedirs(save_to, exist_ok=True)
    for file_name in os.listdir('./files'):
        if file_name != 'wtr.pdf':
            template= PyPDF2.PdfReader(f'./files/{file_name}')
            watermark= PyPDF2.PdfReader('./files/wtr.pdf')
            writer= PyPDF2.PdfWriter()

            for page in template.pages:
                page.merge_page(watermark.pages[0])
                writer.add_page(page)
            with open(f'{save_to}/{file_name}','wb') as new_file:
                writer.write(new_file)

if __name__ =='__main__':
    pdf_appender()
    pdf_merger()
    add_watermark()