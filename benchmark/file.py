from os import PathLike
from typing import Iterable
import pandas as pd


def read_csv(filenames: Iterable[str | PathLike]):
    dfs = []

    for filename in filenames:
        df = pd.read_csv(filename)
        df["type"] = str(filename).split("/")[-1].split(".")[0]
        dfs.append(df)

    return pd.concat(dfs)


def agg_csv(filenames: Iterable[str | PathLike], agg="mean"):
    return read_csv(filenames).groupby("type").agg(agg)
