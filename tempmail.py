from time import sleep
from selenium_base import *

class TempMail:
    '''Class for parse temp-mail service tempmail.plus'''
    def __init__(self):
        self.__driver = create_driver(headless=True)
        self.__driver.get("https://tempmail.plus/")
        sleep(1)
        
        self.__parse_address()

    def __parse_address(self):
        name = self.__driver.find_element_by_xpath("//input[@type='text'][@id='pre_button']"\
            "[@class='form-control mb-10 mb-md-0']").get_attribute('value')

        domain = self.__driver.find_element_by_xpath("//button[@id='domain']"\
            "[@class='form-control dropdown-toggle']").text

        self.__address = name + domain

    def get_address(self) -> str:
        '''Return e-mail address'''

        return self.__address

    def recreate_mail(self):
        '''Creation of a new e-mail'''

        self.__driver.find_element_by_xpath("//button[@id='pre_rand'][@class='btn btn-txt-green']").click()
        self.__parse_address()

    def get_letters(self) -> list:
        '''Getting a list of emails with data'''

        letters = list()
        raw_letters = self.__driver.find_elements_by_xpath("//div[@class='container-xl body']/"\
            "div[@class='inbox']/div[@class='mail']")

        for raw_letter in raw_letters:
            raw_letter.click()
            sleep(1)

            sender = self.__driver.find_element_by_xpath("//div[@id='info']//span[@class='text-truncate']").text
            sender_email = self.__driver.find_element_by_xpath("//div[@id='info']//span[@class='text-muted']").text
            topic = self.__driver.find_element_by_xpath("//div[@id='info']//div[@class='subject mb-20']").text
            text = self.__driver.find_element_by_xpath("//div[@id='info']//div[@class='overflow-auto mb-20']").text

            sender = sender.replace(sender_email, '').strip()

            letter = {
                'sender':sender,
                'sender_email':sender_email,
                'topic':topic,
                'text':text
            }

            letters.append(letter)

            self.__driver.back()

        return letters

    def __del__(self):
        delete_driver(self.__driver)