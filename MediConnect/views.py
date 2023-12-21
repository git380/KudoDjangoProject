from django.shortcuts import render, redirect
from django.http import HttpResponse
from MediConnect.models import Employee, Tabyouin


def index(request):
    request.session.flush()
    return render(request, 'index.html')


def login(request):
    if request.method == 'GET':
        return render(request, 'login/login.html')

    if request.method == 'POST':
        empId = request.POST['empId']
        try:
            employee_info = Employee.objects.get(empid=empId, emppasswd=request.POST['empPasswd'])
            request.session['empId'] = empId
            request.session['emprole'] = employee_info.emprole
            return redirect('welcome')
        except Employee.DoesNotExist:
            return render(request, 'login/error.html')


def welcome(request):
    role = request.session['emprole']
    if role == 1:
        return render(request, 'administrator.html')
    elif role == 2:
        return render(request, 'reception.html')
    elif role == 3:
        return render(request, 'physician.html')

    return HttpResponse('エラー')


def logout(request):
    request.session.flush()
    return render(request, 'login/logout.html')


def register(request):
    if request.method == 'GET':
        return render(request, 'employee/E101/register.html')

    if request.method == 'POST':
        empId = request.POST['empId']

        if Employee.objects.filter(empid=empId).exists():
            return HttpResponse('IDが一致しています')
        else:
            Employee(empid=empId, empfname=request.POST['fName'], emplname=request.POST['lName'],
                     emppasswd=request.POST['empPasswd'], emprole=int(request.POST['empRole'])).save()
            return render(request, 'ok.html')


def hospital_list(request):
    return render(request, 'hospital/H102/hospital_list.html', {'hospitals': Tabyouin.objects.all()})


def tel_change(request):
    if request.method == 'GET':
        return render(request, 'hospital/H105/telChange.html', {'tabyouinid': request.GET['tabyouinid']})

    if request.method == 'POST':
        Tabyouin.objects.filter(tabyouinid=request.POST['tabyouinid']).update(tabyouintel=request.POST['tel'])
        return render(request, 'ok.html')


def hospital_search(request):
    if request.method == 'GET':
        return render(request, 'hospital/H104/hospitalSearch.html')

    if request.method == 'POST':
        shihonkin = request.POST['shihonkin']
        if shihonkin == '':
            shihonkin = 0
        return render(request, 'hospital/H104/hospitalSearchResult.html',
                      {'hospitals': Tabyouin.objects.filter(tabyouinshihonkin__gt=shihonkin)})
