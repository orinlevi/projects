from typing import Coroutine
from time import sleep
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import cv2

act = [ (0, {(24, 21): 'green', (9, 4): 'blue', (10, 4): 'blue', (11, 4): 'blue'})]
ex =   (0, {(20, 15): 'black', (20, 14): 'black', (20, 13): 'black', (9, 4): 'blue', (10, 4): 'blue', (11, 4): 'blue', (24, 21): 'green'})

COLORS = {
    'red': [255, 0, 0],
    'black': [0, 0, 0],
    "green": [0, 255, 0],
    "orange": [255, 255, 0],
    "white": [255, 255, 255]}


size = 15
w, h = 40*size, 30*size
out = cv2.VideoWriter(
    'project.mp4', cv2.VideoWriter_fourcc(*'mp4v'),
    15, (w * 2, h), True)

for i in range(max(len(act), len(ex))):
    data = np.zeros((h, w*2, 3), dtype=np.uint8)
    data[:, :w] = [255, 255, 255]

    try:
        for coord, color in ex[i][1].items():
            x, y = coord[0] * size, coord[1] * size
            c = COLORS[color]
            data[y:(y+size), x:x+size] = c
    except:
        pass
    try:
        for coord, color in act[i][1].items():
            x, y = coord[0] * size, coord[1] * size
            c = COLORS["white" if color == "black" else color]
            x += w
            data[y:(y+size), x:x+size] = c
    except:
        pass
    data = np.flipud(data)
    img = Image.fromarray(data, 'RGB')
    for i in range(15):
        out.write(data)

out.release()
