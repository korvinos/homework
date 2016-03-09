from django.db import models
from django.core.urlresolvers import reverse


# Создаем новый класс наследуемый от models.Model
class Post(models.Model):
	title = models.CharField(max_length=255)
	content = models.TextField()
	creation_date = models.DateTimeField(blank=True)	
	# поле слага для метода get url
	slug = models.SlugField(unyque=True)

	# Связи
	# 1 способ - Многие к одному. Указываем модель на которую ссылаемся 
	# on_delet = что делать с постом при удалении категории
	category = models.ForeignKey(Category, null=True, 
		on_delete=models.SET_NULL)

	# 2 способ - Один к Одному
	status = models.OneToOneField(PostStatus)
	
	# 3 способ - Многие ко многим. Например, тэги и посты
	tags = models.ManyToManyField(Tag)

	# методы модели. Применяются к одной строчке / экземпляру
	# Вызывается когда объект пытаются преобразовать в строку
	def __unicode__(self): 
		return self.title 

	# Не обязательный метод. Позволяет построить путь к объекту
	def get_absolute_url(self):
		return '/post/%d/' % self.pk

	def get_url(self):
		return reverse('blog:post-details',
			kwags={'slug':self.slug})
	
	# Опции модели
	class Meta:	
		db_table = 'blogposts' # Записать модель в данную таблицу. По умолчанию пишет в blog_post
		ordering = ['-creation_date'] # Сортировка по умолчанию


# Использование отношений в коде 

post = Post.objects.get(pk=1)
category = post.category # Category
category_id = post.category_id # Int

status = post.status # Category
status_id = post.status_id # Int

tags_manager = post.tags_manager # RelatetManager
post.tags.all() # [Tags]

category.post_set.all()  # [Post]
tag.post_set.all() # [Post]


# Начало другого урока

from blog.models import Category, Post

# Создание 
c = Category(title='Perl')
c.save()
# За один вызов 
c = Category.objects.create(title='Python')
# create - создать экземпляр модели
# Изменение
c.title = 'About Python'
c.save()

# Создание объектов со связями

t = Tag(title='easy')
t.save()
c = Category(title='Python')
c.save()
p = Post(title='...', ... , category=c или category_id=3)
p.save()

# Многие ко многим
p.tags = Tag.objects.all()[0:3] # [ Tag ]
p.save()
p.tags.add(t)
p.save()

# Загрузка объекта из базы
# по ключу
try:
	post = Post.objects.get(pk=3)
except Post.DoesNotExist:
	post = None

# По другому полю
try:
	post = Post.objects.get(name='Python')
except MultopliObjectsReturned: # Если по Python много объектов
	post = None

# Выборка нескольких объектов из базы
all_posts = Post.objects.all() # выбрать все. Получаем QuerySet
first_three = Post.objects.all()[:3]

c = Category.objects.get(id=3)
python_post = Post.objects.filter(category=c)

css_post = Post.objects.filter(tittle___contains='css') # По наличию в заголовке css
# через ___ разные операторы фильтрации
css = css_post.order_by('-rating')
css_post = css_post[10:20]


# Chaining - Цепочки вызова 

posts = Post.objects 					  # ModelManager
posts = posts.filter(tittle__match='CSS') # QuerySet / Если вызвать еще фильтер, то они сложаться (И)
posts = posts.exclude(category_id=7) 	  # QuerySet
posts = posts.order_by('rating') 		  # QuerySet
posts = reverse() 						  # QuerySet
posts = posts[0:10] 					  # [ Post ] / Индексирование / Слайс


# Свой ModelManager

class PostManager(models.Manager):
	def best_posts(self):
		return self.filter(rating__gt=50)
	def published(self):
		return self.filter(published=True)
	def create_draft(self, **kwags)
		kwags['draft'] = True
		return self.create(**kwags)

class Post(models.Model):
	title = models.CharField()
	objects = PostManager(	)