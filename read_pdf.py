from PyPDF2 import PdfReader
import pyttsx3

speaker = pyttsx3.init()
def is_pdf(filepath):
    """
    Check if the given file path points to a PDF file.
    Args:
        filepath (str): The path to the file.
    Returns:
        bool: True if the file is a PDF, False otherwise.
    """

    if not filepath.endswith(".pdf"):
        return False
    return True

def stop_speech():
    """
    Stop the text-to-speech conversion.
    Returns:
        None
    """
    speaker.stop()
    if speaker._inLoop:
        speaker.endLoop()

def text_to_speech(page):
    """
    Convert text to speech using the pyttsx3 library.
    Args:
        page (str): The text content to be converted to speech.
    Returns:
        None
    """

    speaker.say(page)
    speaker.runAndWait()

def read_pdf_text(filepath,page_number):   
    """
    Reads text from a specific page of a PDF file.
    Args:
        filepath (str): The path to the PDF file.
        page_number (int): The page number to extract text from (0-indexed).
    Returns:
        tuple: A tuple containing:
            - int: The total number of pages in the PDF.
            - str: The text extracted from the specified page.
    """
  
    with open(filepath, "rb") as pdf_file:
        pdf_reader = PdfReader(pdf_file)
        pages = len(pdf_reader.pages)
        page = pdf_reader.pages[page_number - 1]
        return pages, page.extract_text() 
    
if __name__ == "__main__":
    file = "sample.pdf"
    print(is_pdf(file))
    pages, text = read_pdf_text(file,0)
    print(pages)
    print(text)
    text_to_speech(text)

