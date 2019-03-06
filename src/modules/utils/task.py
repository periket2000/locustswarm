import asyncio
from threading import Thread
from time import sleep
import requests
import datetime
import numpy
import urllib3


class Task:
    def __init__(self, sites=['https://www.google.com', 'https://www.bloomberg.com']):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.sites = sites
        self.timeout = 2
        self.times = 1
        self.ok = []
        self.failed = []
        self.unable = []
        self.signaled = False
        self.signal = None

    def overwrite(self, sites=None):
        self.sites = sites

    def set_timeout(self, timeout=5):
        self.timeout = timeout

    def set_times(self, times=5):
        self.times = times

    def _get_url(self, site):
        r = requests.get(site, verify=False, timeout=self.timeout)
        return r

    async def get(self, site):
        start = datetime.datetime.now()
        try:
            r = self._get_url(site=site)
        except:
            r = None
        end = datetime.datetime.now()
        delta = end - start
        ms = int(delta.total_seconds() * 1000)
        return (site, ms, r)

    def get2(self, site, results, timeout, total_seconds=5, step=1):
        elapsed = 0
        trial_start = datetime.datetime.now()
        while elapsed < total_seconds:
            start = datetime.datetime.now()
            try:
                r = self._get_url(site=site)
            except:
                r = None
            end = datetime.datetime.now()
            delta = end - start
            ms = int(delta.total_seconds() * 1000)
            if ms > (timeout*1000):
                print("timeout")
                results.append((site, ms, 'timeout'))
            else:
                results.append((site, ms, r))
            trial_end = datetime.datetime.now() - trial_start
            elapsed = int(trial_end.total_seconds())
        return (site, ms, r)

    def run(self):
        result = []
        futures = []
        loop = asyncio.get_event_loop()
        for i in range(self.times):
            futures += [self.get(i) for i in self.sites]
        result += loop.run_until_complete(asyncio.gather(*futures))
        return result

    def _raise_signal(self, signal):
        self.signal = signal
        self.signaled = True

    def run2(self, site, timeout, nthreads = 5):
        results = []
        threads = []
        for i in range(nthreads):
            t = Thread(target=self.get2, args=(site, results, timeout))
            threads.append(t)
            t.start()
        for t in threads:
            t.join()
        return results

    def median(self, req_ms = None):
        if req_ms:
            return numpy.median(req_ms)
        return -1
