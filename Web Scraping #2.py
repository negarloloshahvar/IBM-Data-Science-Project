from bs4 import BeautifulSoup

html = "<table><tr><td>Pizza Places</td><td>Orders</td>" \
       "<td>Slices</td></tr><tr><td>Domino Pizza</td><td>10</td>" \
       "<td>100</td></tr><tr><td>Little Ceasars</td><td>12</td>" \
       "<td>144</td></tr></table>"

table = BeautifulSoup(html, 'html5lib')
table_row = table.find_all(name='tr')
first_row = table_row[0]

for i,row in enumerate(table_row):
    print('row', i)
    cells = row.find_all('td')
    for j,cell in enumerate(cells):
        print('column', j, 'cell', cell)