# Identity Card : Images Classification by Age and Gender using CNN, Personal Infos Extraction using OpenCV and PyTesseract

First introducing you with the terminologies used in this advanced python project of Gender and Age Classification and Text Extraction 

## What is Computer Vision?

Computer Vision is the field of study that enables computers to see and identify digital images and videos as a human would. The challenges it faces largely follow from the limited understanding of biological vision. Computer Vision involves acquiring, processing, analyzing, and understanding digital images to extract high-dimensional data from the real world in order to generate symbolic or numerical information which can then be used to make decisions. The process often includes practices like object recognition, video tracking, motion estimation, and image restoration.

## What is OpenCV?

OpenCV is short for Open Source Computer Vision. Intuitively by the name, it is an open-source Computer Vision and Machine Learning library. This library is capable of processing real-time image and video while also boasting analytical capabilities. It supports the Deep Learning frameworks TensorFlow, Caffe, and PyTorch.

## What is a CNN?

<p>A <em><strong><a href="https://data-flair.training/blogs/convolutional-neural-networks/">Convolutional Neural Network</a></strong></em> is a deep neural network (DNN) widely used for the purposes of image recognition and processing and <em><strong><a href="https://data-flair.training/blogs/nlp-natural-language-processing/">NLP</a></strong></em>. Also known as a ConvNet, a CNN has input and output layers, and multiple hidden layers, many of which are convolutional. In a way, CNNs are regularized multilayer perceptrons.</p>

# Gender and Age Detection Python Project Objective

<p>To build a gender and age detector that can approximately guess the gender and age of the person (face) in a Identity Card using <a href="https://data-flair.training/blogs/deep-learning/"><em><strong>Deep Learning</strong></em></a> on the Adience dataset.</p>

# Gender and Age Detection – About the Project

<p>In this Python Project, we will use Deep Learning to accurately identify the gender and age of a person from a single image of a face. The predicted gender may be one of ‘Male’ and ‘Female’, and the predicted age may be one of the following ranges- (0 – 2), (4 – 6), (8 – 12), (15 – 20), (25 – 32), (38 – 43), (48 – 53), (60 – 100) (8 nodes in the final softmax layer). It is very difficult to accurately guess an exact age from a single image because of factors like makeup, lighting, obstructions, and facial expressions. And so, we make this a classification problem instead of making it one of regression.</p>

## The CNN Architecture

The convolutional neural network for this python project has 3 convolutional layers:

<ul><li>Convolutional layer; 96 nodes, kernel size 7</li><li>Convolutional layer; 256 nodes, kernel size 5</li><li>Convolutional layer; 384 nodes, kernel size 3</li></ul>

It has 2 fully connected layers, each with 512 nodes, and a final output layer of softmax type.

To go about the python project, we’ll:

<ul><li>Detect faces</li><li>Classify into Male/Female</li><li>Classify into one of the 8 age ranges</li><li>Put the results on the image and display it</li></ul>

# The Dataset

The dataset has been linked in the main.py program......when u run the program, dataset will be downloaded automatically and load to the program training set. If u want use a different dataset. You can through the below link from Kaggle datasets.

<p>For this python project, we’ll use the Adience dataset; the dataset is available in the public domain and you can find it <em><strong><a href="https://www.kaggle.com/ttungl/adience-benchmark-gender-and-age-classification" onclick="javascript:window.open('https://www.kaggle.com/ttungl/adience-benchmark-gender-and-age-classification'); return false;">here</a></strong></em>. This dataset serves as a benchmark for face photos and is inclusive of various real-world imaging conditions like noise, lighting, pose, and appearance. The images have been collected from Flickr albums and distributed under the Creative Commons (CC) license. It has a total of 26,580 photos of 2,284 subjects in eight age ranges (as mentioned above) and is about 1GB in size. The models we will use have been trained on this dataset.</p>

## Prerequisites

You’ll need to install OpenCV (cv2) to be able to run this project. You can do this with pip

   * $ pip install opencv-python
   
Other packages you’ll be needing are math and argparse, but those come as part of the standard Python library.

## Text Extraction 
Personal Infos Extractor - Automatic Data Extraction from Identity Cards

Description:
We utilized computer vision and text extraction techniques to extract key information from identity cards. By uploading an image of our card, the application automatically parses the data and presents it in a clear and organized manner.

Features:

Automatic Data Extraction: Extracts essential fields from the card, including province, regency, identification number, name, gender, blood type, address, village, district, religion, marital status, profession, and validity period.
User-Friendly Interface: Simple and intuitive interface with a dedicated upload field and a well-structured display for the extracted data.
Image Processing: Robust image processing techniques handle variations in image quality and lighting conditions for accurate data extraction.

How to Use:

Install Dependencies: Ensure you have OpenCV, PyTesseract, and Flet libraries installed (pip install opencv-python pytesseract flet).
Run the Application: Execute the Python script (python main.py).
Upload Your card: Click the "Choose File" button and select an image of your identity card.
Process Data: Click the "Process" button to initiate the extraction process.
View Extracted Data: The extracted information will be displayed in the designated fields.


# Summary

In this python project, we implemented a CNN to detect gender and age and a text extractor from Identity Card.

If you enjoyed the above python project, do comment and let us know your thoughts.

Happy learning😊

Follow Me on LinkedIn at <a href = "https://www.linkedin.com/in/chakir-fatima-ez-zahra/">@_hemanth_shetty__</a>

#### ThankYou!

