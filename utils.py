import pandas as pd


def _is_categorical(col: pd.Series):
    n_values = len(col)
    n_unique = len(col.unique())

    # considering the threshold
    if n_values <= 100:  # for smaller datasets
        threshold = 0.5
    else:
        threshold = 0.1

    if n_unique / n_values <= threshold:  # ratio of unique values to the whole feature vector
        return True
    return False
