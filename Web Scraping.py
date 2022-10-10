# We are asked to find the name and salary of players in a National Basketball League, from the following webpage.

from bs4 import BeautifulSoup

html = "<!DOCTYPE html><html><head><title> Page Title</title></head><body>" \
       "<h3><b id= 'boldest'> Lebron James</b></h3><p>Salary: $ 92,000,000 </p>" \
       "<h3>Stephen Curry</h3><p>Salary: $ 85,000,000</p>" \
       "<h3>Kevin Durant</h3><p>Salary: 73,200,000</p></body>"

soup = BeautifulSoup(html, 'html5lib')
# soup.index()

tag_object = soup.h3
tag_child = soup.h3
print(tag_object.string)

