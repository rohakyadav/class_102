Topic Security System using webcam

Goal 

● Capture image from webcam using opencv python module 

● Create a python program which captures webcam image every few minutes and uploads on the dropbox

Last class we had worked on creating a program which performs remote backup service for our files.Today, we will be building a security program for our PC where we will capture a photo of anyone using our system every few minutes and then upload them to the remote cloud storage system simultaneously.

We can do that programmatically by using a library of python called OpenCV. OpenCV is a huge python library which can be used to capture images, manipulate images and perform other kinds of image processing works. We will be using OpenCV here to capture image from our webcam

Lets install the OpenCV library to our system. We will use pip3, the python package manager to install the library.

opens the terminal and writes command pip3 install opencv-python

Syntax: cv2.imwrite(filename, image) It takes 2 Parameters: -filename: A string representing the file name. The filename must include image format like .jpg, .png, etc. -image: It is the image that is to be saved.

There are other modules like time and random.

 [time.time()](https://time.time()/)

 module returns time in seconds and the random module helps us generate random numbers. To use these modules we need to import them first.