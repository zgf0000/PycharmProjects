#信息化远程学习第一个版块的内容--信息化能力提升
from selenium import webdriver

import time
import threading
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from os import path
from tkinter import *
import tkinter.messagebox as aa

#弹出窗口
def getInput(title, message):
    def return_callback(event):
        # print('quit...')
        root.quit()

    def close_callback():
        aa.showinfo('message', 'no click...')
        root.quit()

    root = Tk(className=title)
    root.wm_attributes('-topmost', 1)
    screenwidth, screenheight = root.maxsize()
    width = 300
    height = 100
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    root.geometry(size)
    root.resizable(0, 0)
    lable = Label(root, height=2)
    lable['text'] = message
    lable.pack()
    entry = Entry(root)
    entry.bind('<Return>', return_callback)
    entry.pack()
    entry.focus_set()
    root.protocol("WM_DELETE_WINDOW", close_callback)

    root.mainloop()
    str = entry.get()
    root.destroy()
    return str




def xuexi(zkc):# 标记课程
    a = []
    kcs = 0
    while kcs < zkc:
        a.append(kcs)
        kcs += 1
    # print(a)
    isno = path.isfile('D:/myxuexi_2.txt')  # 判断文件是否存在

    print(isno)
    if isno == False:
        file = open('D:/myxuexi_2.txt', 'w')
        for x in a:
            file.writelines(str(x) + ',')
        file.close()

    f = open('D:/myxuexi_2.txt', 'r')
    b = f.read()
    b = b.rstrip(',')  # 删除最后一个逗号
    c = b.split(',')  # 转换成列表
    f.close()
    d = c[0]  # 第一个元素并赋值给d
    # print(d, c)
    # u = open('D:/myxuexi.txt', 'w')
    # for i in c:
    #     u.writelines(str(i) + ',')
    # u.close()
    return d

#删除已经学习了的
def del_yixuexi():
    f = open('D:/myxuexi_2.txt', 'r')
    b = f.read()
    b = b.rstrip(',')  # 删除最后一个逗号
    c = b.split(',')  # 转换成列表
    f.close()
    d = c.pop(0)  # 删除第一个元素并赋值给d
    # print(d, c)
    u = open('D:/myxuexi_2.txt', 'w')
    for i in c:
        u.writelines(str(i) + ',')
    u.close()



# 判断当前课件是否结束
def is_allend():
    while True:
        try:

            # 获取当前课件的总时长
            all_time = browser.find_element(by=By.ID, value='_ctime').get_attribute('textContent')

            # 该视频的总时间
            time.sleep(20) # 5秒检测一次
            finish_time = browser.find_element(by=By.ID,value='min').get_attribute('textContent')
            wc_time=''.join(finish_time.partition(":")[:1])#去除冒号后的数字以便比较
            print("总时长：", all_time, finish_time,wc_time)
            if all_time == wc_time:
                del_yixuexi() #删除已经学习了的

                # browser.find_element(by=By.ID, value='back_courselist').click()
                # confirm = browser.switch_to.alert  # 不管是 alert 还是 confirm、cprompt ，"switch_to" 的方式是一样的。
                # print(confirm.text)
                # time.sleep(1)
                # confirm.accept()

                old_myweb()




                # browser.switch_to.window(-1)
                # # browser.close()#关闭当前页面
                # old_myweb()

              # 当前课件学习结束应该返回



        except:
            # print("*"*20)
            finish_time = '0'
            all_time = '1'
t1 = threading.Thread(target=is_allend)  #开启线程监测课件学习是否结束
# # 判断当前视频是否结束
def is_end():
    while True:
        try:
            f = browser.find_element(by=By.ID, value='course_video')  # 找到框架网页iframe
            browser.switch_to.frame(f)  # 定位到最底的框架网页

            # 获取当前播放的进度
            current_time = browser.find_element(by=By.XPATH, value='//em[@class="ccH5TimeCurrent"]').get_attribute('textContent')

            # 该视频的总时间
            time.sleep(10) # 10秒检测一次
            total_time = browser.find_element(by=By.XPATH,value='//em[@class="ccH5TimeTotal"]').get_attribute('textContent')
            print(current_time, total_time)
            if current_time == total_time:
              # 当前视频播放结束，我在这里做的是重复播放即可
                plays_old()
                # break  # 退出循环
                # js = "document.ElementById('nextBtn').click()"  # js脚本
                # browser.execute_script(js)


        except:
            # print("*"*20)
            current_time = '00:00'
            total_time = '00:01'



t2 = threading.Thread(target=is_end)  #开启线程监测是否播放结束

browser = webdriver.Chrome()
# 请求登陆页面
browser.get('https://sts.hnteacher.net/Account/Login?ReturnUrl=%2F')


# 登陆
def login(username, password):
    user_name = browser.find_element(By.NAME, 'userName')
    pwd = browser.find_element(By.ID, 'pass')  # 密码
    login_btn = browser.find_element(By.ID,'btn_Login')  # 登陆按钮
    user_name.send_keys(username)  # 输入手机号码
    pwd.send_keys(password)  # 输入密码
    time.sleep(3)
    login_btn.click()  # 点击登陆按钮

#切换到我的办公室新页面
def to_newweb():
    time.sleep(4)
    jiri = browser.find_element(By.LINK_TEXT, '桃源县信息技术骨干教师工作坊')  # 进入学习
    jiri.click()
#重复学习计划新页面
def old_myweb():
    handles = browser.window_handles
    browser.close()
    browser.switch_to.window(handles[1])

    kcs = browser.find_element(By.ID, '3538')  # 进入已选课的学习
    time.sleep(3)
    xxnr = kcs.find_elements(by=By.TAG_NAME, value="li")
    cx = xuexi(len(xxnr))  # 调用课程的函数
    xxnr[int(cx)].find_element(By.PARTIAL_LINK_TEXT,'学习').click()
    time.sleep(3)
    toold_course()
    # print(liEleList)

