import csv

with open("/Users/i346327/pythonds/pythonds/03-FileHandling/file1.csv") as f:
    csv_reader = csv.reader(f)
    for line in csv_reader:
        print(line)

data = ["Cena","Fedility","Bangalore"]
with open("/Users/i346327/pythonds/pythonds/03-FileHandling/file1.csv", "a", newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(data)