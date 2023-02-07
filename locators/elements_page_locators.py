from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    # form fields
    FULL_NAME = (By.CSS_SELECTOR, "input[id='userName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='permanentAddress']")
    SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")

    # created from
    CREATED_FULL_NAME = (By.CSS_SELECTOR, "#output #name")
    CREATED_EMAIL = (By.CSS_SELECTOR, "#output #email")
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, "#output #currentAddress")
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#output #permanentAddress")
    CREATED_SUBMIT = (By.CSS_SELECTOR, "#output #submit")


class CheckBoxPageLocators:
    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, "button[title='Expand all']")
    ITEM_LIST = (By.CSS_SELECTOR, "span[class='rct-title']")                   # locator 17-ти элементов для работы с циклом
    CHECKED_ITEMS = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")  # поиск отмеченных чекбоксов
    TITLE_ITEM = ".//ancestor::span[@class='rct-text']"                        # xpath, путь к тексту элементов CHECKBOX
    OUTPUT_RESULT = (By.CSS_SELECTOR, "span[class='text-success']")            # поиск выведенного списка названий, выбранных елементов в checkbox


class RadioButtonLocators:
    RADIO_BUTTON_YES = (By.CSS_SELECTOR, "label[class^='custom-control'][for='yesRadio']")
    RADIO_BUTTON_IMPRESSIVE = (By.CSS_SELECTOR, "label[class^='custom-control'][for='impressiveRadio']")
    RADIO_BUTTON_NO = (By.CSS_SELECTOR, "label[class^='custom-control'][for='noRadio']")
    OUTPUT_RESULT_RB = (By.CSS_SELECTOR, "span[class='text-success']")         # поиск текста, отмеченного radio_button


class WebTablePageLocators:
    ADD_BUTTON = (By.CSS_SELECTOR, "button[id='addNewRecordButton']")          # кнопка add
    FIRSTNAME_INPUT = (By.CSS_SELECTOR, "input[id='firstName']")               # firs name
    LASTNAME_INPUT = (By.CSS_SELECTOR, "input[id='lastName']")                 # last name
    AGE_INPUT = (By.CSS_SELECTOR, "input[id='age']")                           # age
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[id='userEmail']")                   # email
    SALARY_INPUT = (By.CSS_SELECTOR, "input[id='salary']")                     # salary
    DEPARTMENT_INPUT = (By.CSS_SELECTOR, "input[id='department']")             # department
    SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")                          # кнопка submit

    # table
    # список данных, добавленных пользователей (строка в таблице)
    FULL_PERSON_LIST = (By.CSS_SELECTOR, "div[class='rt-tr-group']")

    SEARCH_INPUT = (By.CSS_SELECTOR, 'input[id="searchBox"]')                  # поле для поиска пользователя в таблице
    DELETE_BUTTON = (By.CSS_SELECTOR, 'span[title="Delete"]')                  # "корзинка" удаления данных в таблице
    # поиск по родительскому элементу строки (xpath)
    ROW_PARENT = ".//ancestor::div[@class='rt-tr-group']"                      # родительская строка в таблице WebTable

