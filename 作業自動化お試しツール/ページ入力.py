from selenium import webdriver
import os
get_element=["user[email]","user[password]","user[profile_attributes][name_last]","user[profile_attributes][name_first]","user[profile_attributes][kana_last]","user[profile_attributes][kana_first]"]
checkbox_output=["メールアドレス","pathword","性","名","せい（ふりがな）","めい（ふりがな）"]
d=os.getcwd()+"\msedgedriver.exe"
driver = webdriver.Edge(executable_path=d)
driver.get('https://omakase.in/users/sign_up')
for i in range(6):
 search_box = driver.find_element_by_name(get_element[i])
 search_box.send_keys(checkbox_output[i])

