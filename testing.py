from selenium import webdriver
from selenium.webdriver.common.by import By
import csv 
import getpass 
import tkinter

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("file:///C:/Users/Sarath/Documents/College/Academics/Theory/Software/DA-3/website.html")

root=tkinter.Tk()
root.title("Testing")

def openingpage():
    root.geometry("200x150")
    label1 = tkinter.Label(root, text="Hi, " + getpass.getuser(), font=("Helvetica", 16))
    label1.pack(pady=20)
    button1 = tkinter.Button(root, text="Continue", font=("Helvetica", 12), command=nextpagecmd)
    button1.pack(pady=10)


def testresultspage(unit_result):
    for child in root.winfo_children():
        child.destroy()
        
    root.geometry("400x300")
    title_label = tkinter.Label(root, text="Test Results", font=("Helvetica", 20, "bold"))
    title_label.pack(pady=20)

    for name, result in unit_result.items():
        fg_color = 'green' if result == 'Passed' else 'red'
        test_label = tkinter.Label(root, text=f'{name}: {result}', fg=fg_color, font=("Helvetica", 14))
        test_label.pack(pady=5)

    close_button = tkinter.Button(root, text='Close', font=("Helvetica", 12), command=root.destroy)
    close_button.pack(pady=20)
    
def nextpagecmd():
    cmd1=testdata()
    testresultspage(cmd1)
    close()

def write_data():
    fr=open('Test_values.csv','w')
    write=csv.writer(fr)
    write.writerow(['name','email','phone','address','card','expiry','cvv','product','quantity'])
    
def read_data():
    fr=open('Test_values.csv','r')
    reader=csv.reader(fr)
    testvalues=[]
    for row in reader:
        row_data=[]
        for col in row:
            row_data.append(col)
        testvalues.append(row_data)
    fr.close()
    print(testvalues)
    return testvalues
    
   
def testdata(): 
    
    testdata=read_data()
    unit_test=[]
    result={}
    testid=['name','email','phone','address','card','expiry','cvv','product','quantity']
    for i in range(1,len(testdata)):
        for j in range(len(testid)):
            element=driver.find_element(By.ID,testid[j])
            element.send_keys(testdata[i][j])
        submit=driver.find_element(By.XPATH,'/html/body/form/input[9]')
        submit.click()
        try:
            alert = driver.switch_to.alert
            unit_test.append("Failed")
            alert.accept()

        except:
            unit_test.append("Passed")
            pass
        for j in range(len(testid)):
            element=driver.find_element(By.ID,testid[j])
            element.clear()
    
    for i in range(len(unit_test)):
        text="Test "+str(i+1)
        result[text]=unit_test[i]
    close()
    return result
     
def close():
    driver.close()
    
openingpage()
root.mainloop()
#write_data()
#read_data()
#testdata()
