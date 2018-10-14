# Asciiii

[![Made in MHacks](https://img.shields.io/badge/Made%20in-MHacks11-d41359.svg?style=flat)](https://mhacks.org)
[![Build Status](https://travis-ci.org/Allen-Wu/AsciiStyleConvertor.svg?branch=master)](https://travis-ci.org/Allen-Wu/AsciiStyleConvertor)

[Asciiii](https://asciiii.com) is an ASCII style converter made during [MHacks11](https://mhacks.org). It supports image (jpg/jpeg/png/gif) inputs and outputs the ASCII-style text strings depicted by the edge information of the input. 

<img src="https://github.com/Allen-Wu/AsciiStyleConvertor/blob/master/dataset.gif" width="300">

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Setup](#setup)
- [Demo](#demo) 
  - [Web Application](#web-application)
  - [Static Images and Gif](#static-images-and-gif)
  - [Colored Edges](#colored-edges)
  - [Real-time Streaming](#real-time-streaming)
- [Optimization Attempts](#optimization-attempts)
  - [Heuristics](#heuristics)
  - [Parallelism](#parallelism)
    - [Mulit-threading](#multi-threading)
    - [Multi-processing](#multi-processing)
  - [Machine Learning](#machine-learning)
    - [Multi-layer-perceptron](#multi-layer-perceptron)
    - [Machine-generated dataset](#machine-generated-dataset)
- [Packages](#packages)
  - [Algorithm Packages](#algorithm-packages)
  - [Server Packages](#server-packages)
  

## Getting Started
There are two ways of accessing our project.

- Visit our [website](http://asciiii.com)
- Clone the repo and run it on your own machine

These following instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Clone the GitHub repository

```
git clone git@github.com:Allen-Wu/AsciiStyleConvertor.git
```

### Setup

- Install required libraries

```
pip install -r requirements.txt
```

- Run the program in terminal

```
python main.py -h
usage: main.py [-h] [-f FILE] [-l LINE] [-v] [-e ETA] [-li] [-g]

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  input image file path
  -l LINE, --line LINE  desired image width
  -v, --video           real-time video mode, need your camera
  -e ETA, --eta ETA     hyper-parameter for ascii matching
  -li, --light          use a small set of ascii with high frequenty
  -g, --gif             generate a real-time gif with specific duration

```

## Demo

#### Web Application

#### Static Images and Gif

Static Image               |  Gif
:-------------------------:|:-------------------------:
<img src="https://github.com/Allen-Wu/AsciiStyleConvertor/blob/master/static_img.png" width="450">  |  <img src="https://github.com/Allen-Wu/AsciiStyleConvertor/blob/master/stream_gif.gif" width="450">

#### Colored Edges
![alt text](https://github.com/Allen-Wu/AsciiStyleConvertor/blob/master/data/demo/color.jpg)

#### Real-time Streaming


## Optimization Attempts
The bottleneck of the algorithm mainly lies in the computation process of determining the proper ascii character for each subpart of the input image. The computation process focuses on the comparing similarity of two grids based on the Hamming Distance. We try to optimize this process by different approaches.


#### Heuristics
Several heuristics methods can be used to directly map one subpart of image into an ascii character. For example, if the average pixel value is lower than one low threshold, it can be directly mapped to a empty space character.

#### Parallelism

##### Multi-threading
We try using multi-threading module `threading` and assign one thread for each subpart computing. The best number of threads is between 8 and 10. However, the cost of creating thread is higher than expected, and the performance is worse than single thread.

##### Multi-processing
Similar approach is used for multi-processing method, which is based on python module `Pool` module. However, the cost of creating separate process is also too high.


#### Machine Learning
In the field of computer vision, machine learning is very popular to analysis the feature in the image. We tried to implement a neural network to classify the windows in the target images based on which ascii character is most similar to the pixels graphically. 

##### Multi-layer-perceptron
Since the sketch image after edge detection can be impressed as a binary image, we employ the multi-layer-percepton instead of complicated neural network such as CNN. The validation accuracy is limited to 70% on the dataset we generated. 

##### Machine-generated dataset
The baseline method is using Hamilton distance to measure the similarity between image windows and asciiii characters. For lack of time, we use the Hamilton algorithm instead of labeling the image window by hand to generate training data. As a result, the validation accuracy is not very impressive. 

We also print windnow and compare the prediction of two algorithms and find the machine learning model makes no more sense. 
In the following picture, "target" corresponds to Hamilton algorithm and prediction corresponds to machine learning. 

![alt text](https://github.com/Allen-Wu/AsciiStyleConvertor/blob/master/machine_learning/model_cmp/12.png)

## Packages

#### Algorithm Packages
- [numpy](http://www.numpy.org/), scientific computing and matrix operations
- [scipy](https://www.scipy.org/), numerical algorithms and statistics
- [opencv-python](https://opencv-python-tutroals.readthedocs.io/en/latest/), computer visions and image processing
- [imageio](https://imageio.github.io/), interface for read and write images
- [PIL](https://pillow.readthedocs.io/), Python image library
- [matplotlib](https://matplotlib.org/), produce quality figures
- [torch](https://pytorch.org/), neural networks

#### Server Packages
- [flask](http://flask.pocoo.org/), built-in web application server
- [sh](https://amoffat.github.io/sh/), function caller
- [Werkzeug](http://werkzeug.pocoo.org/), WSGI utility library
- [Jinja2](http://jinja.pocoo.org/docs/2.10/), HTML templates

