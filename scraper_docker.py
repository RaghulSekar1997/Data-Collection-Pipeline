from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import uuid
import urllib.request
import pandas as pd
from selenium.webdriver.chrome.options import Options
import sys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.core.utils import ChromeType


class Scraper:

    def load_page(self, url) -> None:

        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        s = ChromiumService(ChromeDriverManager().install())



        self.driver = webdriver.Chrome(service=s,options=options)
        # self.driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()),options=options)

        # self.driver = webdriver.Chrome() 
        self.driver.maximize_window()
        self.driver.get(url)
        time.sleep(3)
        
        self.accept_cookies()

        return None

    def accept_cookies(self) -> None:
        try:
             # This is the id of the frame
            accept_cookies_button = self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div/div/div[2]/div/button[2]/span')

            accept_cookies_button.click()
        except:
            pass

    
    
    def get_links(self) -> list:

        recipes_container = self.driver.find_element(by=By.XPATH, value='/html/body/div[5]/div/form/div/div[4]/div[1]/div[1]/div')
        recipes_list = recipes_container.find_elements(by=By.XPATH, value='./div')
        link_list = []

        for r_property in recipes_list:
            a_tag = r_property.find_element(by=By.TAG_NAME, value='a')
            link = a_tag.get_attribute('href')
            link_list.append(link)
        
        return link_list

    def strn(self) -> str:

        strn = 'You can do it'

        return strn


    def get_recipe_info(self,j) -> dict:

        recipe_name_l = '//*[@id="__next"]/div[3]/main/div/section/div/div[3]/div[1]/h1'
        Rating_l = '//*[@id="__next"]/div[3]/main/div/section/div/div[3]/div[3]/div/a[1]/div/div/span[1]'
        Number_of_Rating_l = '//*[@id="__next"]/div[3]/main/div/section/div/div[3]/div[3]/div/a[1]/div/div/span[2]'
        Prep_time_l = '//*[@id="__next"]/div[3]/main/div/section/div/div[3]/ul[1]/li[1]/div/div[2]/ul/li[1]/span[2]/time'
        Cook_time_l = '//*[@id="__next"]/div[3]/main/div/section/div/div[3]/ul[1]/li[1]/div/div[2]/ul/li[2]/span[2]/time'
        Making_l = '//*[@id="__next"]/div[3]/main/div/section/div/div[3]/ul[1]/li[2]/div/div[2]'
        Cook_Name_l = '//*[@id="__next"]/div[3]/main/div/section/div/div[3]/div[2]/div/ul/li/a'
        Recipe_des_l = '//*[@id="__next"]/div[3]/main/div/section/div/div[3]/div[4]/p'
        Image_Url_l = '//*[@id="__next"]/div[3]/main/div/section/div/div[1]/div/div/picture/img'
        kcal_l = '//*[@id="__next"]/div[3]/main/div/section/div/div[3]/table/tbody[1]/tr[1]/td[3]'
        fat_l = '//*[@id="__next"]/div[3]/main/div/section/div/div[3]/table/tbody[1]/tr[2]/td[3]'
        saturates_l = '//*[@id="__next"]/div[3]/main/div/section/div/div[3]/table/tbody[1]/tr[3]/td[3]'
        carbs_l = '//*[@id="__next"]/div[3]/main/div/section/div/div[3]/table/tbody[1]/tr[4]/td[3]'
        sugars_l = '//*[@id="__next"]/div[3]/main/div/section/div/div[3]/table/tbody[2]/tr[1]/td[3]'
        fiber_l = '//*[@id="__next"]/div[3]/main/div/section/div/div[3]/table/tbody[2]/tr[2]/td[3]'
        protein = '//*[@id="__next"]/div[3]/main/div/section/div/div[3]/table/tbody[2]/tr[3]/td[3]'
        salt = '//*[@id="__next"]/div[3]/main/div/section/div/div[3]/table/tbody[2]/tr[4]/td[3]'

        '''data = {'Recipe_Name': [], 'Rating': [], 'Number_of_Rating':[],'Prep_time': [], 'Cook_time': [],
                    'Making': [], 'Cook_Name': [], 'Recipe_des': [], 'Image_ULR': [], 'kcal': [],
                    'fat': [], 'saturates': [], 'carbs':[], 'sugars':[], 'fibre':[], 'protein':[],
                    'salt': []}'''

        if j == 1:
            data = {'Recipe_Name': [self.__get_text(recipe_name_l)], 'Rating': [self.__get_text(Rating_l)], 'Number_of_Rating': [self.__get_text(Number_of_Rating_l)],'Prep_time': [self.__get_text(Prep_time_l)], 'Cook_time': [self.__get_text(Cook_time_l)],
                    'Making': [self.__get_text(Making_l)], 'Cook_Name': [self.__get_text(Cook_Name_l)], 'Recipe_des': [self.__get_text(Recipe_des_l)], 'Image_Url': [self.__get_img_url(Image_Url_l)], 'kcal': [self.__get_text(kcal_l)],
                    'fat': [self.__get_text(fat_l)], 'saturates': [self.__get_text(saturates_l)], 'carbs':[self.__get_text(carbs_l)], 'sugars':[self.__get_text(sugars_l)], 'fibre':[self.__get_text(fiber_l)], 'protein':[self.__get_text(protein)],
                    'salt': [self.__get_text(salt)]}
            
        else:
            data = {'Recipe_Name': self.__get_text(recipe_name_l), 'Rating': self.__get_text(Rating_l), 'Number_of_Rating': self.__get_text(Number_of_Rating_l),'Prep_time': self.__get_text(Prep_time_l), 'Cook_time': self.__get_text(Cook_time_l),
                    'Making': self.__get_text(Making_l), 'Cook_Name': self.__get_text(Cook_Name_l), 'Recipe_des': self.__get_text(Recipe_des_l), 'Image_Url': self.__get_img_url(Image_Url_l), 'kcal': self.__get_text(kcal_l),
                    'fat': self.__get_text(fat_l), 'saturates': self.__get_text(saturates_l), 'carbs':self.__get_text(carbs_l), 'sugars':self.__get_text(sugars_l), 'fibre':self.__get_text(fiber_l), 'protein':self.__get_text(protein),
                    'salt': self.__get_text(salt)}

        if data['kcal'] == 'N/A':
            kcal_l = '//*[@id="__next"]/div[3]/main/div/section/div/div[3]/table/tbody[1]/tr[1]/td[2]'
            fat_l = '//*[@id="__next"]/div[3]/main/div/section/div/div[3]/table/tbody[1]/tr[2]/td[2]'
            saturates_l = '//*[@id="__next"]/div[3]/main/div/section/div/div[3]/table/tbody[1]/tr[3]/td[2]'
            carbs_l = '//*[@id="__next"]/div[3]/main/div/section/div/div[3]/table/tbody[1]/tr[4]/td[2]'
            sugars_l = '//*[@id="__next"]/div[3]/main/div/section/div/div[3]/table/tbody[2]/tr[1]/td[2]'
            fiber_l = '//*[@id="__next"]/div[3]/main/div/section/div/div[3]/table/tbody[2]/tr[2]/td[2]'
            protein = '//*[@id="__next"]/div[3]/main/div/section/div/div[3]/table/tbody[2]/tr[3]/td[2]'
            salt = '//*[@id="__next"]/div[3]/main/div/section/div/div[3]/table/tbody[2]/tr[4]/td[2]'

            data = {}
            if j == 1:
                data = {'Recipe_Name': [self.__get_text(recipe_name_l)], 'Rating': [self.__get_text(Rating_l)], 'Number_of_Rating': [self.__get_text(Number_of_Rating_l)],'Prep_time': [self.__get_text(Prep_time_l)], 'Cook_time': [self.__get_text(Cook_time_l)],
                    'Making': [self.__get_text(Making_l)], 'Cook_Name': [self.__get_text(Cook_Name_l)], 'Recipe_des': [self.__get_text(Recipe_des_l)], 'Image_Url': [self.__get_img_url(Image_Url_l)], 'kcal': [self.__get_text(kcal_l)],
                    'fat': [self.__get_text(fat_l)], 'saturates': [self.__get_text(saturates_l)], 'carbs':[self.__get_text(carbs_l)], 'sugars':[self.__get_text(sugars_l)], 'fibre':[self.__get_text(fiber_l)], 'protein':[self.__get_text(protein)],
                    'salt': [self.__get_text(salt)]}
            else:
                data = {'Recipe_Name': self.__get_text(recipe_name_l), 'Rating': self.__get_text(Rating_l), 'Number_of_Rating': self.__get_text(Number_of_Rating_l),'Prep_time': self.__get_text(Prep_time_l), 'Cook_time': self.__get_text(Cook_time_l),
                    'Making': self.__get_text(Making_l), 'Cook_Name': self.__get_text(Cook_Name_l), 'Recipe_des': self.__get_text(Recipe_des_l), 'Image_Url': self.__get_img_url(Image_Url_l), 'kcal': self.__get_text(kcal_l),
                    'fat': self.__get_text(fat_l), 'saturates': self.__get_text(saturates_l), 'carbs':self.__get_text(carbs_l), 'sugars':self.__get_text(sugars_l), 'fibre':self.__get_text(fiber_l), 'protein':self.__get_text(protein),
                    'salt': self.__get_text(salt)}
        
        return data


    def __get_text(self, locator) -> str:
        
        try:
            text = self.driver.find_element(by=By.XPATH, value = locator).text
        except:
            text = 'N/A'
            

        return text


    def __get_img_url(self, locator) -> str:
        
        try:
            img_url = self.driver.find_element(by=By.XPATH, value=locator)
            url = img_url.get_attribute('src')
        except:
            url = 'N/A'

        return url

    def merge_recipe_details(self,ard,rd) -> dict:

        ard['recipe_url'].append(rd['recipe_url'])
        ard['unique_ID'].append(rd['unique_ID'])

        ard['Recipe_Name'].append(rd['Recipe_Name'])
        ard['Rating'].append(rd['Rating'])
        ard['Number_of_Rating'].append(rd['Number_of_Rating'])
        ard['Prep_time'].append(rd['Prep_time'])
        ard['Cook_time'].append(rd['Cook_time'])

        ard['Making'].append(rd['Making'])
        ard['Cook_Name'].append(rd['Cook_Name'])
        ard['Recipe_des'].append(rd['Recipe_des'])
        ard['Image_Url'].append(rd['Image_Url'])
        ard['kcal'].append(rd['kcal'])

        ard['fat'].append(rd['fat'])
        ard['saturates'].append(rd['saturates'])
        ard['carbs'].append(rd['carbs'])
        ard['sugars'].append(rd['sugars'])
        ard['fibre'].append(rd['fibre'])
        ard['protein'].append(rd['protein'])
        ard['salt'].append(rd['salt'])
        ard['recipe_image'].append(rd['recipe_image'])

        return ard

    def get_image(self, image_url) -> str:
        
        try:
            uid = image_url.split('?')[0]
            uid = uid.split('/')[-1]
            temp_image_location = '/tmp/' + uid
            uid = 'image/' + uid
            
            urllib.request.urlretrieve(image_url, temp_image_location)

            # s3_url = self.aws.upload_file_method(temp_image_location, uid)
            
            return temp_image_location

        except:
            pass
    
    


