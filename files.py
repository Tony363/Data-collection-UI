import csv

for filename in os.listdir(INPUT_DIR):
   with open(os.path.join(INPUT_DIR,filename), dialect='excel-tab') as infile:
      reader = csv.reader(infile)
      for row in reader:
          print row
          
with open(..., 'w', newline='') as myfile:
   wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
   wr.writerow(mylist)
  
yourList = []

with open('yourNewFileName.csv', 'w', ) as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    for word in yourList:
        wr.writerow([word])