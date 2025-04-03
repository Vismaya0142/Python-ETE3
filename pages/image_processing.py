

import streamlit as st
from PIL import Image, ImageEnhance
import os
import numpy as np

# Title of the page
st.title("🖼️ Image Processing & Enhancement")

# Sidebar for Image Upload
st.sidebar.header("📤 Upload an Image")
uploaded_file = st.sidebar.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Load Image
    img = Image.open(uploaded_file)
    original_img = img.copy()  # Store original image for processing

    # **Resizing Image**  
    # resized_img = img.resize((200, 200))

    # **Brightness, Contrast & Sharpness Adjustment**
    st.sidebar.header("🎛️ Adjust Image Properties")
    brightness = st.sidebar.slider("Brightness", 0.5, 2.0, 1.0)
    contrast = st.sidebar.slider("Contrast", 0.5, 2.0, 1.0)
    sharpness = st.sidebar.slider("Sharpness", 0.5, 2.0, 1.0)

    enhancer = ImageEnhance.Brightness(original_img)
    original_img = enhancer.enhance(brightness)

    enhancer = ImageEnhance.Contrast(original_img)
    original_img = enhancer.enhance(contrast)

    enhancer = ImageEnhance.Sharpness(original_img)
    original_img = enhancer.enhance(sharpness)

    # **Apply Filters**
    st.sidebar.header("🎭 Apply Filters")
    filter_option = st.sidebar.radio("Choose a Filter", ["None", "Grayscale", "Sepia", "Invert"])

    if filter_option == "Grayscale":
        original_img = original_img.convert("L")
    elif filter_option == "Sepia":
        sepia_filter = original_img.convert("RGB")
        sepia_data = sepia_filter.getdata()
        sepia_data = [(int(r * 0.393 + g * 0.769 + b * 0.189), 
                       int(r * 0.349 + g * 0.686 + b * 0.168), 
                       int(r * 0.272 + g * 0.534 + b * 0.131)) for r, g, b in sepia_data]
        original_img.putdata(sepia_data)
    elif filter_option == "Invert":
        original_img = Image.eval(original_img, lambda x: 255 - x)

    # # **Convert Image to Sticker (Transparent Background)**
    # st.sidebar.header("🖼️ Convert to Sticker")
    # def make_transparent(img):
    #     img = img.convert("RGBA")
    #     data = np.array(img)
    #     red, green, blue, alpha = data.T
    #     white_areas = (red > 200) & (green > 200) & (blue > 200)
    #     data[..., 3][white_areas] = 0  # Set alpha to 0 where it's white
    #     return Image.fromarray(data)

    # if st.sidebar.button("🟢 Create Sticker"):
    #     resized_img = make_transparent(resized_img)

    # **Display Final Image**
    st.image(original_img, caption="✨ Final Image after Processing", use_container_width=True)
