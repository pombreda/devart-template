__author__ = 'rbarbantan'

import numpy as np
import cv2
import random

w = h = 0
map_bounds = [[23.57, 23.59], [46.75, 46.74]]
names = ['Einstein','Bohr','Darwin','Pasteur','Freud','Galilei','Kepler','Copernicus','Faraday','Heisenberg']

def nothing(*arg):
    pass

def getUniqueId(lineIndex, pointIndex):
    return 5000 + 1000*lineIndex + pointIndex

def saveMap(contours):
    output = open('output.osm','w+')
    output.write("<osm>")

    for i,contour in enumerate(contours):
        for j,point in enumerate(contour):
            id = getUniqueId(i,j)
            lon = np.interp(point[0][0], [0,w],map_bounds[0])
            lat = np.interp(point[0][1], [0,h],map_bounds[1])
            output.write("<node id='{id}' visible='true' user='rbarbantan' lat='{lat}' lon='{lon}'/>".format(id=id,lat=lat,lon=lon))

    for i,contour in enumerate(contours):
        output.write("<way id='{id}' visible='true' user='rbarbantan'>".format(id=i))
        for j,point in enumerate(contour):
            id = getUniqueId(i,j)
            output.write("<nd ref='{id}'/>".format(id=id))
        output.write("<tag k='highway' v='residential'/>")
        output.write("<tag k='is_in:city' v='Cluj-Napoca'/>")
        output.write("<tag k='name' v='{street} St.'/>".format(street=random.choice(names)))
        output.write("</way>")

    output.write("<bounds minlat='{minlat}' minlon='{minlon}' maxlat='{maxlat}' maxlon='{maxlon}'/>".format(minlat=map_bounds[1][0],minlon=map_bounds[0][0],maxlat=map_bounds[1][1],maxlon=map_bounds[0][1]))
    output.write("</osm>")
    output.close()
    print 'saved to file'


cap = cv2.VideoCapture(0)
surf = cv2.SURF(400)

cv2.namedWindow('edge')
cv2.createTrackbar('thrs1', 'edge', 1000, 5000, nothing)
cv2.createTrackbar('thrs2', 'edge', 2000, 5000, nothing)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #gray = cv2.imread('homer.jpg',0)
    gray = cv2.imread('einstein.jpg',0)

    h,w = gray.shape

    #thrs1 = cv2.getTrackbarPos('thrs1', 'edge')
    #thrs2 = cv2.getTrackbarPos('thrs2', 'edge')
    edge = cv2.Canny(gray, 100, 200)

    #ret,thresh = cv2.threshold(gray,127,255,0)
    contours, hierarchy = cv2.findContours(edge,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    cv2.drawContours(gray, contours, -1, (0,255,0), 3)
    # Display the resulting frame
    cv2.imshow('frame',gray)
    key = cv2.waitKey(1)

    if key == ord('s'):
        saveMap(contours)
        cv2.imwrite('traced.png',gray)
    elif key == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
