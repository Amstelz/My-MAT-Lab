from PIL import Image
import numpy as np
import cv2
import matplotlib.pyplot as plt
import argparse
import os
import shutil
import projectMethod as pm
import sys
import csv


def createFileList(myDir, format='.png'):
    fileList = []
    print(myDir)
    for root, dirs, files in os.walk(myDir, topdown=False):
        for name in files:
            if name.endswith(format):
                fullName = os.path.join(root, name)
                fileList.append(fullName)
    return fileList

def main():
    kbdinput = 'x'
    cntimagetillnow = 0
    while kbdinput != 'end':
        print("type your test image name:")
        kbdinput = str(input())
        if kbdinput == 'end':
            break
        inputImg = cv2.imread("Docs/{}".format(kbdinput))
        binimg = pm.preprocess(inputImg)

        dest = 'trainingImgs'
        pm.horizontal_cut(binimg,dest)
        cntimagetillnow = pm.vertical_cutTraining(dest,cntimagetillnow)
        print('{}'.format(cntimagetillnow),' images now loaded.')
    tmp = [] 
    with open('CsvData/TrainBook.csv', mode='r', encoding='utf-8-sig') as outfile:
        reader = csv.reader(outfile)
        for rows in reader:
            tmp.append([rows[0]])
    #print(tmp)
    with open('CsvData/DictBook.csv', mode='r', encoding='utf-8-sig') as infile:
        reader = csv.reader(infile)
        for rows in reader:
            for rows2 in tmp:
                if rows2[0] == rows[0]:
                    rows2.append(rows[1])
    listname = []
    #print(tmp)
    for data in tmp:
        listname.append(data[1])
    #print(listname)
    myFileList = createFileList('trainingImgs/verticalcutoutput')
    res = []
    index = 0 
    for file in myFileList:
        print(file)
        img_file = Image.open(file)
        # img_file.show()

        # get original image parameters...
        width, height = img_file.size
        format = img_file.format
        mode = img_file.mode

        # Make image Greyscale
        img_grey = img_file.convert('L')
        #img_grey.save('result.png')
        #img_grey.show()

        # Save values
        value = np.asarray(img_grey.getdata(), dtype=np.int).reshape((img_grey.size[1], img_grey.size[0]))
        #value = np.select([value <= 127, value>127], [np.zeros_like(value), np.ones_like(value)])
        value = np.where(value > 127 , 1, 0)
        #name = (file.replace('Result\Thai '+ font + '\\', '', 1))
        #name = (file.replace('.png', '', 1))
        name = listname[index]
        value = value.flatten()
        last = np.array([name])
        value = np.concatenate((value, last))
        res.append(value)
        print(value)
        index +=1
    with open("CsvData/traindata.csv", 'w' , newline='') as f:
        writer = csv.writer(f)
        writer.writerows(res)


if __name__ == "__main__":
    main()


