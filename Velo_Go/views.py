from datetime import datetime

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

# Create your views here.
from Velo_Go.models import*


def login(request):
    return render(request,'admin/login.html')

def login_post(request):
    Username1 = request.POST['textfield']
    Password1 = request.POST['textfield2']
    lobj=Login.objects.filter(Username=Username1,Password=Password1)
    if lobj.exists():
        lobj1=Login.objects.get(Username=Username1,Password=Password1)
        request.session['lid']=lobj1.id
        if lobj1.Type == 'admin':
            return redirect('/velogo/admin_home/')
        else:
            return HttpResponse('''<script>alert("Invalid User!");window.location='/velogo/login/'</script>''')
    else:
        return HttpResponse('''<script>alert("Invalid User!");window.location='/velogo/login/'</script>''')


def admin_change_password(request):
    return render(request,'admin/Change password.html')

def admin_change_password_post(request):
    Current_Password=request.POST['textfield']
    New_password=request.POST['textfield2']
    Confirm_password=request.POST['textfield3']
    pobj=Login.objects.filter(id=request.session['lid'],Password=Current_Password)
    if pobj.exists():
        if New_password==Confirm_password:
            pobj1=Login.objects.filter(id=request.session['lid'],Password=Current_Password).update(Password=New_password)
            return HttpResponse('''<script>alert("Password Changed!");window.location='/velogo/login/'</script>''')
        else:
            return HttpResponse('''<script>alert("Password does not match!");window.location='/velogo/admin_change_password/'</script>''')
    else:
        return HttpResponse('''<script>alert("Invalid Credentials!");window.location='/velogo/admin_change_password/'</script>''')

def admin_driver_review(request):
    asd=Reviews.objects.all()

    return render(request,'admin/Driver Review.html',{"data":asd})

def driver_review(request):
    From = request.POST['textfield']
    To = request.POST['textfield2']
    zxc=Reviews.objects.filter(Date__range=[From,To],)
    return render(request, 'admin/Driver Review.html',{"data":zxc})


def admin_view_app_ratingandreview(request):
    var=AppRating.objects.all()
    return render(request,'admin/View app rating and review.html',{'data':var})

def view_app_rating_and_review(request):
    From = request.POST['textfield']
    To = request.POST['textfield2']
    frg=AppRating.objects.filter(Date__range=[From,To])
    return render(request,'admin/View app rating and review.html',{'data':frg})



def admin_view_approved_drivers(request):
    res = Drivers.objects.filter(Status='Approved')

    return render(request,'admin/View approved drivers.html',{'data':res})

def view_approved_drivers_post(request):
    From = request.POST['textfield']
    var=Drivers.objects.filter(name__icontains=From,Status='Approved')


    return render(request, 'admin/View approved drivers.html',{'data':var})

def admin_reply(request,id):
    var=Complaints.objects.get(id=id)
    return render(request,'admin/admin_reply.html',{'data':var})

def reply_post(request):
    id=request.POST['id']
    reply=request.POST['reply']
    var=Complaints.objects.get(id=id)
    var.Reply=reply
    var.ComplaintStatus='Replied'
    var.save()
    return HttpResponse(
        '''<script>alert("Reply Send!");window.location='/velogo/admin_view_driver_complaints/'</script>''')


def admin_view_driver_complaints(request):
    cv=Complaints.objects.all()
    return render(request,'admin/View driver complaints.html',{"data":cv})

def view_driver_complaints(request):
    From = request.POST['textfield']
    To = request.POST['textfield2']
    asd=Complaints.objects.filter(Date__range=[From,To],)

    return render(request, 'admin/View driver complaints.html',{'data':asd})

def admin_view_monthly_payments_from_drivers(request):
    var=SubscriptionPayments.objects.all()
    return render(request,'admin/View monthly payment from drivers.html',{'data':var})

