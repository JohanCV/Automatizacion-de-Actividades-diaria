import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#variables gmail
gmail = "nahoj1992@gmail.com"
contrasena = "dragonball2010"
gmailAulavirtual = "jcalderonva@unsa.edu.pe"

#"creamos una instancia de chrome hacia el aulavirtual"
driver = webdriver.Chrome("C:\Python\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe")

#ingreso al gmail
driver.get("https://docs.google.com/spreadsheets/d/1ADLUu_4Jz1OxYdBRcZfBi3lUS0DjK0F_nFE21-NCGBo/edit#gid=986616540")
email = driver.find_element_by_id('identifierId')
email.send_keys(gmail)
driver.find_element_by_id('identifierNext').click()
time.sleep(5)

contra = driver.find_element_by_xpath("//*[@id='password']/div[1]/div/div[1]/input")
contra.send_keys("dragonball2010")
driver.find_element_by_id('passwordNext').click()
time.sleep(5)


#ingreso al aulavirtual
driver.get("http://dutic.unsa.edu.pe/aulavirtual/login/index.php")
#"nos logeamos"
login_form_sesion_dutic = driver.find_element_by_id('login')
username = driver.find_element_by_id('username')
password = driver.find_element_by_id('password')

username.send_keys("dutic")
password.send_keys("Qwert18*")
driver.find_element_by_id("loginbtn").click()
time.sleep(5)

#"adminastracion de usuarios"
driver.get("http://dutic.unsa.edu.pe/aulavirtual/admin/user.php")
driver.find_element_by_class_name("moreless-toggler").click()
email_usuario = driver.find_element_by_id('id_email')
email_usuario.send_keys(gmailAulavirtual)

driver.find_element_by_id("id_addfilter").click()
driver.find_element_by_id("yui_3_17_2_1_1554140446329_524").click()
