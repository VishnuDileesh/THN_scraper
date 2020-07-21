from requests_html import HTMLSession
import json

session = HTMLSession()

baseURL = 'https://thehackernews.com/search/label/'

categories = ['data%20breach', 'Cyber%20Attack', 'Vulnerability', 'Malware']

data = {}


class CategoryScrape():

    catURL = ''

    r = ''

    category = ''

    def __init__(self, catURL, category):

        #print(f'Scraping starting on Category : {category} \n')

        #print(' ')

        self.category = category

        self.catURL = catURL

        self.r = session.get(self.catURL)

    def scrapeArticle(self):

        data[f'{self.category}'] = []

        blog_posts = self.r.html.find('.body-post')

        for blog in blog_posts:

            storyLink = blog.find('.story-link', first=True).attrs['href']

            storyTitle = blog.find('.home-title', first=True).text

            #print(storyTitle)
            #print(storyLink)

            #print("\n")

            data[f'{self.category}'].append({
                'title': f'{storyTitle}',
                'link': f'{storyLink}'
            })


for category in categories:

    category = CategoryScrape(f'{baseURL}{category}', category)

    category.scrapeArticle()

#print(data)

with open('data.txt', 'w') as f:
    json.dump(data, f)
