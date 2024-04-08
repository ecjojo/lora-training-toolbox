
import os

input_folder = 'tsv_2_folder\input'
output_folder = 'tsv_2_folder\output'

# 確保output文件夾存在
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 讀取input文件夾中的每個檔案
for filename in os.listdir(input_folder):
    if filename.endswith('.tsv'):
        with open(os.path.join(input_folder, filename), 'r') as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                name, content = line.split('\t', 1)
                output_filename = os.path.join(output_folder, f'{name}.txt')
                with open(output_filename, 'w') as output_file:
                    output_file.write(content)