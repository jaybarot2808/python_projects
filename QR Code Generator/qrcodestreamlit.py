import streamlit as st
import qrcode
from PIL import Image
from io import BytesIO


def generate_qr_code(link):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=4,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    return img


st.set_page_config(page_title="QR Code Generator", page_icon="", layout="centered")


hide_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .css-1v3fvcr.e1fqkh3o3 {visibility: hidden;}
    .css-9s5bis.edgvbvh3 {visibility: hidden;}
    </style>
    """
st.markdown(hide_style, unsafe_allow_html=True)

st.title("QR Code Generator")
st.write("Enter the link below and click 'Generate QR Code'.")

link = st.text_input("Enter the link:")

if st.button("Generate QR Code"):
    if link:
        img = generate_qr_code(link)
        
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        img_str = buffered.getvalue()
        
        st.image(img_str, caption="Generated QR Code", use_column_width=True, output_format="PNG")

        st.download_button(
            label="Download QR Code",
            data=img_str,
            file_name="qr_code.png",
            mime="image/png",
        )
    else:
        st.error("Please enter a valid link.")

st.markdown("""
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        width: 100%;
        text-align: center;
        color: grey;
        padding: 10px;
    }
    </style>
    <div class="footer">
        <p>Made by Jay Barot</p>
    </div>
    """, unsafe_allow_html=True)
