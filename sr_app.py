import base64
from io import BytesIO
from PIL import Image

import numpy as np

import streamlit as st
from tensorflow import keras


st.title("Super Resolution Web Application")

img_format = st.radio("Image Format", ["JPG", "PNG"])

if img_format == "JPG":
    ext = ".jpg"
else:
    ext = ".png"

st.set_option('deprecation.showfileUploaderEncoding', False)

im_file = st.file_uploader("Upload an Image", type=["jpg","png", "jpeg"])

def get_encoded_img(file, ext):
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  Image
    out: href string
    """
    if ext == ".jpg":
        ext_stuff = "JPEG"
    elif ext == ".png":
        ext_stuff = "PNG"
    
    buff = BytesIO()
    file.save(buff, ext_stuff)
    buff.seek(0)

    img_base64 = base64.b64encode(buff.read()).decode()

    href = f'<a href="data:image/jpg;base64,{img_base64}" download="SR_image{ext}">Download</a>'
    
    return href

if im_file is not None:
    im = Image.open(im_file).convert('RGB')
    # in place will be replaced by SR'ed image
    st.title("Input Image")
    st.image(im, use_column_width=True)

    model = keras.models.load_model('generator.h5')

    inputs = keras.Input((None, None, 3))
    output = model(inputs)
    model = keras.models.Model(inputs, output)
        
    # Read image
    low_res = np.array(im)

    # Rescale to 0-1.
    low_res = low_res / 255.0

    # Get super resolution image
    sr = model.predict(np.expand_dims(low_res, axis=0))[0]

    # Rescale values in range 0-255
    sr = (((sr + 1) / 2.) * 255).astype(np.uint8)
    # PIL Image
    sr_img = Image.fromarray(sr)
    st.title("Output Image")
    st.image(sr_img, use_column_width=True)
    ## SR
      
    st.markdown(get_encoded_img(sr_img, ext), unsafe_allow_html=True)
