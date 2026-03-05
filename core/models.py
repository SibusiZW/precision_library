from django.db import models

# Create your models here.
class Book(models.Model):
    STATUSES = [
        ('Good', 'Good'),
        ('Borrowed', 'Borrowed'),
        ('Bad', 'Bad'),
    ]

    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    name_of_borrower = models.CharField(default="N/A")
    class_of_borrower = models.CharField(default="N/A")
    status = models.CharField(max_length=100, choices=STATUSES)
    date_issued = models.DateTimeField(auto_now_add=True)