from django.http import HttpResponse, Http404
from django.shortcuts import render


def index(request):
    return render(request, 'singlepage/index.html')


texts = ['Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer sed velit a velit ornare condimentum non luctus arcu.',
         'Sed porta risus vel nisl tincidunt fermentum. Vestibulum facilisis vitae ligula in sodales.',
         'Donec vulputate fringilla risus, tristique eleifend massa consectetur aliquam. Cras euismod mollis elit, at auctor justo.',]


def section(request, num):
    if 1 <= num <= 3:
        return HttpResponse(texts[num - 1])
    else:
        raise Http404("No such section")

