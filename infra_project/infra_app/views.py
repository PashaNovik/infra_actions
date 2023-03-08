from django.http import HttpResponse


def index(request):
    return HttpResponse('У меня получилось! или нет? еще раз? и еще раз ;)')


def second_page(request):
    return HttpResponse('А это вторая страница!')
