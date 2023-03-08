from selenium.webdriver.common.by import By


class AccordionPageLocators:
    SECTION_FIRST = (By.CSS_SELECTOR, 'div[id="section1Heading"]')
    SECTION_CONTENT_FIRST = (By.CSS_SELECTOR, 'div[id="section1Content"] p')
    SECTION_SECOND = (By.CSS_SELECTOR, 'div[id="section2Heading"]')
    SECTION_CONTENT_SECOND = (By.CSS_SELECTOR, 'div[id="section2Content"] p')
    SECTION_THIRD = (By.CSS_SELECTOR, 'div[id="section3Heading"]')
    SECTION_CONTENT_THIRD = (By.CSS_SELECTOR, 'div[id="section3Content"] p')


class AutoCompletePegeLocators:
    MULTI_INPUT = (By.CSS_SELECTOR, 'input[id="autoCompleteMultipleInput"]')
    MULTI_VALUE = (By.CSS_SELECTOR, 'div[class="css-12jo7m5 auto-complete__multi-value__label"]')
    # MULTI_VALUE = (By.CSS_SELECTOR, 'div[css-1rhbuit-multiValue auto-complete__multi-value]')
    MULTI_VALUE_REMOVE = (By.CSS_SELECTOR, 'div[class="css-xb97g8 auto-complete__multi-value__remove"] svg path')

    SINGLE_VALUE = (By.CSS_SELECTOR, 'div[class="auto-complete__single-value css-1uccc91-singleValue"]')
    SINGLE_INPUT = (By.CSS_SELECTOR, 'input[id="autoCompleteSingleInput"]')


class DatePickerPageLocators:
    # select
    DATE_INPUT = (By.CSS_SELECTOR, 'input[id="datePickerMonthYearInput"]')
    DATE_SELECT_YEAR = (By.CSS_SELECTOR, 'select[class="react-datepicker__year-select"]')
    DATE_SELECT_MONTH = (By.CSS_SELECTOR, 'select[class="react-datepicker__month-select"]')
    # class^ - найдёт все элементы в DOM с подобным классом "react-datepicker__day react-datepicker" (42, 6*7 table day)
    DATE_SELECT_DAY_LIST = (By.CSS_SELECTOR, 'div[class^="react-datepicker__day react-datepicker"]')

    # without select
    DATE_AND_TIME_INPUT = (By.CSS_SELECTOR, 'input[id="dateAndTimePickerInput"]')
    DATE_AND_TIME_YEAR = (By.CSS_SELECTOR, 'div[class="react-datepicker__year-read-view"]')
    DATE_AND_TIME_MONTH = (By.CSS_SELECTOR, 'div[class="react-datepicker__month-read-view"]')
    DATE_AND_TIME_YEAR_LIST = (By.CSS_SELECTOR, 'div[class="react-datepicker__year-option"]')
    DATE_AND_TIME_MONTH_LIST = (By.CSS_SELECTOR, 'div[class="react-datepicker__month-option"]')
    DATE_AND_TIME_TIME_LIST = (By.CSS_SELECTOR, 'li[class="react-datepicker__time-list-item "]')


class SliderPageLocators:
    INPUT_SLIDER = (By.CSS_SELECTOR, 'input[class="range-slider range-slider--primary"]')
    SLIDER_VALUE = (By.CSS_SELECTOR, 'input[id="sliderValue"]')


class ProgressBarPageLocators:
    PROGRESS_BAR_BUTTON = (By.CSS_SELECTOR, 'button[id="startStopButton"]')
    PROGRES_BAR_VALUE = (By.CSS_SELECTOR, 'div[class="progress-bar bg-info"]')


class TabsPageLocators:
    TABS_WHAT = (By.CSS_SELECTOR, 'a[id="demo-tab-what"]')
    TABS_WHAT_CONTENT = (By.CSS_SELECTOR, 'div[id="demo-tabpane-what"]')
    TABS_ORIGIN = (By.CSS_SELECTOR, 'a[id="demo-tab-origin"]')
    TABS_ORIGIN_CONTENT = (By.CSS_SELECTOR, 'div[id="demo-tabpane-origin"]')
    TABS_USE = (By.CSS_SELECTOR, 'a[id="demo-tab-use"]')
    TABS_USE_CONTENT = (By.CSS_SELECTOR, 'div[id="demo-tabpane-use"]')
    TABS_MORE = (By.CSS_SELECTOR, 'a[id="demo-tab-more"]')
    TABS_MORE_CONTENT = (By.CSS_SELECTOR, 'div[id="demo-tabpane-more"]')


class ToolTipsPageLocators:
    BUTTON = (By.CSS_SELECTOR, 'button[id="toolTipButton"]')
    TOOL_TIP_BUTTON = (By.CSS_SELECTOR, 'button[aria-describedby="buttonToolTip"]')

    FIELD = (By.CSS_SELECTOR, 'div[id="texFieldToolTopContainer"] input[id="toolTipTextField"]')
    TOOL_TIP_FIELD = (By.CSS_SELECTOR, 'input[aria-describedby="textFieldToolTip"]')

    CONTRARY_LINK = (By.XPATH, '//*[.="Contrary"]')
    TOOL_TIP_CONTRARY = (By.CSS_SELECTOR, 'a[aria-describedby="contraryTexToolTip"]')

    SECTION_LINK = (By.XPATH, '//*[.="1.10.32"]')
    TOOL_TIP_SECTION = (By.CSS_SELECTOR, 'a[aria-describedby="sectionToolTip"]')

    TOOL_TIPS_INNERS = (By.CSS_SELECTOR, 'div[class="tooltip-inner"]')     # селектор текста  (tool tips)


class MenuPageLocators:
    MENU_ITEM_LIST = (By.CSS_SELECTOR, 'ul[id="nav"] li a')                # список всех селекторов элементов MENU


class SelectMenuPageLocators:                                              # задание вкладка "Widgets"-->"Select Menu"
    # field "Select Value"
    SELECT_VALUE_BEFORE = (By.CSS_SELECTOR, '#withOptGroup > div > div.css-1hwfws3 > div.css-1wa3eu0-placeholder')
    SELECT_VALUE_AFTER = (By.CSS_SELECTOR, '#withOptGroup > div > div.css-1hwfws3 > div.css-1uccc91-singleValue')
    SELECT_VALUE_INPUT = (By.CSS_SELECTOR, 'div[id="withOptGroup"] input[id="react-select-2-input"]')

    # field "Select One"
    SELECT_ONE_BEFORE = (By.CSS_SELECTOR, '#selectOne > div > div.css-1hwfws3 > div.css-1wa3eu0-placeholder')
    SELECT_ONE_AFTER = (By.CSS_SELECTOR, '#selectOne > div > div.css-1hwfws3 > div.css-1uccc91-singleValue')
    SELECT_ONE_INPUT = (By.CSS_SELECTOR, 'input[id="react-select-3-input"]')

    # field "Old Style Select Menu"
    OLD_STYLE_SELECT = (By.CSS_SELECTOR, 'select[id="oldSelectMenu"]')

    # "Multiselect drop down"
    MULTI_COLOR_INPUT = (By.CSS_SELECTOR, 'input[id="react-select-4-input"]')
    MULTI_COLOR_VALUE = (By.CSS_SELECTOR, 'div[class="css-12jo7m5"]')
    MULTI_COLOR_VALUE_REMOVE = (By.CSS_SELECTOR, 'div[class="css-xb97g8"] svg path')

    # "Standard multi select"
    MULTI_STANDARD_SELECT = (By.CSS_SELECTOR, 'select[id="cars"]')



