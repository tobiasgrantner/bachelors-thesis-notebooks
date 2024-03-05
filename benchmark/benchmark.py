from time import perf_counter_ns
from typing import Callable, TypeVar
import pandas as pd
from os import PathLike

T = TypeVar("T")


def benchmark(
    func: Callable[[int], T],
    before: Callable[[int], None] = None,
    after: Callable[[T, int], None] = None,
    beforeAll: Callable[[], None] = None,
    afterAll: Callable[[], None] = None,
    iterations=10,
) -> pd.DataFrame:
    """
    Benchmark the runtime of a function for a given number of iterations.

    Args:
        func: The function to benchmark.
        before: A function to run before each iteration. It is passed the iteration number.
        after: A function to run after each iteration. It is passed the result of the function and the iteration number.
        beforeAll: A function to run before all iterations.
        afterAll: A function to run after all iterations.
        iterations: The number of iterations to run.

    Returns:
        A DataFrame containing the iteration number, start time, end time, and duration for each iteration.
    """

    benchmarks = [0] * iterations

    if beforeAll:
        beforeAll()

    for i in range(iterations):
        if before:
            before(i)

        start = perf_counter_ns()
        result = func(i)
        end = perf_counter_ns()

        if after:
            after(result, i)

        benchmarks[i] = {
            "iteration": i,
            "start": start,
            "end": end,
        }

    if afterAll:
        afterAll()

    df = pd.DataFrame(benchmarks)
    df["duration"] = df["end"] - df["start"]

    return df


def benchmark_csv(
    path: str | PathLike,
    func: Callable[[int], T],
    before: Callable[[int], None] = None,
    after: Callable[[T, int], None] = None,
    beforeAll: Callable[[], None] = None,
    afterAll: Callable[[], None] = None,
    iterations=10,
) -> None:
    """
    Benchmark the runtime of a function for a given number of iterations and save the results to a CSV file.

    Args:
        path: The path to save the CSV file.
        func: The function to benchmark.
        before: A function to run before each iteration. It is passed the iteration number.
        after: A function to run after each iteration. It is passed the result of the function and the iteration number.
        beforeAll: A function to run before all iterations.
        afterAll: A function to run after all iterations.
        iterations: The number of iterations to run.
    """

    benchmarks = benchmark(func, before, after, beforeAll, afterAll, iterations)
    benchmarks.to_csv(path, index=False)
    return benchmarks
