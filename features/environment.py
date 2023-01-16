from selenium import webdriver
from selenium.webdriver.chrome.service import Service as Chromeservices
from webdriver_manager.chrome import ChromeDriverManager


def browser_init(context):
    context.driver = webdriver.Chrome(service=Chromeservices(ChromeDriverManager().install()))
    context.driver.implicitly_wait(5)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()