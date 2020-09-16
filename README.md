# ImageSR-web
Image in - Image out, simplifying your SR needs.

#### Dependencies:
- Streamlit
- Tensorflow 2.x
- NumPy

#### Steps to Run:
1. ```pip install -r requirements.txt```
2. ```streamlit run sr_app.py```

#### Motivation
Zooming into a image we get alot of noise rather than the desired
Output now to solve this using computer vision we can train a 
Neural Network in a way that it generates images with super
Resolution.
#### Working 
In the initial stages we had the option to train a simple cnn
But that would require alot of computation and at the end of the day
Didnt give desired results thus the next step was to implement
A Generative Adversarial Network which was trained on a set of 
Images to give a super res output.
The output is Upsampled to 4X.
#### References:
- [Fast SRGAN](https://github.com/HasnainRaz/Fast-SRGAN)
