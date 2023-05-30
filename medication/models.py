from django.db import models


# Create your models here.
class Medicine(models.Model):
    name = models.CharField(max_length=255)  # slug like field letters, numbers, dash and underscore
    weight = models.IntegerField(default=0)  # What if the weight has decimals
    code = models.CharField(max_length=255)  # Uppercase letters, underscore, numbers
    image = models.ImageField(upload_to='medication/')

    class Meta:
        db_table = 'medicines'
        verbose_name = 'Medicine'
        verbose_name_plural = 'Medicines'

    def __str__(self) -> str:
        return self.name
