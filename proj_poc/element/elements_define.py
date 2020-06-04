from selenium.webdriver.common.by import By


class ElementsDefine(object):
    """
    Custom Showcase Element Define
    """

    def __init__(self):
        """
        init function
        """
        #   homepage
        self.homepage_navigation = By.CLASS_NAME, "nae-nav-link "
        self.homepage_screenshot = By.TAG_NAME, "html"
        self.homepage_gallery_component = By.CLASS_NAME, "gallery-title"
        self.homepage_card_component = By.CLASS_NAME, "card-signpost-content"
        self.homepage_card_component = By.PARTIAL_LINK_TEXT, "card-signpost-content"

