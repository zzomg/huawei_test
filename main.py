import sklearn
import pandas as pd
import numpy as np
import csv

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, normalize
from utils import _read_csv, _create_unify_cols, _get_col_type


def load_csv(path):
    data = DatasetObject()
    data._load_csv(path)
    return data


class DatasetObject:
    def __init__(self):
        self.cols = None
        self.dataset = None

    def __repr__(self):
        return f"{self.dataset}"

    def _load_csv(self, path):
        header, rows = _read_csv(path)
        for row in rows:
            assert len(header) == len(row), f"Shape mismatch: row should have {len(header)} elements, got {len(row)}"
        self.cols = header
        # self.dataset = _create_unify_cols(rows)
        self.dataset = np.array(rows)

    def get_col(self, idx):
        return [row[idx] for row in self.dataset]

    def categorize(self, col_ids):
        for col_id in col_ids:
            col_type = _get_col_type(self.get_col(col_id))
            assert "cat" in col_type, "Trying to encode non-categorical feature"

            print(col_type)

        ct = ColumnTransformer(
            [('one_hot_encoder', OneHotEncoder(categories='auto'), col_ids)], remainder='passthrough'
        )
        self.dataset = ct.fit_transform(self.dataset)

    def normalize(self, axis=0):
        self.dataset = normalize(self.dataset, axis=axis)


def main():
    data = load_csv("test2.csv")
    print(data)
    # print(data.get_col(0))
    # # print(data)
    # print(data.dataset[2].shape)
    data.categorize([0, 1])
    data.normalize(axis=0)
    print(data)


if __name__ == '__main__':
    main()
