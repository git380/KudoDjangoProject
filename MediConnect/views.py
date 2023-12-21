from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from MediConnect.models import Employee, Tabyouin, Patient, Medicine, Treatment


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


def pw_change(request):
    if request.method == 'GET':
        return render(request, 'employee/E103/pwChange.html')

    if request.method == 'POST':
        Employee.objects.filter(empid=request.session['empId']).update(emppasswd=request.POST['empPasswd1'])
        return render(request, 'ok.html')


def patient_registration(request):
    if request.method == 'GET':
        return render(request, 'patient/P101/patientRegistration.html')

    if request.method == 'POST':
        patid = request.POST['patId']
        hokenexp = datetime.strptime(request.POST['hokenexp'], '%Y-%m-%d')

        if Patient.objects.filter(patid=patid).exists():
            return HttpResponse('IDが一致しています。')
        else:
            if hokenexp > datetime.now():
                Patient(patid=patid, patfname=request.POST['patFname'], patlname=request.POST['patLname'],
                        hokenmei=request.POST['hokenmei'], hokenexp=hokenexp).save()
                return render(request, 'ok.html')
            else:
                return HttpResponse('新しい日付を入力してください。')


def patient_all(request):
    if Patient.objects.exists():
        return render(request, 'patient/P102/patientAll.html', {'patients': Patient.objects.all()})
    else:
        return HttpResponse("データベースは空です。")


def patient_update(request):
    if request.method == 'GET':
        return render(request, 'patient/P102/patientUpdate.html', {
            'patId': request.GET['patId'],
            'patFname': request.GET['patFname'],
            'patLname': request.GET['patLname'],
            'hokenmei': request.GET['hokenmei'],
            'hokenexp': request.GET['hokenexp'],
        })

    if request.method == 'POST':
        hokenexp = datetime.strptime(request.POST['hokenexp'], "%Y-%m-%d").date()

        if not hokenexp:
            return HttpResponse('日付を入力してください。')

        if hokenexp > datetime.strptime(request.POST['oldhokenexp'], "%Y-%m-%d").date():
            Patient.objects.filter(patid=request.POST['patId']).update(hokenmei=request.POST['hokenmei'], hokenexp=hokenexp)
            return render(request, 'ok.html')
        else:
            return HttpResponse('新しい日付を入力してください。')


def patient_search_by_name(request):
    if request.method == 'GET':
        return render(request, 'patient/P103/search_form.html')

    if request.method == 'POST':
        name = request.POST['name']
        matching_patients = Patient.objects.filter(Q(patlname=name) | Q(patfname=name))

        if not matching_patients:
            return HttpResponse('該当する患者がいません')

        return render(request, 'patient/P103/search_results.html', {'patients': matching_patients})


def patient_search(request):
    if request.method == 'GET':
        return render(request, 'patient/P105/patientSearchResult.html', {'patients': Patient.objects.all()})


def treatment_selection(request):
    if request.method == 'GET':
        return render(request, 'treatment/D101/treatmentSelection.html', {
            'medicines': Medicine.objects.all(),
            'patId': request.GET['patId'],
        })

    if request.method == 'POST':
        return render(request, 'treatment/D101/treatmentSelectionResult.html', {
            'patId': request.POST['patId'],
            'medicineId': request.POST['medicineId'],
            'quantity': int(request.POST['quantity']),
            'impDate': datetime.strptime(request.POST['impDate'], "%Y-%m-%d").date(),
        })


def treatment_delete(request):
    if request.method == 'POST':
        return render(request, 'ok.html')


def treatment_confirmation(request):
    if request.method == 'POST':
        try:
            Treatment(patid=request.POST['patId'],
                      medicineid=request.POST['medicineId'],
                      quantity=request.POST['quantity'],
                      impdate=datetime.strptime(request.POST['impDate'], '%Y-%m-%d').date()).save()
        except Exception as e:
            print(e)
            return HttpResponse('エラー')

        return render(request, 'ok.html')


def treatment_list(request):
    if Treatment.objects.exists():
        return render(request, 'treatment/D104/treatmentList.html', {'treatments': Treatment.objects.all()})
    else:
        return HttpResponse("データベースは空です。")
