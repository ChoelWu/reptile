import re
import os
import xlwt

from utils import read_from_file, write_to_file

# 文本存储路径
folder_path = r'./data/individual/qnhszmzl'
# 获得文件列表
dir_list = os.listdir(folder_path)

# 新建excel
wk = xlwt.Workbook()
sheet1 = wk.add_sheet("团队成员", cell_overwrite_ok=True)
sheet2 = wk.add_sheet("指导教师", cell_overwrite_ok=True)

member_row_number = 0
teacher_row_number = 0
# 循环文件，截取团队编号
for file_name in dir_list:
    # 拼接文件路径
    file_path = os.path.join(folder_path, file_name)
    # 获得文件内容
    content = read_from_file(file_path)
    # 获取项目名称
    project_name = re.findall(r'<div class=\\"info-box\\">\\r\\n              <h4>(.+?)</h4>\\r\\n              <div class=\\"location\\">', content)
    # 参赛状态
    race_state = re.findall(r'参赛状态：\\r\\n              \\r\\n              <span>(.+?)</span>\\r\\n', content)
    # 获取项目参赛赛道
    track_name = re.findall(r'参赛赛道：\\r\\n              \\r\\n              <span>(.+?)</span>\\r\\n', content)
    # 获取项目参赛组别
    race_cat_name = re.findall(r'参赛组别：\\r\\n              <span>(.+?)</span>', content)
    # 获取项目参赛赛道
    race_type = re.findall(r'参赛类别：\\r\\n              <span>(.+?)</span>', content)
    # 报名时间
    apply_time = re.findall(r'报名时间：\\r\\n              <span>(.+?)</span>\\r\\n', content)
    # 团队成员
    team_text = re.findall(
        r'<th>在校时间</th>\\r\\n                <th>手机号</th>\\r\\n                <th>电子邮箱</th>\\r\\n                \\r\\n              </tr>\\r\\n              (.+?)\\r\\n            </table>\\r\\n          </div>\\r\\n          <div class=\\"content-block\\">\\r\\n            <h6>指导教师</h6>',
        content)
    member_info_text_list = re.findall(r'<tr>(.+?)</tr>', team_text[0])

    member_info_list = []
    member_end_row= member_row_number + len(member_info_text_list) - 1
    for member_info_text in member_info_text_list:
        member_info_text = member_info_text.replace("<span>", "").replace("</span>", "")
        member_info_list = re.findall(r'<td>(.+?)</td>', member_info_text)
        # 写数据
        print(member_row_number, member_row_number + len(member_info_text_list) - 1)
        sheet1.write_merge(member_row_number, member_end_row, 0, 0, project_name)
        sheet1.write_merge(member_row_number, member_end_row, 1, 1, race_state)
        sheet1.write_merge(member_row_number, member_end_row, 2, 2, track_name)
        sheet1.write_merge(member_row_number, member_end_row, 3, 3, race_cat_name)
        sheet1.write_merge(member_row_number, member_end_row, 4, 4, race_type)
        sheet1.write_merge(member_row_number, member_end_row, 5, 5, apply_time)

        # 写团队成员信息
        member_col_number = 6
        for member_info in member_info_list:
            sheet1.write(member_row_number, member_col_number, member_info)
            member_col_number = member_col_number + 1

        member_row_number = member_row_number + 1

    # 指导老师
    teacher_group_text = re.findall(
        r'<th>所在部门</th>\\r\\n                <th>手机号</th>\\r\\n                <th>电子邮箱</th>\\r\\n              </tr>\\r\\n\\r\\n              (.+?)\\r\\n            </table>\\r\\n          </div>',
        content)
    if len(teacher_group_text) !=0:
        teacher_info_text_list = re.findall(r'<tr>(.+?)</tr>', teacher_group_text[0])

        teacher_info_list = []
        teacher_end_row= teacher_row_number + len(teacher_info_text_list) - 1
        for teacher_info_text in teacher_info_text_list:
            teacher_info_text = teacher_info_text.replace("<span>", "").replace("</span>", "")
            teacher_info_list = re.findall(r'<td>(.+?)</td>', teacher_info_text)

            # 写数据
            sheet2.write_merge(teacher_row_number, teacher_end_row, 0, 0, project_name)
            sheet2.write_merge(teacher_row_number, teacher_end_row, 1, 1, race_state)
            sheet2.write_merge(teacher_row_number, teacher_end_row, 2, 2, track_name)
            sheet2.write_merge(teacher_row_number, teacher_end_row, 3, 3, race_cat_name)
            sheet2.write_merge(teacher_row_number, teacher_end_row, 4, 4, race_type)
            sheet2.write_merge(teacher_row_number, teacher_end_row, 5, 5, apply_time)

            # 写指导教师信息
            teacher_col_number = 6
            for teacher_info in teacher_info_list:
                sheet2.write(teacher_row_number, teacher_col_number, teacher_info)
                teacher_col_number = teacher_col_number + 1

            teacher_row_number = teacher_row_number + 1

# 保存excel
wk.save("./rel2.xls")
