from sklearn.externals import joblib
from sklearn.ensemble import RandomForestClassifier
from img.scipts.PictureProcessing import *
from img.scipts.getfeature import *
from img.scipts.config import *
from PIL import Image,ImageDraw
import numpy as np
import sys
def getvalue(lable):
    for key in label_map:
        if label_map[key] == lable:
            return key

def predict(filename):
    pp = ImageProcessing(Image.open(filename).convert("L"))
    pp.twoValue()
    pp.clearNoise()
    pp.CharacterSegmentation()
    piclist = pp.getPicList()
    ans = ""
    clf = joblib.load('.//model//rf.model')
    for index in range(len(piclist)):
        if index >= 4:
            continue
        tmppic = ImageProcessing(piclist[index])
        tmppic.twoValue(0)
        feat = np.array(tmppic.t2_val_to_str()[:-1].split(','))
        ans = ans + getvalue(clf.predict(feat))
    return ans

