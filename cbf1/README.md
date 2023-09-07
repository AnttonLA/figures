# F1 - Cell types under study
This collection of scripts generates a tentative F1 for the article we are curerntly writing.

It takes a bunch of PNGs files, generates new images with titles and subtitles
using a python script ('generate_named_images.py') and then merges them into a single PDF using LaTeX.
Finally, the LaTex PDF is converted to a PNG using ImageMagick, and a final PNG is generated using the
'overlay_arrows.py' script, which adds arrows to the figure.

Note that you will not be able to use these scripts unless you have the image data in 'resources/'.
The file names are hardcoded inside 'generate_named_images.py'.
