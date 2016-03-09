# /blog/post_text/?id=123
# По такому урлу(id) отдаем текст такого поста

def post_text(request):
	try:
		id = request.GET.get('id') # GET содержит все параметры (в данном случае нам вернет 123) по названию
		obj = Post.objects.get(pk=id) # Вызов модели (обращение к базе данных)
	except Post.DoesNotExist:
		raise Http404
	return HttpResponse(obg.text, content_type='text/plain')

#	

order = request.GET['sort'] # опасно!
if order == 'rating':
	queryset = queryset.order_by('rating')
page = request.GET.get('page') or 1
try:
	page = int(page)
except ValueError:
	return HttpResponseBadRequest()


# Получение и установка HTTP заголовков

user_agent = request.META.get('HTTP_USER_AGENT')
user_ip = request.META.get('HTTP_X_REAL_IP')
if user_ip is None:
	user_ip = request.META.get('REMOTE_ADDR')
response = HttpResponse(my_data,
	content_type='application/vnd.ms-excel')
response['Content-Disposition'] = 'attachment; filename="foo.xls"'

# Получение и установка coockie

response = HttpResponse(html)
response.set_cookie('visited', '1') 

is_visited = request.COOKIES.get('visited') # '1'


# декораторы в django 

from django.views.decorators.http import require_POST

@require_POST
def like(request):
	pass


# Вызов шаблонизатора

from django.shortcuts import render, render_to_response

return render_to_response('blog/post_detail.html', {
	'post': post,
	'comments': comments,
	})

return render(, request, 'blog/post_detail.html', { # Лучше
	'post': post,
	'comments': comments,
	})

