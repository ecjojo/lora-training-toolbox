from PIL import Image
import os

def resize_images(directory, output_directory, width, height):
    # 檢查輸出目錄是否存在，如果不存在則創建它
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # 遍歷目錄中的所有文件
    for filename in os.listdir(directory):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            # 構建原始圖片的完整路徑
            input_path = os.path.join(directory, filename)
            
            # 使用Pillow庫打開圖片
            image = Image.open(input_path)
            
            # 調整圖片大小
            resized_image = image.resize((width, height))
            
            # 構建輸出圖片的完整路徑
            output_path = os.path.join(output_directory, filename)
            
            # 保存調整大小後的圖片
            resized_image.save(output_path)
            
            print(f"已處理：{filename}")

# 指定原始圖片所在的目錄
input_directory = 'input'

# 指定調整大小後的圖片輸出目錄
output_directory = 'output'

# 調整的目標大小
width = 896
height = 1152

# 執行批量調整大小的函數
resize_images(input_directory, output_directory, width, height)