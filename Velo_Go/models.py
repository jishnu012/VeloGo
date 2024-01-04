from django.db import models

# Create your models here.
class Login(models.Model):
    Username = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    Type = models.CharField(max_length=100)


class Drivers(models.Model):
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    place =models.CharField(max_length=100)
    Post=models.CharField(max_length=50)
    city=models.CharField(max_length=75)
    state=models.CharField(max_length=50)
    pin=models.IntegerField()
    DateOfBirth =models.DateField()
    phone=models.BigIntegerField()
    photo=models.CharField(max_length=250)
    lisence=models.CharField(max_length=300)
    email=models.CharField(max_length=100)
    upi=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    languagesknown=models.CharField(max_length=150)
    Status = models.CharField(max_length=100,default='pending')

class Users(models.Model):
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    place =models.CharField(max_length=100)
    Post=models.CharField(max_length=50)
    city=models.CharField(max_length=75)
    state=models.CharField(max_length=50)
    pin=models.IntegerField()
    DateOfBirth =models.DateField()
    phone=models.BigIntegerField()
    photo=models.CharField(max_length=250)
    email = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)

class Vehicle(models.Model):
    DRIVERS= models.ForeignKey(Drivers, on_delete=models.CASCADE)
    VehicleNumber = models.CharField(max_length=100)
    VehicleModelname=models.CharField(max_length=100)
    photo = models.CharField(max_length=250)
    PollusionCertificate = models.CharField(max_length=100)
    rc= models.CharField(max_length=100)
    Insurance = models.CharField(max_length=100)
    NumberOfSeats= models.IntegerField()
    VehicleType = models.CharField(max_length=100)
    MinimumWagePerHour= models.CharField(max_length=100)
class Seats(models.Model):
    VEHICAL=models.ForeignKey(Vehicle,on_delete=models.CASCADE)
    NumberOfSeats=models.CharField(max_length=100)
    VaccantSeats=models.CharField(max_length=100)

class Booking(models.Model):
    USERS = models.ForeignKey(Users, on_delete=models.CASCADE)
    SEATS = models.ForeignKey(Seats, on_delete=models.CASCADE)
    Date = models.DateField()
    time = models.CharField(max_length=100)
    Destination = models.CharField(max_length=100)
    PickupPoint= models.CharField(max_length=100)
    PickupDate = models.DateField()
    PickupTime = models.CharField(max_length=100)
    EstimatedPrice=models.CharField(max_length=100)
    EstimatedRideTime=models.CharField(max_length=100)

class BookingLogs(models.Model):
    BOOKING= models.ForeignKey(Booking, on_delete=models.CASCADE)
    OtpVerifiaction=models.CharField(max_length=10)
    OtpDate = models.DateField()
    OtpTime=models.CharField(max_length=20)

class Location(models.Model):
    USERS = models.ForeignKey(Users, on_delete=models.CASCADE)
    Lattitude=models.CharField(max_length=100)
    Longitude=models.CharField(max_length=100)
    Place=models.CharField(max_length=100)

class RidePayments(models.Model):
    USERS = models.ForeignKey(Users, on_delete=models.CASCADE)
    BOOKING = models.ForeignKey(Booking, on_delete=models.CASCADE)
    Status=models.CharField(max_length=100)
    Amount=models.CharField(max_length=100)

class SubscriptionPayments(models.Model):
    DRIVERS = models.ForeignKey(Drivers, on_delete=models.CASCADE)
    Date = models.DateField()
    SubscriptionAmount = models.CharField(max_length=100)
    Status = models.CharField(max_length=100)

class Reviews(models.Model):
    USERS = models.ForeignKey(Users, on_delete=models.CASCADE)
    DRIVERS = models.ForeignKey(Drivers, on_delete=models.CASCADE)
    Date = models.DateField()
    Review= models.CharField(max_length=200)
    Rating = models.CharField(max_length=200)

class Complaints(models.Model):
    USERS = models.ForeignKey(Users, on_delete=models.CASCADE)
    Date = models.DateField()
    Complaints=models.CharField(max_length=200)
    Reply = models.CharField(max_length=200)
    ComplaintStatus = models.CharField(max_length=200)

class AppRating(models.Model):
    USERS = models.ForeignKey(Users, on_delete=models.CASCADE)
    Date = models.DateField()
    Review = models.CharField(max_length=200)
    Rating = models.CharField(max_length=200)











