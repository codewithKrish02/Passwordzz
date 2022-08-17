from django.shortcuts import render,redirect
from django.contrib.auth.models import User,Group
from .models import *
from django.contrib.auth import authenticate,logout,login
import uuid
import os
from django.db.models.signals import post_save
from django.dispatch import receiver
import binascii
from .crypt import AESCipher
import hashlib
import pyperclip as pc

# Create your views here.

def gensalt():
	return os.urandom(128)

def randomkey():
	#key=binascii.hexlify(os.urandom(32)) wait
	#return hashlib.sha256(key).digest()
	return os.urandom(32)

def indexpage(request):
	user = 'None'
	if request.method == 'POST':
		email = request.POST['email']
		password = request.POST['password']
		user = authenticate(request,username=email,password=password)
		#print(user)
		try:
			if user is not None:
				login(request,user)
				#print(request.user.email)
				return redirect('addnewpassword')
				#return render(request,'password.html')
		except Exception as e:
			raise e
			
	return render(request,'index.html')

def registration(request):
	if request.method == 'POST':
		salt = gensalt()
		email = request.POST['email']
		password = request.POST['password']
		repassword = request.POST['repassword']
		userid = str(uuid.uuid4())
		randomkey1 = randomkey()

		if password == repassword:
			user = User.objects.create_user(first_name=email,email=email,password=password,username=email)
			user.save()
			extensionuser.objects.create(user = user,salt=salt,uuid = userid,randomkey=randomkey1)
			#print("user Saved")
			return redirect('indexpage')

	return render(request,'createaccount.html')



def Logout(request):
	if not request.user.is_active:
		return render(request,'index.html')
		#return redirect('indexpage')
	logout(request)
	#return render(request,'index.html')
	return redirect('indexpage')


def addnewpassword(request):
	if not request.user.is_active:
		return render(request,'index.html')


	emailid = str(extensionuser.objects.filter(user=request.user)[0].uuid)
	allpasswords = password.objects.filter(uuid=emailid)
	d = { "allpasswords" : allpasswords}

	if request.method == 'POST':

		if 'psave' in request.POST:
			#emailid =  str(request.user.email)	

			# Get random key here..

			url = request.POST['url']
			email = request.POST['email']
			passwords = request.POST['password']
			name = request.POST['name']
			category = request.POST['category']
			salt = extensionuser.objects.filter(user = request.user)[0].salt
			# Encrypt with randomkey
			rk = extensionuser.objects.filter(user=request.user)[0].randomkey
			aes = AESCipher(key=rk)
			encrypted = aes.encrypt(raw=passwords).decode('utf-8')
			print("ENCRYPTED: ",encrypted)

			# insert encrypted to db instead of plain text
			try:
				password.objects.create(uuid = emailid, website = url, email = email, 
					password = encrypted, name = name, category = category)
				print("password added")
				return redirect('addnewpassword')
			except Exception as e:
				#print(e)
				raise e

		elif 'mpdecryptbtn' in request.POST:
			masterpass = request.POST['masterpass']
			passid = request.POST['hiddenid']
			user1 = User.objects.get(email=request.user.email)
			if user1.check_password(masterpass):
				rk = extensionuser.objects.filter(user=request.user)[0].randomkey
				aes = AESCipher(key=rk)
				copypass = password.objects.filter(uuid = emailid,id= passid)[0].password
				decrypted = aes.decrypt(enc = copypass)
				pc.copy(decrypted)
				#print(decrypted)

	return render(request,'password.html',d)


def addsecurenotes(request):
	if not request.user.is_active:
		return render(request,'index.html')

	rk = extensionuser.objects.filter(user=request.user)[0].randomkey
	aes = AESCipher(key=rk)	


	uuid = extensionuser.objects.filter(user = request.user)[0].uuid
	allnotes = securenotes.objects.filter(uuid = uuid).order_by('name')
	

	allnotescount = allnotes.count()
	#print(uuid)

	d = {'allnotes':allnotes,'allnotescount':allnotescount}

	if request.method=='POST':
		nameoftext = request.POST['nameoftext']
		text = request.POST['text']
		
		try:
			#encnotes = aes.encrypt(raw=text).decode('utf-8')
			securenotes.objects.create(uuid = uuid,name = nameoftext,text=text)
			print("securenotes added")
			return redirect('addsecurenotes')

		except Exception as e:
			raise e
	return render(request,'securenotes.html',d)


