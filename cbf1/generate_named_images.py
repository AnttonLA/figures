from fpdf import FPDF
from pdf2image import convert_from_path
import os


def add_title_subtitle_to_image(input_png: str, output_pdf: str, title: str, subtitle: str) -> None:
    """
    Add title and subtitle to the image and save it as a PDF

    :param input_png: PNG image to add the title and subtitle to
    :param output_pdf: Output PDF file
    :param title: Title to add to the image
    :param subtitle: Subtitle to add to the image
    :return:
    """
    # Create a new PDF instance and dd a new page to it
    new_pdf = FPDF(format='letter')
    new_pdf.add_page()

    # Add some space before the image
    if '\n' in title:
        new_pdf.ln(40)
    else:
        new_pdf.ln(20)

    image_width = 180  # Adjust the image width as needed
    center_x = (new_pdf.w - image_width) / 2

    # Add the image to the PDF
    new_pdf.image(input_png, x=center_x, y=new_pdf.get_y(), w=image_width)

    # Add the title to the PDF
    new_pdf.set_y(0)
    new_pdf.set_font("Arial", size=92)
    new_pdf.multi_cell(0, 30, txt=title, border=0, align="C")

    # Add some space between the image and subtitle
    if '\n' in title:
        new_pdf.set_y(220)
    else:
        new_pdf.set_y(200)

    # Add the subtitle to the PDF
    new_pdf.set_font("Arial", size=70)
    new_pdf.multi_cell(0, 20, txt=subtitle, border=0, align="C")

    # Save the PDF to the output file
    new_pdf.output(output_pdf)


def create_png_from_pdf(pdf_file, output_dir, output_image_name: str) -> None:
    """
    Create a PNG image from the PDF
    :param pdf_file:
    :param output_dir:
    :param output_image_name:
    :return:
    """
    pages = convert_from_path(pdf_file)

    # Assuming only one page in the PDF, you can access the first page from 'pages' list
    if pages:
        output_image_path = os.path.join(output_dir, f"{output_image_name}.png")
        pages[0].save(output_image_path, "PNG")
        print(f"PDF converted to PNG: {output_image_path}")
    else:
        print("PDF conversion to PNG failed.")


# Dictionary with Title, Subtitle and Image file name for each cell population
name_marker_image_dict = {
    "CBMCs": ("CBMCs", "", "CBMCs.png"),
    "Leukocytes": ("Leukocytes", "", "Leukocytes.png"),
    "HSPCs": ("HSPCs", "CD34+", "HSPCs_color.png"),
    "T_cells": ("T cells", "CD3+", "CD4_color.png"),
    "Helper_T_cells": ("Helper\nT cells", "CD4+", "CD4_color.png"),
    "Cytotoxic_T_cells": ("Cytotoxic\nT cells", "CD8+", "CD8_color.png"),
    "CD3-": ("CD3-", "", "CD3Neg.png"),
    "B_cells": ("B cells", "CD19+", "B_color.png"),
    "CD19-": ("CD19-", "", "CD19Neg.png"),
    "Monocytes": ("Monocytes", "CD14+", "Mono_color.png"),
    "Classical_Monocytes": ("Classical\nMonocytes", "CD16-", "Mono_color.png"),
    "Non-classical_Monocytes": ("Non-classical\nMonocytes", "CD16+", "Mono_color.png"),
    "CD14-": ("CD14-", "", "CD14Neg.png"),
    "Early_NK_cells": ("Early\nNK cells", "CD16-CD56++", "NK_color.png"),
    "Effector_NK_cells": ("Effector\nNK cells", "CD16++CD56++", "NK_color.png"),
    "Terminal_NK_cells": ("Terminal\nNK cells", "CD16++CD56-", "NK_color.png"),
    "Lineage_Negative_cells": ("Lineage Neg.\ncells", "", "lineage_negative.png"),
    "Lineage_Negative_HSPCs": ("Lineage Neg.\nHSPCs", "CD34+", "HSC_color.png"),
    "CD38+": ("CD38+", "", "HSC.png"),
    "CD90+": ("CD90+", "", "HSC_color.png"),
    "B-NK_progenitors": ("B-NK\nprogenitors", "CD10+", "HSC_color.png"),
    "CD10-": ("CD10-", "", "HSC.png"),
    "CMPs": ("CMPs", "CD135-\nCD45RA+", "CMP_color.png"),
    "MEPs": ("MEPs", "CD135+\nCD45RA+", "MEP_color.png"),
    "GMPs": ("GMPs", "CD135-\nCD45RA-", "GMP_color.png"),
    "CD38-": ("CD38-", "", "HSC.png"),
    "CD90+CD45RA+": ("CD90+\nCD45RA+", "", "HSC_color.png"),
    "HSCs": ("HSCs", "CD90+\nCD45RA-", "HSC_color.png"),
    "CD10-_HSCs": ("CD10- HSCs", "", "HSC_color.png"),
    "MPPs": ("MPPs", "CD90-\nCD45RA-", "MPP_color.png"),
    "MLPs": ("MLPs", "CD90-\nCD45RA+", "MPP_color.png"),
    "CD10-_MLPs": ("CD10- MLPs", "", "MPP_color.png"),
    "CD10+_MLPs": ("CD10+ MLPs", "", "MPP_color.png")
}

if __name__ == "__main__":

    # Check that the resources/ folder and its sub-folders exist
    if not os.path.exists("resources"):
        raise Exception("resources/ folder does not exist. Please create it, as well as a resources/base_png/"
                        "subdirectory,  and add the required files to it.")
    if not os.path.exists("resources/base_png"):
        raise Exception("resources/base_png/ folder does not exist. Please create it and add the required files.")
    if not os.path.exists("resources/interim_pdf"):
        os.makedirs("resources/interim_pdf")
    if not os.path.exists("output"):
        os.makedirs("output")

    # Loop through the dictionary and create a PDF for each cell population. Then convert the PDF to PNG
    for i, cell_population in enumerate(name_marker_image_dict):

        name = cell_population
        output_pdf_path = os.path.join(f"resources", "interim_pdf", f"{name}.pdf")
        title_text = name_marker_image_dict[cell_population][0]
        subtitle_text = name_marker_image_dict[cell_population][1]
        image_name = name_marker_image_dict[cell_population][2]
        if image_name:
            input_image_path = os.path.join("resources/base_png", f"{image_name}")
        else:
            continue

        # Create PDF out of text and image. Gets stored in the resources/interim_pdf folder
        add_title_subtitle_to_image(input_image_path, output_pdf_path, title_text, subtitle_text)

        # Convert the PDF to PNG image and store in output/
        create_png_from_pdf(output_pdf_path, "output/", name)

    # Create a blank PDF
    pdf = FPDF(format='letter')
    pdf.add_page()
    pdf.output("output/blank.pdf")
    create_png_from_pdf("output/blank.pdf", "output/", "blank")
