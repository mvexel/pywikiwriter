#!/usr/bin/env python


class Table(object):

    rows = None  # a list of lists, the table rows
    header = None  # an optional list, the header row

    def __init__(self, header=None, rows=None):
        self.header = header
        self.rows = rows

    def as_wikitext(self):
        wikitext = """{| class="wikitable"\n|-\n"""
        if self.header:
            wikitext += '\n'.join(['! ' + cell for cell in self.header])
            wikitext += '\n|-\n'
        for row in self.rows:
            wikitext += '\n'.join(['| ' + str(cell) for cell in row])
            wikitext += '\n|-\n'
        wikitext += '|}'
        return wikitext

# {| class="wikitable"
# |-
# ! Header 1
# ! Header 2
# ! Header 3
# |-
# | row 1, cell 1
# | row 1, cell 2
# | row 1, cell 3
# |-
# | row 2, cell 1
# | row 2, cell 2
# | row 2, cell 3
# |}
