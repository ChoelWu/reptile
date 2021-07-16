import re
import os
import xlwt

from utils import read_from_file, write_to_file

# 文本存储路径
folder_path = r'./data/individual/zhz'
# 获得文件列表
dir_list = os.listdir(folder_path)

# 新建excel
wk = xlwt.Workbook()
sheet1 = wk.add_sheet("高教赛道", cell_overwrite_ok=True)

row_number = 0
# 循环文件，截取团队编号
for file_name in dir_list:
    # 拼接文件路径
    file_path = os.path.join(folder_path, file_name)
    # 获得文件内容
    content = read_from_file(file_path)

    # 获取项目参赛赛道
    track_name = re.findall(r'参赛赛道：\\r\\n              \\r\\n              <span>(.+?)</span>\\r\\n', content)
    print(track_name)
    if len(track_name) > 0 and track_name[0] == '高教主赛道':
        # 获取项目名称
        project_name = re.findall(
            r'<div class=\\"info-box\\">\\r\\n              <h4>(.+?)</h4>\\r\\n              <div class=\\"location\\">\\r\\n ',
            content)
        # 项目名称
        sheet1.write(row_number, 0, project_name)
        # 团队成员
        team_text = re.findall(
            r'<th>在校时间</th>\\r\\n                <th>手机号</th>\\r\\n                <th>电子邮箱</th>\\r\\n                \\r\\n              </tr>\\r\\n              (.+?)\\r\\n            </table>\\r\\n          </div>\\r\\n          <div class=\\"content-block\\">\\r\\n            <h6>指导教师</h6>',
            content)
        member_info_text_list = re.findall(r'<tr>(.+?)</tr>', team_text[0])

        member_info_list = []
        member_name_list = []
        for key, member_info_text in enumerate(member_info_text_list):
            member_info_text = member_info_text.replace("<span>", "").replace("</span>", "")
            member_info_list = re.findall(r'<td>(.+?)</td>', member_info_text)

            # 负责人
            if key == 0 and member_info_list[1] == '负责人':
                sheet1.write(row_number, 1, member_info_list[0])
            else:
                # 写团队成员信息
                member_name_list.append(member_info_list[0])

        sheet1.write(row_number, 2, "，".join(member_name_list))

        # 指导老师
        teacher_group_text = re.findall(
            r'<th>所在部门</th>\\r\\n                <th>手机号</th>\\r\\n                <th>电子邮箱</th>\\r\\n              </tr>\\r\\n\\r\\n              (.+?)\\r\\n            </table>\\r\\n          </div>',
            content)
        if len(teacher_group_text) != 0:
            teacher_info_text_list = re.findall(r'<tr>(.+?)</tr>', teacher_group_text[0])

            teacher_info_list = []
            teacher_name_list = []
            for teacher_info_text in teacher_info_text_list:
                teacher_info_text = teacher_info_text.replace("<span>", "").replace("</span>", "")
                teacher_info_list = re.findall(r'<td>(.+?)</td>', teacher_info_text)

                # 写指导教师信息

                teacher_name_list.append(teacher_info_list[0])

                sheet1.write(row_number, 3, "，".join(teacher_name_list))

        row_number = row_number + 1
# 保存excel
wk.save("./rel3.xls")
