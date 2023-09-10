pip install streamlit Pillow
# Required Libraries
import streamlit as st
from PIL import Image, ImageOps
import io

# Main app function
def main():
    st.title("Label Your Images")

    # Upload images (max 10)
    uploaded_files = st.file_uploader("Choose images", accept_multiple_files=True, type=['jpg', 'jpeg', 'png', 'gif', 'tif', 'svg', 'ico', 'psd', 'pcx'], max_uploaded_files=10)

    # Input field for renaming label
    label = st.text_input("Enter desired label for renaming:")

    # Sidebar menu for adjustments
    with st.sidebar:
        st.header("Adjustment Options")
        quality = st.slider("Quality (%)", min_value=1, max_value=100, value=100)
        width = st.number_input("Width (pixels)", min_value=1, value=300)
        height = st.number_input("Height (pixels)", min_value=1, value=300)
        file_format = st.selectbox("Select file format", ["jpg", "jpeg", "png", "gif"])

    # Check if files uploaded and label is provided
    if uploaded_files and label:
        st.write("Renamed and Adjusted Images:")
        
        for index, uploaded_file in enumerate(uploaded_files):
            # Convert uploaded file to bytes
            img_data = uploaded_file.read()
            img = Image.open(io.BytesIO(img_data))
            
            # Adjust image as per sidebar options
            img = ImageOps.fit(img, (width, height), method=0, bleed=0.0, centering=(0.5, 0.5))
            
            # Convert to desired format
            buffer = io.BytesIO()
            img.save(buffer, format=file_format.upper(), quality=quality)
            buffer.seek(0)
            
            # Display and provide download option
            st.image(img, caption=f'{label}_{index+1}.{file_format}', use_column_width=True)
            st.download_button(
                label=f"Download {label}_{index+1}.{file_format}",
                data=buffer,
                file_name=f"{label}_{index+1}.{file_format}",
                mime=file_format
            )

    # Social Media Links at the end
    st.write("Connect with me on:")
    st.markdown("1. [LinkedIn](#)")
    st.markdown("2. [Twitter](#)")
    st.markdown("3. [GitHub](#)")

if __name__ == "__main__":
    main()
