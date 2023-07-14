import selenium,time,os,wget
from selenium import webdriver
from selenium.webdriver.common import action_chains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(options=chrome_options)
print(driver.title)
#ctrl+/ 快速註解
driver.get("https://bts.xuanen.com.tw/ts01.aspx?module=net_booking&files=booking_place&StepFlag=2&PT=1&D=2023/07/21&D2=1")

print("要訂 上午(1) 下午(2) 晚上(3) 輸入數字 : ")
Your_account=input()
if Your_account=="1":
    driver.get("https://bts.xuanen.com.tw/ts01.aspx?module=net_booking&files=booking_place&StepFlag=2&PT=1&D=2023/07/21&D2=1")
    print("你選 上午")
elif Your_account=="2":
    driver.get("https://bts.xuanen.com.tw/ts01.aspx?module=net_booking&files=booking_place&StepFlag=2&PT=1&D=2023/07/21&D2=2")
    print("你選 下午")
elif Your_account=="3":
    driver.get("https://bts.xuanen.com.tw/ts01.aspx?module=net_booking&files=booking_place&StepFlag=2&PT=1&D=2023/07/21&D2=3")
    print("你選 晚上")

if Your_account=="1":
    print("訂的時段 06-07(1) 07-08(2) 08-09(3) 09-10(4) 10-11(5) 11-12(6) : ")
    Your_password=input()
    if Your_password=="1":
        print("你選 06-07")
        print("訂的場地 羽(1) 羽(2) 羽(3) 羽(4) 羽(5) 羽(6) : ")
        place=input()
        print("你選 羽"+place)
    elif Your_password=="2":
        print("你選 07-08")
        print("訂的場地 羽(1) 羽(2) 羽(3) 羽(4) 羽(5) 羽(6) : ")    
        place=input()
        print("你選 羽"+place)
    elif Your_password=="3":
        print("你選 08-09")
        print("訂的場地 羽(1) 羽(2) 羽(3) 羽(4) 羽(5) 羽(6) : ") 
        place=input()   
        print("你選 羽"+place)
    elif Your_password=="4":
        print("你選 09-10")
        print("訂的場地 羽(1) 羽(2) 羽(3) 羽(4) 羽(5) 羽(6) : ")    
        place=input()   
        print("你選 羽"+place)
    elif Your_password=="5":
        print("你選 10-11")
        print("訂的場地 羽(1) 羽(2) 羽(3) 羽(4) 羽(5) 羽(6) : ")    
        place=input()   
        print("你選 羽"+place)
    elif Your_password=="6":
        print("你選 11-12")
        print("訂的場地 羽(1) 羽(2) 羽(3) 羽(4) 羽(5) 羽(6) : ") 
        place=input()   
        print("你選 羽"+place)
elif Your_account=="2":
    print("訂的時段 12-13(1) 13-14(2) 14-15(3) 15-16(4) 16-17(5) 17-18(6) : ")
    Your_password=input()
    if Your_password=="1":
        print("你選 12-13")
        print("訂的場地 羽(1) 羽(2) 羽(3) 羽(4) 羽(5) 羽(6) : ")
        place=input()
        print("你選 羽"+place)
    elif Your_password=="2":
        print("你選 13-14")
        print("訂的場地 羽(1) 羽(2) 羽(3) 羽(4) 羽(5) 羽(6) : ")    
        place=input()
        print("你選 羽"+place)
    elif Your_password=="3":
        print("你選 14-15")
        print("訂的場地 羽(1) 羽(2) 羽(3) 羽(4) 羽(5) 羽(6) : ") 
        place=input()   
        print("你選 羽"+place)
    elif Your_password=="4":
        print("你選 15-16")
        print("訂的場地 羽(1) 羽(2) 羽(3) 羽(4) 羽(5) 羽(6) : ")    
        place=input()   
        print("你選 羽"+place)
    elif Your_password=="5":
        print("你選 16-17")
        print("訂的場地 羽(1) 羽(2) 羽(3) 羽(4) 羽(5) 羽(6) : ")    
        place=input()   
        print("你選 羽"+place)
    elif Your_password=="6":
        print("你選 17-18")
        print("訂的場地 羽(1) 羽(2) 羽(3) 羽(4) 羽(5) 羽(6) : ") 
        place=input()   
        print("你選 羽"+place)
