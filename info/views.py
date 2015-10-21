from django.shortcuts import render
from info.forms import DetailForm


def home(request):
    args = {}

    if request.method == 'POST':
        pass
    else:
        form = DetailForm()

    args['form'] = form
    return render(request, 'info/home.html', args)
