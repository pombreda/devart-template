Before I start doing the actual coding, here is a brief description of how I think all of this will work:

1. Image processing will be done in Python using the powerfull [OpenCV](http://opencv.org/) library. I think I should be able to get some quick results using a combination of [Canny Edge Detector](http://docs.opencv.org/doc/tutorials/imgproc/imgtrans/canny_detector/canny_detector.html) and/or [FindContours](http://docs.opencv.org/doc/tutorials/imgproc/shapedescriptors/find_contours/find_contours.html)
2. The list of points/lines (after some post-processing perhaps) should be converted into an [OSM XML](http://wiki.openstreetmap.org/wiki/OSM_XML) file
3. The OSM file will then be rendered into image tiles by a combination of [Mapnik](http://wiki.openstreetmap.org/wiki/Mapnik), some sort of [styling](http://wiki.openstreetmap.org/wiki/Mapnik#OSM_Standard_Mapnik_Style) to give it a look-an-feel of Google Maps and perhaps something for serving the tiles like [TileStache](http://tilestache.org/). All these are new to me so I have some more digging up to do before decinding of the final approach.
4. Displaying will be done in the browser using the Google Maps API and its [Image map types](https://developers.google.com/maps/documentation/javascript/examples/maptype-image)

Sounds easy enough, right? It will be fun to see how far away I end up from this initial "architecture".
I hope to have separate entries for each topic to document my findings, so we'll see.
