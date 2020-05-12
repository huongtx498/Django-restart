from django.shortcuts import render
from django.http import HttpResponse
from .forms import HomeForm

# Create your views here.


def home(request):
    if request.method == 'POST':
        response = HttpResponse()
        response.write("<h1>Thanks for registering</h1></br>")
        response.write("Giống chó: " + request.POST['ten'] + "</br>")
        response.write("Màu lông: " + request.POST['mausac'] + "</br>")
        response.write("Kích thước: " + request.POST['kichthuoc'] + "</br>")
        response.write("Phụ kiện: " + request.POST['phukien'] + "</br>")
        response.write("Ảnh: " + request.POST['anh'] + "</br>")
        return response
    homeForm = HomeForm()
    return render(request, 'home/home.html', {'form': homeForm})
