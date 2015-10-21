from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
from core.shortcuts import reverse_redirect, get_object_or_None

from info.forms import DetailForm
from info.models import Detail

from rest_framework.renderers import JSONRenderer
from info.serializers import DetailSerializer


def home(request):
    args = {}

    if request.method == 'POST':
        form = DetailForm(request.POST)
        if form.is_valid():
            detail = form.save()
            messages.success(request, "Data successfully saved.")
            return reverse_redirect('info:view_detail', args=[detail.pk])

    else:
        form = DetailForm()

    args['form'] = form
    return render(request, 'info/home.html', args)


def view_detail(request, detail_id):
    args = {}
    detail = get_object_or_None(Detail, pk=detail_id, is_active=True)

    if detail:
        args["detail"] = detail
        return render(request, 'info/view_detail.html', args)
    else:
        messages.warning(request, "unable to locate detail")
        return reverse_redirect('info:home')


class JSONResponse(HttpResponse):

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


def detail_list(request):

    if request.method == 'GET':
        details = Detail.objects.all()
        print details
        serializer = DetailSerializer(details, many=True)
        print serializer.data
        return JSONResponse(serializer.data)
