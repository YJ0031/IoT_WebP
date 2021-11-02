from flask import Flask, redirect, url_for, render_template, request, Response, stream_with_context
from flask import jsonify

#Imports for camera
import cv2
from camera import VideoCamera

#Imports for home data
import pandas as pd
import dash
import plotly.express as px
from dash_application import create_dash_application

#Imports for controlling LED
import os 
import json
############## Main code begins here ####################

app = Flask(__name__)
create_dash_application(app)


############# Home page related code
@app.route('/')
def index():
    """Home Page"""
    return render_template('index.html')

############# Camera related code
def gen(camera):
    while True:
        data = camera.get_frame()

        frame = data[0]
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video')
def video():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed')
def video_feed():
    """Camera Feed"""
    return render_template('camera.html')

#############Home data related code

@app.route('/home_data')
def home_data():
    
    """Home data"""

    return render_template('home.html')

#############LED related code
@app.route('/_led')
def _led():
    state = request.args.get("state")
    s = {
            "led" : state
    }
    fname = os.path.join(app.static_folder, "sample.json")

    with open(fname, "w") as outfile:
        jsson.dump(s, outfile)

    return ""

@app.route('/read')
def readJSON():
    fname = os.path.join(app.static_folder, "sample.json")

    with open(fname, "r") as openfile:
        json_obj = json.load(openfile)
    return json_obj['ledl']

@app.route('/led_control')
def led_control():
    return render_template('control_led.html')


if __name__ == '__main__':

    app.run(debug=False)

