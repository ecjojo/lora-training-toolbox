import os
import shutil

txt_folder = 'txt_folder'
img_folder = 'img_folder'

# 確保txt和圖片文件夾存在
if not os.path.exists(txt_folder):
    os.makedirs(txt_folder)
if not os.path.exists(img_folder):
    os.makedirs(img_folder)

# 讀取txt文件夾中的檔案名稱
for filename in os.listdir(txt_folder):
    if filename.endswith('.txt'):
        img_filename = os.path.join(img_folder, filename.replace('.txt', '.png'))
        if os.path.exists(img_filename):
            shutil.copy(img_filename, txt_folder)