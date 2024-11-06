from os import PathLike
from pathlib import Path
from typing import Iterable, Tuple
import pandas as pd


def read_results(
    action: str, improvement: str, state: str, directory: PathLike = Path()
) -> pd.DataFrame:
    df = pd.read_csv(directory / f"{action}_{improvement}_{state}.csv")
    df.columns = df.columns.str.capitalize()
    df["Duration"] = df["Duration"] / 1e9
    df["Action"] = action.replace("-", " ")
    df["Improvement"] = improvement.replace("-", " ").capitalize()
    df["State"] = state.capitalize()
    return df


def concat_results(
    action: str, states: Iterable[Tuple[str, str]], directory: PathLike = Path()
) -> pd.DataFrame:
    dfs = []

    for improvement, state in states:
        dfs.append(read_results(action, improvement, state, directory))

    return pd.concat(dfs)