def addpersonalinfo(request):
	if not request.user.is_active:
		return render(request,'index.html')

	uuid = extensionuser.objects.filter(user = request.user)[0].uuid
	#print(uuid)

	allnames = nameinpersonalinfo.objects.filter(uuid=uuid).order_by('firstname')
	allnamecount = allnames.count()
	#print(request.user.email)
	allemails = emailinpersonalinfo.objects.filter(uuid = uuid).order_by('nameoftheemail')
	#print(allemails)
	allemailcount = allemails.count()
	allphones = phoneinpersonalinfo.objects.filter(uuid = uuid).order_by('nickname')
	allphonecount = allphones.count()
	alladdress = addressinpersonalinfo.objects.filter(uuid = uuid).order_by('nameofaddress')
	alladdresscount = alladdress.count()
	allcompanies = companyinpersonalinfo.objects.filter(uuid = uuid).order_by('companyname')
	allcompanycount = allcompanies.count()
	allwebsites = websiteinpersonalinfo.objects.filter(uuid = uuid).order_by('nameofwebsite')
	allwebsitecount = allwebsites.count()


	d = {'allnames':allnames,'allnamecount':allnamecount,'allemails':allemails,
	'allemailcount':allemailcount,'allphones':allphones,
		'allphonecount':allphonecount,'alladdress':alladdress,'alladdresscount':alladdresscount,
		'allcompanies':allcompanies,'allcompanycount':allcompanycount,
		'allwebsites':allwebsites,'allwebsitecount':allwebsitecount
	}
	#print(allnames)
	#print(allnamecount)

	if request.method == 'POST':
		if 'addnamesave' in request.POST:
			#emailid = str(request.user.email)
			title =  request.POST['title']
			firstname = request.POST['firstname']
			middlename = request.POST['middlename']
			lastname = request.POST['lastname']
			email = request.POST['email']
			dob = request.POST['date']
			pob = request.POST['placeofbirth']

			#print(title,firstname,middlename,lastname,email,dob,pob)
			try:
				nameinpersonalinfo.objects.create(uuid = uuid, title = title, firstname = firstname, 
					middlename = middlename, lastname = lastname ,email = email, dob = dob, 
					placeofbirth = pob)
				print("nameinpersonalinfo added")
				return redirect('addpersonalinfo')
			except Exception as e:
				raise e
		elif 'addemailsave' in request.POST:
			emailid = str(request.user.email)
			email1 = request.POST['email']
			emailtype = request.POST['emailtype']
			nameoftheemail = request.POST['nameoftheemail']

			try:
				emailinpersonalinfo.objects.create(uuid = uuid, email = email1, emailtype = emailtype,
				 nameoftheemail = nameoftheemail)
				print("emailinpersonalinfo added")
				return redirect('addpersonalinfo')
			except Exception as e:
				raise e

		elif 'addphonesave' in request.POST:
			emailid = str(request.user.email)
			pcountry = request.POST['countryCode']
			phonenumber = request.POST['phonenumber']
			nickname = request.POST['nickname']
			phonetype = request.POST['phonetype']

			try:
				phoneinpersonalinfo.objects.create(uuid = uuid, pcountry = pcountry, 
					phonenumber = phonenumber, nickname = nickname, phonetype = phonetype)
				print("phoneinpersonalinfo Saved")
				return redirect('addpersonalinfo')
			except Exception as e:
				raise e

		elif 'addaddresssave' in request.POST:
			emailid = str(request.user.email)
			country = request.POST['country']
			state = request.POST['state']
			city = request.POST['city']
			address = request.POST['address']
			street = request.POST['street']
			pincode = request.POST['pincode']
			nameofaddress = request.POST['nameofaddress']

			try:
				addressinpersonalinfo.objects.create(uuid = uuid,country = country,State = state,
					city = city, address = address, street= street, pincode= pincode, 
					nameofaddress = nameofaddress)
				print("addressinpersonalinfo Saved")
				return redirect('addpersonalinfo')
			except Exception as e:
				raise e

		elif 'addcompanysave' in request.POST:
			emailid = str(request.user.email)
			companyname = request.POST['companyname']
			jobtitle = request.POST['jobtitle']

			try:
				companyinpersonalinfo.objects.create(uuid = uuid, companyname = companyname, 
					jobtitle = jobtitle)
				print("companyinpersonalinfo Saved")
				return redirect('addpersonalinfo')
			except Exception as e:
				raise e

		elif 'addwebsitesave' in request.POST:
			emailid = str(request.user.email)
			urlofwebsite = request.POST['url1']
			nameofwebsite = request.POST['nameofwebsite']

			try:
				websiteinpersonalinfo.objects.create(uuid = uuid, websiteurl = urlofwebsite, 
					nameofwebsite = nameofwebsite)
				print('websiteinpersonalinfo saved')
				return redirect('addpersonalinfo')
			except Exception as e:
				raise e

	return render(request,'personalinfo.html',d)


