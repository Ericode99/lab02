

["abfolge",
  ["setzen", "a", 2],
  ["setzen", "b", 3],
  ["ausgeben", "2*3=", ["multiplizieren", ["abrufen", "a"], ["abrufen", "b"]]],
  ["ausgeben", "3/3=", ["dividieren", ["abrufen", "b"], ["abrufen", "a"]]],
  ["ausgeben", "Now our while statement will count to 5"],
  ["waerend", "i=0", "i<5", ["ausgeben", "i"], "i=i+1"],

  ["liste", 5, "ary1", ["sali", "sali", 1, 2, 3]],
  ["ausgeben", ["listen_wert_holen", "ary1", 1]],
  ["listen_wert_setzen", "ary1", 1, "moin"],
  ["ausgeben", ["abrufen", "ary1"]],

  ["lexikon", "dict1", {"Name": "Max", "Nachname": "Mustermann", "MatrikelNr": 12345}],
  ["lexikon", "dict2", {"Notenschnitt": 6.0, "Hauptfach": "Informatik"}],
  ["ausgeben", ["lexikon_wert_holen", "dict1", "MatrikelNr"]],
  ["lexikon_wert_setzen", "dict1", "MatrikelNr", 67890],
  ["lexika_zusammenfuehren", "dict1and2", "dict1", "dict2"],
  ["ausgeben", ["abrufen", "dict1and2"]]
]