elif Your_account=="3":
    print("訂的時段 18-19  (1) 19-20(2) 20-21(3) 21-22(4)  : ")
    Your_password=input()
    if Your_password=="1":
        print("你選 18-19")
        print("訂的場地 羽(1) 羽(2) 羽(3) 羽(4) 羽(5) 羽(6) : ")
        place=input()
        print("你選 羽"+place)
    elif Your_password=="2":
        print("你選 19-20")
        print("訂的場地 羽(1) 羽(2) 羽(3) 羽(4) 羽(5) 羽(6) : ")    
        place=input()
        print("你選 羽"+place)
    elif Your_password=="3":
        print("你選 20-21")
        print("訂的場地 羽(1) 羽(2) 羽(3) 羽(4) 羽(5) 羽(6) : ") 
        place=input()   
        print("你選 羽"+place)
    elif Your_password=="4":
        print("你選 21-22")
        print("訂的場地 羽(1) 羽(2) 羽(3) 羽(4) 羽(5) 羽(6) : ")    
        place=input()   
        print("你選 羽"+place)

print("時間"+Your_password)
print("場地"+place)
def click_password_and_place(a, place):
    if a=="1":
            if place=="1":
                login=driver.find_element("xpath",'//*[@id="ContentPlaceHolder1_Step2_data"]/table/tbody/tr[2]/td[4]/img')
            elif place=="2":
                login=driver.find_element("xpath",'//*[@id="ContentPlaceHolder1_Step2_data"]/table/tbody/tr[3]/td[3]/img')    
            elif place=="3":
                login=driver.find_element("xpath",'//*[@id="ContentPlaceHolder1_Step2_data"]/table/tbody/tr[4]/td[3]/img')
            elif place=="4":
                login=driver.find_element("xpath",'//*[@id="ContentPlaceHolder1_Step2_data"]/table/tbody/tr[5]/td[3]/img')
            elif place=="5":
                login=driver.find_element("xpath",'//*[@id="ContentPlaceHolder1_Step2_data"]/table/tbody/tr[6]/td[3]/img')
            elif place=="6":
                login=driver.find_element("xpath",'//*[@id="ContentPlaceHolder1_Step2_data"]/table/tbody/tr[7]/td[3]/img')
    elif a=="2":
            if place=="1":
                login=driver.find_element("xpath",'//*[@id="ContentPlaceHolder1_Step2_data"]/table/tbody/tr[8]/td[4]/img')
            elif place=="2":
                login=driver.find_element("xpath",'//*[@id="ContentPlaceHolder1_Step2_data"]/table/tbody/tr[9]/td[3]/img')    
            elif place=="3":
                login=driver.find_element("xpath",'//*[@id="ContentPlaceHolder1_Step2_data"]/table/tbody/tr[10]/td[3]/img')
            elif place=="4":
                login=driver.find_element("xpath",'//*[@id="ContentPlaceHolder1_Step2_data"]/table/tbody/tr[11]/td[3]/img')
            elif place=="5":
                login=driver.find_element("xpath",'//*[@id="ContentPlaceHolder1_Step2_data"]/table/tbody/tr[12]/td[3]/img')
            elif place=="6":
                login=driver.find_element("xpath",'//*[@id="ContentPlaceHolder1_Step2_data"]/table/tbody/tr[13]/td[3]/img')
    elif a=="3":
            if place=="1":
                login=driver.find_element("xpath",'//*[@id="ContentPlaceHolder1_Step2_data"]/table/tbody/tr[14]/td[4]/img')
            elif place=="2":
                login=driver.find_element("xpath",'//*[@id="ContentPlaceHolder1_Step2_data"]/table/tbody/tr[15]/td[3]/img')    
            elif place=="3":
                login=driver.find_element("xpath",'//*[@id="ContentPlaceHolder1_Step2_data"]/table/tbody/tr[16]/td[3]/img')
            elif place=="4":
                login=driver.find_element("xpath",'//*[@id="ContentPlaceHolder1_Step2_data"]/table/tbody/tr[17]/td[3]/img')
            elif place=="5":
                login=driver.find_element("xpath",'//*[@id="ContentPlaceHolder1_Step2_data"]/table/tbody/tr[18]/td[3]/img')
            elif place=="6":
                login=driver.find_element("xpath",'//*[@id="ContentPlaceHolder1_Step2_data"]/table/tbody/tr[19]/td[3]/img')
    elif a=="4":
            if place=="1":
                login=driver.find_element("xpath",'//*[@id="ContentPlaceHolder1_Step2_data"]/table/tbody/tr[20]/td[4]/img')
            elif place=="2":
                login=driver.find_element("xpath",'//*[@id="ContentPlaceHolder1_Step2_data"]/table/tbody/tr[21]/td[3]/img')    
            elif place=="3":
                login=driver.find_element("xpath",'//*[@id="ContentPlaceHolder1_Step2_data"]/table/tbody/tr[22]/td[3]/img')
            elif place=="4":
                login=driver.find_element("xpath",'//*[@id="ContentPlaceHolder1_Step2_data"]/table/tbody/tr[23]/td[3]/img')
            elif place=="5":
                login=driver.find_element("xpath",'//*[@id="ContentPlaceHolder1_Step2_data"]/table/tbody/tr[24]/td[3]/img')
            elif place=="6":
                login=driver.find_element("xpath",'//*[@id="ContentPlaceHolder1_Step2_data"]/table/tbody/tr[25]/td[3]/img')
    elif a=="5":
            if place=="1":
                login=driver.find_element("xpath",'//*[@id="ContentPlaceHolder1_Step2_data"]/table/tbody/tr[26]/td[4]/img')
            elif place=="2":
                login=driver.find_element("xpath",'//*[@id="ContentPlaceHolder1_Step2_data"]/table/tbody/tr[27]/td[3]/img')    
            elif place=="3":
                login=driver.find_element("xpath",'//*[@id="ContentPlaceHolder1_Step2_data"]/table/tbody/tr[28]/td[3]/img')
            elif place=="4":
                login=driver.find_element("xpath",'//*[@id="ContentPlaceHolder1_Step2_data"]/table/tbody/tr[29]/td[3]/img')
            elif place=="5":
                login=driver.find_element("xpath",'//*[@id="ContentPlaceHolder1_Step2_data"]/table/tbody/tr[30]/td[3]/img')
            elif place=="6":
                login=driver.find_element("xpath",'//*[@id="ContentPlaceHolder1_Step2_data"]/table/tbody/tr[31]/td[3]/img')
    elif a=="6":
            if place=="1":
                login=driver.find_element("xpath",'//*[@id="ContentPlaceHolder1_Step2_data"]/table/tbody/tr[32]/td[4]/img')
            elif place=="2":
                login=driver.find_element("xpath",'//*[@id="ContentPlaceHolder1_Step2_data"]/table/tbody/tr[33]/td[3]/img')    
            elif place=="3":
                login=driver.find_element("xpath",'//*[@id="ContentPlaceHolder1_Step2_data"]/table/tbody/tr[34]/td[3]/img')
            elif place=="4":
                login=driver.find_element("xpath",'//*[@id="ContentPlaceHolder1_Step2_data"]/table/tbody/tr[35]/td[3]/img')
            elif place=="5":
                login=driver.find_element("xpath",'//*[@id="ContentPlaceHolder1_Step2_data"]/table/tbody/tr[36]/td[3]/img')
            elif place=="6":
                login=driver.find_element("xpath",'//*[@id="ContentPlaceHolder1_Step2_data"]/table/tbody/tr[37]/td[3]/img')
    return login

