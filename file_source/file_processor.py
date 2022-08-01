""" This module is an interface to be implemented for file processing """
from abc import ABC, abstractmethod


class FileProcessorInterface(ABC):
    @abstractmethod
    def read_file(self, file_path):
        pass

    @abstractmethod
    def write_file(self, data):
        pass
