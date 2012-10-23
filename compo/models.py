from django.db import models
from django import forms


#---------------
# Models
#---------------
class CompanyManager(models.Manager):
    def create_company(self, name, ticker, start_price, end_price):
        company = self.create(name=name,ticker=ticker,start_price=start_price,end_price=end_price)
        # do something with the book
        return company

class Company(models.Model):
    name = models.CharField(max_length=200)
    ticker = models.CharField(max_length=10)
    start_price = models.DecimalField(decimal_places=2, max_digits=10)
    end_price = models.DecimalField(decimal_places=2, max_digits=10)
    #current_price = models.DecimalField()
    '''
    def create(self, name, ticker, start_price, end_price):
        company = self.create(name=name,ticker=ticker,start_price=start_price,end_price=end_price)
        return company
    '''
    objects = CompanyManager()
class Trader(models.Model):
    email = models.EmailField()
    companies = models.ManyToManyField(Company)
    #company_two = models.ForeignKey(Company)
    #company_three = models.ForeignKey(Company)




#---------------
# Forms
#---------------

class TraderForm(forms.ModelForm):
    entries = forms.ModelMultipleChoiceField(
        queryset=Company.objects.all(),
        widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Trader

