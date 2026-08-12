import os
from PIL import Image

brain_dir = r"C:\Users\Jeff Ouro\.gemini\antigravity\brain\6109d565-f11e-4bcb-bc7b-7719befd9211\.user_uploaded"
logo_src_path = os.path.join(brain_dir, "media__1786566128141.jpg")

public_dir = r"c:\Users\Jeff Ouro\Desktop\Captação Odisseia\public"
images_dir = os.path.join(public_dir, "images")
os.makedirs(images_dir, exist_ok=True)

# Open user uploaded image
img = Image.open(logo_src_path).convert("RGBA")
width, height = img.size

# Make the off-white background transparent
# The background color is approximately (245..255, 245..255, 245..255)
datas = img.getdata()
new_data = []

for item in datas:
    r, g, b, a = item
    # Check if pixel is near off-white background
    if r > 235 and g > 235 and b > 235:
        new_data.append((255, 255, 255, 0)) # Fully transparent
    else:
        new_data.append((r, g, b, 255))

img_transparent = Image.new("RGBA", img.size)
img_transparent.putdata(new_data)

# Save full transparent logo PNG
logo_png_path = os.path.join(images_dir, "logo.png")
img_transparent.save(logo_png_path, "PNG")

# Save non-transparent fallback logo JPEG
logo_jpeg_path = os.path.join(images_dir, "logo.jpg")
img.convert("RGB").save(logo_jpeg_path, "JPEG")

# Crop owl icon only for favicon / icon usage
# Find bounding box of non-transparent content or owl specific box
# The owl is located roughly on the left half of the logo
bbox = img_transparent.getbbox()
if bbox:
    # Crop the owl area (left part of image)
    left, upper, right, lower = bbox
    owl_width = (right - left) // 2.5
    owl_box = (left, upper, int(left + owl_width), lower)
    owl_img = img_transparent.crop(owl_box)
    
    # Save owl icon PNG
    owl_png_path = os.path.join(images_dir, "logo-icon.png")
    owl_img.save(owl_png_path, "PNG")
    
    # Make square icon for favicon
    owl_w, owl_h = owl_img.size
    max_dim = max(owl_w, owl_h) + 20
    square_icon = Image.new("RGBA", (max_dim, max_dim), (0, 0, 0, 0))
    offset_x = (max_dim - owl_w) // 2
    offset_y = (max_dim - owl_h) // 2
    square_icon.paste(owl_img, (offset_x, offset_y))
    
    # Save favicons
    square_icon.resize((64, 64), Image.Resampling.LANCZOS).save(os.path.join(public_dir, "favicon.png"), "PNG")
    square_icon.resize((64, 64), Image.Resampling.LANCZOS).save(os.path.join(images_dir, "favicon.png"), "PNG")
    square_icon.resize((64, 64), Image.Resampling.LANCZOS).save(os.path.join(public_dir, "favicon.ico"), format="ICO", sizes=[(32,32), (48,48), (64,64)])

print("Successfully processed user uploaded logo and generated transparent assets!")
