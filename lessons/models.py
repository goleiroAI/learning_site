from django.db import models

class Lesson(models.Model):
    chapter = models.CharField(max_length=20)
    number = models.CharField(max_length=10)
    title = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.chapter} {self.number} {self.title}"
