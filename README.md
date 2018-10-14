# Asciiii

[![Made in MHacks](https://img.shields.io/badge/Made%20in-MHacks11-d41359.svg?style=flat)](https://mhacks.org)
[![Build Status](https://travis-ci.org/Allen-Wu/AsciiStyleConvertor.svg?branch=master)](https://travis-ci.org/Allen-Wu/AsciiStyleConvertor)

[Asciiii](https://asciiii.com) is an ASCII style converter made during [MHacks11](https://mhacks.org). It supports image (jpg/jpeg/png/gif) inputs and ouputs the ASCII-style text strings depicted by the edge information of the input. 

<gif here>

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Setup](#setup)
- [Demo](#demo) 
  - [Web Application](#web-application)
  - [Static Images in Terminal and Gif](#static-images-in-terminal-and-gif)
  - [Colored Edges](#colored-edges)
  - [Real-time Streaming](#real-time-streaming)
- [Optimization Attempts](#optimization-attempts)
  - [Heuristics](#heuristics)
  - [Parallelism](#parallelism)
    - [Mulit-threading](#multi-threading)
    - [Multi-processing](#multi-processing)
  - [Machine Learning](#machine-learning)
    - [Multi-layer-perceptron](#multi-layer-perceptron)
    - [Convolutional Neural Networks](#convolutional-neural-networks)
- [Packages](#packages)
  - [Algorithm Packages](#algorithm-packages)
  - [Server Packages](#server-packages)
  
## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

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

#### Web Application

#### Static Images in Terminal and Gif

#### Colored Edges

#### Real-time Streaming


## Optimization Attempts

#### Heuristics

#### Parallelism

##### Multi-threading

##### Multi-processing


#### Machine Learning

##### Multi-layer-perceptron

##### Convolutional Neural Networks

## Packages

#### Algorithm Packages
- numpy
- scipy
- opencv-python
- imageio
- PIL
- shutil
- matplotlib
- torch

#### Server Packages
- flask
- sh
- setup
- util
