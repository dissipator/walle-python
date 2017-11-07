# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response


def search_form(response):
	return render_to_response("search_form.html")

def search(request):
	request.encoding='utf-8'
	if 'q' in request.GET:
		message = u"你搜索的内容为：" + request.GET['q']
	else:
		message = u'你提交了空表单！'
	return HttpResponse(message)

def search_post(request):
	request.encoding='utf-8'
	ctx = {}
	# ctx['csrf_token'] = 'asdadasdasdasdasdasdasd'
	if 'q' in request.POST:
		ctx['rlt']  = u"你搜索的内容为：" + request.POST['q']
	else:
		ctx['rlt']  = u'你提交了空表单！'
	return render(request,"search_form.html",ctx)