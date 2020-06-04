# **UI自动化**

本文档使用markdown语法编辑，建议下载Typora进行阅读。[下载地址](https://www.typora.io/#windows)
- 框架：采用python+selenium+pytest，市面上比较流行的框架，简单易上手。编辑器选择pycharm
- [python下载地址](https://www.python.org/downloads/windows/)
- [pycharm下载地址](https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=windows&code=PCC)
- [python基础学习地址](https://www.runoob.com/python3/python3-tutorial.html)
- [selenium基础学习地址](https://www.jianshu.com/p/55828262a478)
- [pytest官方文档](https://docs.pytest.org/en/latest/index.html)


## python练习题
### 练习1
从键盘接受输入，当输入的值为大于50，则退出，小于50则一直接收输入，例如：
请输入一个数：30
请输入一个数：50
结束

<details>
    <summary style="color:#00F"> 查看答案</summary>
    <pre><code> 
    def func():
        while True:
            num = int(input("please input a num: "))
            if num > 50:
                print("End")
                break
    func()
    </code></pre>
</details>

### 练习2
从键盘接收一个输入，输入成绩，当输入的成绩在60以下时，打印不及格，60-79打印及格，80及以上打印优秀
循环输入，当成绩为优秀时结束
<details>
    <summary style="color:#00F">查看答案</summary>
    <pre><code> 
    def func():
        while True:
            score = int(input("请输入你的成绩: "))
            if score < 60:
                print("不及格")
            elif 60 <= score <= 79:
                print("及格")
            else:
                print("优秀")
                break
    func()
    </code></pre>
</details>

### 练习3
一个自然数与3的和是5的倍数,与3的差是6的倍数,这个自然数最小是几?
<details>
    <summary style="color:#00F">查看答案</summary>
    <pre><code> 
    def func():
        for num in range(100):
            if (num + 3) % 5 ==0 and (num - 3) % 6 ==0:
                print(num)
                break
    func()
    </code></pre>
</details>

### 练习4
草莓15元一斤，苹果3元一斤，香蕉2元一斤，刚好花完200元，每种至少有一个/斤，有多少种可能，并列举出来。
<details>
    <summary style="color:#00F">查看答案</summary>
    <pre><code> 
    def func():
        berry = 15  # 草莓价格
        apple = 3   # 苹果价格
        banana = 2  # 香蕉价格
        total = 0   # 有多少种可能
        for berry_num in range(1, 100):
            for apple_num in range(1, 100):
                for banana_num in range(1, 100):
                    if berry_num*berry + apple_num*apple + banana_num*banana == 200:
                        total += 1
        return total
    print(func())
    </code></pre>
</details>

### 练习5
打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
<details>
    <summary style="color:#00F">查看答案</summary>
    <pre><code> 
    def func():
        total = 0
        for num in range(100, 1000):
            a = int(str(num)[0])
            b = int(str(num)[1])
            c = int(str(num)[2])
            if a**3 + b**3 + c**3 == num:
                print(num)
                total += 1
        return total
    print(func())
    </code></pre>
</details>

### 练习6
实现登录，账号名为admin，密码123，则提示“登录成功”，如果账号或者密码错误，则提示“账号名或密码错误”并允许重新输入用户名和密码，如果3次登录失败，则提示“登录失败”并退出程序。
<details>
    <summary style="color:#00F">查看答案</summary>
    <pre><code> 
	def login():
        err_num = 0
        username = "admin"
        password = "123"
        while True:
            username_input = input("please input your username: ")
            password_input = input("please input your password: ")
            if username_input == username and password == password_input:
                print("登录成功")
                break
            err_num += 1
            if err_num == 3:
                print("登录失败，退出程序")
                break
            print("账号或密码错误，请重新输入")
	login()
    </code></pre>
</details>

### 练习7
编写输入任意一张银行卡号，输出银行卡号的前6位和后4位，剩下的所有数字用星号（*）表示
     如：card("5189301239921331") -> 518930**************1331

<details>
    <summary style="color:#00F">查看答案</summary>
    <pre><code> 
	def bankcard():
        cardnum = input("请输入银行卡号： ")
        return cardnum[:6]+(len(cardnum)-10)*"*"+cardnum[-4:]
    print(bankcard())
    </code></pre>
</details>

### 练习8
有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？
<details>
    <summary style="color:#00F">查看答案</summary>
    <pre><code> 
	def nums():
        return 4*3*2
    print(nums())
    </code></pre>
</details>

### 练习9
一些四位数,百位数字都是3,十位数字都是6,并且它们既能被2整除,又能被 3整除,求这样的四位数中最大的和最小的两数各是几?
<details>
    <summary style="color:#00F">查看答案</summary>
    <pre><code> 
	def nums():
        li = []
        for i in range(1360, 9370):
            if i % 2 == 0 and i % 3 == 0:
                li.append(i)
        return min(li), max(li)
    print(nums())
    </code></pre>
</details>

### 练习10
有这样一个list["a","b","c",1,2,3]，生成一个字典，将字符作为字典的key，数字作为字典的value。结果{'a': 1, 'b': 2, 'c': 3}
<details>
    <summary style="color:#00F">查看答案</summary>
    <pre><code> 
	def nums():
        li = ["a","b","c",1,2,3]
        key = li[:3]
        value = li[-3:]
        new_dict = dict(zip(key,value))
        return new_dict
    print(nums())
    </code></pre>
</details>

### 练习11
有一个列表['a','b','c','a','e','a']， 使用for循环统计a出现的次数，并删除其中的所有a元素
<details>
    <summary style="color:#00F">查看答案</summary>
    <pre><code> 
	def remove_a():
        li = ['a','b','c','a','e','a']
        total = 0
        for i in li:
            if i == "a":
                li.remove("a")
                total += 1
        return total, li
    print(remove_a())
    </code></pre>
</details>

## selenium基础

### 浏览器相关操作
    创建浏览器对象　　  driver = webdriver.Chrome()
    窗口最大化　　　　  maximize_window()
    获取浏览器尺寸　　  get_window_size()
    设置浏览器尺寸　　  set_window_size()
    获取浏览器位置　　  get_window_position()
    设置浏览器位置　　  set_window_position(x,y)
    关闭当前标签/窗口　 close()
    关闭所有标签/窗口 　quit()
### 页面相关操作
    请求某个url　　　　　 driver.get(url)
    刷新页面操作　　　　　	refresh()
    回退到之前的页面　　　 back()
    前进到之后的页面　　　 forward()
    获取当前访问页面url　　current_url
    获取当前浏览器标题　　 title
    保存图片　　　　　　　 get_screenshot_as_png()/get_screenshot_as_file(file)
    网页源码　　　　　　　 page_source

### 页面元素的定位（八种定位方式）
    两种方式都可以，推荐使用第一种
    一、find_element(By.ID, value),需要先引入By类
    from selenium.webdriver.common.by import By
    id定位　　　　　　　
    	driver.find_element(By.ID, value)
    name属性值定位　　 
    	driver.find_element(By.NAME, value)
    类名定位　　　　　  
    	driver.find_element(By.CLASS_NAME, value)
    标签名定位　　　　  
    	driver.find_element(By.TAG_NAME, value)
    XPATH定位             
    	driver.find_element(By.XPATH, value)
    CSSS定位              
    	driver.find_element(By.CSS_SELECTOR, value)
    文本内容(文本完全匹配)      
    	driver.find_element(By.LINK_TEXT, value)
    文本内容(包含文本)          
    	driver.find_element(By.PARTIAL_LINK_TEXT, value)
    二、 find_element_by_id(value)
    链接文本定位　　　  
    	driver.find_element_by_link_text(value)
    部分链接文本　　　  
    	driver.find_element_by_partial_link_text(value)
    xpath路径表达式　　
    	driver.find_element_by_xpath(value)
    css选择器　　　　　
    	driver.find_element_by_css_selector(value)
### 元素的操作

    对元素的相关操作，一般要先获取到元素，再调用相关方法 
    	element = driver.find_element_by_xxx(value)
    点击操作　　　　
    	element.click()
    清空输入框　　　
    	element.clear()
    输入框输入数据　
    	element.send_keys(data)
    获取元素的文本内容　　
    	element.text
    获取属性值(获取element元素的value属性的值)　　
    	element.get_attribute(value)
### 鼠标和键盘操作
    鼠标操作需要导入类，见第一部分，然后创建对象ActionChains(driver)
    鼠标右击
    	el = driver.find_element_by_xxx(value)
    	context_click(el)
    鼠标双击	
    	el = driver.find_element_by_xxx(value)
    	ActionChains(driver).double_click(el).perform()
    鼠标悬停	
    	el = driver.find_element_by_xxx(value)
    	ActionChains(driver).move_to_element(el).perform()
    常用键盘操作
    	send_keys(Keys.BACK_SPACE) 删除键（BackSpace）
    	send_keys(Keys.SPACE) 空格键(Space)
    	send_keys(Keys.TAB) 制表键(Tab)
    	send_keys(Keys.ESCAPE) 回退键（Esc）
    	send_keys(Keys.ENTER) 回车键（Enter）
    	send_keys(Keys.CONTROL,‘a’) 全选（Ctrl+A）
    	send_keys(Keys.CONTROL,‘c’) 复制（Ctrl+C）
    	send_keys(Keys.CONTROL,‘x’) 剪切（Ctrl+X）
    	send_keys(Keys.CONTROL,‘v’) 粘贴（Ctrl+V）

### 弹出框操作
	进入到弹出框中　　driver.switch_to.alert()
	接收警告　　　　　accept()
	关闭警告　　　　　dismiss()
	发送文本到警告框　send_keys(data)

### 下拉框操作
	将定位到的下拉框元素传入Select类中　　
		selobj = Select(element)
	通过索引选择，index 索引从 0 开始　　
		select_by_index()
	通过值选择(option标签的一个属性值)　　
		select_by_value()
	通过文本选择(下拉框的值)　　
		select_by_visible_text()
	查看所有已选　　
		all_selected_options
	查看第一个已选　　
		first_selected_option
	查看是否是多选　　
		is_multiple
	查看选项元素列表　　
		options
	取消选择 　　
		deselect_by_index()/deselect_by_value()/deselect_by_visible_text()

### 滚动条操作
	x为水平拖动距离，y为垂直拖动举例
		js = "window.scrollTo(x,y) " 
		driver.execute_script(js)
	n为从顶部往下移动滚动举例
		js= "var q=document.documentElement.scrollTop=n" 
		driver.execute_script(js)

### cookies操作
	获取所有cookies　　 	get_cookies()
	获取key对应的值　　    get_cookie(key)
	设置cookies		   add_cookie(cookie_dict)
	删除指定名称的cookie　 delete_cookie(name)
	删除所有cookie　　	delete_all_cookies()

### 多标签/多窗口、多表单/多框架切换
	多表单/多框架切换------------------------------------------
	直接使用id值切换进表单 　　
		driver.switch_to.frame(value)
	定位到表单元素，再切换进入
		el = driver.find_element_by_xxx(value)
		driver.switch_to.frame(el)
	跳回最外层的页面　　
		driver.switch_to.default_content()
	跳回上层的页面　　
		driver.switch_to.parent_frame()
	多标签/多窗口之间的切换--------------------------------------
	获取所有窗口的句柄 　　
		handles = driver.window_handlers
	通过窗口的句柄进入的窗口　　
		driver.switch_to.window(handles[n])


- 写一个简单的线性脚本访问百度并验证搜索内容是否和我们输入一致
```python
from selenium import webdriver
driver = webdriver.Chrome()     # 第一步打开浏览器
driver.maximize_window()        # 窗口最大化
driver.get("https://www.baidu.com")     # 打开网址
driver.find_element_by_id("kw").send_keys("selenium")       # 定位到输入框兵输入selenium
driver.find_element_by_id("su").click()         # 定位到搜索按钮并点击
current_url = driver.current_url        # 获取当前url并取个变量名
assert_url = "wd=selenium"
assert assert_url in current_url
print("Pass")
```

- 接下来我们把它封装一下,可以实现简单的数据分离和方法封装(下方的代码区看不到任何的数据)
```python
from selenium import webdriver
url = "https://www.baidu.com"
input_box_loc = "kw"
submit_button_loc = "su"
search_text = "selenium"
assert_url = "wd=selenium"
def browser():
    driver = webdriver.Chrome()  # 第一步打开浏览器
    driver.maximize_window()  # 窗口最大化
    return driver
def open_url(driver, url):
    driver.get(url) 		# 打开网址
def find_element_by_id(driver, loc):
    return driver.find_element_by_id(loc)		# 定位到元素


driver = browser()
open_url(driver, url)
find_element_by_id(driver, input_box_loc).send_keys(search_text)
find_element_by_id(driver, submit_button_loc).click()
current_url = driver.current_url
assert assert_url in current_url
print("Pass")
```



