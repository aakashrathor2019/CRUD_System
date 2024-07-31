from django.shortcuts import render,redirect
from .models import Employee

# Create your views here.
def home(request):
  emp=Employee.objects.all()
  return render(request,'home.html',{'emp':emp})

def add(request):
  if request.method=='POST':
    enrl=request.POST.get('empid')
    empName=request.POST.get('empName')
    empEmail=request.POST.get('empEmail')
    empAddress=request.POST.get('empAdd')
    empMo=request.POST.get('empMo')
    print('emp name is:',empName)
    print('emp email is:',empEmail)
    data=Employee.objects.create(
       roll=enrl,
       name=empName,
       email=empEmail,
       address=empAddress,
       contact=empMo
    )
    data.save()
    if data:
      print('Data Added')
      return redirect('homepage')
  try:
      last_record=Employee.objects.latest('roll')
      if last_record:
        last_id= last_record.roll
      else:
        last_id=0
  except:
      last_id=0
  return render(request,'add.html',{'roll':last_id+1})

def delete(request,roll):
  del_emp=Employee.objects.get(pk=roll)
  del_emp.delete()
  return redirect('homepage')

def update(request,roll):
  emp=Employee.objects.get(pk=roll)
  return render(request,"update.html",{'emp':emp})


def do_update(request,roll):
  enrl=request.POST.get('empid')
  empName=request.POST.get('empName')
  empEmail=request.POST.get('empEmail')
  empAddress=request.POST.get('empAdd')
  empMo=request.POST.get('empMo')
  print

  emp=Employee.objects.get(id=roll)

  emp.roll=enrl
  emp.name=empName
  emp.email=empEmail
  emp.address=empAddress
  emp.contact=empMo

  emp.save()
  return redirect('homepage')