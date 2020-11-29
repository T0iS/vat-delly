import glob
import os
import csv


folder_path = os.getcwd()
#folder_path = 'G:\Můj disk\URC-FILES\AAA SAT DVD'
count= dict()
for root, dirs, files in os.walk(folder_path):
    for filename in files:
    
        if "SAT-TV" in filename:
            with open(os.path.join(root,filename), 'r') as f:
                text = f.readlines()
                buttons = []
                for line in text[6:]:
                    if ',' in line:
                        line = line.split(',')
                        buttons.append(line[0])
                        if int(line[0]) == 155:
                            print(filename)

                for b in buttons:
                    count[b] = count.get(b,0) + 1
                #print (filename)
                #print (len(text))
                
count = sorted(count.items(), key = lambda kv:(kv[1], kv[0]), reverse=True)


with open('dict.csv', 'w+') as csv_file:  
    writer = csv.writer(csv_file, delimiter =';')
    writer.writerow(['key', 'count'])
    for row in count:
       writer.writerow(row)
#print(count)