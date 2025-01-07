import requests
from bs4 import BeautifulSoup
import pprint

pages= 5 # no of pages to visit
mega_links, mega_scores= [],[]
for i in range(pages):
    url= f'https://news.ycombinator.com/news' + f'?p={i+1}'
    response= requests.get(url)
    soup= BeautifulSoup(response.text, 'html.parser')

    links= soup.select('.titleline')
    scores= soup.select('.subtext')

    mega_links +=links
    mega_scores += scores

def sort_stories_by_vote(news_list):
    print(len(news_list))
    return sorted(news_list,key= lambda k:k['votes'],reverse=True)

def get_custom_news(links,scores):
    hn= []
    for idx, item in enumerate(links):
        title= links[idx].select('a')[0].getText()
        href= links[idx].select('a')[0].get('href')
        score= scores[idx].select('.score')
        if len(score):
            points= int(score[0].getText().replace(' points',''))
            if points >= 100:
                hn.append({'title':title,'href':href, 'votes':points})
    return sort_stories_by_vote(hn)

pprint.pprint(get_custom_news(mega_links,mega_scores))