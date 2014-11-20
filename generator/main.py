'''
Created on Nov 18, 2014

@author: rene
'''
import autopep8
from datetime import date

from generator.class_generator import EPWGenerator
from generator.iddparser import IDDParser


if __name__ == '__main__':
    parser = IDDParser()
    objs = parser.parse("epw.idd")
    source_file = "\"\"\"\n"
    source_file += "WARNING: This is an automatic generated file.\n"
    source_file += "It is based on the EPW IDD specification given in the document \n"
    source_file += "Auxiliary EnergyPlus Programs - Extra programs for EnergyPlus, Date: November 22 2013\n\n"
    source_file += "Do not expect that it actually works!\n\n"
    source_file += "Generation date: {}\n\n".format(date.today())
    source_file += "\"\"\"\n"
    source_file += "from collections import OrderedDict\n"
    source_file += "import re\n"

    generator = EPWGenerator()
    for obj in objs:
        source_file += generator.generate_class(obj)

    source_file += generator.generate_epw(objs)

    print source_file
    source_file = autopep8.fix_code(
        source_file, options=autopep8.parse_args(['--aggressive',
                                                  '--aggressive',
                                                  '']))

    with open("../pyepw/epw.py", 'w') as f:
        f.write(source_file)