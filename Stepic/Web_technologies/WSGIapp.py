# Пример WSGI - обработчика


def wsgi_application(environ, start_responce):
    """
    :param environ: Первый аргумент (!)
    Словарь (dict) со всеми переменными окружения
    :param start_responce:
    :return:
    """
    # бизнес логика/ вызов кода приложения
    status = '200 OK'  # Статус ответа
    headers = [
        ('Content-type', 'text/plan')
    ]  # Набор заголовков ответа
    body = 'Hello, world!'  # Тело ответа
    start_responce(status, headers)  # передача статуса и заголовков
    return [body]