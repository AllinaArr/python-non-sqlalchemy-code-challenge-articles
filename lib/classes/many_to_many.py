class Article:
    all=[]
    
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)
        
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, new_title):
        if hasattr(self, "_title"):
            print('title already exists ')
            return
        if not isinstance(new_title, str):
            print('must be a string')
            return
        if not 5<= len(new_title) <=50:
            print('must be between 5-50 char')
            return
        self._title = new_title
        
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, new_author):
        if isinstance(new_author, Author):
            self._author = new_author
        else:
            print('Invalid author')   
            
    @property
    def magazine(self):
        return self._magazine
    
    @author.setter
    def magazine(self, new_magazine):
        if isinstance(new_magazine, Magazine):
            self._magazine = new_magazine
        else:
            print('Invalid magazine')  
        
class Author:
    all = []
    def __init__(self, name):
        self.name = name
        Author.all.append(self)
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if hasattr(self, "_name"):
            print('name already exists ')
            return
        
        if not isinstance(new_name, str) and len(new_name) > 0:
            print('name must be a string')
            return
        self._name = new_name
        

    def articles(self):
        return [article for article in Article.all if article.author == self]
        # result = []
        # for article in Article.all:
        #     if article.author == self:
        #         result.append(article)
        # return result

    def magazines(self):
        result = []
        for magazine in Article.all:
            if magazine.author == self:
                result.append(magazine)
        return result 

    def add_article(self, magazine, title):
        pass

    def topic_areas(self):
        pass

class Magazine:
    all =[]
    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            print('name must be a string')
            return
        if not 2 <= len(new_name) <=16:
            print('must be 2-16 char')
            return
        self._name = new_name
        
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, new_category):
        if not isinstance(new_category, str):
            print('category must be string')
            return
        if not len(new_category) > 0:
            print('string must be more than 0')
            return
        self._category = new_category

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass