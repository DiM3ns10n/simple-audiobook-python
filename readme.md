# PDF Reader
This repository contains a simple PDF reader application built with Python. The application allows users to upload a PDF file, read text from a specific page, and convert the text to speech.

## Features
* Upload a PDF file
* Read text from a specific page of the PDF
* Convert the text to speech using pyttsx3
* Stop the text-to-speech conversion

## Installation
1. Clone the repository:

```bash
git clone https://github.com/DiM3ns10n/simple-audiobook-python.git
cd simple-audiobook-python
```

2. Install the required Python packages:
```bash
pip install -r requirements.txt
```

## Usage
1. Run the application
```bash
streamlit run main.py
```

## Dependencies
* pyttsx3: Text-to-speech conversion library.
* PyPDF2: Library to read PDF files