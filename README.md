# LGL Interpreter

## 1 More Capabilities

In this part of the README the additional capabilities from the subtask `1) More Capabilities` will be discussed.

### Documentation

-   **do_multiplizieren**: Multiplies 2 numbers. Syntax is a follows: `["multiplizieren", ["aufrufen", var1], ["aufrufen", var2]]`. Note that the user can either pass variables and call them via the `aufrufen` function or pass numbers directly.

-   **do_dividieren**: Divides 2 numbers. Syntax is a follows: `["dividieren", ["aufrufen", var1], ["aufrufen", var2]]`. Note that the user can either pass variables and call them via the `aufrufen` function or pass numbers directly.

-   **do_hochrechnen**: Implementation of power operations. Syntax is a follows: `["hochrechnen", ["aufrufen", number], ["aufrufen", exponent]]`. Note that the user can either pass variables and call them via the `aufrufen` function or pass numbers directly.

-   **do_ausgeben**: Print all arguments. An unlimited amount of arguments can be passed. If a string is passed the string is printed, or the user can also pass a function with a return value and that return value will be printed. The syntax is as follows: `["ausgeben", ..., ..., ...]`

-   **do_waerend**: Tests if the read_file function correctly reads an existing file and returns True.

-   **do_liste**: Tests if the read_file function correctly reads an existing file and returns True.

-   **do_listen_wert_holen**: Tests if the read_file function correctly reads an existing file and returns True.

-   **do_listen_wert_setzen**: Tests if the read_file function correctly reads an existing file and returns True.

-   **do_lexikon**: Tests if the read_file function correctly reads an existing file and returns True.

-   **do_lexikon_wert_holen**: Tests if the read_file function correctly reads an existing file and returns True.

-   **do_lexikon_wert_setzen**: Tests if the read_file function correctly reads an existing file and returns True.

-   **do_lexika_zusammenfuehren**: Tests if the read_file function correctly reads an existing file and returns True.

### Dexisions Taken

## 2 An Object System

In this part of the README the additional capabilities from the subtask `2) An Object System` will be discussed.

### Documentation

### Dexisions Taken

## 3 Tracing

In this part of the README the additional capabilities from the subtask `3) Tracing` will be discussed.

### Documentation

### Dexisions Taken

## Features

1. **Three Test States**: Three states for a test were implemented by the framework: `PASS`, `FAIL` and `ERROR`.

## Decisions Taken

-   **Error Handling**: The framework is designed to handle exceptions. If a test function raises an exception, it is caught, and the test is marked as `ERROR`.
-   **Environment Cleanup**: The `teardown` function deletes any test files created during test execution, ensuring no residual files are left.
-   **Command Line Argument Parsing**: The `argparse` module is used to parse command-line arguments.

## Documentation

The test functions are designed to validate the behavior of corresponding functions in the `file_manager.py` module.

-   **test_read_file_existing**: Tests if the read_file function correctly reads an existing file and returns True.
-   **test_read_file_non_existing**: Tests if the read_file function correcly returns False if promted to read a non existing file.
-   **test_create_file**: Tests if the create_file function successfully creates an empty file and returns True.
-   **test_create_file_for_invalid_name**: Tests if the create_file function correctly returns False if it fails to create the file.
-   **test_create_file_w_functionality**: Tests if the create_file function successfully creates a file and writes content to it.
-   **test_write_file**: Tests if the write_file function successfully writes content to an existing file and returns True.
-   **test_write_file_for_non_existent**: Tests if the write_file function returns False if it fails to write to a file.
-   **test_delete_file**: Tests if the delete_file function successfully deletes a file and returns True.
-   **test_delete_file_for_non_existent**: Tests if the delete_file function correctly returns False if it fails to delete the file.

-   **run_selected_tests**: Runs all tests by default or only certain tests if the command-line select option is applied. It works by creating a list of functions. If there is a pattern selected, it overwrites the function list and only the remaining functions, that have the selected pattern in their name are executed. Then the function list is passed into a for loop in which each test function is exexuted. Before each test execution the setup function is called and after each test execution the teardown function is called.
