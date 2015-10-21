from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import redirect, _get_queryset


def reverse_redirect(url, args=[]):
    try:
        rev = reverse(url, args=args)
    except Exception, e:
        return HttpResponse('Unable to redirect: {0}'.format(e))
    else:
        return redirect(rev)


def get_object_or_None(klass, *args, **kwargs):
    queryset = _get_queryset(klass)
    try:
        return queryset.get(*args, **kwargs)
    except queryset.model.DoesNotExist, queryset.model.MultipleObjectsReturned:
        return None
