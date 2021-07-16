import re
import os

from utils import read_from_file, write_to_file, add_to_file

# 文本存储路径
folder_path = r'./data/team/track_GJ'
# 获得文件列表
dir_list = os.listdir(folder_path)
# 循环文件，截取团队编号
for file_name in dir_list:
    # 拼接文件路径
    file_path = os.path.join(folder_path, file_name)
    # 获得文件内容
    content = read_from_file(file_path)
    # 截取并且保存团队编号
    add_to_file(re.findall(r'<a href=\\"/adminprojects/(.+?)\\" target', content), './data/team/team_links2.txt')
