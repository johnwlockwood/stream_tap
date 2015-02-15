#!/usr/bin/env python
# -*- coding: utf-8 -*-

from stream_tap import Bucket
from stream_tap import stream_tap


def get_fruit(item):
    """Get things that are fruit.

    :returns: thing of item if it's a fruit"""
    if len(item) == 2 and item[1] == u"fruit":
        return item[0]


def get_metal(item):
    """Get things that are metal.

    :returns: thing of item if it's metal"""
    if len(item) == 2 and item[1] == u"metal":
        return item[0]


def certain_kind_tap(data_items):
    """
    :param data_items: A sequence of unicode strings
    """
    fruit_spigot = Bucket(get_fruit)
    metal_spigot = Bucket(get_metal)

    items = stream_tap((fruit_spigot, metal_spigot), data_items)

    # consume iterator.
    tuple(items)

    return fruit_spigot.contents(), metal_spigot.contents()


def run():
    """
    Run the composition of csv_file_consumer and information tap
    with the csv files in the input directory, and collect
    the results from each file and merge them together,
    printing both kinds of results.

    """
    data_items = [
        "mushroom", "fungus",
        "tomato", "fruit",
        "topaz", "mineral",
        "iron", "metal",
        "dróżką", "utf-8 sample",
        "apple", "fruit",
        "cheese", "dairy",
        "peach", "fruit",
        "celery", "vegetable",
        "pear", "fruit",
        "ruby", "mineral",
        "titanium", "metal",
        "cat", "animal",
        "orange", "fruit",
        "WĄŻ", "utf-8 sample",
    ]

    results = certain_kind_tap(data_items)

    fruit_results = []
    metal_results = []

    for fruits, metals in results:
        for fruit in fruits:
            fruit_results.append(fruit)

        for metal in metals:
            metal_results.append(metal)

    print("=== fruits ===")
    for fruit in fruit_results:
        print(fruit)

    print("=== metals ===")
    for metal in metal_results:
        print(metal)


if __name__ == "__main__":
    run()
