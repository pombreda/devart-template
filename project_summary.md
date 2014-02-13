# Mapify

## Rares Barbantan : @rbarbantan

## Description
Mapify is an idea I've been contemplating for a while now, after seeing the amazing work of [Ed Fairburn](http://edfairburn.com/). He creates beautiful portraits on top of geological and street maps.
I began wondering if it would be possible to recreate images, be it portraits or landscapes using just street topography, basically "mapifying" images. Being passionate about mobile, I first thought about turning this into a mobile app but I could not figure out what exactly it would be: a toy, a game, an utility?
I just hoped it will just be something beautiful to look at. And for this reason I think of DevArt as a challenge, the perfect context, an exercise into bringing this idea to life.

So I am starting with this: process an image from a web camera, extract contours and lines, translate them into a map file representing streets and highways and render this file as a map in the browser. Will it work? Can it work? I don't know, but that's what I'm trying to find out; and hopefully, somewhere along the way learn a thing or two and maybe figure out how would one present this in a gallery.

Stay in touch for updates!


## Link to Prototype
Coming soon!

## Example Code

```python
gray = cv2.imread('homer.jpg',0)
edge = cv2.Canny(gray, 100, 200)
cv2.findContours(edge,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
```

## Links to External Libraries
[OpenCV](http://opencv.org/)
[Google Maps](https://developers.google.com/maps/documentation/javascript/)
[Numpy](http://www.numpy.org/)


## Images & Videos
![map](../project_images/map_homer_1.jpg "map")
![contours](../project_images/traced_einstein_1.jpg "contours")
![map](../project_images/map_einstein_1.jpg "map")