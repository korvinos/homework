# Перенаправление в Django
from django.http import HttpResponseRedirect


def some_view(request):
	# логика
	return HttpResponseRedirect('/new_url/') # url попадет в location

# уязвимость open redirect
def dagerous_view(request):
	url = request.GET.get('continue') # в параметре continue url на который пойдер редирект
	# могут направлять на свою страницу через ваш сайт
	# нужно проверять урл	
	return HttpResponseRedirect(url)


# Описание форм
# qa/forms.py
from django import forms


class FeedbackForm(forms.Form):
	# перечисляем поля из модуля forms
	email = forms.EmailField(max_length=100)
	message = forms.CharField(widget=forms.Textarea) # widget - внешний вид поля на html странице
	
	# Метод логики общей валидации форм
	def clean():
		if is_spam(self.clean_data):
			raise forms.ValidationError( # исключение - форма не валидни и сохранять нельзя
				u'Сообщение похожее на спам',
				code='spam'
				)

# форма добавления поста
class AddPostForm(forms.Form):
	tittle = forms.CharField(max_length=100)
	message = forms.CharField(widget=forms.Textarea)

	# имя соответствует названию поля
	# дополнительная валидация одного конкретного поля
	def clean_message(self):
		message = self.cleaned_data['message'] # обращаемся к claned_data свойство формы
		# поля прошедшие очистку CharField
		if not is_ethic(message): 
			raise forms.ValidationError(
				u'Сообщение не корректно', code=12)
			return message + \
			"\nThank ypu for your attention"

	# kлогика сохранения данных
	def save(self):
		post = Post(**self.cleaned_data)
		post.save()
		return post

	# Проверка пользователя
	# поля ...

	def __init__(self, user, **kwargs): # Добавляем обязательный аргумент user
		self._user = user # Сохраняем его в отдельную переменную
		super(AddPostForm, self).__init__(**kwargs) # Вызов конструктор суперкласса
	# Теперь нам доступен текущий пользователь
	def clean(self):  
		if self._user.is_banned:
			raise ValidationError(u'Доступ ограничен')
	
	def save():
		self.cleaned_data['author'] = self._user
		return Post.object.create(**self.cleaned_data)

# вьюха
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

# шаблон
# по умолчанию
