from django.http import HttpResponse


# Create your views here.

def hello_world(request):
    return HttpResponse("Hello World!")


def hello_china(request):
    return HttpResponse("Hello China!")


def hello_html(request):
    """ 响应HTML内容 """
    html = """
    <html>
        <body>
            <h1 style="color:#f00">hello html</h1>
        </body>
    </html>
    """
    return HttpResponse(html)


def article_list(request, month):
    """
    :param month: 今年某一个月的文章列表
    """
    return HttpResponse('article: {}'.format(month))


def search(request):
    """ GET参数的获取 """
    name = request.GET.get('name', '')
    print(name)
    return HttpResponse('查询成功')
