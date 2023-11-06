Klassen definieren
["klasse_definieren", "Shape" 
    ["konstruktor" "shape_new", ["name"]],
    ["setzen", "shape_density",
        ["funktion", ["thing", "weight"],
            ["dividieren", ["abrufen", "weight"], ["abrufen", "area"]]
        ]
    ]
]

Klassen mit vererbung
["vererbung", "Square", "Shape",
    ["konstruktor", "square_new", ["name", "side"]],
    ["setzen", "square_area",
        ["funktion", ["thing"],
            ["hochrechnen", ["abrufen", "side"], 2]
        ]
    ]
]

["vererbung", "Circle", "Shape",
    ["konstruktor", "circle_new", ["name", "radius"]],
    ["setzen", "circle_area",
        ["funktion", ["thing"],
            ["multiplizieren", ["hochrechnen", ["abrufen", "radius"], 2], 3.14]
        ]
    ]
]

Objekte erstellen und in variable speichern
["setzen", "sq1", ["objekt_erstellen", "Square", "sq", 3]]

["setzen", "ci1", ["objekt_erstellen", "Circle", "ci", 2]]



["addieren", ["methode_aufrufen", ["abrufen", "sq1"], "shape_density", [5]], ["methode_aufrufen", "ci1.shape_density(5)"]]




Klassen definieren (Polymorphism -> funktionen gleiche namen)
["klasse_definieren", "Shape1" 
    ["konstruktor" "shape_new", ["name"]],
    ["setzen", "density",
        ["funktion", ["thing", "weight"],
            ["dividieren", ["abrufen", "weight"], ["abrufen", "area"]]
        ]
    ]
]

Klassen mit vererbung
["vererbung", "Square1", "Shape1",
    ["konstruktor", "square_new", ["name", "side"]],
    ["setzen", "area",
        ["funktion", ["thing"],
            ["hochrechnen", ["abrufen", "side"], 2]
        ]
    ]
]

["vererbung", "Circle1", "Shape1",
    ["konstruktor", "circle_new", ["name", "radius"]],
    ["setzen", "area",
        ["funktion", ["thing"],
            ["multiplizieren", ["hochrechnen", ["abrufen", "radius"], 2], 3.14]
        ]
    ]
]