import fitz  # PyMuPDF


def rotate_and_crop_pdf(input_path, output_path):
    with fitz.open(input_path) as pdf_document:
        page = pdf_document[0]  # Assuming you want to rotate and crop the first page

        # Crop the bottom-left corner by specifying a rectangle
        crop_box = fitz.Rect(page.rect.width * 0.21,
                             page.rect.height * 0.1,
                             page.rect.width * 0.78,
                             page.rect.height * 0.64)  # Adjust the height as needed
        page.set_cropbox(crop_box)

        # Rotate the page 270 degrees clockwise
        page.set_rotation(270)

        pdf_document.save(output_path)


# Example usage:
#input_pdf = 'celltypes_horizontal_add_arrows.pdf'
input_pdf = 'celltypes_horizontal_add_arrows_ALT_SECOND_LVL.pdf'
output_pdf = '../F1_image_only.pdf'
rotate_and_crop_pdf(input_pdf, output_pdf)
