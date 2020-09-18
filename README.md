# ImageSR-web
Image in - Image out, simplifying your SR needs.

## Motivation:
With the latest advancement in the field of screens and displays technologies, image quality seems to somewhat fall short in delivering the best experience on the amazing displays available to us. Image Super Resolution aids us to upscale our low quality images to fit modern displays.

## Behing the curtains:
Super resolution is a form of interpolation enabled by deep learning which allows for creating higher resolution images from lower resolution inputs. This is done via the use of a non-linear mapping learnt by a deep neural network between the low and high resolution feature space.
## Requirements:
Python 3.8 or above will all [requirements](requirements.txt) dependencies installed. To install run:
```python
$ pip install -r requirements.txt
```
## To run:
```python
$ streamlit run sr_app.py
```
## Tutorial:
#### Upload the image you want to run under the module and download the output image.
![tutorial](ImageSR_tutorial.gif "Tutorial")

## References:
- [Fast SRGAN](https://github.com/HasnainRaz/Fast-SRGAN)