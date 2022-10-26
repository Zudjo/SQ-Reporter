# LIBRARIES
# --------------------------------------------------
import pdfkit
import os

# VARIABLES
# --------------------------------------------------
options = {
    "javascript-delay": "10000",
    "debug-javascript": "",
    "no-stop-slow-scripts": "",
    "enable-local-file-access": "",
    "dpi": "150",
    "margin-bottom": "0",
    "margin-top": "0",
    "margin-left": "0",
    "margin-right": "0"

}

# FUNCTIONS
# --------------------------------------------------

def clean_file(file_name):
    file = open(file_name, "w")
    file.write("")
    file.close()

def write_file(file_name, data, clean = False):
    if clean:
        clean_file(file_name)

    file = open(file_name, "a")
    file.write(data)
    file.close()

def get_file_as_string(file_name):
    file = open(file_name, "r")
    return file.read()

def convert_to_pdf(file_name, path_output):
    print("Converting to PDF...")
    pdfkit.from_file(file_name, path_output + "/output.pdf", options=options)
    print("\nConversion completed.")

def delete_file(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)
    else:
        print("The file to delete does not exist")
