from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=50)
    price=models.FloatField()
    category=models.CharField(max_length=200)
    description=models.TextField()
    image=models.CharField(max_length=300)
    def __str__(self):
        return '{} {} {}'.format(self.title, self.author, self.category)
class Sell(models.Model):
	contact=models.CharField(max_length=200)
	name=models.CharField(max_length=50)
	title=models.CharField(max_length=200)
	author=models.CharField(max_length=50)
	price=models.FloatField()
	category=models.CharField(max_length=200)
	description=models.TextField()
	condition=models.CharField(max_length=700)
	def __str__(self):
		return '{} {} {}'.format(self.title, self.author, self.category)
class Signup(models.Model):
    name=models.CharField(max_length=50)
    contact=models.CharField(max_length=12)
    email=models.EmailField( max_length=50)
    password=models.CharField(max_length=20)
    date=models.DateField()
    def __str__(self):
        return '{} {} {}'.format(self.name, self.email, self.contact)

    """def __str__(self):
        return self.title,self.author,self.category"""
class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200)

	def __str__(self):
		return self.name
class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return '{}'.format(self.id)
	@property
	def get_cart_total(self):
		orderitems=self.orderitem_set.all()
		total=sum([item.get_total for item in orderitems])
		return total
	@property
	def get_cart_item(self):
		orderitems=self.orderitem_set.all()
		total=sum([item.quantity for item in orderitems])
		return total
	@property
	def shipping(self):
		shipping=True
		OrderItem=self.orderitem_set.all
		return shipping


class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return '{} {} {}'.format(self.order,self.product,self.quantity)
	@property
	def get_total(self):
		total=self.product.price*self.quantity
		return total
	



class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	state = models.CharField(max_length=200, null=False)
	zipcode = models.CharField(max_length=200, null=False)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '{} {} '.format(self.order,self.address)