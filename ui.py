import streamlit as st
from PIL import Image
import os, base64
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
   
    def download(filepath):
        read_file = open(os.path.join("downloads",filename)).read()
        bs64 = base64.b64encode(read_file.encode()).decode()
        href = '<a href="data:file/readfile:base64,{}">Download File</a>(click to download save as file name)'.format(b64)
        return href
    
   link = download(filepath)
   st.markdown(link,unsafe_allow_html=True)
   print("valhalla")
        
