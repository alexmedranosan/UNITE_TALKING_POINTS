import pickle
from typing import List, Dict, Any

import scipy as sp
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer

from src.unite_talking_points.domain.entities.entities import Document
from src.unite_talking_points.utils.nlp_utils.load_documents import load_documents
from src.unite_talking_points.utils.nlp_utils.nlp_utils import lemmatize_spacy


def vectorize_tfidf(documents: List[Document],
                    tfidf_args: Dict[str, Any] = None):
    """
    Vectorize a list of documents using TF-IDF.
    :param documents: List[Document] A list of documents to be vectorized.
    :param tfidf_args: Dict[str, Any] TF-IDF scikit-learn parameters.
    :return: tfidf_matrix Sparse matrix of TF-IDF values.
    """
    # Preprocess and extract the lemmas from each document
    if tfidf_args is None:
        tfidf_args = {"ngram_range": (1, 3), "min_df": 0.025, "max_df": 0.5}
    nlp = spacy.load("en_core_web_sm")
    lemmatized_documents = (lemmatize_spacy(document.content, nlp) for document in documents)

    # Vectorize each document
    tfidf_vectorizer = TfidfVectorizer(**tfidf_args)
    tfidf_matrix = tfidf_vectorizer.fit_transform(lemmatized_documents)

    return tfidf_matrix


def main():
    # Set up the documents directory
    project_directory = r"C:\Users\amedrano\Desktop\UN\UNITE_TALKING_POINTS"
    documents_directory = project_directory + r"\data\documents\raw"
    object_database_directory = project_directory + r"\data\documents"

    documents = load_documents(documents_directory)

    # Create the vectorization
    vectorized_documents = vectorize_tfidf(documents,
                                           tfidf_args={"ngram_range": (1, 3), "min_df": 0.025, "max_df": 0.5})

    print(vectorized_documents.shape)

    # Save the vectorized documents
    sp.sparse.save_npz(object_database_directory + r"\tfidf_vectors.npz", vectorized_documents)

    # Save object_list as JSON file
    with open(object_database_directory + r"\documents.pkl", "wb") as file:
        pickle.dump(documents, file)


if __name__ == "__main__":
    main()
