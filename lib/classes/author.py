from .article import Article

class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise Exception("Author name must be a non-empty string")
        self._name = name 

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        raise AttributeError("Author name is immutable and cannot be changed")

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        if not self.articles():
            return None
        return sorted({magazine.category for magazine in self.magazines()})

