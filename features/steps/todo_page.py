from selenium.webdriver.common.by import By
from behave import given, when, then


INPUT_TAB = (By.XPATH, "//input[@class='form-control']")
ADD_BUTTON = (By.XPATH, "//button[@type='submit']")
UNCHECK_BUTTON = (By.XPATH, "//span[@class='icon']")
UNCHECK_TASK_BUTTON = (By.XPATH, '(//ul[@class="Todo-group"]/li/span[text()="[X]"])[3]')
DELETE_BUTTON = (By.XPATH, "//button[@type='button']")
BASE_ITEMS = (By.CSS_SELECTOR, '#root li')


@given('open todo app page')
def open_todo_app(context):
    context.driver.get('http://localhost:3000/')


@when('user creates a task {actual_task}')
def user_creates_task(context, actual_task):
    context.driver.find_element(*INPUT_TAB).send_keys(actual_task)
    context.driver.find_element(*ADD_BUTTON).click()


@when('user completes the task')
def user_checks_task(context):
    context.driver.find_element(*UNCHECK_BUTTON).click()


@when('user unchecks the task')
def user_unchecks_task(context):
    context.driver.find_element(*UNCHECK_TASK_BUTTON).click()


@when('user deletes the todo task')
def user_deletes_task(context):
    context.driver.find_element(*DELETE_BUTTON).click()


@then('verify task is deleted and left with {expected_items}')
def task_deleted(context, expected_items):
    actual_item_list = context.driver.find_elements(*BASE_ITEMS)
    assert len(actual_item_list) == int(expected_items), f'Expected {expected_items} but got {actual_item_list}'
    print("Test Case Passed")

