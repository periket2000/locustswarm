# -*- coding: utf-8 -*-
import sys
import asyncio
import datetime
import pytest
import requests
from modules.utils.parallel import Parallel


@pytest.mark.multithead_multicore
@pytest.mark.skipif('multithead_multicore' not in sys.argv,
                    reason="no explicitly selected")
def test_multithead_multicore():
    start = datetime.datetime.now()
    r = Parallel.run_timed_core_multi_threaded()
    end = datetime.datetime.now() - start
    sec = int(end.total_seconds()) + 1
    b = []
    c = 0
    for a in r:
        if a:
            b = a + b
        c += 1
    t = [r for r in b if 'timeout' in r]
    print("total timeouts {}".format(len(t)))
    print("total send requests: {}".format(c))
    print("total {} seconds".format(sec))
    print("{} requests/seconds".format((len(b)-len(t))/sec))


def get2(url, loop, results):
    def do_request():
        results.append(requests.get(url, verify=False, timeout=1))
    yield from loop.run_in_executor(None, do_request)


@pytest.mark.multithead
@pytest.mark.skipif('multithead' not in sys.argv,
                    reason="no explicitly selected")
def test_multithead():
    total_seconds = 1
    elapsed = 0
    trial_start = datetime.datetime.now()
    results = []
    futures = []
    loop = asyncio.get_event_loop()
    cont = 0
    while elapsed < total_seconds and cont < 2000:
        coro = get2('https://localhost', loop, results)
        # set timeout
        waiter = asyncio.wait_for(coro, 1)
        futures.append(asyncio.Task(waiter))
        trial_end = datetime.datetime.now() - trial_start
        elapsed = int(trial_end.total_seconds())
        cont += 1

    try:
        loop.run_until_complete(asyncio.gather(*futures))
    except:
        print("Timeout Error")

    assert len(results) > 0
    # print(results)
    print(len(results))
