import glob
import os
SOURCE = 'source'
DESTINATION = 'destination'

files = glob.glob(SOURCE+'/*')

cleaned = []
for file in files:
    cleaned.append(file.split('\\')[-1].split('.')[0])

unique = list(set(cleaned))

dup = []
for uni in unique:
    if cleaned.count(uni) > 1:
        dup.append(uni)

for file in files:
    for du in dup:
        name = file.split('\\')[-1].split('.')[0]
        if name == du:
            os.rename(file ,DESTINATION+'\\'+file.split('\\')[-1])
    