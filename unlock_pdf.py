import os
import pikepdf

# Folder containing encrypted PDFs
source_folder = r"Your source file:"
# Destination folder for unlocked PDFs
output_folder = r"Your destination file path"

# Password for all PDFs
password = input("Enter the PDF password: ")

# Make sure output folder exists
os.makedirs(output_folder, exist_ok=True)

# Process each PDF file
for filename in os.listdir(source_folder):
    if filename.lower().endswith(".pdf"):
        input_pdf = os.path.join(source_folder, filename)
        output_pdf = os.path.join(output_folder, f"unlocked_{filename}")

        try:
            # Open locked PDF with password
            pdf = pikepdf.open(input_pdf, password=password)
            # Save unlocked PDF
            pdf.save(output_pdf)
            pdf.close()
            print(f"Unlocked: {filename}")
        except pikepdf._qpdf.PasswordError:
            print(f"Wrong password for {filename}. Skipping...")
        except Exception as e:
            print(f"Failed to unlock {filename}: {e}")

print("\nBatch unlocking completed!")
