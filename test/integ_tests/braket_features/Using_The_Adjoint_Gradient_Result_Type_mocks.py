import random

import numpy as np


def pre_run_inject(mock_utils):
    mocker = mock_utils.Mocker()
    mock_utils.mock_default_device_calls(mocker)
    res1 = mock_utils.read_file("ag_results.json", __file__)
    res2 = mock_utils.read_file("ag_results_2.json", __file__)
    res3 = mock_utils.read_file("ag_results_3.json", __file__)

    effects = [res1 for _ in range(3)]
    effects.extend([res2 for _ in range(51)])
    effects.extend([res3 for _ in range(20)])

    mocker.set_task_result_side_effect(effects)
    random.seed(42)
    np.random.seed(42)


def post_run(tb):
    pass
