from requests_html import HTMLSession

session = HTMLSession()

baseURL = 'https://thehackernews.com/search/label/'


class CategoryScrape():

    catUrl = ''

    def __init__(self, catUrl):

        print("Starting script")

        self.catUrl = catUrl

        r = session.get(self.catUrl)

        print(r.text)


dataBreach = CategoryScrape(f'{baseURL}data%20breach')
