from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.authtoken.models import Token
from core.shortcuts import reverse_redirect, get_object_or_None

from info.forms import DetailForm
from info.models import Detail
from info.serializers import DetailSerializer

from rest_framework import authentication
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.renderers import JSONRenderer


@login_required(login_url='/account/login/')
def home(request):
    args = {}

    if request.user:
        user = request.user
        token = Token.objects.get_or_create(user=user)
        print token[0]

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


@api_view(['GET'])
@authentication_classes([authentication.TokenAuthentication])
def detail_list(request, format=None):
    details = Detail.objects.all()
    print request.user
    serializer = DetailSerializer(details, many=True)
    return JSONResponse(serializer.data)
