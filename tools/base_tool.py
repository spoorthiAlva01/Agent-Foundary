from abc import ABC, abstractmethod

class BaseTool(ABC):
    name: str
    required_inputs = []

    @abstractmethod
    def execute(self, **kwargs):
        pass
