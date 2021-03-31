import requests # allow us to download the html
from bs4 import BeautifulSoup # allow us to use html to grab different datas
import pprint #to get pretty print, so make your terminal print out more nicely than normal print
res = requests.get('https://news.ycombinator.com/news') # this is the web browsers that we using like actual Windows, use to get datas from website
# print(res.text)
soup= BeautifulSoup(res.text, 'html.parser')#99% you will use html.parser # This data need to be modified into HTML so we can control, convert from string into html we can manipulate
# print(soup) # get all the text converted into html
# print(soup.body) # grab only the body
# print(soup.body.contents) # see only the body contents in LIST
# print(soup.find_all('div') # see all the div obj, or you can see all the links with'a'
# print(soup.title) # see the site title
# print(soup.find('a')) # this is useful because it give us all the info about the link and title as well as the votes we want
#print(soup.select('.score')) # grab all the score from the page from span class, '.' means class
# print(soup.select('#score_26300191')) # with select you can go upon an element
# Go to the website -> grab a specific title or info you need -> right-click and press 'Inspect' -> find the specific code related to the info -> grab it and collect inside Python
# The first link and first vote are together, as well as the second, third etc.
links = soup.select('.storylink')
#votes = soup.select('.score') # not every links contain votes so we have to find sth else upper .score that contains score and always be there
subtext = soup.select('.subtext') # thats why we have to grab subtext
#print(votes[0]) # grab the first elements of votes = the first news
#print(votes[0].get('id')) # get the first vote id

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key = lambda k:k['votes'], reverse = True)  # sorted a list based on the key 'votes' from the dict of link,title and votes with descending order (using reverse =True)

def create_custom_hn(links,subtext):
    hn = []
    for idx, item in enumerate(links): #We have 2 lists links and subtext, that why we need index to access our loop to grab both links and subtext, enumerate get index
# Normally links will be greater than points because some links dont have points(nobody vote for it) so you can catch index out of range
        title = links[idx].getText()
        href = links[idx].get('href',None) # give default None if the link is broken with no href
        vote = subtext[idx].select('.score')
        if len(vote): # you get a list so you need to check if vote exists, sometimes news dont have votes
            points= int(vote[0].getText().replace(' points', ''))
            if points > 99: # only print out any news that have more than 100 votes
                hn.append({'title': title, 'link' : href, 'votes': points}) # create a dict with link,title and votes
    return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(links,subtext))
