import os
import img2pdf

# 指定文件夹路径和后缀名
folder_path = input('Folder Path:')
suffix = '.jpg'

# 获取文件夹中的所有文件
files = os.listdir(folder_path)

# 遍历文件夹中的文件
for file in files:
    if os.path.isfile(os.path.join(folder_path, file)):
        # 添加后缀名
        new_name = os.path.splitext(file)[0] + suffix + os.path.splitext(file)[1]
        
        # 重命名文件
        os.rename(os.path.join(folder_path, file), os.path.join(folder_path, new_name))

os.rename(os.path.join(folder_path, 'img.jpg'), os.path.join(folder_path, 'img(00).jpg'))
os.rename(os.path.join(folder_path, 'img(1).jpg'),os.path.join(folder_path, 'img(01).jpg'))
os.rename(os.path.join(folder_path, 'img(2).jpg'),os.path.join(folder_path, 'img(02).jpg'))
os.rename(os.path.join(folder_path, 'img(3).jpg'),os.path.join(folder_path, 'img(03).jpg'))
os.rename(os.path.join(folder_path, 'img(4).jpg'),os.path.join(folder_path, 'img(04).jpg'))
# os.rename(os.path.join(folder_path, 'img(5).jpg'),os.path.join(folder_path, 'img(05).jpg'))
# os.rename(os.path.join(folder_path, 'img(6).jpg'),os.path.join(folder_path, 'img(06).jpg'))
# os.rename(os.path.join(folder_path, 'img(7).jpg'),os.path.join(folder_path, 'img(07).jpg'))
# os.rename(os.path.join(folder_path, 'img(8).jpg'),os.path.join(folder_path, 'img(08).jpg'))
# os.rename(os.path.join(folder_path, 'img(9).jpg'),os.path.join(folder_path, 'img(09).jpg'))
print("文件名处理完成")

# 获取文件夹中的所有.jpg文件
img_files = (f for f in os.listdir(folder_path) if f.endswith('.jpg'))

# 指定生成的PDF文件名
output_pdf = r'C:/Users/Mengqiu/Desktop/Outcome 1.1- sectors of the economy/output.pdf'

# 合成PDF
with open(output_pdf, "wb") as pdf_file:
    pdf_data = img2pdf.convert([os.path.join(folder_path, img) for img in img_files])
    pdf_file.write(pdf_data)

print(f"合成的PDF文件已保存为 {output_pdf}")