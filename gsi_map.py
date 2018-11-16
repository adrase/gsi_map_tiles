import math
import os
import shutil
import urllib
import Image

def deg2num(lat_deg, lon_deg, zoom):
  lat_rad = math.radians(lat_deg)
  n = 2.0 ** zoom
  xtile = int((lon_deg + 180.0) / 360.0 * n)
  ytile = int((1.0 - math.log(math.tan(lat_rad) + (1 / math.cos(lat_rad))) / math.pi) / 2.0 * n)
  return (xtile, ytile)

#zoom
zoom = 16

#bbox
#left lower
lat_min = 34.637163
lon_min = 135.475992
#right upper
lat_max = 34.737163
lon_max = 135.575992

def tile_range(lat_min, lon_min, lat_max, lon_max, zoom):
    x_min, y_max = deg2num(lat_min,lon_min,zoom)
    x_max, y_min = deg2num(lat_max,lon_max,zoom)
    return (x_min, x_max, y_min, y_max, zoom)

x_min, x_max, y_min, y_max, zoom = tile_range(lat_min, lon_min, lat_max, lon_max, zoom)

#folders structure & download
dir_path = os.path.dirname(os.path.realpath(__file__))
#print(dir_path)
shutil.rmtree(str(zoom), ignore_errors=True)
os.makedirs(str(zoom))
os.chdir(str(zoom))
zoom_dir = os.path.join(dir_path,str(zoom))
#print(zoom_dir)

#image creation
img_size_x = (x_max - x_min)*256 #tile size is 256
img_size_y = (y_max - y_min)*256 
#print (img_size_x, img_size_y)

new_img = Image.new('RGB', (img_size_x,img_size_y))
i = 0
j = 0

for x in range(x_min,x_max):
    print(x)
    os.makedirs(str(x))
    os.chdir(str(x))
    s_url = 'https://maps.gsi.go.jp/xyz/std/' + str(zoom) + '/' +str(x) + '/'
    for y in range(y_min, y_max):
        print(i,j)
        t_url = s_url + str(y) + '.png'
        fname = str(y) + '.png'
        print(t_url, fname)
        urllib.urlretrieve(t_url, fname)
        img = Image.open(fname)
        new_img.paste(img, (i,j))
        j += 256
    os.chdir(zoom_dir)
    i += 256
    j = 0
new_img.save("out.png")




