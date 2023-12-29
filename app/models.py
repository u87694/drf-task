from django.db import models

class Author(models.Model):
    """This model is reponsible to represent Author that must have following attributes"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    bio = models.TextField()

    def __str__(self):
        return self.name

class Book(models.Model):
    """This model is responsible to represent Book that is associated to an Author"""
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    publication_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title