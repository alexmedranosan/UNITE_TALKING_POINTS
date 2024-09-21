import re


def lemmatize_spacy(text: str, nlp) -> str:
    """
    Lemmatize text using spacy.
    :param text: str Text to lemmatize.
    :param nlp: Spacy NLP object.
    :return: lemmatized text: str The lemmatized text.
    """
    # Remove non-letter characters and convert to lowercase
    text = re.sub(r'[^a-zA-Z\s]', '', text.lower())

    # Tokenize text
    doc = nlp(text)

    # Lemmatize and remove stopwords
    lemmatized_text = [token.lemma_ for token in doc if not token.is_stop]
    lemmatized_text = ' '.join(lemmatized_text)

    return lemmatized_text
