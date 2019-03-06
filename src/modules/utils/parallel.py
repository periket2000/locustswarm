import multiprocessing
import asyncio
import requests

from modules.utils.task import Task


def run_timed_multi_thread(url='https://localhost'):
    t = Task()
    t.set_timeout(timeout=1)
    r = t.run2(url, 1, nthreads=10)
    return r

def get2(url, loop, results):
    def do_request():
        results.append(requests.get(url, verify=False, timeout=1))
    yield from loop.run_in_executor(None, do_request)

def test_multithreaded(max_threads=1000):
    timeout = 1
    results = []
    futures = []
    loop = asyncio.get_event_loop()
    cont = 0
    while cont < max_threads:
        coro = get2('https://localhost', loop, results)
        # set timeout
        waiter = asyncio.wait_for(coro, timeout)
        futures.append(asyncio.Task(waiter))
        cont += 1
    try:
        loop.run_until_complete(asyncio.gather(*futures))
    except:
        pass # timeout
    # print(results)
    print(len(results))

class Parallel:

    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())

    def __init__(self):
        pass

    @staticmethod
    async def _spawn_core(target=None, *args, **kwargs):
        timeout = kwargs.get('with_timeout')
        res = Parallel.pool.apply_async(target, args=args)
        try:
            out = res.get(timeout)
            return out
        except multiprocessing.TimeoutError:
            print("Timeout")
            return None

    @staticmethod
    def run_core_multi(workers=100, target=None, args=None, with_timeout=0):
        """
        Never overwhelm, pool is in charge of creating processes accordingly
        :param workers:
        :param target:
        :param args:
        :param with_timeout:
        :return:
        """
        loop = asyncio.get_event_loop()
        futures = [Parallel._spawn_core(target=target, args=args, with_timeout=with_timeout) for _ in range(workers)]
        return loop.run_until_complete(asyncio.gather(*futures))

    @staticmethod
    def run_timed_core_multi_threaded():
        r = Parallel.run_core_multi(workers=multiprocessing.cpu_count(),
                                target=test_multithreaded,
                                args=None,
                                with_timeout=10)
        return r
