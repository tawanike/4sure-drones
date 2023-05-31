import re
from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.
class Medicine(models.Model):
    name = models.CharField(max_length=255)  # slug like field letters, numbers, dash and underscore
    weight = models.IntegerField(default=0)  # What if the weight has decimals
    code = models.CharField(max_length=255)  # Uppercase letters, underscore, numbers
    image = models.ImageField(upload_to='medication/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'medicines'
        verbose_name = 'Medicine'
        verbose_name_plural = 'Medicines'

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        if not re.match(r'^[A-Za-z0-9_-]+$', self.name):
            raise ValidationError("Only letters, numbers, _ or - are allowed.")

        if not re.match(r'^[A-Z0-9_-]+$', self.code):
            raise ValidationError(
                "Only uppercase letters, numbers and underscores are allowed.")

        return super(Medicine, self).save(*args, **kwargs)
