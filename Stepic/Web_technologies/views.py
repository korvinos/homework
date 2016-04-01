# Базовый view

from django.http import Http404
from django.shortcuts import render

# Вот так слишком длинно
def post_details(request, slug):
	try:
		post = Post.odjects.get(slug=slug)
	except Post.DoesNotExist: # Если нет поста
		raise Http404 
	return render(request, 'blog/post_detail.html', {
		'post':post,
		})

# Можно использовать shortcut
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET


@require_GET # Деоратор который запретит метод POST
def post_details(request, slug):
	post = get_object_or_404(Post, slug=slug) # 1. Модель 2. Условие выборки
	return render(request, 'blog/post_detail.html', {
		'post':post,
		})	

# Отображение связанных сущностей

def post_details(request, slug):
	post = get_object_or_404(Post, slug=slug) # 1. Модель 2. Условие выборки
	try:
		vote = post.votes.filter(user=request.user)[0] # Фильтер голосов по одному пользователю
	except Vote.DoesNotExist:
		vote = None
	# Отображение от одной модели лучше делать в шаблонизаторе
	return render(request, 'blog/post_detail.html', {
		'post' : post,
		'category' : post.category,
		'tags': post.tags.all()[:],
		'vote' : vote,
		})

# Постраничкое отображение
from django.core.paginator import Paginator


def post_list_all(request):
	posts = Post.odjects.filter(is_published=True) # Создаем выбору постов QuerySet
	limit = request.GET.get('limit', 10) # Сколько отображать постов
	page = request.GET.get('page', 1) # Какую страницу смотрим
	paginator = Paginator(posts, limit) # Объект рассчитывающий параметры для отображения
	paginator.baseurl = '/blog/all_posts/?page=' # К этому параметру приклеивается номер страницы
	page = paginator.page(page)
	return render(request, 'blog/post_by_tag.html', { # Передаем все в траницу
			posts: page.odject_list, # Список постов относяжихся к странице
			paginator: paginator, page:page, 
		})

# Пагинатор в шаблоне Bootstrap
<nav><ul class="paginator">
{% for p in paginator.page_range %} # page_range - список всех страниц 
									# которые будут отображаться рядом с текущей
	{% if p.number == page.number %} # Если номер совпадает с текущей
	<li class="active"> # Отображаем её как active
	{% else %}	
	<li>
	{% endif %}
		<a href="{{ paginator.baseurl }}{{ p.number }}">
		{{ p.number }}	</a>
	</li>
{% endfor %}
</ul></nav>

# Пагинатор для любог листинга
def paginate(request, qs):
	try:
		limit = int(request.GET.get('limit', 10))
	except ValueError:
		limit = 10
	if limit > 100
		limit = 10
	try:
		page = int(request.GET.get('page', 1))
	except ValueError:
		raise Http404
	paginator = Paginator(qs, limit)
	try:
		page = paginator.page(page)
	except EmptyPage:
		page = paginator.page(paginator.num_pages)
	return page


# форма
# И отображение формы и отправка 
def post_add(request):
	# проверка метода запроса 
	if request.method == 'POST':
		form = AddPostForm(request.POST)
		if form.is_valid(): # очистка и валидация формы
			post = form.save() # сохраняет в базу
			url = post.get_url() # получаем url страницы
			return HttpResponceRedirect(url)
	else:
		# Создаем новый экземпляр формы не привязанной к данным
		form = AddPostForm()
	return render(request, 'blog/post_add.html', {
		'form': form
		})