def delete_name(request,pid):
	if not request.user.is_active:
		return redirect('indexpage')
	name = nameinpersonalinfo.objects.get(id=pid)
	name.delete()
	return redirect('addpersonalinfo')

def delete_email(request,pid):
	if not request.user.is_active:
		return redirect('indexpage')
	email = emailinpersonalinfo.objects.get(id=pid)
	email.delete()
	return redirect('addpersonalinfo')

def delete_phone(request,pid):
	if not request.user.is_active:
		return redirect('indexpage')
	phone = phoneinpersonalinfo.objects.get(id=pid)
	phone.delete()
	return redirect('addpersonalinfo')

def delete_address(request,pid):
	if not request.user.is_active:
		return redirect('indexpage')
	address = addressinpersonalinfo.objects.get(id=pid)
	address.delete()
	return redirect('addpersonalinfo')

def delete_company(request,pid):
	if not request.user.is_active:
		return redirect('indexpage')
	company = companyinpersonalinfo.objects.get(id=pid)
	company.delete()
	return redirect('addpersonalinfo')

def delete_web(request,pid):
	if not request.user.is_active:
		return redirect('indexpage')
	website = websiteinpersonalinfo.objects.get(id=pid)
	website.delete()
	return redirect('addpersonalinfo')

def delete_card(request,pid):
	if not request.user.is_active:
		return redirect('indexpage')
	card = cardsinpayments.objects.get(id=pid)
	card.delete()
	return redirect('addpayments')


def delete_idcard(request,pid):
	if not request.user.is_active:
		return redirect('indexpage')
	idcard = idcardinids.objects.get(id=pid)
	idcard.delete()
	return redirect('addids')

def delete_driverlicense(request,pid):
	if not request.user.is_active:
		return redirect('indexpage')
	driverlicense = driverlicenseinids.objects.get(id=pid)
	driverlicense.delete()
	return redirect('addids')

def delete_passport(request,pid):
	if not request.user.is_active:
		return redirect('indexpage')
	passport = passport.objects.get(id=pid)
	passport.delete()
	return redirect('addids')

def delete_tax(request,pid):
	if not request.user.is_active:
		return redirect('indexpage')
	tax = taxnumber.objects.get(id=pid)
	tax.delete()
	return redirect('addids')

def delete_notes(request,pid):
	if not request.user.is_active:
		return redirect('indexpage')
	notes = securenotes.objects.get(id=pid)
	notes.delete()
	return redirect('addsecurenotes')

def delete_password(request,pid):
	if not request.user.is_active:
		return redirect('indexpage')
	password2 = password.objects.get(id=pid)
	password2.delete()
	return redirect('addnewpassword')


