#!/usr/bin/env python
# ACCelerate22 code building upon 
#   https://github.com/pygame/pygame/blob/main/examples/sprite_dateTex1ture.py  
#   https://www.patreon.com/posts/finger-painting-43786073?l=fr
# Brygg Ullmer, Clemson University
# Begun 2022-01-23

import os, math
import pygame as pg

os.environ['SDL_MOUSE_TOUCH_EVENTS'] = '1'

if pg.get_sdl_version()[0] < 2:
    raise SystemExit("This example requires pygame 2 and SDL2.")

from pygame._sdl2 import Window, Texture, Image, Renderer, touch

data_dir = os.path.join(os.path.split(os.path.abspath(__file__))[0], "data")

def load_img(file): return pg.image.load(os.path.join(data_dir, file))

pg.display.init()
pg.key.set_repeat(10, 10)
#pg.event.set_grab(True)

win = Window("win1", resizable=True)
renderer = Renderer(win)

#winW = pg.display.get_surface().get_width()
#winH = pg.display.get_surface().get_height()

dateTex1 = Texture.from_surface(renderer, load_img("1860a.png"))
dateTex2 = Texture.from_surface(renderer, load_img("1880a.png"))

###################### distance between rectangle and point ######################
# Adaptation of MultiRRomero from:
# https://stackoverflow.com/questions/5254838/calculating-distance-between-a-point-and-a-rectangular-box-nearest-point

def distRectPoint(rect, x, y): 
  rminx = rect.x; rmaxx = rminx + rect.w
  rminy = rect.y; rmaxy = rminy + recty.h
  dx = max(rminx - x, 0, x - rmaxx)
  dy = max(rminy - y, 0, y - rmaxy)
  return sqrt(dx*dx + dy*dy)

###################### Date Sprite ######################

class DateSprite(pg.sprite.Sprite):
  def __init__(self, img):
    pg.sprite.Sprite.__init__(self)

    self.rect  = img.get_rect()
    self.image = img

    #self.rect.w *= 5; self.rect.h *= 5
    img.origin = self.rect.w / 2, self.rect.h / 2

###################### main ######################

d1 = DateSprite(Image(dateTex1, (0, 0, dateTex1.width-1, dateTex1.height-1)))
d1.rect.x = 250; d1.rect.y = 50

d2 = DateSprite(Image(dateTex2, (0, 0, dateTex1.width-1, dateTex1.height-1)))
d2.rect.x = 500; d2.rect.y = 50

group = pg.sprite.Group()
group.add(d1)
group.add(d2)

t = 0
running = True
clock = pg.time.Clock()
#renderer.draw_color = (255, 0, 0, 255)
renderer.draw_color = (1, 0, 0, 255)

#numTouchDevices = touch.get_num_devices()
#print("numTouchDevices:", numTouchDevices)

while running:
  for event in pg.event.get():
    if event.type == pg.QUIT:       running = False
    elif event.type == pg.KEYDOWN:
      if event.key == pg.K_ESCAPE:  running = False
      elif event.key == pg.K_LEFT:  d1.rect.x -= 5
      elif event.key == pg.K_RIGHT: d1.rect.x += 5
      elif event.key == pg.K_DOWN:  d1.rect.y += 5
      elif event.key == pg.K_UP:    d1.rect.y -= 5

    elif event.type == pg.VIDEORESIZE:
      winW, winH = event.size
      print("resize noted")

    elif event.type == pg.FINGERDOWN:
      print("fingerdown:  ", event.finger_id, event.x, event.y)
      targ = (event.x * winW, event.y * winH)
      animate(d1,tween='accel_decel', pos=targ, duration=0.5)

    elif event.type == pg.FINGERMOTION:
      print("fingermotion:", event.finger_id, event.x, event.y)

    elif event.type == pg.FINGERUP:
      print("fingerup    :", event.finger_id, event.x, event.y)

  renderer.clear()
  t += 1

  #img = sprite.image
  #img.angle += 1
  #img.flipX = t % 50 < 25
  #img.flipY = t % 100 < 50
  #img.color[0] = int(255.0 * (0.5 + math.sin(0.5 * t + 10.0) / 2.0))
  #img.alpha = int(255.0 * (0.5 + math.sin(0.1 * t) / 2.0))
  # img.draw(dstrect=(x, y, 5 * img.srcrect['w'], 5 * img.srcrect['h']))

  group.draw(renderer)

  renderer.present()

  clock.tick(60)
  win.title = str("FPS: {}".format(clock.get_fps()))

pg.quit()
