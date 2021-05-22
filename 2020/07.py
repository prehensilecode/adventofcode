#!/usr/bin/env python3
import sys
import os
import itertools
import argparse
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
        self.contains = set()

    # XXX
    def __hash__(self):
        return hash((self.color, self.texture))

    def __repr__(self):
        return f'Bag(texture={self.texture}, color={self.color}, contains={self.contains})'

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()

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
        retval.append(Color(line_split[6]))
    if len(line_split) > 11:
        retval.append(Color(line_split[10]))
    if len(line_split) > 15:
        retval.append(Color(line_split[14]))
    if len(line_split) > 19:
        retval.append(Color(line_split[18]))

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
        retval.append(Texture(line_split[0]))
        if line_split[4].isdigit():
            retval.append(Texture(line_split[5]))
    if len(line_split) > 11:
        retval.append(Texture(line_split[9]))
    if len(line_split) > 15:
        retval.append(Texture(line_split[13]))
    if len(line_split) > 19:
        retval.append(Texture(line_split[17]))

    return retval

def read_rules(filename):
    r = []
    with open(filename, 'r') as f:
        for l in f:
            r.append(l.strip())

    return tuple(r)


def setup_bags():
    global rules
    bags = set()
    for r in rules:
        rule = r.split()
        print(len(rule), rule)
        this_bag = Bag(texture=Texture(rule[0]), color=Color(rule[1]))
        if len(rule) == 7:
            continue

        if len(rule) >= 8:
            b2 = Bag(texture=Texture(rule[5]), color=Color(rule[6]))
            if not b2 in bags:
                bags.add(b2)
            this_bag.contains.add((b2, int(rule[4])))

        if len(rule) >= 12:
            b3 = Bag(texture=Texture(rule[9]), color=Color(rule[10]))
            if not b3 in bags:
                bags.add(b3)
            this_bag.contains.add((b3, int(rule[8])))

        if len(rule) >= 16:
            b4 = Bag(texture=Texture(rule[13]), color=Color(rule[14]))
            if not b4 in bags:
                bags.add(b4)
            this_bag.contains.add((b4, int(rule[12])))

        if len(rule) >= 20:
            b5 = Bag(texture=Texture(rule[17]), color=Color(rule[18]))
            if not b5 in bags:
                bags.add(b5)
            this_bag.contains.add((b5, int(rule[16])))

        bags.add(this_bag)

    return bags

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Advent of Code 2020 #7')
    parser.add_argument('rulefile', nargs='?', type=str, default='input07')
    args = parser.parse_args()

    rules = read_rules(args.rulefile)

    colors = get_colors()
    print('Colors:', len(colors), colors)
    print('')

    textures = get_textures()
    print('Textures:', len(textures), textures)
    print('')

    bags = setup_bags()
    print(len(bags))
    #for b in bags:
    #    print(b)

    light_brown_bag = Bag(texture=Texture('light'), color=Color('brown'))
    dotted_red_bag = Bag(texture=Texture('dotted'), color=Color('red'))
    foo_bag = Bag(texture=Texture('dotted'), color=Color('red'))
    print(light_brown_bag == dotted_red_bag)
    print(foo_bag == dotted_red_bag)
