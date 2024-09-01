import requests
from bs4 import BeautifulSoup

url = "https://stackoverflow.com/?tab=week"
response = requests.get(url)
stackoverflow = response.text

new_soup = BeautifulSoup(stackoverflow, "html.parser")
question_titles = []
question_links = []
questions = new_soup.find_all(name="h3", class_="s-post-summary--content-title")
for question_tag in questions:
    question_title = question_tag.getText().strip()
    question_titles.append(question_title)
    question_link = "www.stackoverflow.com"+question_tag.find(name="a").get("href")
    question_links.append(question_link)

votes = []
vote_tags = new_soup.find_all(name="div", class_="s-post-summary--stats-item s-post-summary--stats-item__emphasized")
for vote_tag in vote_tags:
    vote = int(vote_tag.getText().strip("\nvotes"))
    votes.append(vote)


print(votes)
print(len(votes))
print(len(question_links))
print(len(question_titles))
maximum_vote = max(votes)
index = votes.index(maximum_vote)
print(f"Maximum vote : {maximum_vote}\nTitle : {question_titles[index]}\nLink : {question_links[index]}")
vote_tag = new_soup.find(name = "span", class_ = "s-post-summary--stats-item-number")
# print(question_tag)
print(vote_tag)
question_link = "www.stackoverflow.com" + question_tag.find(name="a").get("href")
question_vote = vote_tag.getText()
print(question_link)
print(question_vote)