def view_monthly_payments_from_drivers(request):
    From = request.POST['textfield']
    To = request.POST['textfield2']
    var=SubscriptionPayments.objects.filter(Date__range=[From,To])
    return render(request, 'admin/View monthly payment from drivers.html',{'data':var})

def admin_view_pending_drivers(request):
    res=Drivers.objects.filter(Status='pending')
    return render(request,'admin/View pending drivers.html',{'data':res})

def view_pending_drivers(request):
    From = request.POST['textfield']
    xyz= Drivers.objects.filter(name__icontains=From,Status='Pending')
    return render(request, 'admin/View pending drivers.html',{'data':xyz})

# def admin_view_rejected_drivers(request):
#     From = request.POST['textfield']
#     var = Drivers.objects.filter(name__icontains=From, Status='Rejected')
#     return render(request,'admin/View rejected drivers.html',{'data':var })
#
# def view_rejected_drivers(request):
#     res = Drivers.objects.filter(Status='Rejected')
#
#
#     return render(request, 'admin/View rejected drivers.html',{'data':res})


def view_reject_driver(request):
    var=Drivers.objects.filter(Status='Rejected')
    return render(request,'admin/View rejected drivers.html',{'data':var})

def view_reject_driver_post(request):
    f=request.POST['textfield']
    var=Drivers.objects.filter(name__icontains=f,Status='Rejected')
    return render(request,'admin/View rejected drivers.html',{'data':var})





def admin_view_user(request):
    poi=Users.objects.all()
    return render(request,'admin/View user.html',{'data':poi})

def view_user(request):
    From = request.POST['textfield']
    rew=Users.objects.filter(Name__icontains=From)
    return render(request, 'admin/View user.html',{'data':rew})

def admin_home(request):
    return render(request,'admin/home.html')

def approve_drivers(request,id):
    abc=Drivers.objects.filter(LOGIN_id=id).update(Status="Approved")
    jish=Login.objects.filter(id=id).update(Type="driver")
    return HttpResponse(
        '''<script>alert("Approve Drivers!");window.location='/velogo/admin_view_approved_drivers/'</script>''')

def reject_drivers(request,id):
    abc=Drivers.objects.filter(LOGIN_id=id).update(Status="Rejected")
    jish=Login.objects.filter(id=id).update(Type="pending")
    return HttpResponse(
        '''<script>alert("Reject Drivers!");window.location='/velogo/view_reject_driver/'</script>''')






def DriverLogin(request):
    username=request.POST["name"]
    password=request.POST["password"]
    print(username,"uuu")
    print(password,"haiii")
    a=Login.objects.filter(Username=username,Password=password)
    if a.exists():
        b = Login.objects.get(Username=username, Password=password)
        print("haii")
        if b.Type=="driver":
            return JsonResponse({"status":"ok","type":'driver',"lid":str(b.id)})
        elif b.Type=="User":
            return JsonResponse({"status":"ok","type":"User","lid":str(b.id)})
        else:
            print("gggggggg")
            return JsonResponse({"Status": "notok"})
    else:
        return JsonResponse({"Status": "notok"})



