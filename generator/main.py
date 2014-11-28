'''
Created on Nov 18, 2014

@author: rene
'''
import autopep8
from docformatter import format_code

from generator import generate_epw
from iddparser import IDDParser


if __name__ == '__main__':
    parser = IDDParser()
    objs = parser.parse("epw.idd")

    for obj in objs:
        for f in obj.fields:
            f.conv_vals()

    source_file = generate_epw(objs)
#     source_file = autopep8.fix_code(
#         source_file, options=autopep8.parse_args(['--aggressive',
#                                                   '--aggressive',
#                                                   '--aggressive',
#                                                   '']))
#     source_file = format_code(source_file)

    with open("../pyepw/epw.py", 'w') as f:
        f.write(source_file)
