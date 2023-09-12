#!/bin/bash

# Generate the individual images with titles and subtitles from the bare PNG images
python generate_named_images.py

# Use LaTex to generate the PDF that combines the named images into a single PDF
pdflatex celltypes_vertical.tex

# Use ImageMagick to convert the PDF to a PNG
convert -density 300 celltypes_vertical.pdf[0] celltypes_vertical.png

# Overlay the arrows on top of the image we just created
python overlay_vertical_arrows_manual_full.py
