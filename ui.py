import streamlit as st
from PIL import Image
import os
import copy

st.set_option('deprecation.showfileUploaderEncoding', False)

im_file = st.file_uploader("Choose an image", type=["jpg","png", "jpeg"])

if im_file is not None:
    im = Image.open(im_file)
    
    # in place will be replaced by SR'ed image
    second_im = copy.deepcopy(im)
    st.image(im, caption="Input Image", use_column_width=True)
    
    ## SR

    st.image(second_im, caption="Output Image", use_column_width=True)
    
    html_download = '<a href="output_img_from_the_model" download><img src="output_img_from_the_model" alt="thumbnail" width="120"/></a>'

    st.markdown(html_download,unsafe_allow_html=True)

    st.text("valhalla")
