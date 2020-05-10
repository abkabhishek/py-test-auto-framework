"""
This is module to contain commonly used functionality like find elements
"""
import time
from sys import stdout as console

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

WAIT_TIME_OUT = 180

class Com:

    driver = None
    wait = None
    windowTabs = {}

    def __init__(self, driver):
        Com.driver = driver
        Com.wait = Wait(driver)

    @classmethod
    def is_exist(cls, locatr):
        return cls.driver.find_elements(*Locatr.get_locatr_by(locatr))

    @classmethod
    def get_element_text_else_false(cls, elem):
        if elem:
            return elem.text
        else:
            return False

    @classmethod
    def findElement(cls, locatr, elem=None):
        """
        locatr param should be of "css|string" style
        elem param is optional selenium element, if provided then find_element will be done on that passed element
        """
        try:
            if elem:
                return elem.find_element(*Locatr.get_locatr_by(locatr))
            else:
                return cls.driver.find_element(*Locatr.get_locatr_by(locatr))
        except NoSuchElementException as e:
            print(e)
            print("Unable to find the element by: {}, locator: {}".format(*Locatr.get_locatr_by(locatr)))
            raise Exception("Element not found")

    @classmethod
    def findElements(cls, locatr, elem=None):
        """
        locatr param should be of "css|string" style
        elem param is optional selenium element, if provided then find_element will be done on that passed element
        """
        if elem:
            return elem.find_elements(*Locatr.get_locatr_by(locatr))
        else:
            return cls.driver.find_elements(*Locatr.get_locatr_by(locatr))

    @classmethod
    def element(cls, locatr):
        """
        This is the custom element function, in every pom class, every locator is created of this type function.
        User can perform action direction on the element, no need to find element first.
        Example:

        Home.Search_box().send_keys("search_text")

        It can get multiple optional parameters at the time of actions:

        Home.Results(True,1).click()
             => first param = find_all=True - To find list of elements
             => second param = element index to return, else it will return all list.

        """

        def find_element(find_all=False, return_item=False):
            try:
                if find_all:
                    elems = cls.findElements(locatr)
                else:
                    elem = cls.findElement(locatr)

                if find_all and return_item == False and elems:
                    return elems
                elif find_all and return_item != False and elems:
                    return elems[return_item - 1]
                else:
                    return elem
            except Exception as ex:
                #                 console.write(str(ex))
                console.write("---- Element not found, Exception occurred while finding the element ----")
                print(ex)
                raise Exception("Element Not found")
                # return False

        return find_element

    @classmethod
    def elements(cls, locatr):
        """
        This is similar like element function above but its for list of elements specifically

        """

        def find_elements(return_item=False):
            try:
                elems = cls.findElements(locatr)

                if return_item == False and elems:
                    return elems
                elif return_item != False and elems:
                    return elems[return_item - 1]
                else:
                    return elems
            except Exception as ex:
                # console.write(str(ex))
                console.write("---- Element not found, Exception occurred while finding the elements ----")
                console.write(ex)
                raise Exception("Elements Not found")

        return find_elements



class Locatr:
    """
    Helper class to convert "css|string" type locator to (CSS_SELECTOR,"string")
    """

    @staticmethod
    def get_locatr_by(locatr):
        if "|" in locatr:
            locatrBy, locatrStr = locatr.split("|")

            if locatrBy.lower() == "xpath":
                return By.XPATH, locatrStr
            elif locatrBy.lower() == "id":
                return By.ID, locatrStr
            elif locatrBy.lower() == "css":
                return By.CSS_SELECTOR, locatrStr
            elif locatrBy.lower() == "name":
                return By.NAME, locatrStr
            elif locatrBy.lower() == "class":
                return By.CLASS_NAME, locatrStr
            elif locatrBy.lower() == "tagname":
                return By.TAG_NAME, locatrStr
            else:
                return By.ID, locatrStr
        else:
            raise Exception("Invalid locatr string : {}".format(locatr))


class Wait:

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element_visible(self, locatr, timeout=WAIT_TIME_OUT):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(Locatr.get_locatr_by(locatr))
            )
            return element
        except Exception as e:
            print(e)
            raise Exception("Element ( by: {}, locator: {}) is not visible after waiting until timeout {}".format(*Locatr.get_locatr_by(locatr),timeout))

    def wait_for_element_with_text_present(self,locatr,text,timeout=WAIT_TIME_OUT):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.text_to_be_present_in_element(Locatr.get_locatr_by(locatr),text)
            )
            return element
        except Exception as e:
            print(e)
            raise Exception("Element ( by: {}, locator: {}) is not present with text {} after waiting until timeout {}".format(*Locatr.get_locatr_by(locatr),text,timeout))


    def is_element_present(self, locatr):
        try:
            self.driver.find_element(*Locatr.get_locatr_by(locatr))
            return True
        except Exception:
            return False

    def is_element_text_visible(self,locatr,text):
        try:
            element = self.driver.find_element(*Locatr.get_locatr_by(locatr))
            return element.is_displayed() and text in element.text
        except Exception:
            return False