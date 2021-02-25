import random
import colorsys

from display import *
from draw import *

def new_hsv_to_rgb(h, s, v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h,s,v))

def complementary(r, g, b):
	hsv = colorsys.rgb_to_hsv(round(r/255), round(g/255), round(b/255))
	return new_hsv_to_rgb((hsv[0] + 0.5) % 1, hsv[1], hsv[2])

s = new_screen()

dx = XRES
dy = YRES

for i in range(dx):
	r = random.randint(0, 255)
	g = random.randint(0, 255)
	b = random.randint(0, 255)
	color = [r, g, b]

	ir, ig, ib = complementary(r, g, b)
	icolor = [ir, ig, ib]

	draw_line(i, 0, i, dy, s, color)
	draw_line(XRES, dy, i, dy, s, icolor)

	dy -= 1

display(s)
save_extension(s, 'lines.png')
