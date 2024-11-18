from django.http import HttpResponse
from django.shortcuts import render

def hello(request): 
    total = 10+28
    return render(request,'index.html',{total:total})

def about(request):
    return HttpResponse('about')

def analyzar(request):
    # this is string 
    get = request.POST.get('text','pass')
    # this is validation
    removepunc= request.POST.get('removepunc','off')
    upper = request.POST.get('uppercase','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspace = request.POST.get('extraspace','off')
    puncs = '!@#$%^&*()_+:"{}[]/?'
    # all condations
    
    if removepunc == 'on':
        analyzar = ''
        for i in get:
            if i not in puncs:
                analyzar += i
        param = {'get':get,'analyzar':analyzar}
        get = analyzar
    
    if upper == 'on':
        analyzar = ''
        for i in get:
            if i not in puncs:
                analyzar += i.upper()    
        param = {'get':get,'analyzar':analyzar}
        get = analyzar
    
    if newlineremover == 'on':
        analyzar = ''
        for i in get:
            if i != '\n' and i != '\r' and i not in puncs:
                analyzar += i
        param = {'get':get,'analyzar':analyzar}
        get =  analyzar
    
    if extraspace == 'on':
        analyzar = ''
        for index,char in enumerate(get):
            if get[index] == ' ' and get[index+1] == ' ' :
                pass
            analyzar += char
        param = {'get':get,'analyzar':analyzar}
        get = analyzar
    if removepunc != 'on' and  upper != 'on' and  newlineremover != 'on' and  extraspace != 'on' :
        return HttpResponse('none')
    return render(request,'analyz.html',param)

def about(request):
    return HttpResponse('about')

def add(request):
    return HttpResponse('add')

def update(request):
    return HttpResponse('update')

def remove(request):
    return HttpResponse('remove')