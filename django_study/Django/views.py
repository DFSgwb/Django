from Django.http import HttpResponse
def page_2003(request):
    html="<h1>这是第一个页面</h1>"
    return HttpResponse(html)

def index_view(request):
    html='这是我的首页'
    return  HttpResponse(html)

def pagen_view(request,pg):
    html='这是编号为%s的网页'%(pg)
    return HttpResponse(html)

def cal_view(request,n,op,m):
    if op not  in ['add','sub','mul']:
        return HttpResponse('You op is Error!')
    result=0
    if op=='add':
        result= m+n
    if op=='sub':
        result= n-m
    if op=='mul':
        result= n*m
    return HttpResponse('结果为：%s'%(result))

def cal_view2(request,x,op,y):
    html = 'x:%s op:%s y:%s'%(x,op,y)
    return HttpResponse(html)

def brithday_view(requset,y,m,d):
    html='生日为%s年%s月%s日'%(y,m,d)
    return HttpResponse(html)


def test_request(request):
    print('path_info is:',request.path_info)
    print('method is',request.method)
    return HttpResponse('test request ok')