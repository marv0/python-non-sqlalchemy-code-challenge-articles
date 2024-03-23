class Article:
    def __init__(self, author, magazine, title):
        self._title = title
        self.author = author
        self.magazine = magazine
        self.magazine.add_article(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        raise AttributeError("Article title is immutable")

    @staticmethod
    def all():
        return Article._articles

    _articles = []

class Author:
    def __init__(self, name):
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        raise AttributeError("Author name is immutable")

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)
        return article

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def topic_areas(self):
        return list(set(article.magazine.category for article in self._articles))

class Magazine:
    def __init__(self, name, category):
        self._name = name
        self._category = category
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = value

    def add_article(self, article):
        self._articles.append(article)

    def articles(self):
        return self._articles

    def contributors(self):
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        return [article.title for article in self._articles]

    def contributing_authors(self):
        authors = {}
        for article in self._articles:
            author = article.author
            authors[author] = authors.get(author, 0) + 1
        return [author for author, count in authors.items() if count > 2]
