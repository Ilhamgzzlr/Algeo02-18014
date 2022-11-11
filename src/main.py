import os
from matrix import *
from picture import *

S = resize_images(load_images(".\dataset"), (256, 256))
displayListMatrix(S)