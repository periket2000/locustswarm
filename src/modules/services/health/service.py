# -*- coding: utf-8 -*-
"""
Concrete implementation of health service
"""

from modules.services.interfaces.health import HealthInterface


class HealthService(HealthInterface):
    """The health service

    """
    def process(self, salute=None):
        if salute:
            ret = "Hi from master"
        else:
            ret = "Bad boy"
        return ret