def driver_Signup(request):
    name=request.POST["name"]
    place=request.POST["place"]
    post=request.POST["post"]
    city=request.POST["city"]
    state=request.POST["state"]
    pin = request.POST["pin"]
    DateofBirth = request.POST["DateOfBirth"]
    phone = request.POST["phone"]
    photo = request.POST["photo"]
    lisence = request.POST["lisence"]
    email = request.POST["email"]
    upi=request.POST["upi"]
    gender=request.POST["gender"]
    languagesknown=request.POST["languagesKnown"]
    Password=request.POST["password"]
    ConfirmPassword=request.POST["confirmpassword"]


    import datetime
    import base64
    #
    date = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    a = base64.b64decode(photo)
    fh = open("C:\\Users\\jishn\\OneDrive\\Desktop\\velogo\\VeloGO\\media\\driver\\" + date + ".jpg", "wb")
    # fh = open("C:\\Users\\91815\\PycharmProjects\\cyber\\media\\" + date + ".jpg", "wb")
    path = "/media/driver/" + date + ".jpg"
    fh.write(a)
    fh.close()



    date1 = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    a1 = base64.b64decode(lisence)
    fh1 = open("C:\\Users\\jishn\\OneDrive\\Desktop\\velogo\\VeloGO\\media\\Licence\\" + date + ".jpg", "wb")
    # fh = open("C:\\Users\\91815\\PycharmProjects\\cyber\\media\\" + date + ".jpg", "wb")
    path1 = "/media/Licence/" + date1 + ".jpg"
    fh1.write(a1)
    fh1.close()
    b = Login()
    b.Username = email
    b.Password = ConfirmPassword
    b.Type = "pending"
    b.save()

    a = Drivers()
    a.name = name
    a.place = place
    a.post = post
    a.city = city
    a.state = state
    a.pin = pin
    a.DateOfBirth = DateofBirth
    a.phone = phone
    a.photo = path
    a.lisence = path1
    a.email = email
    a.upi = upi
    a.gender = gender
    a.languagesknown = languagesknown
    a.LOGIN = b
    a.Status = "pending"
    a.save()
    return JsonResponse({"status": "ok"})
    # res = Drivers.objects.filter(LOGIN=lid).update(name=name, dob=DateofBirth, gender=gender, phone=phone, email=email,
    #                                                photo=path, place=place, post=post, pin=pin, state=state,
    #                                                city=city, lisence=lisence, upi=upi, languagesknown=languagesknown)
    # if Password==ConfirmPassword:
    #     b = Login()
    #     b.Username = email
    #     b.Password = ConfirmPassword
    #     b.Type = "pending"
    #     b.save()
    #
    #     a = Drivers()
    #     a.name = name
    #     a.place = place
    #     a.post = post
    #     a.city = city
    #     a.state = state
    #     a.pin = pin
    #     a.DateOfBirth = DateofBirth
    #     a.phone = phone
    #     a.photo = path
    #     a.lisence = path1
    #     a.email = email
    #     a.upi = upi
    #     a.gender = gender
    #     a.languagesknown = languagesknown
    #     a.LOGIN = b
    #     a.Status = "pending"
    #     a.save()
    #     return JsonResponse({"Status":"ok"})
    # else:
    #     return JsonResponse({"Status":"notok"})


def DriverChangepasswd(request):
    Oldpasswd=request.POST["Old"]
    Confirm=request.POST["Confirm"]
    Newpasswd=request.POST["New"]
    pobj = Login.objects.filter(id=request.session['lid'], Password=Oldpasswd)
    if pobj.exists():
        if Confirm == Newpasswd:
            pobj1 = Login.objects.filter(id=request.session['lid'], Password=Oldpasswd).update(
                Password=Newpasswd)
            return JsonResponse({"Status": "ok"})
        else:
            return JsonResponse({"Status": "notok"})
    else:
        return JsonResponse({"Status":"notok"})




def DriversViewProfile(request):
    lid=request.POST["lid"]
    print(lid,"lid")
    i=Drivers.objects.get(LOGIN_id=lid)
    print(i.lisence,"hii")
    return JsonResponse({"status": "ok",'name':i.name,'place':i.place,'post':i.Post,'city':i.city,'state':i.state,'pin':i.pin,
                  'DateOfBirth':i.DateOfBirth,'phone':i.phone,'photo':i.photo,'lisence':i.lisence,'email':i.email,
                  'upi':i.upi,'gender':i.gender,'languagesknown':i.languagesknown})



