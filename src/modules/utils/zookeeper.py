from kazoo.client import KazooClient
from kazoo import client
import time
import json
import os

#zookeeper_hosts = os.getenv('ZOOKEEPER_HOSTS', '192.168.100.10:2181,192.168.100.11:2181,192.168.100.12:2181')

class zk_power():
    def __init__(self, zookeeper_hosts=None):
        self.zookeeper_hosts = zookeeper_hosts
        self.zk = KazooClient(hosts=self.zookeeper_hosts)
        self.listeners = set()
        self.listeners_dict = {}

    def config(self, zookeeper_hosts = None):
        h = zookeeper_hosts if zookeeper_hosts else self.zookeeper_hosts
        self.zk = KazooClient(hosts=h)

    def exist(self, path=None):
        with self as session:
            o = session.zk.exists(path)
        if o:
            return True
        return False

    def get(self, path=None):
        with self as session:
            v = session.zk.get(path)[0]
        try:
            o = json.loads(v.decode('utf-8'))
        except:
            o = None
        return o

    def set(self, path=None, value=None):
        with self as session:
            if not session.zk.exists(path):
                session.zk.create(path)
            session.zk.set(path, json.dumps(value).encode('utf-8'))

    # can be used as self.track(path='/apigw', func=print)
    # add a listener in self.zk.state_listeners
    def track(self, path=None, func=None):
        @client.DataWatch(self.zk, path)
        def _(data, stat):
            if data:
                o = json.loads(data.decode('utf-8'))
                if func:
                    func(o)
        # remove old listener if exist
        self.untrack(path=path)
        # new added listener
        added_listener = self.zk.state_listeners - self.listeners
        self.listeners_dict[path] = added_listener.pop()
        self.listeners = self.zk.state_listeners - self.listeners

    def untrack(self, path=None):
        # self.zk.state_listeners = set()
        ls = self.listeners_dict.get(path, None)
        if ls:
            self.listeners_dict[path] = None
            self.zk.state_listeners.remove(ls)

    def untrack_all(self):
        self.zk.state_listeners = set()            

    def delete(self, path=None):
        with self as session:
            session.zk.delete(path)

    def __enter__(self):
        self.zk.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.zk.stop()
