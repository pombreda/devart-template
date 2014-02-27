import mapnik

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
print "rendered image to 'world.png'"