def DriversEditProfile(request):
    lid=request.POST["lid"]
    i=Drivers.objects.get(LOGIN_id=lid)
    l=[]
    l.append(
        {'id': i.id, 'name': i.name, 'place': i.place, 'post': i.post, 'city': i.city, 'state': i.state, 'pin': i.pin,
         'DateOfBirth': i.DateOfBirth, 'phone': i.phone, 'photo': i.photo, 'lisence': i.lisence, 'email': i.email,
         'upi': i.upi, 'gender': i.gender, 'languagesknown': i.languagesknown})
    return JsonResponse({"status": "ok"})



def Driver_edit_profile_post(request):
    lid=request.POST['lid']
    name = request.POST["name"]
    place = request.POST["place"]
    post = request.POST["post"]
    city = request.POST["city"]
    state = request.POST["state"]
    pin = request.POST["pin"]
    DateofBirth = request.POST["DateOfBirth"]
    phone = request.POST["phone"]
    photo = request.POST["photo"]
    lisence = request.POST["lisence"]
    email = request.POST["email"]
    upi = request.POST["upi"]
    gender = request.POST["gender"]
    languagesknown = request.POST["languagesKnown"]
    # blood=request.POST['blood']
    from datetime import datetime
    # date = datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpg"
    print(len(photo+"hloooo"))
    if len(photo)<5:
        import datetime
        import base64
        #
        date = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        a = base64.b64decode(photo)
        fh = open("C:\\Users\\jishn\\OneDrive\\Desktop\\velogo\\VeloGO\\media\\driver\\" + date + ".jpg", "wb")
        # fh = open("C:\\Users\\91815\\PycharmProjects\\cyber\\media\\" + date + ".jpg", "wb")
        path = "/media/driver/" + date + ".jpg"
        fh.write(a)
        fh.close()
        res=Drivers.objects.filter(LOGIN=lid).update(name=name,DateOfBirth=DateofBirth,gender=gender,phone=phone,email=email,photo=path,place=place,Post=post,pin=pin,state=state,
                                                    city=city,upi=upi,languagesknown=languagesknown)
        return JsonResponse({'status':"ok"})
    elif len(lisence)<5:
        import datetime
        import base64
        date1 = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        a1 = base64.b64decode(lisence)
        fh1 = open("C:\\Users\\jishn\\OneDrive\\Desktop\\velogo\\VeloGO\\media\\Licence\\" + date1 + ".jpg", "wb")
        # fh = open("C:\\Users\\91815\\PycharmProjects\\cyber\\media\\" + date + ".jpg", "wb")
        path1 = "/media/Licence/" + date1 + ".jpg"
        fh1.write(a1)
        fh1.close()


        res=Drivers.objects.filter(LOGIN=lid).update(name=name,DateOfBirth=DateofBirth,gender=gender,phone=phone,email=email,place=place,Post=post,pin=pin,state=state,
                                                    city=city,lisence=path1,upi=upi,languagesknown=languagesknown)

    res=Drivers.objects.filter(LOGIN=lid).update(name=name,DateOfBirth=DateofBirth,gender=gender,phone=phone,email=email,place=place,Post=post,pin=pin,state=state,
                                                 city=city, lisence=lisence, upi=upi, languagesknown=languagesknown)
    return JsonResponse({'status':"ok"})






