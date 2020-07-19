from requests_html import HTMLSession

session = HTMLSession()

baseURL = 'https://thehackernews.com/search/label/'

categories = ['data%20breach', 'Cyber%20Attack', 'Vulnerability', 'Malware']


class CategoryScrape():

    catURL = ''

    r = ''

    def __init__(self, catURL, category):

        print(f'Scraping starting on Category : {category} \n')

        print(' ')

        self.catURL = catURL

        self.r = session.get(self.catURL)

    def scrapeArticle(self):

        blog_posts = self.r.html.find('.body-post')

        for blog in blog_posts:

            storyLink = blog.find('.story-link', first=True).attrs['href']

            storyTitle = blog.find('.home-title', first=True).text

            print(storyTitle)
            print(storyLink)

            print("\n")


for category in categories:

    category = CategoryScrape(f'{baseURL}{category}', category)

    category.scrapeArticle()
