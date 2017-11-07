# -*- coding: utf-8 -*-

from django.http import HttpResponse

from TestModel.models import Test
 
# 数据库操作
def testdb(request):
	#初始化
	response = ""
	response1 = ""

	# data = ['runoob','luoml','dissipator','judy','hyy','lucas']
	# for test1 in data:
	# 	test1 = Test(name=test1)
	# 	test1.save()

	list = Test.objects.all()
	# response2 = Test.objects.filter(id=1)
	# response3 = Test.objects.get(id=1)
	Test.objects.order_by('name')[0:2]

	# Test.objects.order_by('id')
	# Test.objects.filter(name='runoob').order_by('id')

	for var in list:
		response1 += "<li>" + var.name + "</li>"
		# list.delete()
	
	# 另外一种方式
	# Test.objects.filter(id=1).delete()
	# Test.objects.all().delete()
	response = response1
	return HttpResponse(response)



