import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join
import random

id_val = random.sample(range(1,20001),5000)
tfc_val = open('tfc_val.txt', 'w')
val = open('val_num.txt','w')
for image_id in id_val:
    tfc_val.write('/data3/wangyuhu/traffic_data/images/IMG_'+str(image_id).zfill(5)+'.jpg\n')
    val.write(str(image_id).zfill(5)+'\n')
tfc_val.close()
val.close()

j=0
tfc_train = open('tfc_train.txt','w')
train = open('train_num.txt','w')
for i in range(1,20001):
    if i not in id_val:
        j=j+1
        tfc_train.write('/data3/wangyuhu/traffic_data/images/IMG_'+str(i).zfill(5)+'.jpg\n')
        train.write(str(i).zfill(5)+'\n')
tfc_train.close()
train.close()
print j

        