from django.db import models


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()
    n_visits = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'blog'


class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'author'


class Post(models.Model):
    blog = models.ForeignKey(Blog)
    title = models.CharField(max_length=255)
    body = models.TextField()
    authors = models.ManyToManyField(Author)
    n_visits = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'post'
