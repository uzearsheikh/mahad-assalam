from django.db import models

class Semester(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Marhala(models.Model):
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE,related_name='marhalas')
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.semester.name} - {self.name}"

class Book(models.Model):
    marhala = models.ForeignKey(Marhala, on_delete=models.CASCADE,related_name='books')
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='books/')

    def __str__(self):
        return self.title

class Note(models.Model):
    marhala = models.ForeignKey(Marhala, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='notes/')

    def __str__(self):
        return self.title
