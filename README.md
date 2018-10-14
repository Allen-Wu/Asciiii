# AsciiStyleConvertor


Ascii Style Converter project for MHacks 2018

[![Made in MHacks](https://img.shields.io/badge/Made%20in-MHacks11-d41359.svg?style=flat)](https://mhacks.org)
[![Build Status](https://travis-ci.org/Allen-Wu/AsciiStyleConvertor.svg?branch=master)](https://travis-ci.org/Allen-Wu/AsciiStyleConvertor)

Asciiii is an ASCII style converter made during MHacks11. It supports image (jpg/jpeg/png/gif) inputs and ouputs the ASCII-style text strings depicted by the edge information of the input. 

<gif here>

[Asciiii](https://asciiii.com) is an ASCII style converter made during [MHacks11](https://mhacks.org). It supports image (jpg/jpeg/png/gif) inputs and ouputs the ASCII-style text strings depicted by the edge information of the input. 

<gif here>

## Table of Contents

- [Getting Started](## Getting Started)
  - [Prerequisites](###erequisites)
  - [Setup](###Setup)
- [Demo](## Demo) 
  - Web Application
  - Static and Gif Images in Terminal
  - Colored Edges
  - Real-time Streaming
- [Optimization Attempts](## Optimization Attempts)
  - Heuristics
  - Parallelism
    - Mulit-threading
    - Multi-processing
  - Machine Learning
    - MultiLayerPerceptron
    - Covolutional Neural Networks
- [Packages](## Packages)
  - Algorithm Packages
  - Server Packages

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

- quired libraries

```
pip install -r requirements.txt
```

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