def AddVehicle(request):
    lid=request.POST["lid"]
    VehicleNumber=request.POST["VehicleNumber"]
    VehicleName=request.POST["VehicleName"]
    photo=request.POST["photo"]
    PollusionCertificate = request.POST["PollusionCertificate"]
    rc = request.POST["rc"]
    Insurance = request.POST["Insurance"]
    NumberOfSeats = request.POST["NumberOfSeats"]
    VehicleType = request.POST["VehicleType"]
    MinimumWagePerHour = request.POST["MinimumWagePerHour"]
    import datetime
    import base64
    #
    date = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    a = base64.b64decode(photo)
    fh = open("C:\\Users\\jishn\\OneDrive\\Desktop\\velogo\\VeloGO\\media\\vehicle\\" + date + ".jpg", "wb")
    # fh = open("C:\\Users\\91815\\PycharmProjects\\cyber\\media\\" + date + ".jpg", "wb")
    path = "\\media\\vehicle\\" + date + ".jpg"
    fh.write(a)
    fh.close()


    date1 = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    a1 = base64.b64decode(rc)
    fh1 = open("C:\\Users\\jishn\\OneDrive\\Desktop\\velogo\\VeloGO\\media\\rc\\" + date1 + ".jpg", "wb")
    # fh = open("C:\\Users\\91815\\PycharmProjects\\cyber\\media\\" + date + ".jpg", "wb")
    path1 = "\\media\\rc\\" + date1 + ".jpg"
    fh1.write(a1)
    fh1.close()

    date2 = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    a2 = base64.b64decode(PollusionCertificate)
    fh2 = open("C:\\Users\\jishn\\OneDrive\\Desktop\\velogo\\VeloGO\\media\\pollusion\\" + date2 + ".jpg", "wb")
    # fh = open("C:\\Users\\91815\\PycharmProjects\\cyber\\media\\" + date + ".jpg", "wb")
    path2 = "\\media\\pollusion\\" + date2 + ".jpg"
    fh2.write(a2)
    fh2.close()

    date3 = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    a3 = base64.b64decode(Insurance)
    fh3 = open("C:\\Users\\jishn\\OneDrive\\Desktop\\velogo\\VeloGO\\media\\insurance\\" + date3 + ".jpg", "wb")
    # fh = open("C:\\Users\\91815\\PycharmProjects\\cyber\\media\\" + date + ".jpg", "wb")
    path3 = "\\media\\insurance\\" + date3 + ".jpg"
    fh3.write(a3)
    fh3.close()











    d=Vehicle()
    d.DRIVERS=Drivers.objects.get(LOGIN_id=lid)
    d.VehicleNumber=VehicleNumber
    d.VehicleModelname=VehicleName
    d.photo=path
    d.PollusionCertificate=path2
    d.rc=path1
    d.Insurance=path3
    d.NumberOfSeats=NumberOfSeats
    d.VehicleType=VehicleType
    d.MinimumWagePerHour=MinimumWagePerHour
    d.save()
    return JsonResponse({"status":"ok"})

def DriverViewVehicle(request):
    lid=request.POST["lid"]
    e=Vehicle.objects.filter(DRIVERS__LOGIN__id=lid)

    l=[]
    for i in e:
        l.append({"id":i.id,'VehicleNumber':i.VehicleNumber,'VehicleModelname':i.VehicleModelname,'photo':i.photo,'PollusionCertificate':i.PollusionCertificate,'rc':i.rc,'Insurance':i.Insurance,
                  'NumberOfSeats':i.NumberOfSeats,'VehicleType':i.VehicleType,'MinimumWagePerHour':i.MinimumWagePerHour})

        return JsonResponse({"status":"ok",'data':l})


def DriverEditVehicle(request):
    lid = request.POST["lid"]
    i=Vehicle.objects.get(DRIVERS__LOGIN_id=lid)

    l=[]
    l.append(
        {"id": i.id, 'name': i.name, 'place': i.place, 'post': i.post, 'city': i.city, 'state': i.state, 'pin': i.pin,
         'DateOfBirth': i.DateOfBirth, 'phone': i.phone, 'photo': i.photo, 'lisence': i.lisence, 'email': i.email,
         'upi': i.upi, 'gender': i.gender, 'languagesknown': i.languagesknown})
    return JsonResponse({"status": "ok", 'data': l})

