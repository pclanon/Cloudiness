# Cloudiness2

import cv2 as cv
import numpy as np
from fnmatch import fnmatch
import os.path
from datetime import datetime, timedelta
import os
import sys
import re
import json

# basepath = '/Users/paulclanon/Documents/shasta/20210617/'
# basepath = '/Users/paulclanon/Documents/Jupyter/Meteors/cloudy/'
basepath = '/media/allsky/allsky/images/'

daily_image_directories = []
image_means=[]
nightly_means=[]
reg_compile = re.compile('202106.')

for dirpath, dirnames, filenames in os.walk(basepath):
    daily_image_directories = daily_image_directories + [dirname for dirname in dirnames if reg_compile.match(dirname)]
    
daily_image_directories.sort()

for daily_dir in daily_image_directories:

    imagefiles = [name for name in os.listdir(''.join(basepath + daily_dir)) if fnmatch(name, 'image*.jpg')]

    for imagefile in imagefiles:
        img = cv.imread(''.join(basepath + daily_dir + '/' + imagefile))
        gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
        nan_gray = gray.copy().astype(float)
        nan_gray[nan_gray == 0] = np.nan
        image_means.append(np.nanmean(nan_gray))
    nightly_means.append(sum(image_means)/len(image_means))

    print(daily_dir)
    
cloudiness_dict = dict(zip(daily_image_directories, nightly_means))

with open("/media/allsky/allsky/cloudiness.json", "w") as outfile:
    json.dump(cloudiness_dict, outfile)
    
    
