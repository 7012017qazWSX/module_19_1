from django.db import models

class Buyer(models.Model):
    name = models.CharField(max_length=150)  # Имя покупателя (username аккаунта)
    balance = models.DecimalField(max_digits=10, decimal_places=2)  # Баланс
    age = models.IntegerField()  # Возраст

    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(max_length=150)  # Название игры
    cost = models.DecimalField(max_digits=10, decimal_places=2)  # Цена
    size = models.DecimalField(max_digits=10, decimal_places=2)  # Размер файлов игры
    description = models.TextField()  # Описание (неограниченное количество текста)
    age_limited = models.BooleanField(default=False)  # Ограничение возраста 18+
    buyer = models.ManyToManyField(Buyer)  # Покупатели, обладающие игрой

    def __str__(self):
        return self.title