import time

from typing import Any, Callable, Generator, List, Tuple, Union

import matplotlib.pyplot as plt
import numpy as np


def measure_time(
        input_function: Callable, input_data: List[int]
) -> Tuple[float, Any]:
    """
    Calls 'input_function' with param 'input_list' and computes execution time.

    :param input_function: input function
    :param input_data: data that is an argument to 'input_function', e.g.
    :return: time of execution in seconds
    """
    start = time.time()
    y = input_function(*input_data)
    end = time.time()
    return end - start, y


def timer(
        function1: Callable,
        function2: Callable,
        data: Generator,
) -> None:
    """
    Computes "time complexity" for two given functions.

    :param function1: function to perform computations for
    :param function2: function to perform computations for
    :param data: a data generator that yields two element tuples with (1) data
        label, (2) arguments to inject to the tested functions
    """
    mean_times1 = []
    mean_times2 = []
    complexities = []
    correct_results = []

    for data_label, input_data in data():

        time1, result1 = measure_time(function1, input_data)
        time2, result2 = measure_time(function2, input_data)

        mean_times1.append(time1)
        mean_times2.append(time2)
        complexities.append(data_label)

        if result1 == result2:
            correct_results.append(data_label)

    plt.plot(complexities, mean_times1, label=function1.__name__, color='red')
    plt.plot(complexities, mean_times2, label=function2.__name__, color='blue')
    plt.vlines(
        correct_results,
        0,
        max(mean_times2),
        label='Similar result for both functions',
        alpha=0.3,
        color='limegreen'
    )
    plt.xlabel("Complexity of data")
    plt.ylabel("Time of execution [s]")
    plt.title(f"{function1.__name__} vs {function2.__name__}")
    plt.legend()
    plt.xticks(np.arange(min(complexities), max(complexities), 200))
    plt.show()
