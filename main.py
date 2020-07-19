from requests_html import HTMLSession

session = HTMLSession()

baseURL = 'https://thehackernews.com/search/label/'


class CategoryScrape():

    catUrl = ''

    r = ''

    def __init__(self, catUrl):

        print("Starting script")

        self.catUrl = catUrl

        self.r = session.get(self.catUrl)

    def scrapeArticle(self):

        blog_posts = self.r.html.find('.body-post')

        #print(blog_posts)


dataBreach = CategoryScrape(f'{baseURL}data%20breach')

dataBreach.scrapeArticle()
