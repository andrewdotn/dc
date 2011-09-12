#!/usr/bin/env python

"""Convert JSON to JSON-like python code with multi-line strings.

Sample usage:

    ../manage.py dumpdata chart | ../common/utils/pyencode.py \
            >> migrations/0002_initial_data.py

Not thoroughly tested, use with caution.

TODO: Convert to django serialization plugin format.
"""

import json
import sys
from unittest import TestCase

REPLACE_DICT = {
    '\\': '\\\\',
    '"': '\\"',
}

# HACK: sort by field order
def _make_dict_field_sort_key_func():
    fields = [ "title", "sparkblocks", "tweet", "source_url",
              "source_title", "source_detail", "chart_creator",
              "chart_creator_avatar", "chart_creator_detail",
              "disqus_identifier", "chart_data", "chart_settings" ]
    d = {}
    for i in range(len(fields)):
        d[fields[i]] = i

    def key(item):
        return d.get(item[0], 0)
    return key
_sort_key_func = _make_dict_field_sort_key_func()

class PyEncoder(object):
    def encode(self, o):
        return "".join(self.iterencode(o))

    def iterencode(self, o, indent=0):
        if isinstance(o, basestring) and '\n' in o:
            yield 'r"""' + o.replace('"""', '""" + \'"""\' + """') + '"""'
        elif isinstance(o, basestring):
            yield '"' + o.replace('\\', '\\\\').replace('"', '\\"') + '"'
        elif isinstance(o, list):
            yield '['
            first = True
            for i in o:
                if first:
                    first = False
                else:
                    yield ",\n"

                for e in self.iterencode(i, indent + 1):
                    yield e
            yield ']'
        elif isinstance(o, dict):
            yield '{'
            first = True
            for k, v in sorted(o.items(), key=_sort_key_func):
                if first:
                    first = False
                else:
                    yield ',\n'
                for i in range(indent):
                    yield ' '

                for i in self.iterencode(k, indent + 1):
                    yield i
                yield ': '
                for i in self.iterencode(v, indent + 1):
                    yield i
            yield '}'
        else:
            yield repr(o)

class _EncoderTests(TestCase):
    def recode_check(self, o):
        self.assertEquals(o, eval(PyEncoder().encode(o)))

    def test_str(self):
        self.recode_check('foo')

    def test_list(self):
        self.recode_check(['foo', 1, 2, 3])

    def test_dict(self):
        self.recode_check([{1: 2, '3': 'four'}, {1: {2: {3: 4}}}])

if __name__ == '__main__':
    data = json.load(sys.stdin)
    print PyEncoder().encode(data)
