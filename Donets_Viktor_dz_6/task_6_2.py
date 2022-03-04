# * (вместо 1) Найти IP адрес спамера и количество отправленных им запросов по
# данным файла логов из предыдущего задания. Примечания: спамер — это клиент,
# отправивший больше всех запросов; код должен работать даже с файлами, размер
# которых превышает объем ОЗУ компьютера.

list_tuple = []
spammer = dict()
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    line = f.readline().strip()
    while line:
        remote_addr = line[:line.find(' -')]
        request_type = line[line.find('"') + 1:line.find(' /')]
        requested_resource = line[line.find(' /'):line.find('HTTP')].strip()
        list_tuple.append((remote_addr, request_type, requested_resource))
        if remote_addr not in spammer:
            spammer[remote_addr] = 1
        else:
            spammer[remote_addr] += 1

        line = f.readline().strip()


for key, value in spammer.items():
    if value == max(spammer.values()):
        print(f'Спамер с IP: {key} и количество '
              f'отправленных им запросов {value}')
