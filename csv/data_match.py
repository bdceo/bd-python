import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

first_text = texts[0]
print('"First record of texts, <{}> texts <{}> at time <{}>"'.format(*first_text))
