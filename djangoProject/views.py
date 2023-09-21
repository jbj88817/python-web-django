from django.http import HttpResponse


def page_500(request):
    """ 500页面 """
    return HttpResponse('服务器内部错误', status=500)
