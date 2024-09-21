from abc import abstractmethod
from pipelines.pipeline import Pipeline


class Service(Pipeline):
    @abstractmethod
    def _pre_process(self):
        pass

    @abstractmethod
    def _process(self):
        pass

    @abstractmethod
    def _post_process(self):
        pass
