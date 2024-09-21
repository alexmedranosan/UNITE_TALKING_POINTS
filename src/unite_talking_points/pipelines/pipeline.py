from abc import ABC, abstractmethod


class Pipeline(ABC):
    @abstractmethod
    def _pre_process(self):
        pass

    @abstractmethod
    def _process(self):
        pass

    @abstractmethod
    def _post_process(self):
        pass

    def run(self):
        self._pre_process()
        self._process()
        result = self._post_process()

        return result
