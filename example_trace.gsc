[
  "abfolge",
  ["lexikon", "Shape", [["_new", "shape_new"], ["density", "shape_density"], ["_parent", "None"], ["_classname", "Shape"]]],

  ["lexikon", "Square", [["_new", "square_new"], ["area", "square_area"], ["_parent", "Shape"], ["_classname", "Square"]]],

  ["lexikon", "Circle", [["_new", "circle_new"], ["area", "circle_area"], ["_parent", "Shape"], ["_classname", "Circle"]]],

  ["setzen", "shape_new",
    ["funktion", ["this_name"],
      ["lexikon", "new_dict", [["name", ["abrufen", "this_name"], ["_class", "Shape"]]]]
    ]
  ],

   ["setzen", "shape_density",
    ["funktion", ["class", "weight"],
      ["dividieren", ["abrufen", "weight"], ["rufen", ["abrufen", "class"], "area"]]
    ]
  ],



  ["setzen", "square_new",
    ["funktion", ["name", "side"],
        ["lexikon", "new_dict1", [["side", ["abrufen", "side"]], ["_class", "Square"], ["_parent", "Shape"]]]
    ]
  ],

  ["setzen", "square_area",
    ["funktion", ["cls"],
      ["hochrechnen", ["lexikon_wert_holen", "cls", "side"], 2]
    ]
  ],

  ["setzen", "circle_new",
    ["funktion", ["name", "radius"],
        ["lexikon", "new_dict1", [["radius", ["abrufen", "radius"]], ["_class", "Circle"], ["_parent", "Shape"]]]
    ]
  ],

  ["setzen", "circle_area",
    ["funktion", ["cls"],
      ["multiplizieren",["hochrechnen", ["lexikon_wert_holen", "cls", "radius"], 2], 3.14]
    ]
  ],

  ["setzen", "sq", ["machen", ["abrufen", "Square"], "sq", 3]],
  ["setzen", "ci", ["machen", ["abrufen", "Circle"], "ci", 2]],
  ["setzen", "density_sq", ["rufen", ["abrufen", "sq"], "density", 5]],
  ["setzen", "density_ci", ["rufen", ["abrufen", "ci"], "density", 5]],
  ["addieren", ["abrufen", "density_sq"], ["abrufen", "density_ci"]]

]