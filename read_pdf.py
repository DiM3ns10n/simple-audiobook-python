from PyPDF2 import PdfReader

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


def str_to_sentence_list(page):
    """
    Convert a string of text into a list of sentences.
    Args:
        page (str): The text content to be converted.
    Returns:
        list: A list of sentences extracted from the text.
    """
    text_list = [text.replace("\n", " ") for text in page.split(".")]
    return text_list

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
        sentence_list = str_to_sentence_list(page.extract_text())
        return pages, sentence_list 
    
    

    
if __name__ == "__main__":
    file = "sample.pdf"
    print(is_pdf(file))
    pages, text = read_pdf_text(file,0)
    print(pages)
    print(text)

