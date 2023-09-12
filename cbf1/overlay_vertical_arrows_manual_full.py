from PIL import Image

# Open the base image (the image you want to overlay on)
base_image = Image.open("celltypes_vertical.png")

# Open the image you want to overlay
overlay_image = Image.open("resources/vertical_arrows_manual_full.png")

# Scale and shift the overlay image
scale_factor = 1  # Adjust this value to control the scaling factor
x_position_shift_pixels = 300
y_position_shift_pixels = 300

# Calculate the new size of the overlay image, and resize it
new_width = int(overlay_image.width * scale_factor)
new_height = int(overlay_image.height * scale_factor)
overlay_image = overlay_image.resize((new_width, new_height))

# Create a new image with RGBA mode
result_image = base_image.copy()
result_image = result_image.convert("RGBA")

# Paste the overlay image onto the result image at the calculated position using the mask
result_image.paste(overlay_image, (x_position_shift_pixels, y_position_shift_pixels), mask=overlay_image.convert("RGBA").getchannel(3))

# Save the overlaid image
result_image.save("cbf1.png")

# Close the images
base_image.close()
overlay_image.close()
