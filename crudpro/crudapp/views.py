from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from crudapp.models import Entry

# Create your views here.
def home(request):
    return render(request,'home.html')
def show(request):
    data = Entry.objects.all()
    return render(request,'show.html',{'data':data})
def send(request):
    if request.method == 'POST':
        id = request.POST['id']
        data1 = request.POST['data1']
        data2 = request.POST['data2']
        Entry(id = id, data1 = data1, data2 = data2).save()
        msg = "data stored successfully."
        return render(request,"home.html",{'msg':msg})
    else:
        return HttpResponse('<h1>404 not found</h1>')

def delete(request):
    id = request.GET['id']
    Entry.objects.filter(id=id).delete()
    return HttpResponseRedirect('show')

def edit(request):
    id = request.GET['id']
    data1 = data2 = "not_available"
    for data in Entry.objects.filter(id=id):
        id = data.id
        data1 = data.data1
        data2 = data.data2
    return render(request,"edit.html",{'id':id,'data1':data1,'data2':data2})

def RecordEdited(request):
    if request.method == 'POST':
        id = request.POST['id']
        data1 = request.POST['data1']
        data2 = request.POST['data2']
        Entry.objects.filter(id=id).update(id = id, data1 = data1,data2 = data2)
        return HttpResponseRedirect("show")
    else:
        return HttpResponse('<h1>404 not found</h1>')