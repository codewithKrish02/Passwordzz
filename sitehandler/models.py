from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class extensionuser(models.Model):
	 user = models.OneToOneField(User,on_delete=models.CASCADE)
	 salt = models.BinaryField()
	 uuid = models.TextField()
	 randomkey = models.TextField(default=None)

class password(models.Model):
	uuid =  models.TextField()
	website = models.TextField()
	email = models.EmailField()
	password = models.CharField(max_length=32)
	name = models.CharField(max_length=10)
	category = models.CharField(max_length=20)

	def __str__(self):
		return self.name +"	"+ self.email

class nameinpersonalinfo(models.Model):
	uuid = models.TextField()
	title = models.CharField(max_length=15)
	firstname =  models.TextField()
	middlename = models.TextField()
	lastname = models.TextField()
	email = models.CharField(max_length=40)
	dob = models.DateField()
	placeofbirth = models.CharField(max_length=50)

	def __str__(self):
		return self.firstname+" "+self.middlename+" "+self.lastname

class emailinpersonalinfo(models.Model):
	uuid = models.TextField()
	email = models.CharField(max_length=40)
	emailtype = models.CharField(max_length=20)
	nameoftheemail = models.TextField()

	def __str__(self):
		return self.nameoftheemail+" "+self.email

class phoneinpersonalinfo(models.Model):
	uuid = models.TextField()
	pcountry = models.TextField()
	phonenumber = models.TextField()
	nickname = models.TextField()
	phonetype = models.TextField()

	def __str__(self):
		return self.nickname+" "+self.phonenumber


class addressinpersonalinfo(models.Model):
	uuid = models.TextField()
	country = models.TextField()
	State = models.TextField()
	city = models.TextField()
	address = models.TextField()
	street = models.TextField()
	pincode = models.TextField()
	nameofaddress = models.TextField()

	def __str__(self):
		return self.nameofaddress+" "+self.address


class companyinpersonalinfo(models.Model):
	uuid = models.TextField()
	companyname = models.TextField()
	jobtitle = models.TextField()

	def __str__(self):
		return self.companyname+" "+self.jobtitle


class websiteinpersonalinfo(models.Model):
	uuid = models.TextField()
	websiteurl = models.TextField()
	nameofwebsite = models.TextField()

	def __str__(self):
		return self.nameofwebsite+" "+self.websiteurl


class cardsinpayments(models.Model):
	uuid = models.TextField()
	cardholdername = models.TextField()
	cardnumber = models.TextField()
	cvv = models.TextField()
	expirymonth = models.TextField()
	expiryyear = models.TextField()
	nameofcard = models.TextField()

	def __str__(self):
		return self.nameofcard+" "+self.cardholdername

class idcardinids(models.Model):
	uuid = models.TextField()
	name = models.TextField()
	idnumber = models.TextField()
	issuedate = models.TextField()
	expirydate = models.TextField()
	country = models.TextField()

	def __str__(self):
		return self.name+" "+self.idnumber+" "+self.expirydate

class driverlicenseinids(models.Model):
	uuid = models.TextField()
	name = models.TextField()
	idnumber = models.TextField()
	issuedate = models.TextField()
	expirydate = models.TextField()
	country = models.TextField()

	def __str__(self):
		return self.name+" "+self.idnumber+" "+self.expirydate


class passport(models.Model):
	uuid = models.TextField()
	name = models.TextField()
	idnumber = models.TextField()
	issuedate = models.TextField()
	expirydate = models.TextField()
	country = models.TextField()
	placeofissue = models.TextField()

	def __str__(self):
		return self.name+" "+self.idnumber+" "+self.expirydate

class taxnumber(models.Model):
	uuid = models.TextField()
	taxno = models.TextField()
	taxname = models.TextField()

	def __str__(self):
		return self.taxname


class securenotes(models.Model):
	uuid = models.TextField()
	name = models.TextField()
	text = models.TextField()

	def __str__(self):
		return self.name
