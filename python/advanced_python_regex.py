import pandas as pd
from pandas import Series
#Q1
faculty = pd.read_csv('faculty.csv')
columns = Series(faculty.columns)
columns = columns.apply(lambda a: a.lstrip(' ').rstrip(' '))
faculty.columns = columns
degree = faculty['degree']
degree = degree.apply(lambda a: a.rstrip(' ').lstrip(' ').replace('.', ''))
degree = degree.drop(degree.index[degree == '0'])
degree.index = range(len(degree))
degree_full = []
for i in range(len(degree)):
    degree_full += degree[i].split(' ')
degree_full = Series(degree_full)
print (degree_full.value_counts())

#Q2
titles = Series(faculty['title'])
titles = titles.apply(lambda a: a.rstrip(' of Biostatistics'))
print(titles.value_counts())

#Q3
emails = faculty['email']
print(list(emails))

#Q4
import re
emails_domain = emails.apply(lambda a: a.replace(re.search("[\w.]+@", a).group(), ''))
print(emails_domain.unique())

#Alternative
emails_domain = emails.apply(lambda a: a[(a.find('@') + 1):])
