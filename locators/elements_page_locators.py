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
    NO_ROWS_FOUND = (By.CSS_SELECTOR, 'div[class="rt-noData"]')                # локатор отсутствия строк в таблице
    ROWS_DROP_BOX = (By.CSS_SELECTOR, 'select[aria-label="rows per page"]')    # drop_box с количеством строк

    # update
    UPDATE_BUTTON = (By.CSS_SELECTOR, "span[title='Edit']")                    # кнопка Edit "карандаш"


class ButtonsPageLocators:
    DOUBLE_CLICK_BUTTON = (By.CSS_SELECTOR, "button[id='doubleClickBtn']")     # кнопка двойного клика
    RIGHT_CLICK_BUTTON = (By.CSS_SELECTOR, "button[id='rightClickBtn']")       # кнопка правого клика
    # click me кнопка с динамически id можно обойти по поиску 3го элемента доч.кл от род.кл ":nth-child(3n) button"
    # или //div[3]/button - xpath
    CLICK_ME_BUTTON = (By.CSS_SELECTOR, "div[class='mt-4']:nth-child(3) button")

    # result click messages
    RESULT_DOUBLE = (By.CSS_SELECTOR, "p[id='doubleClickMessage']")            # сообщение о нажатии кнопки
    RESULT_RIGHT = (By.CSS_SELECTOR, "p[id='rightClickMessage']")              # сообщение о нажатии кнопки
    RESULT_CLICK_ME = (By.CSS_SELECTOR, "p[id='dynamicClickMessage']")         # сообщение о нажатии кнопки


class LinksPageLocators:
    HOME_LINK = (By.CSS_SELECTOR, "a[id='simpleLink']")                        # "Home" link
    BAD_REQUEST = (By.CSS_SELECTOR, "a[id='bad-request']")                     # "Bad Request" link
    UNAUTHORIZED = (By.CSS_SELECTOR, "a[id='unauthorized']")                   # "Unauthorized" link


class UpLoadAndDownloadPageLocators:
    INPUT_UPLOAD_FILE = (By.CSS_SELECTOR, "input[id='uploadFile']")            # input для загрузки файла
    UPLOADED_FILE_RESULT = (By.CSS_SELECTOR, "p[id='uploadedFilePath']")       # строка с path на web

    DOWNLOAD_FILE = (By.CSS_SELECTOR, "a[id='downloadButton']")                # кнопка Download


class DynamicPropertiesPageLocators:
    COLOR_CHANGE_BUTTON = (By.CSS_SELECTOR, "button[id='colorChange']")        # кнопка с изменяемым цветом Color Change
    VISIBLE_AFTER_5S_BUTTON = (By.CSS_SELECTOR, "button[id='visibleAfter']")   # кнопка видимая через 5 сек
    ENABLE_BUTTON = (By.CSS_SELECTOR, "button[id='enableAfter']")              # disable button, after 5s - enable

