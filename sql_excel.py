import xlwings as xw
import pymssql

# a = sheet1.range('A1:B2').value
# print(a)

#测试与SQL数据库的连接3
server = "WNSG-003.xincache.cn"     # 连接服务器地址
user = "host1057340"                 # 连接帐号
password = "z1g2f388"             # 连接密码

with pymssql.connect(server, user, password, "host1057340",charset="utf8") as conn:
    with conn.cursor(as_dict=True) as cursor:   # 数据存放到字典中
        cursor.execute('SELECT top 3 * FROM Admin_user ',2)

        a=[['a','b','c','d','e']]

        for row in cursor:
            list1=list(row.values())
            a.append(list1)
        print(a)
wb = xw.Book()  # this will create a new workbook
# wb = xw.Book(r'D:\abc.xlsx')  # on Windows: use raw strings to escape backslashes

sheet1 = wb.sheets['Sheet1']
sheet1.range('A1').value=a

# # 按间距中的绿色按钮以运行脚本。
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
