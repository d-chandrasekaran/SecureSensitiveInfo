""" This module is an interface to be implemented for DB processing for future extensibility"""
from abc import ABC, abstractmethod


class DBProcessorInterface(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass
