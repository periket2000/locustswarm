# -*- coding: utf-8 -*-
"""
Metaclass as interface for the health service
"""

from abc import ABCMeta, abstractmethod


class HealthInterface(metaclass=ABCMeta):
    @abstractmethod
    def process(self, salute=None):
        """
        Health interface
        :salute: the salute to the system
        :return: Json response
        """
        pass
