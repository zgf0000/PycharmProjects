
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import threading
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import inspect
import ctypes
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



def xuexi():  # 标记课程

    f = open('D:/sxt_2.txt', 'r',encoding='UTF-8')
    b = f.read()

    c = b.split(';')  # 转换成列表
    f.close()
    d = c[0]  # 第一个元素并赋值给d

    return d


# 删除已经学习了的
def del_yixuexi():
    f = open('D:/sxt_2.txt', 'r',encoding='UTF-8')
    b = f.read()
    c = b.split(';')  # 转换成列表
    f.close()
    d = c.pop(0)  # 删除第一个元素并赋值给d
    # print(d, c)
    u = open('D:/sxt_2.txt', 'w',encoding='UTF-8')
    for i in c:
        u.writelines(str(i) + ';')
    u.close()


# 判断是否有答题窗口弹出
def is_exist():
    while True:
        try:

            code_yzm=browser.find_element(by=By.ID,value='codespan').get_attribute('textContent')
            browser.find_element(by=By.ID, value='code').send_keys(code_yzm)
            print("正在努力识别验证")
            time.sleep(3)
            browser.find_element(by=By.LINK_TEXT, value='提交').click()
            # browser.switch_to.default_content()
            # browser.switch_to.frame('tmDialog_iframe')  # 答题窗口在另一个frame里面，要切换
            # box = browser.find_elements_by_class_name('answerOption')  # 答题列表
            # radio = box[0].find_element_by_tag_name('input')  # 找到第一个选项
            # radio.click()  # 选择
            # browser.switch_to.default_content()
            # browser.find_element_by_link_text('关闭').click()  # 关闭答题窗口

        except:
            pass # 空操作
            # print("没有弹出验证？")

            # browser.switch_to.parent_frame()  # 没有弹出，切换回本来的frame

        time.sleep(30)

t1 = threading.Thread(target=is_exist) #开启线程监测是否有弹出窗口
# 判断当前视频是否结束
def is_end():
    while True:
        try:
            all_time=browser.find_element(by=By.ID,value= 'courseStudyBestMinutesNumber').get_attribute('textContent')
            time.sleep(60)
            finish_time = browser.find_element(by=By.ID, value='courseStudyMinutesNumber').get_attribute('textContent')
            print(all_time,finish_time)
            if all_time==finish_time:
                del_yixuexi()
                browser.close()
                new_window()
        except:
            pass

        try:

            # 获取当前播放的进度
            current_time = browser.find_element(by=By.CLASS_NAME,value= 'ccH5TimeCurrent').get_attribute('textContent')
            # 该视频的总时间
            total_time = browser.find_element(by=By.CLASS_NAME,value='ccH5TimeTotal').get_attribute('textContent')
            print(current_time, total_time)
            if current_time == total_time:

                queren_bt=browser.find_element(by=By.LINK_TEXT,value='Ok，我知道了！')
                queren_bt.click()
                video = browser.find_element(by=By.ID, value='replaybtn')  # 定位视频窗口
                video.click()  # 点击播放

                # break  # 退出循环


                # js = "document.ElementById('nextBtn').click()"  # js脚本
                # browser.execute_script(js)

            time.sleep(10)  # 10秒检测一次
        except:
            # print("*"*20)
            current_time = '00:00'
            total_time = '00:01'

t2 = threading.Thread(target=is_end)  #开启线程监测是否播放结束


browser = webdriver.Chrome()
# 请求登陆页面
browser.get('http://cn202243006.stu.teacher.com.cn/')


# 登陆
def login(username, password):
    links = browser.find_element(by=By.LINK_TEXT, value='登录')
    links.click()
    time.sleep(3)
    user_name = browser.find_element(By.ID, 'user')
    pwd = browser.find_element(By.ID, 'pwd')  # 密码
    login_btn = browser.find_element(By.ID,'phoneLoginSubmit')  # 登陆按钮
    user_name.send_keys(username)  # 输入手机号码
    pwd.send_keys(password)  # 输入密码
    login_btn.click()  # 点击登陆按钮

#切换到我的办公室新页面
def to_newweb():
    time.sleep(4)
    jiri = browser.find_element(By.CLASS_NAME, 'button-item')  # 进入学习
    jiri.click()

#切换到进行中的学习计划新页面
def to_myweb():
    time.sleep(5)
    kclb_ul = browser.find_element(by=By.XPATH, value='//div/ul[@class="selectItemSecond"]')  # 进入学习计划页面
    # print(kclb_ul)
    time.sleep(3)
    liEleList = kclb_ul.find_elements(by=By.TAG_NAME, value="li")
    # for item in liEleList:
    #     text = item.text
    #     print(text)


    liEleList[1].click()#进入第二个选项

# 切换进行中的学习计划窗口
def new_window():
    # print("重复选择开始了")


    time.sleep(3)
    # 因为跳转到新的页面，所以browser要切换到新的页面操作
    handles = browser.window_handles
    browser.switch_to.window(handles[0])
    current = browser.current_window_handle  # 当前页面的句柄
    kc_nr = xuexi()
    key = browser.find_element(by=By.PARTIAL_LINK_TEXT, value=kc_nr)  # 找到课程
    key.click()  # 跳转到学习页面
    handles = browser.window_handles

    for handle in handles:
        if handle != current:
            browser.switch_to.window(handle)
    time.sleep(10)

    try:
        video = browser.find_element(by=By.ID,value= 'replaybtn')  # 定位视频窗口
        video.click()  # 点击播放




    except:
        # print("没有找到播放")
        # stop_thread(t2)
        pass



# 转到播放视频页面
def to_course():

    time.sleep(5)
    current = browser.current_window_handle  # 当前页面的句柄
    kc_nr=xuexi()
    print("准备学习： ",kc_nr)
    key = browser.find_element(by=By.LINK_TEXT,value= kc_nr)  # 找到课程
    key.click()  # 跳转到学习页面
    time.sleep(1)  # 等待页面加载
    # 因为跳转到新的页面，所以browser要切换到新的页面操作
    handles = browser.window_handles
    for handle in handles:
        if handle != current:
            browser.switch_to.window(handle)
    time.sleep(10)
    t1.start()  # 开始线程2 是否弹出
    time.sleep(5)
    t2.start()  # 开始线程1 是否播放结束
    time.sleep(3)

    try:
        video = browser.find_element(by=By.ID,value= 'replaybtn')  # 定位视频窗口
        video.click()  # 点击播放





    except:
        # stop_thread(t2)
        pass






if __name__ == '__main__':
    print("*"*10,"只用于研究学习，勿应用于其他用途","*"*10)
    print("=" * 10, "设计者：周高飞", "=" * 10)
    time.sleep(3)

    yfm = getInput('登录提示', '手机号')

    pwd = getInput('登录提示', '密码')

    print("学习即将自动进入无人值守情形")
    time.sleep(2)


    login(yfm, pwd)
    to_newweb()
    to_myweb()

    to_course()

    # #开两个线程     从讲到不讲的课堂转型    “本色语文”课堂的基本特征
    # t1=threading.Thread(target=is_exist)
    # t2=threading.Thread(target=is_end)
    # t2.start()
    # time.sleep(3)
    # t1.start()
    # t2.join()
    # t1.join()
