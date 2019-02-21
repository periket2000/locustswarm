# -*- coding: utf-8 -*-
import multiprocessing
import sys

import asyncio
import time
import datetime
import pytest
from modules.utils.task import Task
from modules.utils.parallel import Parallel

loop = asyncio.get_event_loop()

# Marked as integration test
# Could be launched isolated with 'pytest -v -m meter'

@pytest.mark.meter
@pytest.mark.skipif('meter' not in sys.argv,
                    reason="no explicitly selected")
def test_meter():
    t = Task()
    s = ['https://localhost', 'https://localhost/dqt']
    t.overwrite(sites=s)
    t.set_timeout(timeout=1)
    r = t.run(times=300)
    assert r is not None


@pytest.mark.meter
@pytest.mark.skipif('meter' not in sys.argv,
                    reason="no explicitly selected")
def test_meter_parallel_processes():
    t = Task()
    s = ['https://localhost']
    t.overwrite(sites=s)
    t.set_timeout(timeout=1)
    t.set_times(times=100)
    start = datetime.datetime.now()

    s = time.time()
    elapsed = 0
    seconds = 10
    result = []
    while elapsed < seconds:
        r = Parallel.run_core_multi(workers=multiprocessing.cpu_count(), target=t.run, args=None, with_timeout=10)
        for res in r:
            result += res
        elapsed = time.time() - s

    end = datetime.datetime.now()
    delta = end - start
    sec = int(delta.total_seconds())

    print(result)
    print("total requests {}".format(len(result)))
    print("test run in {} seconds".format(sec))
    assert r is not None
