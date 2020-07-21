import csv
import datetime
with open('img_pixels.csv') as csv_file:
    lis = [line.split() for line in csv_file]
uss_dat = [l[0].split(",") for l in lis]
#print(uss_dat)


#rawdat = []
#for li in range(len(uss_dat)):
#    rawdat.append(li+1)
#print(rawdat)
res = []
for i in range(len(uss_dat)):
    if i==0:
        for j in range(32):
            res.append(uss_dat[i])
    elif i==1:
        for j in range(9):
            res.append(uss_dat[i])
    elif i==3:
        for j in range(12):
            res.append(uss_dat[i])
    elif i==6:
        for j in range(27):
            res.append(uss_dat[i])
    elif i==7:
        for j in range(3):
            res.append(uss_dat[i])
    else:
        res.append(uss_dat[i])
#print(res)
with open('result.csv', 'w', newline='') as fires:
    writer = csv.writer(fires)
    writer.writerows(res)