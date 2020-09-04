import streamlit as st
from PIL import Image

st.set_option('deprecation.showfileUploaderEncoding', False)

im_file = st.file_uploader("Choose an image", type=["jpg","png", "jpeg"])

if im_file is not None:
    im = Image.open(im_file)
    st.image(im, caption="Input Image", use_column_width=True)
    
    ## SR

    st.image(im, caption="Output Image", use_column_width=True)
    
    button = st.button("Download")
    if button:
        print("valhalla")
