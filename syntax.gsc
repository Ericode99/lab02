Multiplication:
["multiplizieren", ["aufrufen", var1], ["aufrufen", var2]]
Division:
["dividieren", ["aufrufen", var1], ["aufrufen", var2]] //var2 uf 0 checke
Power:
["hochrechnen", ["aufrufen", nummer], ["aufrufen", exponent]]
Print:
["ausgeben", ..., ..., ...]
While:
["waerend", variable_initialisation(e.g. i=0), while_condition(e.g. i<5), while_statement(e.g. ["ausgeben", i]), increment(e.g. i+=1)]
Arrays:
["liste", size, "array_name", list]
["listen_wert_holen", "array_name", index]
["listen_wert_setzen", "array_name", index, new_value]
Dictionary:
["lexikon", "dict_name", dictionary]
["lexikon_wert_holen", "dict_name", "keyname"]
["lexikon_wert_setzen", "dict_name", "keyname", "new_value"]
["lexika_zusammenfuehren", "new_dict_name", "dict1_name", "dict2_name"]