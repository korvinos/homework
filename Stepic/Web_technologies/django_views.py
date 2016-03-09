# /blog/post_text/?id=123
# По такому урлу(id) отдаем текст такого поста

def post_text(request):
	try:
		id = request.GET.get('id') # GET содержит все параметры (в данном случае нам вернет 123) по названию
		obj = Post.objects.get(pk=id) # Вызов модели (обращение к базе данных)
	except Post.DoesNotExist:
		raise Http404
	return HttpResponse(obg.text, content_type='text/plain')