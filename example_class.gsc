[
  "abfolge",
  [
    "klasse_definieren",
    "Shape",
    [
      "konstruktor",
      "shape_new",
      ["name"]
    ],
    [
      "methode",
      "shape_density",
      ["thing", "weight"],
      ["dividieren", ["abrufen", "weight"], ["methode_aufrufen", ["abrufen", "thing"], "get_area"]]
    ]
  ],
  [
    "vererbung",
    "Square",
    "Shape",
    [
      "abfolge",
      [
        "konstruktor",
        "square_new",
        ["name", "side"]
      ],
      [
        "methode",
        "get_area",
        ["thing"],
        ["hochrechnen", ["abrufen", "thing", "side"], 2]
      ]
    ]
  ],
  [
    "vererbung",
    "Circle",
    "Shape",
    [
      "abfolge",
      [
        "konstruktor",
        "circle_new",
        ["name", "radius"]
      ],
      [
        "methode",
        "get_area",
        ["thing"],
        ["multiplizieren", ["hochrechnen", ["abrufen", "thing", "radius"], 2], "3.14"]
      ]
    ]
  ],
  [
    "setzen",
    "sq1",
    ["objekt_erstellen", "Square", "sq", 3]
  ],
  [
    "setzen",
    "ci1",
    ["objekt_erstellen", "Circle", "ci", 2]
  ],
  [
    "ausgeben",
    ["abrufen", "ci1"],["abrufen", "ci1"] 
  ],
  [
    "ausgeben",
    ["methode_aufrufen]
  ]
]