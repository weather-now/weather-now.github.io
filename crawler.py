import globalmaptiles
import shutil
import requests
import os

mercator = globalmaptiles.GlobalMercator()

def writeToFile(reqUrl, filename):
    try:
        os.makedirs(os.path.dirname(filename))
    except OSError:
        pass

    res = requests.get(reqUrl, stream=True)
    with open(filename, 'w') as f_out:
        shutil.copyfileobj(res.raw, f_out)
    res.close()

def latLngToTile(latlng, zoom):
    mx, my = mercator.LatLonToMeters(latlng['lat'], latlng['lng'])
    return mercator.MetersToTile(mx, my, zoom)

def crawl_at_zoom(northEast, southWest, z, pad, out_dir):
    URL = 'http://localhost:9090/styles/basic/%s/%s/%s.png'
    minx, miny = latLngToTile(southWest, z)
    maxx, maxy = latLngToTile(northEast, z)

    minx -= pad
    miny -= pad
    maxx += pad
    maxy += pad

    for x in range(minx, maxx + 1):
        for y in range(miny, maxy + 1):
            gx, gy = mercator.GoogleTile(x, y, z)
            reqUrl = URL % (z, gx, gy)
            print 'Get file from %s' % reqUrl
            filename = '%s/%s/%s.png' % (z, gx, gy)
            writeToFile(reqUrl, os.path.join(out_dir, filename))


def main():
    bounds = [ 124.3188, 32.36076, 132.3386, 38.64966 ]
#     northEast = {'lat': 42.827638636242284, 'lng':  146.18408203125003}
#     southWest = {'lat':  28.844673680771795, 'lng':  111.02783203125001}
    northEast = {'lat': bounds[3], 'lng':  bounds[2]}
    southWest = {'lat':  bounds[1], 'lng':  bounds[0]}

    out_dir = 'static/tiles'

    for z in range(6, 12):
        pad = 3
        crawl_at_zoom(northEast, southWest, z, pad, out_dir)

if __name__ == '__main__':
    main()