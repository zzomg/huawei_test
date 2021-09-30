import csv
import numpy as np


def _is_categorical(col):
    n_unique = len(set(col))
    n_values = len(col)

    # considering the threshold
    if n_values <= 100:  # for smaller datasets
        threshold = 0.5
    else:
        threshold = 0.1

    if n_unique / n_values <= threshold:  # ratio of unique values to the whole feature vector
        return True
    return False


def _get_col_type(col):
    if all(isinstance(x, (int, float)) for x in col):  # numericals
        # if all(isinstance(x, int) for x in col):
        #     col_type = "int"
        # elif all(isinstance(x, float) for x in col):
        #     col_type = "float"
        # else:
        col_type = "num"
    elif all(isinstance(x, str) for x in col):  # strings
        col_type = "str"
    else:
        col_type = "mixed"

    if _is_categorical(col):  # both types can be categorical as well
        col_type += "_cat"

    return col_type


def _create_unify_cols(data):
    # csv_cols = []
    #
    # for j in range(len(data[0])):
    #     csv_cols.append([])
    #     for i in range(len(data)):
    #         csv_cols[j].append(data[i][j])

    for i in range(len(data)):
        col_type = _get_col_type(data[i])
        if "num" in col_type or "float" in col_type:
            data[i] = list(map(float, data[i]))
        elif "int" in col_type:
            data[i] = list(map(int, data[i]))

    print(data)

        #     csv_cols[i] = np.array(csv_cols[i], dtype=float)
        # elif "int" in col_type:
        #     csv_cols[i] = np.array(csv_cols[i], dtype=int)
        # else:
        #     csv_cols[i] = np.array(csv_cols[i], dtype=str)
    # csv_cols = dict()
    #
    # for j in range(len(header)):
    #     csv_cols[header[j]] = []
    #     for i in range(len(data)):
    #         csv_cols[header[j]].append(data[i][j])
    #
    # for h, v in csv_cols.items():
    #     col_type = _get_col_type(v)
    #     if "num" in col_type:
    #         csv_cols[h] = list(map(float, v))

    return csv_cols


def _read_csv(path):
    with open(path, 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        rows = []
        for row in csv_reader:
            str2type_row = []
            for el in row:
                assert el != '', "Empty element"
                new_el = el
                if "." in el:
                    try:
                        new_el = float(el)
                    except ValueError:
                        pass
                else:
                    try:
                        new_el = int(el)
                    except ValueError:
                        pass
                str2type_row.append(new_el)
            rows.append(str2type_row)
    return header, rows
