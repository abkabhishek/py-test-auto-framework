from sys import platform
from selenium import webdriver
import os

from selenium.webdriver.chrome.options import Options

dir_path = os.path.dirname(os.path.realpath(__file__))


class Browser:

    @classmethod
    def get_driver(cls, settings={"browser": "chrome", "environment": "local","headless":"false"}):
        print('==============INIT=================')
        driver = None
        if settings["environment"] == "local":
            if platform == "darwin":
                # OS X
                if settings["browser"] == 'chrome':
                    chrome_options = Options()
                    if settings["headless"] == "true":
                        chrome_options.add_argument("--headless")
                    driver = webdriver.Chrome(executable_path="resources/chromedriver_mac",options=chrome_options)

                else:
                    print("Invalid Browser passed")
                    raise Exception("Invalid Browser passed")

            elif platform == "win32":
                # Windows...
                if settings["browser"] == 'chrome':
                    chrome_options = Options()
                    if settings["headless"] == "true":
                        chrome_options.add_argument("--headless")

                    driver = webdriver.Chrome(
                        executable_path='./resources/chromedriver.exe',
                        options=chrome_options
                    )

                else:
                    print("Invalid Browser passed")
                    raise Exception("Invalid Browser passed")
            elif platform == "linux" or platform == "linux2":
                # linux
                raise Exception("TBD for Linux")
        elif settings["environment"] == "remote":
             # Make sure to run "docker-compose up -d" before running test
            remote_grid_url = 'http://localhost:4444/wd/hub'
            chrome_options = Options()
            if settings["headless"] == "true":
                chrome_options.add_argument('--headless')
            capabilities = {'browserName': 'chrome', 'javascriptEnabled': True}
            capabilities.update(chrome_options.to_capabilities())
            driver = webdriver.Remote(
                command_executor=remote_grid_url,
                desired_capabilities=capabilities
            )

        return driver


if __name__ == "__main__":
    driver = Browser.get_driver()
    driver.get("https://www.google.com")
    print(driver.title)
    driver.quit()
