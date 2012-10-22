from django.db import models
from django.forms import ModelForm


#---------------
# Models
#---------------

class Trader(models.Model):
    email = models.EmailField()
    company1 = models.ForeignKey(Company)
    company2 = models.ForeignKey(Company)
    company3 = models.ForeignKey(Company)


class Company(models.Model):
    name = models.CharField()
    ticker = models.CharField(max_length=10)
    start_price = models.DecimalField()
    end_price = models.DecimalField()
    #current_price = models.DecimalField()



#---------------
# Forms
#---------------

class TraderForm(ModelForm):
    class Meta:
        model = Trader