login = click_password_and_place(Your_password, place)

actions = ActionChains(driver)
actions.click(login).perform()
alertt = driver.switch_to.alert
print(alertt.text)

while "是否確定預約" not in alertt.text:
    num=int(place)
    numpass=int(Your_password)

    if Your_account!="3":
        for i in range(numpass,7):
            Your_password=str(i)
            for j in range(num,7):
                intstr=str(j)
                if alertt.text=="已被預約！":
                    print("已被預約！"+intstr)
                    print("時段"+Your_password)
                    driver.switch_to.alert.accept()
                elif alertt.text.find("是否確定預約"):
                    break
                login = click_password_and_place(Your_password, intstr)
                actions = ActionChains(driver)
                actions.click(login).perform()
                alertt = driver.switch_to.alert
                
    if Your_account=="3":
        num=int(place)
        numpass=int(Your_password)
        for i in range(numpass,5):
            Your_password=str(i)
            for j in range(num,7):
                intstr=str(j)
                if alertt.text=="已被預約！":
                    print("已被預約！"+intstr)
                    print("時段"+Your_password)
                    driver.switch_to.alert.accept()
                elif alertt.text.find("是否確定預約"):
                    break
                login = click_password_and_place(Your_password, intstr)
                actions = ActionChains(driver)
                actions.click(login).perform()
                
               
    

if  alertt.text.find("是否確定預約"):               
    print("預約(1) 不預約(2)")
    yes=input()
    if yes=="1":
        driver.switch_to.alert.accept()
    else :
        driver.switch_to.alert.dismiss()



