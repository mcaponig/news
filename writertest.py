import csv

csvfile = open('pipe_out.csv')
reader = csv.DictReader(csvfile)
for row in reader:
	a = row['title']

print a