#切换到进行中的学习计划新页面
def to_myweb():

    time.sleep(4)
    current = browser.current_window_handle  # 当前页面的句柄
    handles = browser.window_handles

    for handle in handles:
        if handle != current:
            browser.switch_to.window(handle)
    time.sleep(2)

    browser.find_element(By.LINK_TEXT, '我的工作台').click()  # 进入我的工作台
    time.sleep(2)
    browser.find_element(By.LINK_TEXT, '学习研究').click()  # 进入学习研究
    time.sleep(2)
    browser.find_element(By.LINK_TEXT, '课程学习').click()  # 进入学习

    time.sleep(5)
    kc1=browser.find_element(By.LINK_TEXT,'2022年信息化环境下的课堂教学能力提升初中')
    kc1.click()
    time.sleep(5)

    kclb_ul = browser.find_element(By.ID, 'courseList')  # 进入已选课的学习
    time.sleep(3)
    liEleList = kclb_ul.find_elements(by=By.TAG_NAME,value="li")
    for item in liEleList:
        text = item.text
        print(text)
    liEleList[0].click()

    time.sleep(8)
    kcs = browser.find_element(By.ID, '3538')  # 进入已选课的学习
    time.sleep(3)
    xxnr = kcs.find_elements(by=By.TAG_NAME,value="li")
    for item in xxnr:
        text = item.text
        print(text)
    print(len(xxnr))
    cx=xuexi(len(xxnr))# 调用课程的函数
    time.sleep(2)
    xxnr[int(cx)].find_element(By.PARTIAL_LINK_TEXT,'学习').click()





# 重复播放
def plays_old():
    time.sleep(5)

    try:
        video = browser.find_element(by=By.ID, value='replaybtn')  # 定位视频窗口
        video.click()  # 点击播放


    except:
        # stop_thread(t2)
        pass


# 再次的播放视频页面
def toold_course():


    current = browser.current_window_handle  # 当前页面的句柄

    # 因为跳转到新的页面，所以browser要切换到新的页面操作
    handles = browser.window_handles
    for handle in handles:
        if handle != current:
            browser.switch_to.window(handle)
    time.sleep(10)
    ulyf_py = browser.find_element(by=By.ID, value='ulCommant')  # 定位其他人第一个已经填写了的用户评语Ul
    onepy_nr = ulyf_py.find_elements(by=By.TAG_NAME, value='dl')
    onepy_dd = onepy_nr[0].find_element(by=By.TAG_NAME, value='dd')
    onepy_p = onepy_dd.find_element(by=By.TAG_NAME, value='p').get_attribute('textContent')  # 找到评语内容
    user_py = browser.find_element(by=By.ID, value='txtCommant')  # 定位本人评语输入框
    user_py.send_keys(onepy_p)  # 书写评语到输入框
    time.sleep(2)
    user_pybt = browser.find_element(by=By.ID, value='btnCommant')  # 定位本人评语提交按钮
    user_pybt.click()

    print(onepy_p)


    # f = browser.find_element(by=By.ID, value='course_video')
    # browser.switch_to.frame(f)  # 定位到最底的框架网页
    #
    #
    # try:
    #     video = browser.find_element(by=By.ID,value= 'replaybtn')  # 定位视频窗口
    #     video.click()  # 点击播放
    #     time.sleep(3)
    #     browser.switch_to.parent_frame()# 切换到最外层
    #
    #
    #
    #
    #
    #
    # except:
    #     # stop_thread(t2)
    #     pass

# 转到播放视频页面
def to_course():

    time.sleep(5)
    current = browser.current_window_handle  # 当前页面的句柄

    # 因为跳转到新的页面，所以browser要切换到新的页面操作
    handles = browser.window_handles
    for handle in handles:
        if handle != current:
            browser.switch_to.window(handle)

    time.sleep(3)
    # ulyf_py= browser.find_element(by=By.ID,value= 'ulCommant')  # 定位其他人第一个已经填写了的用户评语Ul
    # onepy_nr=ulyf_py.find_elements(by=By.TAG_NAME,value='dl')
    # onepy_dd = onepy_nr[0].find_element(by=By.TAG_NAME, value='dd')
    # onepy_p = onepy_dd.find_element(by=By.TAG_NAME, value='p').get_attribute('textContent')# 找到评语内容
    # user_py = browser.find_element(by=By.ID, value='txtCommant')  # 定位本人评语输入框
    # user_py.send_keys(onepy_p)# 书写评语到输入框
    # time.sleep(2)
    # user_pybt = browser.find_element(by=By.ID, value='btnCommant')  # 定位本人评语提交按钮
    # user_pybt.click()
    #
    # print(onepy_p)



    time.sleep(1)
    # f=browser.find_element(by=By.ID,value= 'course_video')# 找到框架网页iframe
    # browser.switch_to.frame(f)# 定位到最底的框架网页

    t1.start()  # 开始线程2 是否播放结束因为不需要播放就计时，这里就只判断是否学习完成了









if __name__ == '__main__':
    print("*" * 10, "只用于研究学习，勿应用于其他用途", "*" * 10)
    print("=" * 10, "设计者：周高飞", "=" * 10)
    time.sleep(3)

    yfm = getInput('登录提示', '身份证号码')

    pwd = getInput('登录提示', '密码')

    print("学习即将自动进入无人值守情形")
    time.sleep(2)

    login(yfm, pwd)
    to_newweb()
    to_myweb()
    to_course()


