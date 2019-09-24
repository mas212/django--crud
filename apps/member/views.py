from django.shortcuts import render, redirect
from . import models as m
# Create your views here.
def index(request):
        contex = {
            'members' : m.Members.objects.order_by('-created_at')
        }
        return render(request, 'index.html', contex)

def create(request):
    return render(request, 'create.html') 

def store(request):
    if request.method == 'POST':
        member              = m.Members()
        member.name         = request.POST['name'] 
        member.position     = request.POST['position']  
        member.age          = request.POST['age']
        member.gender       = request.POST['gender']
        member.phone        = request.POST['phone']
        member.address      = request.POST['address']
        member.save()
    return redirect('member:index')

