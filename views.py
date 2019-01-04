"""
Routes and views for the flask application.
"""

from datetime import datetime
import DAC
import os
from flask import render_template, send_from_directory
from flask import Flask, request, flash,g, session
from DAC.algorithm.BL2xy import BL2xy
from DAC import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/BL',methods=['GET'])
def BL():
    BValue=float(request.args.get('B'))
    LValue=float(request.args.get('L'))
    x,y=BL2xy(BValue,LValue,0)
    return '转换后的平面坐标为x：'+ str(x) +'  转换后的平面坐标为y：'+ str(y) 

@app.route('/freq')
def freq():
     FreqX='[]' 
     FreqY='[]' 
     return render_template('shm//accfft.html',FreqX=FreqX,FreqY=FreqY)


@app.route('/freqCal')
def freqCal():
    FreqX='[0, 3.9063, 7.8125, 11.719, 15.625, 19.531, 23.438, 27.344, 31.25, 35.156, 39.063, 42.969, 46.875, 50.781, 54.688, 58.594, 62.5, 66.406, 70.313, 74.219, 78.125, 82.031, 85.938, 89.844, 93.75, 97.656, 101.56, 105.47, 109.38, 113.28, 117.19, 121.09, 125, 128.91, 132.81, 136.72, 140.63, 144.53, 148.44, 152.34, 156.25, 160.16, 164.06, 167.97, 171.88, 175.78, 179.69, 183.59, 187.5, 191.41, 195.31, 199.22, 203.13, 207.03, 210.94, 214.84, 218.75, 222.66, 226.56, 230.47, 234.38, 238.28, 242.19, 246.09, 250, 253.91, 257.81, 261.72, 265.63, 269.53, 273.44, 277.34, 281.25, 285.16, 289.06, 292.97, 296.88, 300.78, 304.69, 308.59, 312.5, 316.41, 320.31, 324.22, 328.13, 332.03, 335.94, 339.84, 343.75, 347.66, 351.56, 355.47, 359.38, 363.28, 367.19, 371.09, 375, 378.91, 382.81, 386.72, 390.63, 394.53, 398.44, 402.34, 406.25, 410.16, 414.06, 417.97, 421.88, 425.78, 429.69, 433.59, 437.5, 441.41, 445.31, 449.22, 453.13, 457.03, 460.94, 464.84, 468.75, 472.66, 476.56, 480.47, 484.38, 488.28, 492.19, 496.09, 500]' 
    FreqY='[0.042055, 0.034267, 0.1131, 0.027278, 0.06184, 0.0073596, 0.099505, 0.11018, 0.048843, 0.035937, 0.075456, 0.2087, 0.36568, 0.6459, 0.035291, 0.046618, 0.085817, 0.011569, 0.020745, 0.051647, 0.03244, 0.047147, 0.018124, 0.027503, 0.032603, 0.035543, 0.10101, 0.048506, 0.055406, 0.2392, 0.58495, 0.97803, 0.037765, 0.16159, 0.12311, 0.05546, 0.050514, 0.024156, 0.046132, 0.035743, 0.089351, 0.050963, 0.038724, 0.0085281, 0.0673, 0.030942, 0.013952, 0.024595, 0.0084223, 0.036954, 0.016023, 0.020934, 0.01701, 0.018168, 0.04372, 0.03889, 0.013744, 0.041648, 0.010051, 0.038201, 0.026588, 0.054384, 0.029333, 0.0082937, 0.01833, 0.039061, 0.00956, 0.031283, 0.01738, 0.019359, 0.0088286, 0.021496, 0.013689, 0.019912, 0.018182, 0.012886, 0.028003, 0.034604, 0.023191, 0.011059, 0.036406, 0.011225, 0.045051, 0.030731, 0.0063184, 0.04647, 0.015545, 0.025072, 0.036822, 0.018918, 0.027211, 0.020352, 0.02759, 0.017107, 0.028404, 0.029066, 0.040911, 0.038344, 0.021398, 0.015062, 0.013984, 0.033632, 0.031308, 0.02999, 0.040085, 0.021976, 0.034967, 0.030383, 0.016886, 0.024314, 0.037339, 0.027506, 0.025883, 0.026058, 0.029199, 0.0020038, 0.011274, 0.012234, 0.012581, 0.02685, 0.043819, 0.013955, 0.035128, 0.048968, 0.022686, 0.020141, 0.020696, 0.029351, 0.011434]' 
    
    return render_template('shm//accfft.html',FreqX=FreqX,FreqY=FreqY)

@app.route('/coor',methods=['GET','POST'])
def coor():
    XY=''
    if request.method == 'POST':
        varString=str(request.form['BLValue'])
        L0=str(request.form['L0'])
        #varString=str('29.0,121.32,121.0')
        varString=varString.replace('，',',')
        BL=varString.split(',')
        XY=BL2xy(float(BL[0]),float(BL[1]),float(L0))
        XY=varString + '-->' + str(XY)

    #return redirect(url_for('show_entries'))
    return render_template('demo//add-edit.html',var1=XY)

@app.route('/acc')
def acc():
     FreqX='[]' 
     FreqY='[]' 
     return render_template('shm//acceleration.html',FreqX=FreqX,FreqY=FreqY)

@app.route('/wind')
def wind():
    return render_template('shm//wind.html')

@app.route('/disp')
def disp():
    return render_template('shm//displacement.html')

@app.route('/vehicle')
def vehicle():
    return render_template('shm//vehicle.html')

@app.route('/strain')
def strain():
    return render_template('shm//strain.html')