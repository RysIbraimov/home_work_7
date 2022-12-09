from django.db import models

# Create your models here.
class JobTitle(models.Model):
    job_t = models.CharField(max_length=30)
    department = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.job_t} - {self.department}'

class Employee(models.Model):
    name = models.CharField(max_length=30)
    job_title_id = models.ForeignKey(JobTitle, on_delete=models.CASCADE)
    birth_date = models.DateField()
    salary = models.IntegerField()

    def __str__(self):
        return self.name