def EditVehicle_post(request):
    lid = request.POST["lid"]
    VehicleNumber = request.POST["VehicleNumber"]
    photo = request.POST["photo"]
    PollusionCertificate = request.POST["PollusionCertificate"]
    rc = request.POST["rc"]
    Insurance = request.POST["Insurance"]
    NumberOfSeats = request.POST["NumberOfSeats"]
    VehicleType = request.POST["VehicleType"]
    MinimumWagePerHour = request.POST["MinimumWagePerHour"]

    if len(photo) > 0:

        import datetime
        import base64
        #
        date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        a = base64.b64decode(photo)
        fh = open("C:\\Users\\jishn\\OneDrive\\Desktop\\velogo\\VeloGO\\Velo_Go\\media\\vehicle\\" + date + ".jpg", "wb")
        # fh = open("C:\\Users\\91815\\PycharmProjects\\cyber\\media\\" + date + ".jpg", "wb")
        path = "/media/" + date + ".jpg"
        fh.write(a)
        fh.close()
        res = Vehicle.objects.filter(LOGIN=lid).update(VehicleNumber=VehicleNumber, photo=path, PollusionCertificate=PollusionCertificate,
                                                       rc=rc, Insurance=Insurance,NumberOfSeats=NumberOfSeats, VehicleType=VehicleType, MinimumWagePerHour=MinimumWagePerHour,)
        return JsonResponse({'status': "ok"})

    else:
        res = Vehicle.objects.filter(LOGIN=lid).update(VehicleNumber=VehicleNumber,
                                                       PollusionCertificate=PollusionCertificate,
                                                       rc=rc, Insurance=Insurance, NumberOfSeats=NumberOfSeats,
                                                       VehicleType=VehicleType, MinimumWagePerHour=MinimumWagePerHour, )
        return JsonResponse({'status': "ok"})

def Driver_delete_vehicle(request):
    vid = request.POST['vid']
    ress = Vehicle.objects.filter(id=vid).delete()
    return JsonResponse({"status": "ok"})



def Driver_Add_Seat(request):
    vid = request.POST["vid"]
    NumberOfSeats=request.POST["Number Of Seats"]
    VaccantSeats=request.POST["Vaccant Seats"]
    a=Seats()
    a.NumberOfSeats=NumberOfSeats
    a.VaccantSeats=VaccantSeats
    a.VEHICAL=Vehicle.objects.get(id=vid)
    a.save()
    return JsonResponse({'status': "ok"})

def Driver_view_seats(request):
    vid = request.POST["vid"]
    var=Seats.objects.filter(VEHICAL__id=vid)
    l=[]
    for i in var:
        l.append({'id':i.id,"NumberOfSeats":i.NumberOfSeats,"VaccantSeats":i.VaccantSeats})
        return JsonResponse({'status': "ok","data":l})


def Driver_edit_seats(request):
    sid = request.POST["sid"]
    i=Seats.objects.get(id=sid)
    return JsonResponse({"status": "ok","id": i.id,'NumberOfSeatsme': i.NumberOfSeats,'VaccantSeats': i.VaccantSeats})






def Driver_edit_seats_post(request):
    sid = request.POST["sid"]
    NumberOfSeats = request.POST["NumberOfSeats"]
    VaccantSeats = request.POST["VaccantSeats"]

    a=Seats.objects.get(id=sid)
    a.NumberOfSeats = NumberOfSeats
    a.VaccantSeats = VaccantSeats
    a.save()
    return JsonResponse({'status': "ok"})

def delete_seat(request):
    vid=request.POST['vid']
    ress=Seats.objects.filter(VEHICAL__id=vid).delete()
    return JsonResponse({"status":"ok"})



def Driver_view_allocated_booking(request):
    lid = request.POST["lid"]
    a=Booking.objects.filter(SEATS__VEHICAL__DRIVERS__LOGIN_id=lid)
    l=[]
    for i in a:
        l.append({"id":i.id,"VaccantSeats":i.SEATS.VaccantSeats,"NumberOfSeats":i.SEATS.NumberOfSeats,"Date":i.Date,"time":i.time,"Destination":i.Destination,
                  "PickupPoint":i.PickupPoint,"PickupDate":i.PickupDate,"PickupTime":i.PickupTime,"EstimatedPrice":i.EstimatedPrice,
                  "EstimatedRideTime":i.EstimatedRideTime,"Name":i.USERS.Name,"phone":i.USERS.phone})
    return JsonResponse({'status': "ok",'data':l})




