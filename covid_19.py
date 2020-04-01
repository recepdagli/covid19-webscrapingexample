from selenium import webdriver
import xlsxwriter
import matplotlib.pyplot as plt

import time


driver = webdriver.Chrome()

driver.get('https://gisanddata.maps.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6')

time.sleep(7)

elems_contry = driver.find_elements_by_xpath('/html/body/div/div/div[2]/div/div/div/margin-container/full-container/div[2]/margin-container/full-container/div/div[2]/nav/span')
                                              
for i in elems_contry:
    i.click()
    name = i.find_element_by_xpath('div/div/h5/span[3]').text
    print(name)

    time.sleep(5)

    elems_data1 = driver.find_element_by_xpath('//*[@id="ember118"]/div/div')

    elems_data = elems_data1.find_elements_by_tag_name('circle')

    data_arr = []
    data_date_arr = []
    date_day_count = 1
    for j in elems_data:
        data = j.get_attribute('aria-label')
        spl_data = data.split(' ')
        print(spl_data[-1].replace(',',''))
        data_arr.append(int(spl_data[-1].replace(',','')))
        data_date_arr.append(date_day_count)
        date_day_count += 1

    plt.plot(data_date_arr,data_arr)
    plt.xlabel("day")
    plt.ylabel("confirmed")
    plt.savefig("data/"+name.replace('*','')+".svg",format="svg")
    #plt.show()
    plt.close()

