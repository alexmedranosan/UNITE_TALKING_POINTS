from datetime import datetime
from typing import List


class Document:
    def __init__(self, content: str, _id: str = None, origin: str = None, title: str = None, author: str = None,
                 keywords: List[str] = None, date_created: datetime.date = None, date_modified: datetime.date = None,
                 source: str = None):
        """
        This class represents a document.
        :param content: str Represents the content of the document.
        :param _id: str Represents the unique identifier of the document.
        :param origin: str Represents the origin of the document.
        :param title: str Represents the title of the document.
        :param author: str Represents the author of the document.
        :param keywords: List[str] Represents the keywords of the document.
        :param date_created: datetime.date Represents the date the document was created.
        :param date_modified: datetime.date Represents the date the document was last modified.
        :param source: str Represents the source of the document.
        """
        self.content = content
        self._id = _id
        self.origin = origin
        self.title = title
        self.author = author
        self.keywords = keywords
        self.date_created = date_created
        self.date_modified = date_modified
        self.source = source


class GeneratedDocument(Document):
    """
    This class represents a document.
    :param content: str Represents the content of the document.
    :param prompt: str Represents the prompt used to generate the document.
    :param _id: str Represents the unique identifier of the document.
    :param origin: str Represents the origin of the document.
    :param title: str Represents the title of the document.
    :param author: str Represents the author of the document.
    :param keywords: List[str] Represents the keywords of the document.
    :param date_created: datetime.date Represents the date the document was created.
    :param date_modified: datetime.date Represents the date the document was last modified.
    :param source: str Represents the source of the document.
    :param references: List[Document] Represents the Documents used to generate the document.
    """
    def __init__(self, content: str, prompt: str, _id: str = None, origin: str = None, title: str = None,
                 author: str = None, keywords: List[str] = None,
                 date_created: datetime.date = None, date_modified: datetime.date = None,
                 source: str = None, references: List[Document] = None):
        super().__init__(content=content, origin=origin, title=title, author=author, keywords=keywords,
                         date_created=date_created, date_modified=date_modified, source=source)
        self.prompt = prompt
        self.references = references
