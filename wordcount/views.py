from django.shortcuts import render

def home(request):
    return render(request,'home.html')
def count(request):
    var1=request.GET['textfield']
    var2=var1.split()
    var3={}
    for i in var2:
        if i in var3:
            var3[i]+=1
        else:
            var3[i]=1

    return render(request,'count.html',{'var1':var1,'var2':len(var2),'var3':var3.items()})
def about(request):
    return render(request,'about.html')