def addpayments(request):

	uuid = extensionuser.objects.filter(user = request.user)[0].uuid

	allcards = cardsinpayments.objects.filter(uuid = uuid).order_by('nameofcard')
	allcardcount = allcards.count()

	d = {'allcards':allcards,'allcardcount':allcardcount}

	if request.method == 'POST':
		#emailid = str(request.user.email)
		cardholdername = request.POST['cardholdername']
		cardnumber = request.POST['cardnumber']
		cvv = request.POST['cvv']
		expirymonth = request.POST['expirymonth']
		expiryyear = request.POST['expiryyear']
		nameofcard = request.POST['nameofcard']

		try:
			cardsinpayments.objects.create(uuid = uuid, cardholdername = cardholdername, 
				cardnumber = cardnumber, cvv = cvv, expirymonth = expirymonth, 
				expiryyear = expiryyear, nameofcard = nameofcard)
			print('cardsinpayments saved')
			return redirect('addpayments')
		except Exception as e:
			raise e


	return render(request,'payments.html',d)


def addids(request):

	uuid = extensionuser.objects.filter(user = request.user)[0].uuid

	allidcards = idcardinids.objects.filter(uuid = uuid).order_by('name')
	allidcardscount = allidcards.count()
	alldriverslicense = driverlicenseinids.objects.filter(uuid = uuid).order_by('name')
	alldriverslicensecount = alldriverslicense.count()
	allpassports = passport.objects.filter(uuid = uuid).order_by('name')
	allpassportscount = allpassports.count()
	alltaxnos = taxnumber.objects.filter(uuid = uuid).order_by('taxname')
	alltaxnoscount = alltaxnos.count()

	d = {
	'allidcards':allidcards,
	'allidcardscount':allidcardscount,
	'alldriverslicense':alldriverslicense,
	'alldriverslicensecount':alldriverslicensecount,
	'allpassports':allpassports,
	'allpassportscount':allpassportscount,
	'alltaxnos':alltaxnos,
	'alltaxnoscount':alltaxnoscount
	}

	if request.method == 'POST':
		if 'addidsave' in request.POST:
			#emailid = str(request.user.email)
			name = request.POST['name']
			number = request.POST['number']
			issuedate = request.POST['issuedate']
			expirydate = request.POST['expirydate']
			country = request.POST['country']

			try:
				idcardinids.objects.create(uuid = uuid, name = name, idnumber = number, issuedate = issuedate, expirydate = expirydate, country = country)
				print('idcardinids saved')
				return redirect('addids')
			except Exception as e:
				raise e

		elif 'addlicensesave' in request.POST:
			#emailid = str(request.user.email)
			name = request.POST['name']
			number = request.POST['number']
			issuedate = request.POST['issuedate']
			expirydate = request.POST['expirydate']
			country = request.POST['country']

			try:
				driverlicenseinids.objects.create(uuid = uuid, name = name, idnumber = number, issuedate = issuedate, expirydate = expirydate, country = country)
				print('driverlicenseinids saved')
				return redirect('addids')
			except Exception as e:
				raise e

		elif 'addpassportsave' in request.POST:
			#emailid = str(request.user.email)
			name = request.POST['name']
			number = request.POST['number']
			issuedate = request.POST['issuedate']
			expirydate = request.POST['expirydate']
			country = request.POST['country']
			placeofissue = request.POST['placeofissue']

			try:
				passport.objects.create(uuid = uuid, name = name, idnumber = number, issuedate = issuedate, expirydate =expirydate, country = country, placeofissue = placeofissue)
				print('passport saved')
				return redirect('addids')
			except Exception as e:
				raise e

		elif 'addtaxsave' in request.POST:
			#emailid = str(request.user.email)
			taxno = request.POST['taxno']
			nameoftax = request.POST['nameoftax']

			try:
				taxnumber.objects.create(uuid = uuid, taxno = taxno, taxname=nameoftax)
				print("taxno saved")
				return redirect('addids')			
			except Exception as e:
				raise e

	return render(request,'ids.html',d)