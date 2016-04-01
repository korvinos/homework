var xhr = new XMLHttpRequest();  //Создаем объект (разный для браузеров)
xhr.open('POST', '/xhr/test.html', true); //опен указывает с каким методом и по какому урлу запрос
// true - значит асинхронный
xhr.onreadystatechange = function() { //Создаем функцию callback 
	if (xhr.readyState == 4) {
		if (xhr.status == 200) {
		alert(xhr.responseText);
		}
	}
};
xhr.send("a=5&b=4"); //Тело запроса

// Использование Ajax при ромоще jQuerry

$.ajax({ $ // вывод метода ajax с параметрами
	url: '/blog/comments/add/', // урл
	type: 'POST', // метод
	data: { post_id: 12, text: 'Занятная идея!' }, // данные
// задаем функции обработчки
}).success(function(data) { // если успешно и вернулся 200
	// получаем объект data (в данном случае продпологаем что это json)
	if (data.status == 'ok') {
		console.log(data.comment_id);	
	}
}).error(function() { // если вернулись 4хх или 5хх
	console.log('http error')
});

