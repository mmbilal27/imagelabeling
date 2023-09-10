import streamlit as st
from PIL import Image, ImageOps
import io
import base64

# Function to convert image to desired format, resolution, and quality
def process_image(img, file_format, width, height, quality):
    img = ImageOps.fit(img, (width, height), method=0, bleed=0.0, centering=(0.5, 0.5))
    buffer = io.BytesIO()
    img.save(buffer, format=file_format.upper(), quality=quality)
    buffer.seek(0)
    return buffer

# Function to provide a download link for the processed image
def get_image_download_link(buffer, file_format, label, index):
    b64 = base64.b64encode(buffer.getvalue()).decode()
    return f'<a href="data:image/{file_format};base64,{b64}" download="{label}_{index}.{file_format}">Download {label}_{index}.{file_format}</a>'

def main():
    st.title("Label Your Images")

    uploaded_files = st.file_uploader("Choose images")
    label = st.text_input("Enter desired label for renaming:")

    # Sidebar menu for adjustments
    with st.sidebar:
        st.header("Adjustment Options")
        quality = st.slider("Quality (%)", min_value=1, max_value=100, value=100)
        width = st.number_input("Width (pixels)", min_value=1, value=300)
        height = st.number_input("Height (pixels)", min_value=1, value=300)
        file_format = st.selectbox("Select file format", ["jpg", "jpeg", "png", "gif"])

    if uploaded_files and label:
        st.write("Renamed and Adjusted Images:")

        for index, uploaded_file in enumerate(uploaded_files):
            img_data = uploaded_file.read()
            img = Image.open(io.BytesIO(img_data))
            
            img_buffer = process_image(img, file_format, width, height, quality)
            
            st.image(img, caption=f'{label}_{index+1}.{file_format}', use_column_width=True)
            st.markdown(get_image_download_link(img_buffer, file_format, label, index+1), unsafe_allow_html=True)

    # Social Media Links at the end
    st.write("Connect with me on:")
    st.markdown("1. [LinkedIn](#)")
    st.markdown("2. [Twitter](#)")
    st.markdown("3. [GitHub](#)")

if __name__ == "__main__":
    main()
