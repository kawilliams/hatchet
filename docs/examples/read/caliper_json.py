#!/usr/bin/env python

import hatchet as ht


if __name__ == "__main__":
    # Path to caliper json-split file.
    json_file = "../../../hatchet/tests/data/caliper-lulesh-json/lulesh-sample-annotation-profile.json"

    # Use hatchet's ``from_caliper_json`` API with the resulting json-split.
    # The result is stored into Hatchet's GraphFrame.
    gf = ht.GraphFrame.from_caliper_json(json_file)

    # Printout the DataFrame component of the GraphFrame.
    print(gf.dataframe)

    # Printout the graph component of the GraphFrame.
    # Because no metric parameter is specified, ``time`` is used by default.
    print(gf.tree())
