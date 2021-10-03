import pandas as pd
from sklearn.preprocessing import normalize

from utils import _is_categorical


def load_csv(path):
    data = DatasetObject()
    data._load_csv(path)
    return data


class DatasetObject:
    def __init__(self):
        self.dataset = None

    def __repr__(self):
        return f"{self.dataset}"

    def _load_csv(self, path):
        self.dataset = pd.read_csv(path)

    def get_col_type(self, col_id):
        col = self.dataset[col_id]
        print(col)
        if all(isinstance(x, (int, float)) for x in col):  # numericals
            col_type = "num"
        elif all(isinstance(x, str) for x in col):  # strings
            col_type = "str"
        else:
            col_type = "mixed"

        if _is_categorical(col):  # both types can be categorical as well
            col_type += "_cat"

        return col_type

    def categorize(self, col_ids):
        for col_id in col_ids:
            col_type = self.get_col_type(col_id)
            assert "cat" in col_type, "Trying to encode non-categorical feature"

            print(col_type)

        self.dataset = pd.get_dummies(self.dataset, prefix=col_ids, columns=col_ids)

    def normalize(self, axis=0):
        self.dataset = pd.DataFrame(normalize(self.dataset, axis=axis), columns=self.dataset.columns)


def test(csv):
    data = load_csv(csv)
    data.categorize(data.dataset.columns)
    data.normalize(axis=0)
    print(data)


def main():
    test(csv="car.csv")


if __name__ == '__main__':
    main()
