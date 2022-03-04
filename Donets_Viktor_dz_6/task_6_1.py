#  Не используя библиотеки для парсинга, распарсить (получить определённые
#  данные) файл логов web-сервера nginx_logs.txt (https://github.com/elastic
#   /examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) —
#  получить список кортежей вида:
#  (<remote_addr>, <request_type>, <requested_resource>). Например:
# [
# ...
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('173.255.199.22', 'GET', '/downloads/product_2'),
# ...
# ]
# Примечание: код должен работать даже с файлами, размер которых превышает
#  объем ОЗУ компьютера.

list_tuple = []
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    line = f.readline().strip()
    while line:
        remote_addr = line[:line.find(' -')]
        request_type = line[line.find('"') + 1:line.find(' /')]
        requested_resource = line[line.find(' /'):line.find('HTTP')].strip()
        list_tuple.append((remote_addr, request_type, requested_resource))
        line = f.readline().strip()
print(list_tuple)
