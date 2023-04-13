from gtts import gTTS
import pdfplumber
from pathlib import Path

def pdf_to_mp3(file_path="test.pdf", language="en"):
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':

        print(f"Your file's name {Path(file_path).name}")
        print('Proccessing...')

        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]

        text = ''.join(pages)
        text = text.replace('\n', '')

        my_audio = gTTS(text=text, lang=language, slow=False)
        file_name = Path(file_path).stem
        my_audio.save(f"{file_name}.mp3")

        return f'{file_name}.mp3 was save successfully! \n'

    else:
        return "Sorry.. We can't to find your file, check the file name!"

def main():
    print("PDF to MP3")
    file_path = 'pdf_files/' + input("\nEnter a file's name: ")
    language = input("Choose language, for example 'ru' or 'en': ")
    print(pdf_to_mp3(file_path=file_path, language=language))


if __name__ == "__main__":
    main()
