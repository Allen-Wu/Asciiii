# AsciiStyleConvertor


Ascii Style Convertor project for MHacks 2018

[![Made in MHacks](https://img.shields.io/badge/Made%20in-MHacks11-d41359.svg?style=flat)](https://mhacks.org)
[![Build Status](https://travis-ci.org/Allen-Wu/AsciiStyleConvertor.svg?branch=master)](https://travis-ci.org/Allen-Wu/AsciiStyleConvertor)

Asciiii is an ASCII style converter made during MHacks11. It supports image (jpg/jpeg/png/gif) inputs and ouputs the ASCII-style text strings depicted by the edge information of the input. 

<gif here>

Table of Contents

- Getting Started
  - Prerequisites
  - Setup
- Demo 
  - Web Application
  - Static and Gif Images in Terminal
  - Colored Edges
  - Real-time Streaming
- Optimization Attempts
  - Heuristics
  - Parallelism
    - Mulit-threading
    - Multi-processing
  - Machine Learning
    - MultiLayerPerceptron
    - Covolutional Neural Networks
- Packages
  - Algorithm Packages
  - Server Packages

Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

Prerequisites

- Clone the GitHub repository

    git clone git@github.com:Allen-Wu/AsciiStyleConvertor.git

Setup

- quired libraries

    pip install -r requirements.txt

- Install required libraries

    pip install -r requirements.txt

- Run the program in terminal

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
    

Demo



Packages

Algorithm Packages

- 
- 

Server Packages
