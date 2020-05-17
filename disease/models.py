from django.db import models
from datetime import datetime, timedelta


# Create your models here.
class Diseases(models.Model):
    CHOICES=(
        ('HI','Highly Infectious'),
        ('I','Infectious'),
        ('Nc','Not Communicable')
    )
    disease=models.CharField(max_length=50)
    symptoms=models.CharField(max_lenth=199)
    recoveryperiod=models.CharField(max_length=20)
    medications=models.CharField(max_length=200)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=50, null=True)
    district = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)
    pincode = models.IntegerField(null=True)
    CaseDate=models.DateField(auto_now=True)
    Expected_recovery_data=models.DateTimeField(blank=True)
    threat_level=models.CharField(max_length=20,choices=CHOICES)
    

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        days=timedelta(days=self.recoveryperiod)
        self.Expected_recovery_data=self.CaseDate + days
        super(Diseases, self).save(force_insert, force_update, *args, **kwargs)


