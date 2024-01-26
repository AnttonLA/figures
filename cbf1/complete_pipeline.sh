#!/bin/bash

# This script runs the complete pipeline for the project.
# The scrips that are run are:
# 1. generate_named_images.py
# 2. celltypes_horizontal.tex
# 3. celltypes_horizontal_add_arrows.tex
# 4. celltypes_horizontal_add_arrows_ALT_FIRST_LVL.tex
# 5. celltypes_horizontal_add_arrows_ALT_SECOND_LVL.tex
# 6. rotate_and_crop_pdf.py


python generate_named_images.py
pdflatex celltypes_horizontal.tex
pdflatex celltypes_horizontal_add_arrows.tex
pdflatex celltypes_horizontal_add_arrows_ALT_FIRST_LVL.tex
pdflatex celltypes_horizontal_add_arrows_ALT_SECOND_LVL.tex
python rotate_and_crop_pdf.py
