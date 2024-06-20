import urllib.parse

# Заданный запрос
user_query = 'как стать бэкенд-разработчиком'

# Кодируем запрос для URL
encoded_query = urllib.parse.quote(user_query)

# Собираем полный URL для поиска
url = 'https://yandex.ru/search/?text=' + encoded_query

# Выводим URL
print(url)
