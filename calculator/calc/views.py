from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"home.html")


def eval(request):
    n1 = request.POST.get("num1")
    n2 = request.POST.get("num2")
    s = request.POST.get("sym")

    
    if s == '+':
        result = int(n1)+int(n2)
    elif s == "*":
        result = int(n1)*int(n2)
    elif s == "/":
        result = int(n1)/int(n2)
    elif s == "-":
        result = int(n1)-int(n2)
    else:
        result= None
    

    return render(request,"home.html",{'result':result})