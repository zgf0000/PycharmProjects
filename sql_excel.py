import xlwings as xw
import pymssql

# a = sheet1.range('A1:B2').value
# print(a)

# #测试与SQL数据库的连接3
# server = "WNSG-003.xincache.cn"     # 连接服务器地址
# user = "host1057340"                 # 连接帐号
# password = "z1g2f388"             # 连接密码
#
# with pymssql.connect(server, user, password, "host1057340",charset="utf8") as conn:
#     with conn.cursor(as_dict=True) as cursor:   # 数据存放到字典中
#         cursor.execute('SELECT top 3 * FROM Admin_user ',2)
#
#         a=[['a','b','c','d','e']]
#
#         for row in cursor:
#             list1=list(row.values())
#             a.append(list1)
#         print(a)
# wb = xw.Book()  # this will create a new workbook
wb = xw.Book(r'D:\kb.xlsx')  # on Windows: use raw strings to escape backslashes

sheet1 = wb.sheets['Sheet1']

# print(km_jz[1])
sheet2 = wb.sheets['Sheet2']

def tc():
    xq = sheet1.range('B3').value
    jc = sheet1.range('C5').value
    for i in range(6,19):
        # print(i)

        bj_value="A"+str(i)
        km_value = "C" + str(i)
        bj = sheet1.range(bj_value).value
        km_jz = sheet1.range(km_value).value
        km_jz = km_jz.split('\n')
        print(km_jz[1])
        tbj_value = "A" + str(i-4)
        txq_value = "D" + str(i-4)
        tjc_value = "E" + str(i - 4)
        tjz_value = "B" + str(i - 4)
        tkm_value = "C" + str(i - 4)

        sheet2.range(tbj_value).value = bj
        sheet2.range(txq_value).value = xq
        sheet2.range(tjc_value).value = jc
        sheet2.range(tjz_value).value = km_jz[0]
        sheet2.range(tkm_value).value = km_jz[1]



# # 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    tc()

# # 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
