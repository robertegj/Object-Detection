# Object-Detection
Object detection for video streams (webcams, IP cameras, video files) using Tensorflow.
## Installation Instructions
Follow Tensorflow setup instructions here:
https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/installation.md

This requires protobuf compilation!  
Once that's done, just run:  
__Windows:__  
set FLASK_APP=main.py  
flask run  
__Linux:__  
export FLASK_APP=main.py  
python3 -m flask run  

Then check your browser! See Flask guide for production hosting (port forwarding, CORS)  
## See it in action
![that's me!](https://github.com/robertegj/Object-Detection/blob/master/screenshot.gif)
