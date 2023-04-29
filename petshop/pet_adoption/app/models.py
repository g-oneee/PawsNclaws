
# Create your models here.
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
import datetime

# from matplotlib.style import available

class product_Category(models.Model):
    name = models.CharField(max_length=150)

    def  __str__(self):
        return self.name

class product_Sub_Category(models.Model):
    name = models.CharField(max_length=150)

    product_category = models.ForeignKey(product_Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Product(models.Model):
    # Availability = (('In Stock ','In Stock' ),('Out of Stock','Out of Stock'))
    category = models.ForeignKey(product_Category,on_delete=models.CASCADE,null=True)
    sub_category = models.ForeignKey(product_Sub_Category, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='ecomerce/pimg',null=True,blank=True)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    # Availability = models.CharField(choices=Availability,null=True,max_length=100)
    date = models.DateField(auto_now_add= True)
    stock = models.IntegerField()

    def __str__(self):
        return self.name

class pet_Category(models.Model):
    name = models.CharField(max_length=150)

    def  __str__(self):
        return self.name



class breed_Category(models.Model):
    name = models.CharField(max_length=150)

    petCategory = models.ForeignKey(pet_Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class Adopt(models.Model):
    GENDER_CHOICES = (
        ('M' , 'Male'),
        ('F' , 'Female'),
    )
    yes_no_choices=(
        ('y','Yes'),
        ('n','No'),
    )
    age_choices = (
        ('p','Puppyhood'),
        ('a','Adolescence'),
        ('ad','Adulthood'),
        ('s','Senior'),
    )
    available_choices = (
        ('y','Yes'),
        ('in','Inprocess'),
        ('n','No'),
    )
    petCategory = models.ForeignKey(pet_Category,on_delete=models.CASCADE,null=True)
    Breed = models.ForeignKey(breed_Category, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='ecomerce/adopt_img/',null=True,blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)   
    # birthdate = models.CharField(max_length=100)
    location = models.CharField(max_length=10000)
    age = models.CharField(max_length=2, choices=age_choices)
    vacinated = models.CharField(max_length=1, choices=yes_no_choices)
    vaccineinfo = models.CharField(max_length=100 , default='DHPP')
    neutered_or_spayed = models.CharField(max_length=1, choices=yes_no_choices)
    contact_info = models.IntegerField(default='987654321')
    good_with_dogs = models.CharField(max_length=1, choices=yes_no_choices,default='y')
    good_with_kids = models.CharField(max_length=1, choices=yes_no_choices)
    shots_upto_date = models.CharField(max_length=1, choices=yes_no_choices)
    needs_loving_adopter = models.CharField(max_length=1, choices=yes_no_choices,default='y')
    is_available = models.CharField(max_length=100 ,default='yes')
    def __str__(self):
        return self.name

class Order(models.Model):
    image = models.ImageField(upload_to='ecomerce/order/image')
    product =  models.CharField(max_length=1000, default='')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    quantity = models.CharField(max_length=10)
    price = models.IntegerField()
    total = models.CharField(max_length=100,default='')
    # first_name = models.CharField(max_length=15)
    # last_name = models.CharField(max_length=15)
    # city = models.CharField(max_length=20)
    # phone = models.CharField(max_length=10)
    # pincode = models.CharField(max_length=6)
    # address  = models.TextField()

    # class Order(models.Model):
    #     image = models.ImageField(upload_to='ecomerce/order/image')
    #     product = models.CharField(max_length=1000, default='')
    #
    #     user = models.ForeignKey(User, on_delete=models.CASCADE)
    #     quantity = models.IntegerField(max_length=10)
    #     price = models.IntegerField()
    #     total = models.CharField(max_length=100, default='')
    #     date = models.DateField(default=datetime.datetime.today)
    #
    #     def __str__(self):
    #         return self.product


    date = models.DateField(default=datetime.datetime.today)


    def __str__(self):
        return self.product



class Responses(models.Model):
    username=models.CharField(max_length=100)
    responsibilty=models.CharField(max_length=100)
    scaretaker=models.CharField(max_length=100)
    lalone=models.CharField(max_length=100)
    firstime=models.CharField(max_length=100)
    petname=models.CharField(max_length=100)

class Services(models.Model):
    name = models.CharField(max_length=150)
    def  __str__(self):
        return self.name


class ServiceResponses(models.Model):
    name=models.CharField(max_length=100)
    # forreq=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    detailedreq=models.CharField(max_length=1000)
    service = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=100,default='987654321') 
    # firstime=models.CharField(max_length=100)
    # petname=models.CharField(max_length=100)
    def __str__(self):
        return self.name




# registration wala
class details(models.Model):
    username=models.CharField(max_length=100)
    contact=models.IntegerField()
    address=models.CharField(max_length=100)
    email=models.CharField(max_length=100)

class contact_us(models.Model):
    name = models.CharField(max_length=50)
    email =models.EmailField(max_length=50)
    subject =models.CharField(max_length=200)
    message =models.TextField(max_length=200)

    def __str__(self):
        return self.name