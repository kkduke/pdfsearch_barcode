import os
import shutil
import fitz  # PyMuPDF
from PIL import Image
import cv2
import zxingcpp

def rename_pdfs_based_on_barcode():
    directory = os.getcwd()  # Get the current working directory
    new_directory = os.path.join(directory, 'new')
    os.makedirs(new_directory, exist_ok=True)
    
    no_barcode_files = []  # List to store filenames where no barcode was found
    
    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(directory, filename)
            
            # Open the PDF file
            doc = fitz.open(pdf_path)
            
            # Set the resolution to 300 dpi
            dpi = 300
            zoom = dpi / 72  # Default: 72 dpi
            magnify = fitz.Matrix(zoom, zoom)  # Magnify in x and y direction
            
            # Convert the first page of the PDF to an image with high resolution
            pix = doc.get_page_pixmap(0, matrix=magnify)
            
            # Save the image
            image_path = "temp_image.png"
            pix.save(image_path)
            
            # Load the image
            img = cv2.imread(image_path)

            # Define the coordinates of the area where the barcode is located
            x, y, w, h = 220, 1100, 900, 200

            # Crop the image
            cropped_img = img[y:y+h, x:x+w]
            
            # Save the cropped image
            cropped_image_path = f"cropped_{filename}.png"
            cv2.imwrite(cropped_image_path, cropped_img)
            
            # Decode the barcode from the cropped image using zxing-cpp
            results = zxingcpp.read_barcodes(cropped_img)

            if results:
                for result in results:
                    barcode_value = result.text
                    
                    # Copy the PDF file to new directory with new name based on the barcode value
                    new_filename = f"LFSR_{barcode_value}.pdf"
                    new_filepath = os.path.join(new_directory, new_filename)
                    shutil.copy(pdf_path, new_filepath)
                    
                # Delete temporary images after use
                os.remove(image_path)
                os.remove(cropped_image_path)
                
            else:
                no_barcode_files.append(filename)
                
                # Copy the PDF file to new directory with its original name if no barcode is found
                shutil.copy(pdf_path, os.path.join(new_directory, filename))

    print("Files where no barcode was found:")
    for filename in no_barcode_files:
        print(filename)

# Call the function
rename_pdfs_based_on_barcode()
