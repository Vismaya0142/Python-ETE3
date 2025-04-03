# import streamlit as st

# # Title of the App
# st.title("📊 Hackathon Event Analysis Dashboard")

# # Sidebar
# st.sidebar.header("Select a page")
# page = st.sidebar.radio("Go to", ["Dashboard", "Text Analysis", "Image Gallery & Processing"])

# # Display the selected page content
# if page == "Dashboard":
#     st.write("### Welcome to the Dashboard")
#     # Your existing dashboard content goes here...
# elif page == "Text Analysis":
#     st.write("### Welcome to the Text Analysis Page")
#     # Your existing text analysis content goes here...
# elif page == "Image Gallery & Processing":
#     st.write("### Welcome to the Image Gallery & Processing Page")
#     # The content from the image_processing.py page will be automatically included here
#     import pages.image_processing  # Automatically imports the page from the 'pages' folder



import streamlit as st
from PIL import Image

# Title of the App
st.title("📊 Hackathon Event Analysis Dashboard")

# Display an image related to the hackathon
hackathon_image = Image.open("hackhome.jpg")  # Make sure the image is in the same folder or provide the path
st.image(hackathon_image, caption="Welcome to the Hackathon!", use_container_width=True)

# Sidebar
st.sidebar.header("Select a page")
page = st.sidebar.radio("Go to", ["Dashboard", "Text Analysis", "Image Gallery & Processing"])

# Display the selected page content
if page == "Dashboard":
    st.write("### Welcome to the Dashboard")
    # Your existing dashboard content goes here...
elif page == "Text Analysis":
    st.write("### Welcome to the Text Analysis Page")
    # Your existing text analysis content goes here...
elif page == "Image Gallery & Processing":
    st.write("### Welcome to the Image Gallery & Processing Page")
    # The content from the image_processing.py page will be automatically included here
    import pages.image_processing  # Automatically imports the page from the 'pages' folder

# Footer with a cool design
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Made with ❤️ by the Hackathon Team</p>", unsafe_allow_html=True)
