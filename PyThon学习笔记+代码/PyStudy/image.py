#  -*- coding:utf-8 -*-
from PIL import Image

#交互式界面  pip install Pillow  有了Pillow，处理图片易如反掌。随便找个图片生成缩略图：

im = Image.open('yuanshiDatu20160902134856.jpg')
print(im.format, im.size, im.mode)
im.thumbnail((400, 200))
im.save('thumb.jpg', 'JPEG')




# MySQL的驱动  mysql-connector-python
# 用于科学计算的NumPy库：numpy
# 用于生成文本的模板工具Jinja2

