from abc import ABC, abstractmethod

from src.domain.pipeline import Pipeline


class InteractionState(ABC):

    def __init__(self, pipeline: Pipeline):
        self.pipeline = pipeline

    @abstractmethod
    def fetch_next_state(self, input_text):
        pass

    # TODO: pass a domain service (like InputTextProcessor) instead of the actual repository
    @abstractmethod
    def process_input_text(self, input_text_repository):
        pass
