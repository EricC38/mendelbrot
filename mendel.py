from __future__ import division
from PIL import Image
import math
import cmath
from sys import argv

def comp_to_rgb(z):
  hprime=3*cmath.phase(z)/math.pi
  hprime=hprime%6
  x=(1-abs(hprime%2-1))
  if 0<=hprime<1:
    (red,green,blue)=(1,x,0)
  elif 1<=hprime<2:
    (red,green,blue)=(x,1,0)
  elif 2<=hprime<3:
    (red,green,blue)=(0,1,x)
  elif 3<=hprime<4:
    (red,green,blue)=(0,x,1)
  elif 4<=hprime<5:
    (red,green,blue)=(x,0,1)
  elif 5<=hprime<6:
    (red,green,blue)=(1,0,x)
  
  return (int(255*red),int(255*green),int(255*blue))


def is_in_mandel(c):
  z=0
  iter=0
  while abs(z)<1000 and iter<100:
    z=z**2+c
    iter+=1
      
  if abs(z)>=100:
    return False
  else: 
    return True
        
def mandel_color(c):
  z=0
  iter=0
  max_iter=100
  while iter<max_iter and abs(z)<1000:
    z=z**2+c
    iter+=1
  return abs(z)
    
def hsv_to_rgb(color):
  h=color[0]
  s=color[1]
  v=color[2]
  
  c=v*s
  h_prime=h/60
  x=c*(1-abs(h_prime%2-1))
  
  if h_prime>=0 and h_prime<1:
      (red, green, blue) = (c,x,0)
  elif h_prime>=1 and h_prime<2:
      (red, green, blue) = (x,c,0)
  elif h_prime>=2 and h_prime<3:
      (red, green, blue) = (0,c,x)
  elif h_prime>=3 and h_prime<4:
      (red, green, blue) = (0,x,c)
  elif h_prime>=4 and h_prime<5:
      (red, green, blue) = (x,0,c)
  elif h_prime>=5 and h_prime<6:
      (red, green, blue) = (c,0,x)
  else:
      (red, green, blue) = (0,0,0)
      
  m=v-c
  red+=m
  green+=m
  blue+=m
  
  return (int(255*red), int(255*green), int(255*blue))

    
white=(255,255,255)
black=(0,0,0)
    
script, filename = argv

size=1000
im = Image.new("RGB",(size,size))
p=im.load()

for x in range(size):
  for y in range(size):
    z = complex((x - size/2)/(size/2), (y - size/2)/(size/2))
    if is_in_mandel(z):
      p[x,y]=white
    else:
      p[x,y]=black
        
im.save(filename)


