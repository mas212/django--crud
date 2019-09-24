from django.shortcuts import render, redirect
from . import models as m
from django.contrib import messages
# Create your views here.
#EMAIL_REGEX = re.compile(r'^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$')
def index(request):
        contex = {
            'members' : m.Members.objects.order_by('-created_at')
        }
        return render(request, 'index.html', contex)

def create(request):
    return render(request, 'create.html') 

def store(request):
    errors = []
    if request.method == 'POST':
        try:
            name         = request.POST['name'] 
            position     = request.POST['position']  
            age          = request.POST['age']
            gender       = request.POST['gender']
            phone        = request.POST['phone']
            address      = request.POST['address']
            if  len(name) == 0 or len(position) == 0 or len(age) == 0 or len(gender) == 0 or len(phone)== 0 or len(address) == 0:
                errors.append("Fields cannot be blank.")
                messages.error(request, "Fields cannot be blank.")
            if len(errors) == 0 :
                member              = m.Members()
                member.name         = name 
                member.position     = position 
                member.age          = age
                member.gender       = gender
                member.phone        = phone
                member.address      = address
                member.save()
                return redirect('member:index')
        except:
            messages.error(request, 'Invalid input') 
    return redirect('member:create')

def edit(request, member_id):
    contex = {
        'member' : m.Members.objects.get(id=member_id)
    }
    return render(request, 'edit.html', contex)

def update(request, member_id):
    errors = []

    if request.method == "POST":
        member        = m.Members.objects.get(id=member_id)
        contex = {
            'member' : member
        }
        try:
            member.name         = request.POST['name'] 
            member.position     = request.POST['position']  
            member.age          = request.POST['age']
            member.gender       = request.POST['gender']
            member.phone        = request.POST['phone']
            member.address      = request.POST['address']
            member.save()
            return redirect('member:index')
        except:
            messages.error(request, 'Member update error')
            return render(request, 'edit.html', contex)
    else:
       return render(request, 'edit.html', contex) 

def delete(request, member_id):
    member  = m.Members.objects.get(id=member_id)
    member.delete()
    return redirect('member:index')

