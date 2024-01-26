# F1 - Cell types under study
This collection of scripts generates a tentative F1 for the article we are curerntly writing.

Note that you will not be able to use these scripts unless you have the image data in 'resources/'.
The file names are hardcoded inside `generate_named_images.py`.

The pipeline takes a bunch of PNGs files, generates new images with titles and subtitles
using a python script (`generate_named_images.py`) and then merges them into a single PDF using LaTeX.
A final python script (`rotate_and_crop_pdf.py`) is then used to crop the final PDF.

You can run the entire pipeline with `complete_pipeline.sh`

## Horizontal version (current way)
In the horizontal version, the LaTex PDF is used as an input in another LaTex script
('celltypes_horizontal_add_arrows.tex'), which adds the arrows on top of the image.

## Vertical version (old way)
In the original vertical version, the LaTex PDF is converted to a PNG using ImageMagick, and a final PNG is generated
using the 'overlay_arrows.py' script, which adds arrows to the figure (The arrows PNG was previously generated manually).


