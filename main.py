
def register2(request):
    return render(request,
        'register.html',
        {}
    )

def do_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/')
    else:
        return HttpResponse('Ты не залогинен')

def index2(request):
    return render(request,
        'index2.html',
        {}
    )


def do_logout2(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/')
    else:
        return HttpResponse('Ты не залогинен')

def index22(request):
    return render(request,
        'index2.html',
        {}
    )