Let me start by saying things did not progress as I expected. The previews I have shown before were rendered manually using the [Maperitive](http://maperitive.net/) desktop software.
Before I continued optimizing the image processing algorithm, I set out to build my automatic rendering pipeline. This meant replacing Maperitive with a proper renderer. Digging around pointed to [Mapnik](http://mapnik.org/) being the preferred rendering engine for most tools (and it also has python bindings).
It seemed pretty straight forward. Well, a couple of days .. , two virtual machines, AND several attempts to compile three libraries and two servers .. later, I managed to get the python bindings to Mapnik to work. And that's in Windows, I still have some strange error in Ubuntu to figure out later.

Now, it seems the XML format used by OpenStreetMap is not very popular (imagine that!) and that people/tools prefer to use either a database or [GeoJSON](http://geojson.org/). So I added the possibility to export my contours as JSON as well, and feed this JSON to Mapnik.

```python
import mapnik

#define map size and background colour
m = mapnik.Map(800,600)
m.background = mapnik.Color('steelblue')

...
#add custom styling rules
s = mapnik.Style()
r = mapnik.Rule()
r.symbols.append(line_symbolizer)
m.append_style('My Style',s)
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('rgb(50%,50%,50%)'),0.1)
s.rules.append(r)

#define json file as data source
ds = mapnik.Datasource(type='geojson', file='output.json')
layer = mapnik.Layer('world')
layer.datasource = ds
layer.styles.append('My Style')
m.layers.append(layer)

#prepare and print the map as a .png file
m.zoom_all()
mapnik.render_to_file(m,'world.png', 'png')
```

The beautiful thing about Mapnik is that it allows you to customize your map like crazy, but the downside is that I need to learn how to do that as well, as I don't get a nice default styling as I did with Maperitive. So with the very basic styling defined above, I get a very ugly rendering compared to what I had before:
![mapnik rendering](../project_images/map_homer_2.png)

Still, I consider this as progress, as Mapnik has more tricks up its sleeve. It has a custom xml format in which I can define the styling of the map. And the good news I do not need to write it myself, but I can use [TileMill](https://www.mapbox.com/tilemill/). I played with it already and it's quite promising: it is basically a desktop application that allows you to style your map using something resembling .css which is much more friendly than xml:
![TileMill](https://www.mapbox.com/tilemill/img/hero-tilemill.png)

Once I am happy with my styling, I can export the entire project as a Mapnik XML. Or at least that's the theory, but I'll leave that for another day.