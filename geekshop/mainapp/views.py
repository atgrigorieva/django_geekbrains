from django.shortcuts import render

def main(request):
    return render(request, 'mainapp/index.html')


def contacts(request):
    return render(request, 'mainapp/contacts.html')


def cooperation(request):
    return render(request, 'mainapp/cooperation.html')


def about_us(request):
    return render(request, 'mainapp/about_us.html')