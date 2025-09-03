from django.shortcuts import render

from django.shortcuts import redirect

def compiler(request):
    return render(request,"subject/compiler.html",{})


def automata(request):
    return render(request,"subject/automata.html",{})

def discrete(request):
    return render(request,"subject/discrete.html",{})

def microprocessor(request):
    return render(request,'subject/microprocessor.html',{})

def internet(request):
    return render(request,'subject/internet.html',{})

def fundamentals(request):
    return render(request,'subject/fundamentals.html',{})

def softwaretest(request):
    return render(request,'subject/softwaretest.html',{})

def subject_page_redirect(request):
    # گرفتن درس انتخاب شده از فرم
    subject_name = request.GET.get('subject_name')

def speciallanguage(request):
    return render(request,'subject/speciallanguage.html',{})



def subject_page_redirect(request):
    # گرفتن درس انتخاب شده از فرم
    subject_name = request.GET.get('subject_name')
    if subject_name:
        # اگر نام view با نام درس یکی است، مستقیم redirect کن
        return redirect(subject_name)
    else:
        # اگر چیزی انتخاب نشده بود، برگرد به صفحه login
        return redirect('login')