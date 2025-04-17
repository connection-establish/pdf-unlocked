# pdf-unlocked
i am trying to make a python program to unlock pdf

----Important notes----------

This script only works if you know the correct password for the PDF.
The script removes the password protection, creating a new unprotected PDF file.
This should only be used for PDF files that you legitimately have the right to access.
It won't work with PDFs that have other security restrictions beyond just password protection.


-----How to use this script:------------

First, install the required library:
    pip install PyPDF2

Save the script as unlock_pdf.py
Run the script with the following command:
    python unlock_pdf.py path/to/encrypted.pdf -p "your_password"

Optionally specify an output path:
      python unlock_pdf.py path/to/encrypted.pdf -p "your_password" -o path/to/output.pdf
