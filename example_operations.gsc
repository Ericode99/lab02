

["abfolge",
  ["setzen", "a", 2],
  ["setzen", "b", 3],
  ["ausgeben", "Some basic calculations:"],
  ["ausgeben", "2*3=", ["multiplizieren", ["abrufen", "a"], ["abrufen", "b"]]],
  ["ausgeben", "3/2=", ["dividieren", ["abrufen", "b"], ["abrufen", "a"]]],
  ["ausgeben", "\n"],

  ["ausgeben", "Now our while statement will count to 4"],
  ["setzen", "i", 0],
  ["waehrend", ["leq", ["abrufen", "i"], 4], ["abfolge", ["ausgeben", "i"], ["addieren", ["abrufen", "i"], 1]]],
  ["waehrend", "i=0", "i<5", ["ausgeben", "i"], "i=i+1"],
  ["ausgeben", "\n"],

  ["ausgeben", "Let's create a list"],
  ["liste", ["dividieren", 10, 2], "ary1", ["test", "test", 1, 2, 3]],
  ["ausgeben", ["abrufen", "ary1"]],
  ["ausgeben", "And print value at index 1:"],
  ["ausgeben", ["listen_wert_holen", "ary1", 1]],
  ["ausgeben", "Let's change the value at index 1 and print the entire list:"],
  ["listen_wert_setzen", "ary1", 1, "changed"],
  ["ausgeben", ["abrufen", "ary1"]],
  ["ausgeben", "\n"],

  ["ausgeben", "Now we create 2 dictionaries:"],
  ["lexikon", "dict1", {"Name": "Max", "Nachname": "Mustermann", "MatrikelNr": 12345}],
  ["lexikon", "dict2", {"Notenschnitt": 6.0, "Hauptfach": "Informatik"}],
  ["ausgeben", ["abrufen", "dict1"]],
  ["ausgeben", ["abrufen", "dict2"]],
  ["ausgeben", "\n"],

  ["ausgeben", "Now we print the MatrikelNr:"],
  ["ausgeben", ["lexikon_wert_holen", "dict1", "MatrikelNr"]],
  ["ausgeben", "Let's change the MatrikelNr to 67890."],
  ["lexikon_wert_setzen", "dict1", "MatrikelNr", 67890],
  ["ausgeben", "\n"],

  ["ausgeben", "Now let's merge our 2 dictionaries and print the result:"],
  ["lexika_zusammenfuehren", "dict1and2", "dict1", "dict2"],
  ["ausgeben", ["abrufen", "dict1and2"]]
]