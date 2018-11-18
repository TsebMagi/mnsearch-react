#!/usr/bin/env python3
# Requires: PyYAML library

import json
import os
#
import yaml

whereami = os.path.dirname(os.path.abspath(__file__))
print(whereami)
filenames = os.listdir(whereami)
yaml_files = [fn for fn in filenames if fn.endswith('.yaml')]
print(yaml_files)

carddata = []

for fn in yaml_files:
    print("Loading:", fn, "...")
    with open(fn, 'r') as f:
        data = f.read()
    raw_data = yaml.load(data)
    carddata.extend(raw_data)

print("Writing output file...")
js_out_path = os.path.join(whereami, "..", "src", "cards.json")
with open(js_out_path, 'w') as g:
    json.dump(carddata, g, sort_keys=True, indent=4)

print("OK")
