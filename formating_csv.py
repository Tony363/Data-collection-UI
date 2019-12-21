import csv
import os
import sys
import traceback
import psutil

new_format = []

INPUT_DIR = r"C:\Users\Tony\Desktop\stock market data\new york"

# def iterate_rows(infile,new_format):
  
#     try:
#         head = [int(next(infile))]
#         for row in head:
#             # print(row)
#             new_format.append(row)
#         # print(new_format)
#     except MemoryError:

#         raise StopIteration()
    

     
for filename in os.listdir(INPUT_DIR):

    with open(os.path.join(INPUT_DIR,filename), 'r+',encoding='utf-8-sig') as infile:
      
        try:
            while True:
                try:
                    head = [int(next(infile))]
                    for row in head:
                        # if row == 'ï»¿1\n':
                        #     row = 1
                        # print(row)
                        new_format.append(row)
                
                except MemoryError:

                    raise StopIteration()
    
        except StopIteration:
            continue
                
                

print(new_format)


with open('Formated.csv', 'w', newline='') as myfile:
     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     for row in new_format:
        wr.writerow([row])