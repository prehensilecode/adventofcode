#!/usr/bin/env python3
import sys
import os
import itertools
import argparse
import copy
from dataclasses import dataclass, field
from typing import Set

color_names = set()
colors = set()
texture_names = set()
textures = set()

debug_p = True


@dataclass(frozen=True)
class Color:
    name: str


@dataclass(frozen=True)
class Texture:
    name: str


class Bag:
    def __init__(self, color: Color, texture: Texture):
        self.color = color
        self.texture = texture
        self.contains = set()

    def desc(self):
        return f'{self.texture.name} {self.color.name}'

    # XXX
    def __hash__(self):
        return hash((self.color, self.texture))

    def __repr__(self):
        #return f'Bag(texture={self.texture}, color={self.color}, contains={self.contains})'
        return f'{self.desc()} bag - contains={self.contains}'

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()


def get_colors(rules):
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


def get_textures(rules):
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


def setup_bags(rules):
    global debug_p

    bags = set()
    for r in rules:
        rule = r.split()
        if debug_p:
            print(f'DEBUG: setup_bags() - working on rule: {r}')
            print(f'DEBUG: setup_bags() - len(rule) = {len(rule)}')

        this_bag = Bag(texture=Texture(rule[0]), color=Color(rule[1]))

        if len(rule) == 7:
            continue

        if len(rule) >= 8:
            b2 = Bag(texture=Texture(rule[5]), color=Color(rule[6]))
            if b2 not in bags:
                bags.add(b2)
            this_bag.contains.add((b2, int(rule[4])))

        if len(rule) >= 12:
            b3 = Bag(texture=Texture(rule[9]), color=Color(rule[10]))
            if b3 not in bags:
                bags.add(b3)
            this_bag.contains.add((b3, int(rule[8])))

        if len(rule) >= 16:
            b4 = Bag(texture=Texture(rule[13]), color=Color(rule[14]))
            if b4 not in bags:
                bags.add(b4)
            this_bag.contains.add((b4, int(rule[12])))

        if len(rule) >= 20:
            b5 = Bag(texture=Texture(rule[17]), color=Color(rule[18]))
            if b5 not in bags:
                bags.add(b5)
            this_bag.contains.add((b5, int(rule[16])))

        bags.add(this_bag)

        if debug_p:
            print(f'DEBUG: setup_bags() - this_bag = {this_bag}; id(this_bag) = {id(this_bag)}')
            print(f'DEBUG: setup_bags() - this_bag in set bags = {this_bag in bags}')
            print('')

    if debug_p:
        print(f'DEBUG: setup_bags() - id(bags) = {id(bags)}')
        print('DEBUG: setup_bags() - all bags:')
        for b in bags:
            print(f'    {b}, id(b) = {id(b)}')

    return bags


def main(rulefile):
    global debug_p

    rules = read_rules(args.rulefile)

    if debug_p:
        print('DEBUG: main() - rules:')
        for r in rules:
            print(f'    {r}')
        print('')

    colors = get_colors(rules)
    if debug_p:
        print(f'DEBUG: {len(colors)} Colors:')
        for c in colors:
            print(f'    {c}')
        print('')

    textures = get_textures(rules)
    if debug_p:
        print(f'DEBUG: {len(textures)} Textures:')
        for t in textures:
            print(f'    {t}')
        print('')

    # test Bag class
    if debug_p:
        light_brown_bag = Bag(texture=Texture('light'), color=Color('brown'))
        dotted_red_bag = Bag(texture=Texture('dotted'), color=Color('red'))
        foo_bag = Bag(texture=Texture('dotted'), color=Color('red'))
        bar_bag = dotted_red_bag
        print(light_brown_bag == dotted_red_bag)
        print(foo_bag == dotted_red_bag)
        print(foo_bag is dotted_red_bag)
        print(bar_bag is dotted_red_bag)

    bags = setup_bags(rules)
    if debug_p:
        print(f'DEBUG: main() - {len(bags)} Bags:')
        for b in bags:
            print(f'    {b}')
        print('')

    num_shiny_gold_containers = 0
    shiny_gold = 'shiny gold'
    for b in bags:
        print(f'FOOBAR: {b}')
        if b.contains:
            print(f'Non-empty contains: {b}')
            for b1 in b.contains:
                if b1[0].desc() == shiny_gold:
                    print(b1[0].desc())
                    num_shiny_gold_containers += 1

                for b2 in b1[0].contains:
                    if b2[0].desc() == shiny_gold:
                        print(b2[0].desc())
                        num_shiny_gold_containers += 2

                    for b3 in b2[0].contains:
                        if b3[0].desc() == shiny_gold:
                            print(b3[0].desc())
                            num_shiny_gold_containers += 3

                        for b4 in b3[0].contains:
                            if b4[0].desc() == shiny_gold:
                                print(b4[0].desc())
                                num_shiny_gold_containers += 4

    print(f'num_shiny_gold_containers = {num_shiny_gold_containers}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Advent of Code 2020 #7')
    parser.add_argument('rulefile', nargs='?', type=str, default='input07')
    args = parser.parse_args()

    main(args.rulefile)

