import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join

xmldir="/data3/wangyuhu/traffic_data/Annotations/"
classes=[]
for xmlfile in os.listdir(xmldir):
    xmlname = os.path.splitext(xmlfile)[0]
    in_file = open('/data3/wangyuhu/traffic_data/Annotations/%s.xml'%(xmlname))
    tree=ET.parse(in_file)
    root = tree.getroot()
    for obj in root.iter('object'):
        cls = obj.find('name').text
        if cls not in classes:
            classes.append(cls)

print(classes)
        