def updatelocation(request):

    lat = request.POST['lat']
    lon = request.POST['lon']
    lid = request.POST['lid']
    try:
        ob=DriverLocation.objects.get(BUS__LOGIN=lid)
        ob.Lattitude=lat
        ob.Longitude=lon
        ob.save()
        print("===============")
        return JsonResponse({"task": "ok"})
    except:
        ob = DriverLocation()
        ob.Lattitude = lat
        ob.Longitude = lon
        ob.date=datetime.now()
        ob.time=datetime.now().strftime("%H:%M:%S")
        bb=Bus.objects.get(id=aid)
        ob.BUS = bb
        ob.save()
        print("+++++++++++++++++")
        return JsonResponse({"task": "ok"})











def Driver_otp_Verification(request):
    lid = request.POST["lid"]
    OtpVerifiaction = request.POST["OtpVerifiaction"]
    date=datetime.now().date().today()
    time=datetime.now().time()
    a=BookingLogs()
    a.OtpVerifiaction=OtpVerifiaction
    a.OtpDate=date
    a.OtpTime=time
    a.BOOKING=Booking.objects.filter(SEATS__VEHICAL__DRIVERS__LOGIN__id=lid)
    return JsonResponse({'status': "ok"})


def Driver_view_Passengers_And_DropPoints(request):
    lid=request.POST["lid"]
    # a=Booking.objects.filter(SEATS__VEHICAL__DRIVERS__LOGIN_id=lid)
    a=Booking.objects.all()
    l=[]
    for i in a:
        l.append({"id":i.id,"name":i.USERS.Name,"PickupPoint":i.PickupPoint,"Destination":i.Destination,"PickupDate":i.PickupDate,
                  "PickupTime":i.PickupTime,"EstimatedPrice":i.EstimatedPrice,"EstimatedRideTime":i.EstimatedRideTime})
        return JsonResponse({'status': "ok", 'data': l})

def Driver_View_payment(request):
    lid=request.POST["lid"]
    a=RidePayments.objects.filter(BOOKING__SEATS__VEHICAL__DRIVERS__LOGIN_id=lid)
    l=[]
    for i in a:
        l.append({"id":i.id,"name":i.USERS.Name,"date":i.BOOKING.PickupDate,"time":i.BOOKING.PickupTime,
                  "Destination":i.BOOKING.Destination,"pickupPoint":i.BOOKING.PickupPoint,"Amount":i.Amount,
                  "Status":i.Status})
        return JsonResponse({'status': "ok", 'data': l})

def Driver_view_previous_booking(request):
    lid = request.POST["lid"]
    a = Booking.objects.filter(SEATS__VEHICAL__DRIVERS__LOGIN_id=lid)
    l = []
    for i in a:
        l.append(
            {"id": i.id, "name": i.USERS.Name, "PickupPoint": i.PickupPoint, "Destination": i.Destination, "PickupDate": i.PickupDate,
             "PickupTime": i.PickupTime, "EstimatedPrice": i.EstimatedPrice, "EstimatedRideTime": i.EstimatedRideTime})
        return JsonResponse({'status': "ok", 'data': l})

def Driver_view_rating(request):
    lid = request.POST["lid"]
    a=Reviews.objects.filter(DRIVERS__LOGIN__id=lid)
    l=[]
    for i in a:
        l.append({"id":i.id,"name":i.USERS.Name,"Review":i.Review,"Rating":i.Rating,"Date":i.Date})
    return JsonResponse({'status': "ok", 'data': l})

