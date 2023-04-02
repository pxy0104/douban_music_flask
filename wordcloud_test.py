# -*- coding: utf-8 -*-
# @Time    : 2023/3/5 16:18
# @File    : wordcloud.py
# @Software: PyCharm
# @Author  : pxy
import jieba  # 分词模块 结巴
from matplotlib import pyplot as plt  # 绘图，数据可视化
from wordcloud import WordCloud
from PIL import Image  # 图片处理
import numpy as np  #
import sqlite3

conn = sqlite3.connect('music.db')
cur = conn.cursor()
sql = "select mname from music247"
data = cur.execute(sql)
text = ""
# print(type(data))
for item in data:
    # print(item[0])
    # print(key)
    text = text + item[0]
# print(text)
cur.close()
conn.close()

cut = jieba.cut(text)
string = ' '.join(cut)
print(string)

print(len(string))

img = Image.open(r'tree.jpg')  # 打开遮罩图片
img_array = np.array(img)
wc = WordCloud(
    background_color='white',
    mask=img_array,
    font_path='SIMLI.TTF',  # 字体所在位置
    width=960,
    height=720
)
wc.generate_from_text(string)

# 绘制图片
fig = plt.figure(1)
plt.imshow(wc)

plt.axis('off')
# plt.show()
plt.savefig(r'res_tree_1.jpg')
