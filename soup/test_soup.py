from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc)
# 格式化输出
# print(soup.prettify())

# 去除所有标签后的网页文本
# print('soup.get_text()', soup.get_text())

# head
print('soup.head=', soup.head)
for child in soup.head.descendants:
    print('\tsoup.head.descendants.child=', child)
print()

# title
print('type(soup.title)=', type(soup.title))
print('soup.title=', soup.title)
print('soup.title.name=', soup.title.name)
print('soup.title.string=', soup.title.string)
print('soup.title.parent.name=', soup.title.parent.name)
print()

# p
print('soup.p=', soup.p)
print('soup.p[\'class\']=', soup.p['class'])
print('soup.p.contents=', soup.p.contents)
for child in soup.p.children:
    print('\tp.children=',child)
print()

# a
print('type(soup.a)=', type(soup.a))
print('soup.a=', soup.a)
print('soup.a.attrs=', soup.a.attrs)

# 获取相邻元素
first_p = soup.p
print('tag.next_sibling=', first_p.next_sibling)
print('tag.previous_sibling=', first_p.previous_sibling)
for next in first_p.next_siblings:
    print('\ttag.previous_siblings=', next)
print('tag.next_element=', first_p.next_element)
print('tag.previous_element=', first_p.previous_element)
for next in first_p.next_elements:
    print('\ttag.next_elements=', next)

# 搜索
id_a = soup.find(id='link2')
print('soup.find(id=\'link2\')', id_a)

all_a = soup.find_all('a')
print('type(soup.find_all(\'a\'))=', type(soup.find_all('a')))
print('soup.find_all(\'a\')=', all_a)
for aa in all_a:
    print('\ta.href=', aa.get('href'))













