import sys
from matplotlib import pyplot as plt
import numpy as np
import util
import pdb

img_path = util.io.get_absolute_path(sys.argv[1])
score_path = util.str.replace_all(img_path, "image_2", "score")
score_path = util.str.replace_all(score_path, ".png", ".npy")

image = util.img.imread(img_path)
score = np.load(score_path)
pdb.set_trace()
print(image.shape)