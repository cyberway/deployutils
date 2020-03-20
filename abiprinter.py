#!/usr/bin/env python3

import sys
import json
from console import Console
from jsonprinter import Items, JsonPrinter

structItems = Items().line() \
    .add('name', 'base').line() \
    .add('fields', items=Items(atnewline=True, items=Items().add('name','type')).line()).line()

indexItems = Items().line() \
    .add('name', 'unique').line() \
    .add('orders', items=Items(atnewline=True, items=Items().add('field','order')).line()).line()

tableItems = Items().line() \
    .add('name', 'type').add('scope_type', optional=True).line() \
    .add('indexes', items=Items(items=indexItems).line()).line()

variantItems = Items().line() \
    .add('name').line() \
    .add('types', items=Items(atnewline=True).line()).line()

abiItems = Items(atnewline=True).line() \
    .add('____comment', optional=True).line() \
    .add('version').line() \
    .add('types', items=Items(atnewline=True, items=Items().add('new_type_name','type')).line()).line() \
    .add('structs', items=Items(items=structItems).line()).line() \
    .add('actions', items=Items(atnewline=True, items=Items().add('name','type')).line()).line() \
    .add('events', items=Items(atnewline=True, items=Items().add('name','type')).line()).line() \
    .add('tables', items=Items(items=tableItems).line()).line() \
    .add('variants', items=Items(items=variantItems).line()).line()

abi = json.load(sys.stdin)

printer = JsonPrinter(Console())
print(printer.format(abiItems, abi))
