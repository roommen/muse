import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('camera/Shelf_Image6.jpg',0)
ret,th1 = cv2.threshold(img,100,255,cv2.THRESH_BINARY)
width=th1.shape[0]
height=th1.shape[1]
def fill_rate(img,xmin,ymin,xmax,ymax):
    cp= img[xmin:xmax,ymin:ymax]
    width=(xmax-xmin)
    height=(ymax-ymin)
    count=0
    i=0
    j=0
    for i in range(width-1):
        for j in range(height-1):
            if cp[i,j] > 1:
                count =count+1
    #print 'count =',count
    #print 'area of window =',width*height
    fill_percent = round(float(count)/(float(height*width))*100)
    return fill_percent  

shelf=[]
i=0
for h in range(4*height/5)[::height/5]:
   # print 0,h,width,h+height/5
    fill=fill_rate(th1,0,h,width,h+height/5)
    i=i+1
#    print 'occupance for row:'+str(i)+'=',fill
    shelf.append(fill)
counter=1
json_text=""
for i in shelf:
    if counter ==1 :   
        json_text+= "{"
    json_text += "row" + str(counter)+':'+str(i)+','
    counter +=1
json_text=json_text[:-1]    
json_text += "}"
print json_text
