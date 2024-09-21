from typing import List, Dict, Any

import spacy
from sklearn.feature_extraction.text import TfidfVectorizer

from src.unite_talking_points.domain.entities.entities import Document
from src.unite_talking_points.utils.nlp.misc import lemmatize_spacy


def vectorize_tfidf(documents: List[Document],
                    tfidf_args: Dict[str, Any] = None):
    """
    Vectorize a list of documents using TF-IDF.
    :param documents: List[Document] A list of documents to be vectorized.
    :param tfidf_args: Dict[str, Any] TF-IDF scikit-learn parameters.
    :return: tfidf_matrix Sparse matrix of TF-IDF values.
             tfidf_vectorizer TF-IDF sklearn vectorizer.
    """
    # Preprocess and extract the lemmas from each document
    if tfidf_args is None:
        tfidf_args = {"ngram_range": (1, 3), "min_df": 0.025, "max_df": 0.5}
    nlp = spacy.load("en_core_web_sm")
    lemmatized_documents = (lemmatize_spacy(document.content, nlp) for document in documents)

    # Vectorize each document
    tfidf_vectorizer = TfidfVectorizer(**tfidf_args)
    tfidf_matrix = tfidf_vectorizer.fit_transform(lemmatized_documents)

    return tfidf_matrix, tfidf_vectorizer
