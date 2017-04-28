#!/usr/bin/env python3

'''
    Python Serpinski Triangle Generator
        utilizing randomly incrimented point
        placement within a pre-defined triangle
        determined by randomly selecting a vertex
        then translating half way towards that vertex
        from the current point
        Begin with a 'random' point inside the triangle
        
    Created by Justyn Chaykowski, github.com/frawst
    git:github.com/frawst/thetriangle
    
    #TODO
    # generating a random start point inside the triangle
    # Fucking comment and organize shit, jezus damn.
    # Impliment parameter naming
    # Impliment paramater image sizing
    # Impliment parameter dot-count
'''

from graphics import *
from random import *
import time
from PIL import Image as NewImage
from math import *

def main():
    
    def doDraw(thing):
        thing.draw(win)
        
    def unDraw(thing):
        thing.undraw()
    
    def randVal():
        value = randint(0,4085)
        return value
    
    def rgbMap(val, limiter):
        val2 = (val/limiter) * 255
        int(val2)
        return int(val2)
    
    def dfc(pointx, pointy, originx, originy):
        output = abs(sqrt(pow(pointx - originx, 2) + pow(pointy - originy, 2)))
        return int(output)
            
    def allAsCircles(item):
        for i in item:
            c = Circle(i, 2)
            # if item.index(i) % 2 == 1:
            #     c.setFill('red')
            # else:
            #     c.setFill('green')
            # dfc = abs(sqrt(pow(startx - i.getX(), 2) + pow(starty - i.getY(), 2)))
            # int(dfc)
            '''
            c.setFill(color_rgb(rgbMap(i.getY(),height), rgbMap(i.getX(), width),
                                rgbMap(dfc(i.getX(), i.getY(), originx, originy), width)))
            c.setOutline(color_rgb(rgbMap(i.getY(),height), rgbMap(i.getX(), width),
                                rgbMap(dfc(i.getX(), i.getY(), originx, originy), width)))'''
                                
            c.setFill(color_rgb(rgbMap(i.getY(), height), rgbMap(i.getX(), width), 200))
            c.setOutline(color_rgb(rgbMap(i.getY(),height), rgbMap(i.getX(), width), 200))
            doDraw(c)
            if item.index(i)%150 == 1:
                print ("Drawn ", item.index(i), " points in ", time.clock() - epochtime, ".")
            
    def genBGPixels():
        bgpixels = []
        for x in range(width):
            for y in range(height):
                newpoint = Point(x,y)
                #newpoint.setFill(color_rgb(rgbMap(dfc(x,y,originx,originy), 1600)), rgbMap(dfc(x,y,originx,originy), 1600), rgbMap(dfc(x,y,originx,originy), 1600))
                bgpixels.append(newpoint)
                
        return bgpixels
            
    def doDrawCircles(thing):
        c = Circle(thing, 2)
        c.setFill('red')
        doDraw(c)
            
    def genPoint():  # Create the next point
        lastPoint = points[-1]
        lastPointX = lastPoint.getX()
        lastPointY = lastPoint.getY()
        
        compare = randVal()
        
        if compare % 3 + 1 == 1:
            focusPoint = triangle[0]
            focusPointX = focusPoint[0]
            focusPointY = focusPoint[1]
        elif compare % 3 + 1 == 2:
            focusPoint = triangle[1]
            focusPointX = focusPoint[0]
            focusPointY = focusPoint[1]
        else:
            focusPoint = triangle[2]
            focusPointX = focusPoint[0]
            focusPointY = focusPoint[1]
            
        if focusPointX > lastPointX:
            newX = ((focusPointX - lastPointX) / 2) + lastPointX
        else:
            newX = ((lastPointX - focusPointX) / 2) + focusPointX
        
        if focusPointY > lastPointY:
            newY = ((focusPointY - lastPointY) / 2) + lastPointY
        else:
            newY = ((lastPointY - focusPointY) / 2) + focusPointY
            
        newpoint = Point(newX, newY)
        newpoint.setFill('red')
        points.append(newpoint)
    
    width = 2000
    height = 1600
    triangle = [[0, 0], [width, 0], [width/2, height]] # Starting Triangle
    originx = width/2
    originy = height/2
    # triangle = [[50, 50], [150, 50], [150, 150]] # Starting Triangle
    # startx =  125
    # starty = 60
    points = []
    loop = True
    
    drawAsCircles = True
    
    startpoint = Point(originx, originy)
    
    win = GraphWin('Serpinski Triangle', width, height) # Base Window
    win.setBackground('black')
    setdress = Rectangle(Point(0,0),Point(width,height))
    setdress.setFill('black')
    
    # Create the pseudo-random first point
    # TODO: Figure out how to generate a random point inside a triangle
    # newpoint = Point(randrange())

    
    for i in triangle: # Generates points for initial triangle
        item = Point(i[0],i[1])
        points.append(item)
        
    points.append(startpoint)
    
    # for z in range(10000):
    epochtime = time.clock()
    loopcount = 0
    while loop:
        nowtime = time.clock()
        
        genPoint()
        
        # for i in points:
        #     unDraw(i)
        #     doDraw(i)
        #     #doDrawCircles(i)
            
        pdrawtime = time.clock() - nowtime
        print ("time since last point = ", pdrawtime)
        
        loopcount += 1
        
        #allAsCircles(points)
        
        if win.checkMouse():
            loop = False
        
        if loopcount >= 5000:
            loop = False
        
    pointtime = time.clock() - epochtime
    print ("Overall time calculating points: ", pointtime)
    print ("Points added: ", len(points))
    setdress.draw(win)
    # sdpoints = genBGPixels()
    # for i in sdpoints:
    #     doDraw(i)
    
    if drawAsCircles == False:
        for i in points:
            #unDraw(i)
            doDraw(i)
            if points.index(i)%150 == 1:
                print ("Drawn ", points.index(i), " points in ", time.clock() - epochtime, ".")
    else:
        allAsCircles(points)

        
    drawtime = time.clock() - epochtime
    print ("Overall time post drawing: ", drawtime)
    
    # imagefile = Image(width, height)
    # imagefile.draw(win)
    # imagefile.save('lasttfile.png')
    
    print ("Converting TKinter properties to images...")
    win.postscript(file='image.eps', colormode='color')
    img = NewImage.open('image.eps')
    img.save('new5.png', 'png')
    
    print ("File saved as new3.png")
    time.sleep(0.5)
    win.getMouse()
    win.close()
    
main()
