from django.db import models
from django.forms import ModelForm


#---------------
# Models
#---------------

class Company(models.Model):
    name = models.CharField(max_length=200)
    ticker = models.CharField(max_length=10)
    start_price = models.DecimalField(decimal_places=2, max_digits=10)
    end_price = models.DecimalField(decimal_places=2, max_digits=10)
    #current_price = models.DecimalField()


class Trader(models.Model):
    email = models.EmailField()
    companies = models.ManyToManyField(Company)
    #company_two = models.ForeignKey(Company)
    #company_three = models.ForeignKey(Company)



#---------------
# Forms
#---------------

class TraderForm(ModelForm):
    class Meta:
        model = Trader

