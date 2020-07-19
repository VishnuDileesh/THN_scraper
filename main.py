from requests_html import HTMLSession

session = HTMLSession()

baseURL = 'https://thehackernews.com/search/label/'

data = {}


class CategoryScrape():

    catUrl = ''

    catName = ''

    r = ''

    def __init__(self, catUrl, catName):

        print("Starting script")

        self.catUrl = catUrl

        self.catName = catName

        self.r = session.get(self.catUrl)

    def scrapeArticle(self):

        blog_posts = self.r.html.find('.body-post')

        #print(blog_posts)

        data[f'{self.catName}'] = {}

        for blog in blog_posts:

            storyLink = blog.find('.story-link', first=True).attrs['href']

            storyTitle = blog.find('.home-title', first=True).text

            data[f'{self.catName}'][f'{storyTitle}'] = f'{storyLink}'

        print(data)


dataBreach = CategoryScrape(f'{baseURL}data%20breach', 'dataBreach')

dataBreach.scrapeArticle()
