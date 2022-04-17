#! /usr/bin/python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("horizontal", help="number of images along the horizontal axis",
                    type=int)
parser.add_argument("vertical", help="number of images along the vertical axis",
                    type=int)           
args = parser.parse_args()

h=args.horizontal
v=args.vertical

# position images in lines from left to right
image_order=list()
for x in range(0,h):
  for y in range(0,v):
    image_order.append(x+(y*h))

# reverse order (GIMP layer import order)
image_order.reverse()

counter = 0
for x in range(0,h):
  if x == h-1:
    for y in range(0,v):
      if y == v-1:
        print(str(image_order[counter])+')', end='')
        counter = counter + 1
        for y in range(0,v-2):
          print(')', end='')
      else:
        print('V('+str(image_order[counter])+',', end='')
        counter = counter + 1
    print(')', end='')
    
    for x in range(0,h-2):
      print(')', end='')
  else:
    print('H(', end='')
    for y in range(0,v):
      if y == v-1:
        print(str(image_order[counter])+')', end='')
        counter = counter + 1
        for y in range(0,v-2):
          print(')', end='')
      else:
        print('V('+str(image_order[counter])+',', end='')
        counter = counter + 1
    print(',', end='')
print('\n')