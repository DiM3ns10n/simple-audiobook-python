import streamlit as st
import os
import shutil
from read_pdf import is_pdf, read_pdf_text, stop_speech, text_to_speech

st.title("PDF Reader")
pdf_file = st.file_uploader(label="Upload a PDF file", type=["pdf"])

st_page_no = st.number_input(label="Enter the page number", value=1, min_value=1)
st_submit = st.button(label="Submit", key="submit")
st_stop = st.button("Stop", key="stop")

# temp_dir = tempfile.mkdtemp()
current_dir = os.getcwd()
temp_dir_path = os.path.join(current_dir, "temp")

if not os.path.exists("temp"):
    temp_dir = os.mkdir(temp_dir_path)
else:
    temp_dir = temp_dir_path
    
if st_submit:
    if pdf_file is not None:
        print(pdf_file.name)
        
        path = os.path.join(temp_dir_path, pdf_file.name)
        with open(path, "wb") as f:
            f.write(pdf_file.getvalue())
            
        st.write("File uploaded successfully!")
        st.write(path)

        if is_pdf(path):
            
            pages,text = read_pdf_text(path, st_page_no)
            st.write(f"Total number of pages in the PDF: {pages}")
            
            text_to_speech(text)

        else:
            st.write("Invalid PDF file")

    else:
        st.write("Please upload a PDF file")
                                  
if st_stop:
    stop_speech()
    try:
       shutil.rmtree(temp_dir)
    except:
        st.write("File not found")
    
                



                
            


