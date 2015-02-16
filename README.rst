Stream Tap
==============

Capture data from an iterator as it gets pulled down stream.


Example
---------

::

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
        for item in items:
            print item

        return fruit_spigot.contents(), metal_spigot.contents()


    def run():
        """
        Run the composition of csv_file_consumer and information tap
        with the csv files in the input directory, and collect
        the results from each file and merge them together,
        printing both kinds of results.

        """
        data_items = [
            [u"mushroom", u"fungus"],
            [u"tomato", u"fruit"],
            [u"topaz", u"mineral"],
            [u"iron", u"metal"],
            [u"dróżką", u"utf-8 sample"],
            [u"apple", u"fruit"],
            [u"cheese", u"dairy"],
            [u"peach", u"fruit"],
            [u"celery", u"vegetable"],
            [u"pear", u"fruit"],
            [u"ruby", u"mineral"],
            [u"titanium", u"metal"],
            [u"cat", u"animal"],
            [u"orange", u"fruit"],
            [u"WĄŻ", u"utf-8 sample"],
        ]

        results = certain_kind_tap(data_items)

        fruits, metals = results

        print("=== fruits ===")
        for fruit in fruits:
            print(fruit)

        print("=== metals ===")
        for metal in metals:
            print(metal)


    if __name__ == "__main__":
        run()

Documentation
===============================

Read the docs: http://stream_tap.readthedocs.org/en/latest/


Contributing:
==================
Submit any issues or questions here: https://github.com/johnwlockwood/stream_tap/issues.

Make pull requests to **development** branch of
 https://github.com/johnwlockwood/stream_tap.

**Documentation** is written in reStructuredText and currently uses the
 Sphinx style for field
 lists http://sphinx-doc.org/domains.html#info-field-lists

Check out closed pull requests to see the flow of development, as almost
every change to master is done via a pull request on **GitHub**. Code Reviews
are welcome, even on merged Pull Requests. Feel free to ask questions about
the code.
