class Article:
    all = []
    def __init__(self, author, magazine, title):
        from .author import Author
        from .magazine import Magazine

        if not isinstance(author, Author):
            raise Exception("author must be an Author instance")
        if not isinstance(magazine, Magazine):
            raise Exception("magazine must be a Magazine instance")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise Exception("title must be a string (5–50 chars)")

        self._author = author
        self._magazine = magazine
        self._title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title 

    @title.setter
    def title(self, value):
        raise AttributeError("Title cannot be changed")


    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        from .author import Author
        if not isinstance(new_author, Author):
            raise Exception("author must be an Author instance")
        self._author = new_author

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, new_magazine):
        from .magazine import Magazine
        if not isinstance(new_magazine, Magazine):
            raise Exception("magazine must be a Magazine instance")
        self._magazine = new_magazine
