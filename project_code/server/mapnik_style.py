__author__ = 'rares'

import mapnik

stylesheet = 'mapify_style.xml'
image = 'mapify_style.png'
m = mapnik.Map(1000, 500)
mapnik.load_map(m, stylesheet)
m.zoom_all()
mapnik.render_to_file(m, image)
print "rendered image to '%s'" % image