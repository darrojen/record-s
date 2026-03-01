from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    roll_number = models.PositiveIntegerField(unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField()
    grade = models.CharField(max_length=10, choices=[
        ('JSS1', 'JSS1'), ('JSS2', 'JSS2'), ('JSS3', 'JSS3'),
        ('SSS1', 'SSS1'), ('SSS2', 'SSS2'), ('SSS3', 'SSS3')
    ])
    address = models.TextField(blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.roll_number})"

    class Meta:
        ordering = ['roll_number']