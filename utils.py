import glob
from pathlib import Path
from typing import Tuple, Union

import pandas as pd


def load_data(data_dir: Union[str, Path]) -> Tuple[pd.DataFrame]:
    """Load data from csv files.

    Args:
        data_dir (Union[str, Path]): Path to the data dir.

    Returns:
        Tuple[pd.DataFrame]: Tuple of dataframes.
    """
    if isinstance(data_dir, str):
        data_dir = Path(data_dir)
    train_csv_paths = glob.glob(str(data_dir / "train" / "*.csv"))
    train_df_list = []
    for path in train_csv_paths:
        train_one_df = pd.read_csv(path, low_memory=False)
        train_df_list.append(train_one_df)
    train_df = pd.concat(train_df_list)
    train_df.reset_index(drop=True, inplace=True)
    test_df = pd.read_csv(data_dir / "test.csv", low_memory=False)
    sub_df = pd.read_csv(data_dir / "sample_submission.csv", low_memory=False)

    return (train_df, test_df, sub_df)


if __name__ == "__main__":
    ans = load_data("./data")
    print(ans)
