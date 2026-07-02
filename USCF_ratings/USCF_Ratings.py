from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time, pandas as pd
options = Options()
options.add_argument("--headless=new")

df_data={'Full Name': [],
         'Regular Rating':[],
         'Blitz Rating':[],
         'Improvement': []}
browser = webdriver.Chrome(options=options)

def get_rating(id):
    global df_data, browser
    browser.get(f'https://ratings.uschess.org/player/{id}')
    time.sleep(1)
    rating_tables = browser.find_elements(By.CSS_SELECTOR, '.flex.items-center.gap-1.text-lg')
    reg_rating = rating_tables[0].text.split('/')[0].strip()
    blitz_rating = rating_tables[2].text.split('/')[0].strip()
    first_name = browser.find_elements(By.CSS_SELECTOR, '.font-regular.overflow-hidden.text-ellipsis.whitespace-nowrap.min-w-0.shrink')[1].text.upper()
    last_name = browser.find_elements(By.CSS_SELECTOR, '.font-semibold.shrink-0')[1].text
    
    button = browser.find_element(By.XPATH, '//*[@id="radix-:rl:-trigger-rating-table"]')
    button.click()
    past_rating = browser.find_element(By.XPATH, '//*[@id="radix-:rl:-content-rating-table"]/div/div/div/div[5]/table/tbody/tr[2]/td[2]').text
    df_data['Full Name'].append(first_name + ' ' + last_name)
    df_data['Regular Rating'].append(int(reg_rating))
    df_data['Blitz Rating'].append(blitz_rating)
    df_data['Improvement'].append(int(reg_rating)-int(past_rating))


id_list = input("List of IDs seperated by spaces: ").split()
for id in id_list:
    get_rating(id)
    print("Data from ID", id,"collected")

df = pd.DataFrame(df_data)

top_reg_rating_df = df.sort_values('Regular Rating', ascending=False).iloc[:, 0:2].set_index('Full Name')
print('\n')
print('Sorted by Regular Rating:')
print(top_reg_rating_df)

top_blitz_rating_df = df.sort_values('Blitz Rating', ascending=False).loc[:, ["Full Name", "Blitz Rating"]].set_index('Full Name')
print('\n')
print('Sorted by Blitz Rating:')
print(top_blitz_rating_df)

top_improvement_df = df.sort_values('Improvement', ascending=False).loc[:, ["Full Name", "Improvement"]].set_index('Full Name')
print('\n')
print('Sorted by Most Improvement:')
print(top_improvement_df)