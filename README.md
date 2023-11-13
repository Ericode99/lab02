# LGL Interpreter

## 1 More Capabilities

In this part of the README the additional capabilities from the subtask `1) More Capabilities` will be discussed.

### Documentation

-   **do_multiplizieren**: Multiplies 2 numbers. Syntax is a follows: `["multiplizieren", ["aufrufen", var1], ["aufrufen", var2]]`. Note that the user can either pass variables and call them via the `aufrufen` function or pass numbers directly.

-   **do_dividieren**: Divides 2 numbers. Syntax is a follows: `["dividieren", ["aufrufen", var1], ["aufrufen", var2]]`. Note that the user can either pass variables and call them via the `aufrufen` function or pass numbers directly.

-   **do_hochrechnen**: Implementation of power operations. Syntax is a follows: `["hochrechnen", ["aufrufen", number], ["aufrufen", exponent]]`. Note that the user can either pass variables and call them via the `aufrufen` function or pass numbers directly.

-   **do_ausgeben**: Print all arguments. An unlimited amount of arguments can be passed. If a string is passed the string is printed, or the user can also pass a function with a return value and that return value will be printed. The syntax is as follows: `["ausgeben", ..., ..., ...]`

-   **kleinerAls**: Evaluates true if var1 is smaller that var2. Syntax is as follows: `["kleinerAls", ["aufrufen", var1], ["aufrufen", var2]]`.

-   **groesserAls**: Evaluates true if var1 is greater that var2. Syntax is as follows: `["kleinerAls", ["aufrufen", var1], ["aufrufen", var2]]`.

-   **gleich**: Evaluates true if var1 and var2 are equal. Syntax is as follows: `["kleinerAls", ["aufrufen", var1], ["aufrufen", var2]]`.

-   **do_waehrend**: Executes a while loop. The syntax is as follows: `["waehrend", while_condition(e.g. ["setzen", "var1", "test"]), while_statement(e.g. ["abfolge", ["ausgeben", ["abrufen","i"]], ["setzen", "i",["addieren", ["abrufen", "i"], 1]]])]`. The user has to make sure to define the variable he is using in the while loop beforehand with `setzten`. Also he has to include an increment in his while_statement.

-   **do_liste**: Creates a list of a predefined size. The syntax is as follows: `["liste", size, "list_name", list]`. In the input list operations, numbers or strings can be passed.

-   **do_listen_wert_holen**: Gets a value of a list at a certain position. Syntax is as follows: `["listen_wert_holen", "list_name", index]`

-   **do_listen_wert_setzen**: Sets a value at a certain position in a list. Syntax is as follows: `["listen_wert_setzen", "list_name", index, new_value]`. The new_value can be an operation, string or number.

-   **do_lexikon**: Creates a new dictionary. Syntax is as follows: `["lexikon", "dict_name", [[key1, val1], [key2, val2]]]`. The keys and values can be an operation, string or number.

-   **do_lexikon_wert_holen**: Gets a value in a dictionary with a certain key. Syntax is as follows: `["lexikon_wert_holen", "dict_name", "keyname"]`

-   **do_lexikon_wert_setzen**: Sets a value in a dictioniary at a certain key. Syntax is as follows: `["lexikon_wert_setzen", "dict_name", "keyname", new_value]`. The new_value can be an operation, string or number.

-   **do_lexika_zusammenfuehren**: Merges 2 dictionaries into a new dictionary. The syntax is as follows: `["lexika_zusammenfuehren", "new_dict_name", "dict1_name", "dict2_name"]`. Note that the original dictionaries are deleted after the merge.

### Decisions Taken

**Input parameters and variables**

-   In the functions `do_subtrahieren`, `do_multiplizieren`, `do_dividieren` and `do_hochrechene` all inputs can be passed either as numbers or as an operation.

-   In the function `do_ausgeben` either operations or strings can be passed as input parameters.

-   In the `do_waehrend` function, as the while_condition and while statemnt only operations can be passed.

-   In the `do_liste` function, as a size input operations or numbers can be passed. The list_name has to be a string or a "aufrufen" call as well as in the other list operations (do_listen_wert_holen, do_listen_wert_setzen) The initial list items have to be passed as a list. The initial list can also contain operations, e.g. "aufrufen". In the other list operations the position can be passed as a number or operation.

-   The size input and the list index input are rounded with the `round()` function in order to avoid errors if a float is passed, or the result of an operation returns a float.

-   The dictionary operations have a similar behaviour to the list operations.

**Keeping things clean**

-   If two dictinaries are merged using the `do_lexika_zusammenfuehren` function, the original dictionaries are deleted and only the merged dictionary is kept in order to avoid dublicate date.

## 2 An Object System

In this part of the README the additional capabilities from the subtask `2) An Object System` will be discussed.

### Documentation

### Decisions Taken

## 3 Tracing

In this part of the README the additional capabilities from the subtask `3) Tracing` will be discussed.

### Documentation
*lgl_interpreter.py*
- extend `main` with the possibility of tracing the file dding an optional argument: --trace trace_file.log
- if --trace trace_file.log is added trace_file.log will be opened and passed to do as the named parameter file

- `decorator_funciton` takes as argument the original function which is wrapped with `@decorator_function`
- `wrapper_function` implements the optional possibility of tracing by checking if a logging file was passed.
- If so it logs the information of the original function to the trace_file.log file in the csv format: `unique_id`, `function_name`, `start/stop`, `start_time/ stop_time` 
- start_time and stop_time is implemented using the datetime api

*reporting.py*
- can be executed with `reporting.py trace_file.log`

- `get_function_data` takes the logged data from lgl_interpreter and creates a dictionary which keeps track of all the functions called,
- how often the function was called, the time all the calls to the function took and the average time the execution of 
- the function took. In the format of e.g. {'do': [1, 23, 23]}


### Decisions Taken
- we use the prettytable to formate and output the data of the dictionary returned by `get_funciton_data`
