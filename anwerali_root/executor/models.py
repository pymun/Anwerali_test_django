from django.db import models

# Create your models here.
class ExecutorModel(models.Model):
    executor_name = models.CharField(max_length=200, 
                                     verbose_name='Имя')
    executor_phone = models.CharField(max_length=20, 
                                      verbose_name='Телефон')
    executor_experience = models.TextField(verbose_name='Опыт')
    
    def __str__(self):
        return self.executor_name
    
    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'