"""Module startup code for Raspberry Pi book reader.

Uses Google Python Style Guide: https://google.github.io/styleguide/pyguide.html
"""


class Website:
    """Represents a typical website.

    Attributes:
        name: A string containing the name of the website.
        url: A string containing the url of the website.
        account: An Account object associated with the website.
        web_driver: The web driver used open and utilize the website.
    """

    def __find_element_by_xpath(self, xpath):
            """Finds a web element by its xpath.

            Searches for the element until a certain time
            limit is reached, after which an exception is raised.

            Args:
                xpath: The xpath of the desired element.

            Returns:
                The element whose xpath matches the user-specified xpath.

            Raises:
                TimeoutException: The element was not found on the webpage
                    before the time limit was reached.
            """
            try:
                element = WebDriverWait(self.web_driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH, xpath)))
                return element
            except TimeoutException:
                print("Error: Timeout reached. Could
