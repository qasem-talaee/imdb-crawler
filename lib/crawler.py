from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json

from lib.func import os_rec

class IMDB:
    
    def __init__(self):
        DRIVER_PATH = os_rec.recognize_os()
        options = Options()
        options.headless = True
        options.add_argument("--window-size=1920,1200")
        firefox_profile = webdriver.FirefoxProfile()
        firefox_profile.set_preference('permissions.default.stylesheet', 2)
        firefox_profile.set_preference('permissions.default.image', 2)
        firefox_profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
        self.driver = webdriver.Firefox(executable_path=DRIVER_PATH, options=options, firefox_profile=firefox_profile)
        self.__result = []
    
    def get_id(self, id):
        self.__id = id
        self.driver.get("https://www.imdb.com/title/{id}/".format(id=id))
        self.__get_details()
        self.driver.close()

    def get_list(self, url):
        self.driver.get(url)
        ids = self.driver.find_elements_by_xpath('//div[@class="lister-item mode-advanced"]'
                                                 '//h3[@class="lister-item-header"]'
                                                 '//a')
        ids = list(filter(None, [x.get_attribute('href').split('/')[4] for x in ids]))
        i = 0
        for id in ids:
            if i == 2:
                break
            else:
                self.get_id(id)
            i = i +1
    
    def __get_details(self):
        self.__title = self.__poster = self.__images = self.__year = self.__ages = self.__duration = self.__rate = self.__meta = self.__popularity = self.__genre = self.__director = self.__writers = self.__stars = self.__desc = self.__country = self.__lang = self.__budget = self.__world_sell = None
        try:
            self.__title = self.driver.find_element_by_xpath('//h1[@class="sc-b73cd867-0 eKrKux"][@data-testid="hero-title-block__title"]').text
            sub_title = self.driver.find_elements_by_xpath('//a[@class="ipc-link ipc-link--baseAlt ipc-link--inherit-color sc-8c396aa2-1 WIUyh"]')
            self.__year = sub_title[0].text
            self.__ages = sub_title[1].text
            self.__duration = self.driver.find_elements_by_xpath('//li[@class="ipc-inline-list__item"][@role="presentation"]')[2].text
            self.__rate = self.driver.find_element_by_xpath('//div[@class="sc-7ab21ed2-0 fAePGh"]'
                                                            '//div[@class="sc-7ab21ed2-2 kYEdvH"][@data-testid="hero-rating-bar__aggregate-rating__score"]'
                                                            '//span[@class="sc-7ab21ed2-1 jGRxWM"]').text
            self.__popularity = self.driver.find_element_by_xpath('//div[@class="ipc-button__text"]'
                                                                '//div[@class="sc-edc76a2-0 bZeUlh"][@data-testid="hero-rating-bar__popularity__up"]'
                                                                '//div[@class="sc-edc76a2-1 gopMqI"][@data-testid="hero-rating-bar__popularity__score"]').text
            self.__meta = self.driver.find_element_by_xpath('//div[@class="sc-10602b09-5 kBrxsq"]'
                                                            '//ul[@class="ipc-inline-list sc-124be030-0 ddUaJu baseAlt"][@data-testid="reviewContent-all-reviews"]'
                                                            '//span[@class="score-meta"][@style="background-color:#54A72A"]').text
            genre = self.driver.find_elements_by_xpath('//div[@class="sc-16ede01-8 hXeKyz sc-10602b09-11 cNJBaT"]'
                                                    '//div[@class="ipc-chip-list sc-16ede01-4 bMBIRz"][@data-testid="genres"]'
                                                    '//a')
            self.__genre = list(filter(None, [x.text for x in genre]))
            director = self.driver.find_elements_by_xpath('//ul[@class="ipc-metadata-list ipc-metadata-list--dividers-all title-pc-list ipc-metadata-list--baseAlt"]'
                                                        '//li[@class="ipc-metadata-list__item"]'
                                                        '//div[@class="ipc-metadata-list-item__content-container"]'
                                                        '//li[@class="ipc-inline-list__item"]'
                                                        '//a[@class="ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link"]')
            self.__director = list(filter(None ,[x.text for x in director]))
            writer = self.driver.find_elements_by_xpath('//ul[@class="ipc-metadata-list ipc-metadata-list--dividers-all title-pc-list ipc-metadata-list--baseAlt"]'
                                                        '//li[@class="ipc-metadata-list__item ipc-metadata-list-item--link"][1]'
                                                        '//div[@class="ipc-metadata-list-item__content-container"]'
                                                        '//li[@class="ipc-inline-list__item"]')
            self.__writers = list(filter(None, [x.text for x in writer]))
            stars = self.driver.find_elements_by_xpath('//ul[@class="ipc-metadata-list ipc-metadata-list--dividers-all title-pc-list ipc-metadata-list--baseAlt"]'
                                                        '//li[@class="ipc-metadata-list__item ipc-metadata-list-item--link"][2]'
                                                        '//div[@class="ipc-metadata-list-item__content-container"]'
                                                        '//li[@class="ipc-inline-list__item"]')
            self.__stars = list(filter(None, [x.text for x in stars]))
            images = self.driver.find_elements_by_xpath('//section[@class="ipc-page-section ipc-page-section--base celwidget"][@cel_widget_id="StaticFeature_Photos"]'
                                                        '//div[@class="ipc-shoveler ipc-shoveler--base ipc-shoveler--page0"]'
                                                        '//div[@class="ipc-sub-grid ipc-sub-grid--page-span-2 ipc-sub-grid--nowrap ipc-shoveler__grid"]'
                                                        '//div[@class="ipc-photo ipc-photo--base ipc-photo--dynamic-width photos-image ipc-sub-grid-item ipc-sub-grid-item--span-2"]'
                                                        '//img[@class="ipc-image"]')
            self.__images = list(filter(None, [x.get_attribute('srcset').split(', ')[-1].split(' ')[0] for x in images]))
            poster = self.driver.find_element_by_xpath('//div[@class="sc-43e10848-0 fpjqna"]'
                                                    '//div[@class="ipc-poster ipc-poster--baseAlt ipc-poster--dynamic-width sc-bc5f13ed-0 eCJjuc celwidget ipc-sub-grid-item ipc-sub-grid-item--span-2"]'
                                                    '//div[@class="ipc-media ipc-media--poster-27x40 ipc-image-media-ratio--poster-27x40 ipc-media--baseAlt ipc-media--poster-l ipc-poster__poster-image ipc-media__img"]'
                                                    '//img[@class="ipc-image"]')
            self.__poster = poster.get_attribute('srcset').split(', ')[-1].split(' ')[0]
            self.__desc = self.driver.find_element_by_xpath('//section[@class="ipc-page-section ipc-page-section--base celwidget"][@data-cel-widget="StaticFeature_Storyline"]'
                                                            '//div[@class="sc-1d9a673d-0 epALbK"]'
                                                            '//div[@class="ipc-html-content ipc-html-content--base"]').text
            country = self.driver.find_elements_by_xpath('//div[@class="sc-f65f65be-0 ktSkVi"]'
                                                        '//ul[@class="ipc-metadata-list ipc-metadata-list--dividers-all ipc-metadata-list--base"]'
                                                        '//li[@class="ipc-metadata-list__item"][@data-testid="title-details-origin"]'
                                                        '//li[@class="ipc-inline-list__item"]')
            self.__country = list(filter(None, [x.text for x in country]))
            lang = self.driver.find_elements_by_xpath('//div[@class="sc-f65f65be-0 ktSkVi"]'
                                                    '//ul[@class="ipc-metadata-list ipc-metadata-list--dividers-all ipc-metadata-list--base"]'
                                                    '//li[@class="ipc-metadata-list__item"][@data-testid="title-details-languages"]'
                                                    '//li[@class="ipc-inline-list__item"]')
            self.__lang = list(filter(None, [x.text for x in lang]))
            self.__budget = self.driver.find_element_by_xpath('//section[@class="ipc-page-section ipc-page-section--base celwidget"][@data-testid="BoxOffice"]'
                                                            '//div[@data-testid="title-boxoffice-section"]'
                                                            '//li[@class="ipc-metadata-list__item sc-3c7ce701-2 eYXppQ"][@data-testid="title-boxoffice-budget"]'
                                                            '//span[@class="ipc-metadata-list-item__list-content-item"]').text.split(' ')[0]
            self.__world_sell = self.driver.find_element_by_xpath('//section[@class="ipc-page-section ipc-page-section--base celwidget"][@data-testid="BoxOffice"]'
                                                                '//div[@data-testid="title-boxoffice-section"]'
                                                                '//li[@class="ipc-metadata-list__item sc-3c7ce701-2 eYXppQ"][@data-testid="title-boxoffice-cumulativeworldwidegross"]'
                                                                '//span[@class="ipc-metadata-list-item__list-content-item"]').text
        except:
            pass
        result_dict = {
            'Title': self.__title,
            'Poster': self.__poster,
            'Year': self.__year,
            'Ages': self.__ages,
            'Duration': self.__duration,
            'Images': self.__images,
            'IMDB Rate': self.__rate,
            'Meta Score': self.__meta,
            'Popularity': self.__popularity,
            'Genre': self.__genre,
            'Directors': self.__director,
            'Writers': self.__writers,
            'Stars': self.__stars,
            'Story Line': self.__desc,
            'Country': self.__country,
            'language': self.__lang,
            'Budget': self.__budget,
            'Gross worldwide': self.__world_sell,
            'IMDB Id': self.__id,
        }
        self.__result.append(result_dict)
        
    def print_json(self):
        json_str = json.dumps(self.__result)
        self.__result = []
        return json_str
    
    def print_dict(self):
        out = self.__result
        self.__result = []
        return out