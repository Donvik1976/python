import sys


def show_sales(hence=1):
    for string, reader in enumerate(open('bakery.csv', 'r+', encoding='utf-8'),
                                    start=1):
        if hence <= string:
            print(reader.strip())


def show_sales_1(hence, to):
    for string, reader in enumerate(open('bakery.csv', 'r+', encoding='utf-8'),
                                    start=1):
        if hence <= string <= to:
            print(reader.strip())


x = sys.argv
if len(x) == 1:
    show_sales(1)
elif len(x) == 3:
    show_sales_1(int(x[1]), int(x[2]))
elif len(x) == 2:
    show_sales(int(x[1]))
else:
    exit()
