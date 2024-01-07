from django.shortcuts import render

def LoadIndex(request):
    return render(request, 'website/index.html')


def LoadAbout(request):
    return render(request, 'website/about.html')


def LoadContact(request):
    return render(request, 'website/contact.html')