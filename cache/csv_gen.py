import csv
import datetime
import os
while True:
    try:
        filename = input("Input your original csv file:")
        with open('{}.csv'.format(filename)) as csv_file:
            lis = [line.split() for line in csv_file]
    except:
        print("Try again! /File not found!!!")
        pass
    else:
        break
print("In process 1/4...")
print("In process 2/4...")
pre_dat = [l[0].split(",") for l in lis]
print("In process 3/4...")
use_dat = []
print("In process 4/4...")
for l in pre_dat:
    pre_line = []
    for n in range(len(l)-1):
        pre_line.append(int(l[n]))
    pre_line.append(l[len(l)-1])
    use_dat.append(pre_line)
#print(use_dat)
print("Collect CSV Data complete!!")
print("Now type number that you want to clone that line")

clonetimedat = []
for t in range(len(use_dat)):
    ct = int(input(f"c{t+1}"))
    clonetimedat.append(ct)

print(clonetimedat)

res = []
for n in range(len(use_dat)):
    if clonetimedat[n] != 0:
        for t in range(clonetimedat[n]):
            res.append(use_dat[n])

print("save result as")
resname = input("Name is :")

os.chdir("result")
with open('{}.csv'.format(resname), 'w', newline='') as fires:
    writer = csv.writer(fires)
    writer.writerows(res)