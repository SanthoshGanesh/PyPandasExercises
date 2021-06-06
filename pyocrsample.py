import os

import easyocr
from PIL.ImagePath import Path
from PIL.ImageShow import show
from networkx.classes.filters import show_nodes
from pdf2image import convert_from_path
import numpy as np
import PIL
from PIL import ImageDraw
import spacy

reader= easyocr.Reader(['en'])
images= convert_from_path('functionalSample.pdf')

from IPython.display import Image,display
display(images[0])
# show(images[0])

bounds=reader.readtext(np.array(images[0]))
# print(bounds)

# def draw_boxes(image, bounds, color='yellow', width=2):
#     draw = ImageDraw.Draw(image)
#     for bound in bounds:
#         p0, p1, p2, p3 = bound[0]
#         draw.line([*p0, *p1, *p2, *p3, *p0], fill=color, width=width)
#     return image

# draw_boxes(images[0], bounds)
# show(images[0])

# print(bounds[2][1])

text=''
for i in range(len(bounds)):
    text=text+bounds[i][1]+'\n'

# print(text)

nlp=spacy.load('en_core_web_sm')
doc=nlp(text)

from spacy import displacy
svg=displacy.render(nlp(doc.text),style='ent')







