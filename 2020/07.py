#!/usr/bin/env python3
import sys
import os
import itertools
from dataclasses import dataclass, field

color_names = set()
colors = set()
texture_names = set()
textures = set()

@dataclass(frozen=True)
class Color:
    name : str

@dataclass(frozen=True)
class Texture:
    texture : str

class Bag:
    def __init__(self, color : Color, texture : Texture):
        self.color = color
        self.texture = texture
        self.contains = {}

    def __repr__(self):
        return f'Bag(color={self.color}, contains={self.contains})'

def get_colors():
    global rules
    color_list = []
    for r in rules:
        these_colors = get_colors_from_line(r)
        for c in these_colors:
            color_list.append(c)

    return set(color_list)

def get_colors_from_line(line):
    retval = []
    line_split = line.split()
    if len(line_split) > 7:
        retval.append(line_split[6])
    if len(line_split) > 11:
        retval.append(line_split[10])
    if len(line_split) > 15:
        retval.append(line_split[14])
    if len(line_split) > 19:
        retval.append(line_split[18])

    return retval


def get_textures():
    global rules
    texture_list = []
    for r in rules:
        these_textures = get_textures_from_line(r)
        for c in these_textures:
            texture_list.append(c)

    return set(texture_list)

def get_textures_from_line(line):
    retval = []
    line_split = line.split()
    if len(line_split) > 7:
        retval.append(line_split[0])
        if line_split[4].isdigit():
            retval.append(line_split[5])
    if len(line_split) > 11:
        retval.append(line_split[9])
    if len(line_split) > 15:
        retval.append(line_split[13])
    if len(line_split) > 19:
        retval.append(line_split[17])

    return retval

def read_rules(filename):
    r = []
    with open(filename, 'r') as f:
        for l in f:
            r.append(l.strip())

    return tuple(r)


if __name__ == '__main__':
    rules = read_rules('input07')

    colors = get_colors()
    print('Colors:', len(colors), colors)
    print('')

    textures = get_textures()
    print('Textures:', len(textures), textures)
