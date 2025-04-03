import streamlit as st
import os
from PIL import Image

# Set page title
st.title("🖼️ Hackathon Event - Day-wise Image Gallery")

# Sidebar for selecting the day
st.sidebar.header("📅 Select a Day")
selected_day = st.sidebar.radio("Choose the event day:", ["All", "Day1", "Day2", "Day3"])

# Path to images folder
image_folder = "images"

# Function to display images in a 2-column grid with equal sizes
def display_images(day):
    if day == "All":
        days = ["Day1", "Day2", "Day3"]
    else:
        days = [day]

    for d in days:
        st.subheader(f"📸 {d} Highlights")
        day_folder = os.path.join(image_folder, d)

        if os.path.exists(day_folder):
            images = [img for img in os.listdir(day_folder) if img.endswith(("jpg", "png", "jpeg"))]
            image_paths = [os.path.join(day_folder, img) for img in images]

            if image_paths:
                cols = st.columns(2)  # 2 images per row
                
                for i, img_path in enumerate(image_paths):
                    img = Image.open(img_path)
                    img = img.resize((400, 300))  # Set all images to the same size (adjust as needed)
                    
                    with cols[i % 2]:  # Distribute images evenly across 2 columns
                        st.image(img, caption=images[i], use_container_width=True)
            else:
                st.warning(f"No images found for {d}.")
        else:
            st.error(f"Folder '{d}' does not exist!")

# Display images based on selection
display_images(selected_day)
