# -*- coding: utf-8 -*-
"""
Factory for the several sentence analizer implementations.
Depending on the environment variable ENGINE it returns a suitable instance.
"""

import os

from modules.utils.config import get_log


class HealthFactory:
    def __init__(self):
        self.engine = os.getenv("ENGINE", "DEFAULT").upper()
        logger_name = self.__module__ + "." + self.__class__.__name__
        self.logger = get_log(log_name=logger_name)

    def instance(self):
        self.logger.info('Getting instance: %s', self.engine)
        if self.engine == "DEFAULT":
            from modules.services.health.service import HealthService
            return HealthService()
        return None
