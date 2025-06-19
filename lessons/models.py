from django.db import models

class Lesson(models.Model):
    chapter = models.CharField(max_length=100)  # 第1章 など
    number = models.CharField(max_length=10)    # 1-1 など
    title = models.CharField(max_length=200)    # レッスンタイトル
    content = models.TextField(blank=True)      # レッスン本文（今は空欄OK）

    def __str__(self):
        return f"{self.chapter} {self.number}: {self.title}"
