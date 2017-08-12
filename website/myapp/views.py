# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response

from django.http import HttpResponse,Http404
from django.template import loader
import time
from myapp.models import*
from django.db.models import F,Q
import datetime

# Create your views here.

def global_setting(request):
    NAME = '顺'
    TEL = '18340612162'
    GEYAN = '人生苦短,我用python'

    return locals()

def fun():
    return "hello"

class A(object):
    a = "calss->a"
    def f(self):
        return "jest a A:fun"


def first(request):
    return HttpResponse("my first app")

def bs(request):
    t = loader.get_template('bs.html')
    html = t.render({})
    return HttpResponse(html)

def test(request):
    return render_to_response('bs.html',{})
    # return render(request,'bs.html',{})

def temp(request):
    t = time.localtime()
    return render(request,"time.html",{'datetime':t})

def ctime(request):
    t = time.ctime()
    return render(request,"time.html",{'ctime':t})

def display_meta(request):
    num = 1
    s = "hello"
    l = [1,2,'c','nihao']
    t = (4,5,'d','tuple')
    d = {'a':'one','b':'two','c':'three'}
    f = fun()
    obj = A()
    return render(request,"meta.html",{'num':num,'s':s,'list':l,'tuple':t,'dict':d,'fun':f,'obj':obj})

def tag(request):
    error = "error"
    l = [1,2,3,4]
    return render(request,'tags.html',{"error":"a",'list':l})

def fil(request):
    num = 1
    s = "HELLO WORLD"
    return render(request,'filter.html',{'num':num,'s':s})

def base(request):
    return render(request,'extend.html',{})
def nav(request):
    return render(request,'nav.html',{})
def load(request):
    return render(request,'static.html',{})

def mydb(request):
    #增1
    # Author.objects.create(first_name = 'Jin',last_name = 'Kies',email = "123@qq.com")
    # #增2
    # obj = Author(first_name = 'Jinx',last_name = 'Eve',email = "014@qq.com")
    # obj.save()
    # #增3
    # dic = {'first_name' : 'Jink','last_name' : 'Kill','email' : "456@qq.com"}
    # obj = Author(**dic)
    # obj.save()

    # Publisher.objects.create(name = "人民",address = "beijing",city = "beijing",state_province = "haidian",country = "China",website = 'http://192.168.1.1')
    # Publisher.objects.create(name = "少年",address = "shanghai",city = "shanghai",state_province = "pudong",country = "China",website = 'http://192.168.0.132')
    # Book.objects.create(title = "Python Book",publication_date = datetime.datetime.now(),publisher_id = 1)
    # Book.objects.create(title = "Html5",publication_date=datetime.datetime.now(),publisher_id = 1)
    # Book.objects.create(title = "Javascript",publication_date=datetime.datetime.now(),publisher_id =1)
    # #删
    # Author.objects.filter(id__gt=3).delete()


    #改1
    # Author.objects.filter(id=3).update(last_name = 'Kill',email = '210@qq.com')
    #
    # #改2
    # obj = Author.objects.get(id = 10)
    # obj.first_name = 'lucy'
    # obj.save()

    # 查
#     a = Author.objects.all()  #每一条记录生成一个对象
#     b = Author.objects.all().values('email')  #取出所有记录的指定字段
#     c = Author.objects.all().values_list('first_name','email')  #取出所有记录的指定字段
#     d = Author.objects.get(id = 1)  #获取某一记录的对象
#     # e = Author.objects.filter(id = 1)#获取某一记录的对象
# #每一个对象的某一个属性都进行一个  加法
#     Author.objects.filter().update(age = F('age') + 1)
# #按条件查找
#     q = Q()
#     # print dir(q)
#     q.connector = 'AND'
#     q.children.append(('id',3))
#     q.children.append(('last_name','kill'))
#
#     f = Author.objects.filter(q)

    return HttpResponse("ok")
def mtm(request):
    book1 = Book.objects.get(id =1)
    s = book1.publisher.name

    pub1 = Publisher.objects.get(id =1)
    book_list = pub1.book_set.all()

    author1 = Author.objects.get(id = 1)
    book1_list = author1.book_set.all()

    author_list = book1.author.all()

    book2_list = Book.myobjects.all().little()

    return HttpResponse(book2_list)
