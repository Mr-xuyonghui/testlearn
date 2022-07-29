from PIL import Image
import pytesseract

img = Image.open('piccode.jpeg')

print(img.size)
# 展示图片对象
# img.show()
"""针对有线条干扰验证的验证码，可以对图片进行灰度和二值化"""
# 将图片转为灰度图片
img = img.convert('L')
# convert()传入1，可以将图片二值化，使用默认的阈值127，可以直接转化原图
# img= img.convert('1')
"""
若需要自定义阈值转化图片，需要先将原图转为灰度，再二值化
"""
thresold = 127
table = []
for i in range(256):
    if i < thresold:
        table.append(0)
    else:
        table.append(1)
img = img.point(table, '1')
#img.show()
# 识别成字符串
res = pytesseract.image_to_string(img)
print(pytesseract.image_to_boxes(img))
print(res)
