from django.db import models

# Create your models here.
class CustomerModel(models.Model):
    customer_name = models.CharField(max_length=200, 
                                     verbose_name='Имя')
    customer_phone = models.CharField(max_length=20, 
                                      verbose_name='Телефон')
    customer_experience = models.TextField(verbose_name='Опыт')
    
    def __str__(self):
        return self.customer_name
    
    class Meta:
        verbose_name = 'Заказчик'
        verbose_name_plural = 'Заказчики'