#Success on Collecting URL and Collecting Data - Running in headless mode

if __name__ == "__main__":
    scraper = Scraper()
    scraper.load_page('https://www.bbcgoodfood.com/search/recipes/page/2/?q=Easy+dinner+recipes&sort=-relevance')


    user_choice = input("Enter number of pages : ")

    user_choice = int(user_choice)
    if user_choice < 200:
        number_of_page = user_choice
    else: 
        sys.exit('Enter value below 200')

    user_choice = input("Enter number of recipes to collect : ")

    user_choice = int(user_choice)
    if user_choice < (number_of_page * 24):
        number_of_recipes = user_choice
    else: 
        sys.exit('Enter value below',number_of_page*24)
        
    big_list = []
    for i in range(number_of_page):
        try:
        
            big_list.extend(scraper.get_links())
            scraper.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(2)
            next_button = scraper.driver.find_element(by=By.XPATH, value='/html/body/div[5]/div/form/div/div[4]/div[1]/div[2]/div/ul/li[7]/a/span')
            next_button.click()
        except:
            pass
    scraper.driver.close()

    i = 0

    all_recipe_details = {}
    
    for link in big_list:
        
        i = i + 1
        scraper.load_page(link)
        recipe_details = {'recipe_url': [], 'unique_ID': []}

        if i == 1:
            recipe_details['recipe_url'] = [link]
            recipe_details['unique_ID'] = [uuid.uuid4().hex]
        else:
            recipe_details['recipe_url'] = link
            recipe_details['unique_ID'] = uuid.uuid4().hex

        recipe_details = {**recipe_details, **scraper.get_recipe_info(i)}
        if i == 1:
            recipe_details['recipe_image'] = [scraper.get_image(recipe_details['Image_Url'][0])]
            all_recipe_details = recipe_details
        else:
            recipe_details['recipe_image'] = scraper.get_image(recipe_details['Image_Url'])
            all_recipe_details = scraper.merge_recipe_details(all_recipe_details,recipe_details)
            
        if i == number_of_recipes:
            break

        pass 
    
    all_recipe_details_df = pd.DataFrame.from_dict(all_recipe_details)
    all_recipe_details_df.to_csv('recipe_details.csv')
    print('Data collected successful')
   
   

