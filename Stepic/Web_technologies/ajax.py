def comments_list(request):
	post_id = request.GET.get('post_id')
	post = get_object_or_404(Post, post_id)
	comments = paginate(request, post.comments)
	return render(request, 'blog/comments.html', {
		'comments': comments
	})


# HttpResponceAjax
import json

# класс для успешных ответов 
class HttpResponseAjax(HttpResponse):
	def __init__(self, status='ok', **kwargs): 
		kwargs['status'] = status  # Добавляем статус 
		super(HttpResponseAjax, self).__init__( 
			content = json.dumps(kwargs),
			content_type = 'application/json',
		)

# класс для ошибок
class HttpResponseAjaxError(HttpResponseAjax): # наследуем от первого 
	def __init__(self, code, message):
		super(HttpResponseAjaxError, self).__init__(
			status = 'error', code = code, message = message
		)

# использоване HttpResponseAjax
@login_required_ajax # 	Для вьюшки пользователь должен быть авторизован
def comment_add(request):
	form = AddCommentForm(request.POST)
	if form.is_valid():
		comment = form.save()
		return HttpResponseAjax(comment_id=comment.id)
	else:
		return HttpResponseAjaxError(
			code = "bad_params",
			message = form.errors.as_text(), # Не очень хорошо
		)	