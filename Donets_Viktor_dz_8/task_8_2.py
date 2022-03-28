# * (вместо 1) Написать регулярное выражение для парсинга файла логов
# web-сервера из ДЗ 6 урока nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/
# nginx_logs/nginx_logs) для получения информации вида:
# (<remote_addr>, <request_datetime>,
# <request_type>, <requested_resource>,
# <response_code>, <response_size>), например:
#
# raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/
# product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"'
# parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET',
# '/downloads/product_2', '304', '0')

# Примечание: вы ограничились одной строкой или проверили на всех записях
# лога в файле? Были ли особенные строки? Можно ли для них уточнить регулярное
# выражение?

import re

list_tuple = []
with open('nginx_logs.txt') as file:
    for raw in file:
        remote_addr = re.findall(r"^\S+", raw)[0]
        request_datetime = re.findall(r"\[(\S+ \D\d{4})", raw)[0]
        request_type = re.findall(r"\"(\S+) /", raw)[0]
        requested_resource = re.findall(r"\ /(\S+) ", raw)[0]
        response_code = re.findall(r"\" (\d{3})", raw)[0]
        response_size = re.findall(r"\ (\d+) \"", raw)[0]
        list_tuple.append((remote_addr, request_datetime, request_type,
                           requested_resource, response_code, response_size))

print(list_tuple)

# Второй вариант
# pars = re.compile(r"(^\S+) - - \[(\S+ \D\d{4})] \"(\S+) (\S+) \S+ (\d+) (\d+)")
# list_tuple = []
# with open('nginx_logs.txt') as file:
#     for raw in file:
#         for info in pars.findall(raw):
#             r_addr, r_datetime, r_type, r_resource, r_code, r_size = info
#             list_tuple.append((r_addr, r_datetime, r_type, r_resource,
#                                r_code, r_size))
# print(list_tuple)
