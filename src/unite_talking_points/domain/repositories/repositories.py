import os
import pickle
from abc import ABC
from typing import Dict, Any

import scipy as sp

from src.unite_talking_points.utils.nlp_utils.load_documents import load_documents
from src.unite_talking_points.utils.nlp_utils.vectorize_documents import vectorize_tfidf


class AbstractDocumentRepository(ABC):
    def __init__(self):
        pass


class FileDocumentRepository(AbstractDocumentRepository):
    def __init__(self, data_path: str):
        """
        :param data_path: The folder where the documents are stored it needs the following structure:
        <data_path>/
            <data_path>/raw/
                <data_path>/raw/doc1.pdf
                <data_path>/raw/doc2.word
                <data_path>/raw/...
        Then, documents.pkl and vectors.npz will be created in the data_folder to make the start faster.
        """
        super().__init__()

        # Define data paths
        self.data_path = data_path
        self.raw_documents_path = os.path.join(self.data_path, 'raw')
        self.vectors_path = os.path.join(self.data_path, 'vectors.npz')
        self.documents_path = os.path.join(self.data_path, 'documents.pkl')

        # Define the documents and vectors
        self.documents = []
        self.vectors = None

    # Set up functions
    def setup_documents(self):
        """
        Load the documents from the raw folder and transform them into a list of Documents
        :return:
        """
        # We read the documents from the raw folder
        self.documents = load_documents(self.raw_documents_path)

    def setup_vectors(self, tfidf_args: Dict[str, Any] = None):
        """
        Vectorize the loaded documents into tfidf vectors
        :param tfidf_args: Dict[str, Any] The arguments for the scikit-learn tfidf vectorization
        :return:
        """
        # Vectorize the documents
        self.vectors = vectorize_tfidf(self.documents, tfidf_args)

    def setup(self, tfidf_args: Dict[str, Any] = None):
        """
        Set up the documents and vectors
        :param tfidf_args: Dict[str, Any] The arguments for the scikit-learn tfidf vectorization
        :return:
        """
        # Set up the documents
        self.setup_documents()

        # Set up the vectors
        self.setup_vectors(tfidf_args)

    # Save functions
    def save_documents(self):
        """
        Save the list of Documents into a pickle file
        :return:
        """
        with open(self.documents_path, "wb") as file:
            pickle.dump(self.documents, file)

    def save_vectors(self):
        """
        Save the tfidf vectors into a scipy sparse matrix
        :return:
        """
        sp.sparse.save_npz(self.vectors_path, self.vectors)

    def save(self):
        """
        Save the documents and vectors
        :return:
        """
        # Save the documents
        self.save_documents()

        # Save the vectors
        self.save_vectors()

    # Load functions
    def load_documents(self):
        """
        Load the list of Documents from a pickle file
        :return:
        """
        with open(self.documents_path, "rb") as file:
            self.documents = pickle.load(file)

    def load_vectors(self):
        """
        Load the tfidf vectors from a scipy sparse matrix
        :return:
        """
        self.vectors = sp.sparse.load_npz(self.vectors_path)

    def load(self):
        """
        Load the documents and vectors
        :return:
        """
        # Load the documents
        self.load_documents()

        # Load the vectors
        self.load_vectors()
