import multiprocessing
import asyncio


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
