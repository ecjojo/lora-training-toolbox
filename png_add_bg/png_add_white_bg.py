from PIL import Image
import os

def add_white_background(input_folder, output_folder):
    # 檢查輸出文件夾是否存在，如果不存在則創建它
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 獲取輸入文件夾中的所有文件
    file_list = os.listdir(input_folder)

    # 遍歷所有文件
    for file_name in file_list:
        # 檢查文件是否為PNG格式
        if file_name.endswith('.png'):
            # 構建輸入文件的完整路徑
            input_path = os.path.join(input_folder, file_name)
            # 讀取圖像
            image = Image.open(input_path).convert("RGBA")
            

            
            # 創建一個新的白色背景圖像
            background = Image.new('RGB', image.size, (255, 255, 255))
            # 將原始圖像粘貼到白色背景上
            background.paste(image, (0, 0), image)

            # 構建輸出文件的完整路徑
            output_path = os.path.join(output_folder, file_name)
            # 將圖像保存到輸出文件
            background.save(output_path)

            print(f"已處理: {file_name}")

# 要處理的輸入文件夾路徑
input_folder = 'input'
# 處理後的輸出文件夾路徑
output_folder = 'output'

# 執行函數
add_white_background(input_folder, output_folder)