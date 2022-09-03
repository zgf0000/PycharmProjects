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
sheet2 = wb.sheets['Sheet2']


def numToStr(num):
    size = 26  # 一共26个字母
    list = ['Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
            'U', 'V', 'W', 'X', 'Y', 'Z']
    result = list[num % size]
    if num > size:
        while (num % size == 0 and num // size - 1 > size) | (num % size != 0 and num // size > size):
            num = num // size
            result = list[num % size] + result
        if num % size == 0:
            result = list[num // size - 1] + result
        else:
            result = list[num // size] + result
    return result


# Test


def tc():
    xq = sheet1.range('B3').value
    jc = sheet1.range('C5').value
    counts=2 #插入的行数标记
    n=3
    while n<8:
        print("开始外循环")
        i=6
        while i<19:  # 13个班有13行数据
            # print(i)

            bj_value = "A" + str(i)
            km_value = numToStr(n) + str(i)
            bj = sheet1.range(bj_value).value
            km_jz = sheet1.range(km_value).value
            km_jz = km_jz.split('\n')
            print(km_jz[1])
            tbj_value = "A" + str(counts)  # 填充sheet2表格
            txq_value = "D" + str(counts)
            tjc_value = "E" + str(counts)
            tjz_value = "B" + str(counts)
            tkm_value = "C" + str(counts)

            sheet2.range(tbj_value).value = bj  # 班级
            sheet2.range(txq_value).value = xq  # 星期
            sheet2.range(tjc_value).value = jc  # 节次
            sheet2.range(tjz_value).value = km_jz[0]  # 科目
            sheet2.range(tkm_value).value = km_jz[1]  # 教者
            i=i+1
            counts=counts+1
        n=n+1
        counts=counts+1


# # 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print(numToStr(4))
    tc()

# # 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
