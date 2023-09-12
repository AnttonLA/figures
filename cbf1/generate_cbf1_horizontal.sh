#!/bin/bash

# Generate the individual images with titles and subtitles from the bare PNG images
python generate_named_images.py

# Use LaTex to generate the PDF that combines the named images into a single PDF
pdflatex celltypes_horizontal.tex

# Overlay the arrows on top of the image we just created
pdflatex celltypes_horizontal_add_arrows.tex

# Rename the resulting file to 'F1.pdf'
mv celltypes_horizontal_add_arrows.pdf F1.pdf
