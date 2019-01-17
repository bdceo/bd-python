import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

first_text = texts[0]
print('type(first_text)=', type(first_text))
print(first_text)
print('"First record of texts, <{}> texts <{}> at time <{}>"'.format(*first_text))
