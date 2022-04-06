from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from analysci import get_content


text = open('word_new.txt','r',encoding= 'utf8').read()


img = Image.open(r'static\image\tree.jpg')   #打开遮罩图片
img_array = np.array(img)   #将图片转换为数组

# 产生词云
wordcloud = WordCloud(
    background_color='white',
    mask=img_array,
    font_path='font\msyh.ttf' 
  

    ).generate(text)

#绘制图片
fig = plt.figure(1)
plt.imshow(wordcloud)
plt.axis('off')     #是否显示坐标轴

#输出词云图片到文件
plt.savefig(r'static\image\key_word.png')
plt.show()    #显示生成的词云图片   

