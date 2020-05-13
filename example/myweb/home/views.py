from django.shortcuts import render
 
def index(request):
    msg = 'My Message'
    return render(request, 'index.html', {'message': msg})