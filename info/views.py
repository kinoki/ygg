from django.contrib import messages
from django.shortcuts import render
from info.forms import DetailForm


def home(request):
    args = {}

    if request.method == 'POST':
        form = DetailForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Data successfully saved.")

    else:
        form = DetailForm()

    args['form'] = form
    return render(request, 'info/home.html', args)