def Driver_Send_monthly_payment(request):
    lid = request.POST["lid"]
    Amount=request.POST['Amount']
    a=SubscriptionPayments()
    a.SubscriptionAmount=Amount
    from  datetime import  datetime
    a.Date=datetime.now().strftime('%Y-%m-%d')
    a.Status='Pending'
    a.DRIVERS=Drivers.objects.get(LOGIN_id=lid)
    a.save()
    return JsonResponse({'status': "ok"})











def user_Signup(request):
    name=request.POST["name"]
    place=request.POST["place"]
    post=request.POST["post"]
    city=request.POST["city"]
    state=request.POST["state"]
    pin = request.POST["pin"]
    DateofBirth = request.POST["DateOfBirth"]
    phone = request.POST["phone"]
    photo = request.POST["photo"]
    email = request.POST["email"]
    gender=request.POST["gender"]
    Password=request.POST["password"]
    ConfirmPassword=request.POST["confirmpassword"]


    import datetime
    import base64
    #
    date = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    a = base64.b64decode(photo)
    fh = open("C:\\Users\\jishn\\OneDrive\\Desktop\\velogo\\VeloGO\\media\\User\\" + date + ".jpg", "wb")
    # fh = open("C:\\Users\\91815\\PycharmProjects\\cyber\\media\\" + date + ".jpg", "wb")
    path = "/media/User/" + date + ".jpg"
    fh.write(a)
    fh.close()

    b = Login()
    b.Username = email
    b.Password = ConfirmPassword
    b.Type = "User"
    b.save()

    a = Users()
    a.Name = name
    a.place = place
    a.Post = post
    a.city = city
    a.state = state
    a.pin = pin
    a.DateOfBirth = DateofBirth
    a.phone = phone
    a.photo = path
    a.email = email
    a.gender = gender
    a.LOGIN = b
    a.save()
    return JsonResponse({"status": "ok"})


def UserViewProfile(request):
    lid=request.POST["lid"]
    print(lid,"lid")
    i=Users.objects.get(LOGIN_id=lid)
    return JsonResponse({"status": "ok",'name':i.Name,'place':i.place,'post':i.Post,'city':i.city,'state':i.state,'pin':i.pin,
                  'DateOfBirth':i.DateOfBirth,'phone':i.phone,'photo':i.photo,'email':i.email,
            'gender':i.gender})

def UserChangepasswd(request):
    Oldpasswd=request.POST["Old"]
    Confirm=request.POST["Confirm"]
    Newpasswd=request.POST["New"]
    pobj = Login.objects.filter(id=request.session['lid'], Password=Oldpasswd)
    if pobj.exists():
        if Confirm == Newpasswd:
            pobj1 = Login.objects.filter(id=request.session['lid'], Password=Oldpasswd).update(
                Password=Newpasswd)
            return JsonResponse({"Status": "ok"})
        else:
            return JsonResponse({"Status": "notok"})
    else:
        return JsonResponse({"Status":"notok"})


# def User_send_AppRating(request):
#     lid = request.POST["lid"]
#     a=Reviews.objects.filter(DRIVERS__LOGIN__id=lid)
#     l=[]
#     for i in a:
#         l.append({"id":i.id,"name":i.USERS.Name,"Review":i.Review,"Rating":i.Rating,"Date":i.Date})
#     return JsonResponse({'status': "ok", 'data': l})
#

def User_send_AppRating(request):
        lid = request.POST["lid"]
        # i = AppRating.objects.get(USERS__LOGIN_id=lid)
        from datetime import datetime
        review=request.POST['review']
        rating=request.POST['Rating']
        r=AppRating()
        r.USERS=Users.objects.get(LOGIN=lid)
        r.Date=datetime.now().date().today()
        r.Review=review
        r.Rating=rating
        r.save()
        return JsonResponse({"status": "ok"})

def User_Send_complaint(request):
    lid=request.POST["lid"]
    complaint=request.POST["complaint"]
    from datetime import datetime
    c=Complaints()






























