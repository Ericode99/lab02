import sys

from prettytable import PrettyTable
from datetime import datetime


def get_function_data(trace_file):
    current_running_functions = {}
    # function_data -> {'name': [nr_of_calls, total_time_(ms), average_time_(ms)]}
    function_data = {}
    trace_file = trace_file
    for line in trace_file:

        line = line.split(",")
        assert len(line) == 4, f"badly formate line"
        if line[2] == " start":

            # add {'unique_id': ['name', 'start_time']}
            current_running_functions[line[0].strip()] = [line[1].strip(), line[3].strip()]
        else:
            data = current_running_functions[line[0]]

            name, start_time = data[0].strip(), datetime.strptime(data[1].strip(), "%Y-%m-%d %H:%M:%S.%f")
            end_time = datetime.strptime(line[3].strip(), "%Y-%m-%d %H:%M:%S.%f")
            time_taken = end_time.microsecond - start_time.microsecond

            if name in function_data:
                function_data[name][0] += 1
                function_data[name][1] += time_taken
                function_data[name][2] = round(function_data[name][1] / function_data[name][0], 3)
            else:
                function_data[name] = [1, time_taken, time_taken]
    return function_data


def main(trace_file):
    table = PrettyTable()

    table.field_names = ["Function Name", "Num. of calls", "Total Time (ms)", "Average Time (ms)"]

    function_data = get_function_data(trace_file)
    for name, values in function_data.items():
        new_row = [name]
        new_row.extend([round(x, 3) for x in values])
        table.add_row(new_row)

    return table


if __name__ == "__main__":
    assert len(sys.argv) == 2, "usage: reporting.py trace_file.log"
    file = open(sys.argv[1], "r")
    res = main(file)
    file.close()
    print(res)
