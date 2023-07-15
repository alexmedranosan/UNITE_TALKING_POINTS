from typing import Union

from sklearn.metrics.pairwise import cosine_similarity

from src.unite_talking_points.domain.repositories.file_document_repository.file_document_repository import \
    FileDocumentRepository
from src.unite_talking_points.domain.services.service import Service


class QueryService(Service):
    """
    A service for querying the documents. It returns the indexes of the documents with the highest similarity.
    """

    def __init__(self, query: str, repository: Union[FileDocumentRepository]):
        super().__init__()
        self.query = query
        self._query_vector = None
        self.repository = repository
        self.sorted_indexes = None

    def _pre_process(self):
        """
        Pre-process the query.

        This includes vectorizing the query.
        """
        # Vectorization of the query
        self._query_vector = self.repository.vectorizer.transform([self.query])

    def _process(self):
        """
        Process the query.

        This includes calculating the cosine similarity between the query vector and all the document vectors.
        The indexes of the documents with the highest similarities are sorted in descending order and stored.
        """
        # Calculate cosine similarity
        similarities = cosine_similarity(self.repository.vectors, self._query_vector)
        self.sorted_indexes = similarities.flatten().argsort()[::-1]

    def _post_process(self):
        """
        Post-process the query.

        This includes returning the sorted indexes.
        """
        # Return the sorted indexes
        return self.sorted_indexes
