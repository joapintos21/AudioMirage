from py5 import *

def settings():
    size(400, 400)

def setup():
    background(200)

def draw():
    fill(255, 0, 0)
    ellipse(width / 2, height / 2, 100, 100)

run_sketch()