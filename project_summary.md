# Mapify

## Rares Barbantan : @rbarbantan

## Description
Mapify is an idea I've been contemplating for a while now, after seeing the amazing work of [Ed Fairburn](http://edfairburn.com/). He creates beautiful portraits on top of geological and street maps like this one:
![inspiration](../project_images/inspiration.jpg)

I began wondering if it would be possible to recreate images, be it portraits or landscapes using just street topography, basically "mapifying" images. Being passionate about mobile, I first thought about turning this into a mobile app but I could not figure out what exactly it would be: a toy, a game, an utility?
I just hoped it will just be something beautiful to look at. And for this reason I think of DevArt as a challenge, the perfect context, an exercise into bringing this idea to life.

So I am starting with this: process an image from a web camera, extract contours and lines, translate them into a map file representing streets and highways and render this file as a map in the browser. Will it work? Can it work? I don't know, but that's what I'm trying to find out; and hopefully, somewhere along the way learn a thing or two and maybe figure out how would one present this in a gallery.

Stay in touch for updates!


## Link to Prototype
Coming soon!

## Example Code

```python
gray = cv2.imread('homer.jpg',0)
gray = cv2.blur(gray,(3,3))
edge = cv2.Canny(gray, 50, 150)
cv2.findContours(edge,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

...

m = mapnik.Map(1000,500)
m.background = mapnik.Color('#e9e5dc')
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer(mapnik.Color('#deb'))
r.symbols.append(polygon_symbolizer)
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('#fff'),2)
r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('My Style',s)
ds = mapnik.Datasource(type='geojson', file='output.json')
layer = mapnik.Layer('world')
layer.datasource = ds
layer.styles.append('My Style')
m.layers.append(layer)
m.zoom_all()
mapnik.render_to_file(m,'world.png', 'png')
```

## Links to External Libraries
[OpenCV](http://opencv.org/)
[Google Maps](https://developers.google.com/maps/documentation/javascript/)
[Numpy](http://www.numpy.org/)
[Mapnik](http://mapnik.org/)
[TileMill](https://www.mapbox.com/tilemill/)
[Tilestache](http://tilestache.org/)

## Images & Videos
http://www.youtube.com/watch?v=HX-Sn3gT_is
![map](../project_images/map_homer_1.jpg "map")
![contours](../project_images/traced_einstein_1.jpg "contours")
![map](../project_images/map_einstein_1.jpg "map")
