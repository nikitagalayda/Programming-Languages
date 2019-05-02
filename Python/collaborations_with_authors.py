# Prints all authors with which the desired author has collaborated, and number of
# times they collaborated (collaborated = both authors took part in writing a paper)

import urllib.request
import matplotlib.pyplot as plt
import re
from coauthors import *

def get_articles(url, author, all_coauthors):
	art_num = 0
	pattern_article = 'li class="arxiv-result">[\s\S]*?</li>'
	content = urllib.request.urlopen(url)
	html_str = content.read().decode('utf-8')
	result_article = re.findall(pattern_article, html_str)
	for article in result_article:
		in_coauthors, coauthors_list = author_in_article_coauthors(article, author, 1)
		if(in_coauthors):
			all_coauthors += coauthors_list
		art_num += 1
	
	return art_num

def count_values(val_list):
	values_dict = dict()
	for val in val_list:
		if val in values_dict:
			values_dict[val] += 1
		else:
			values_dict[val] =  1
	return values_dict

author_t = input("Input Author: ")
author = author_t.strip().replace(" ", "+")
base_url = "https://arxiv.org"
page_iter = '&start='
url = "https://arxiv.org/search/?query=" + author + "&searchtype=author"
pattern_page = 'a href="/search/?[\s]*[\S]*start=[\d]+"[\s]*class="pagination-link'
all_coauthors = []

count = 50
i = 0
while(count >= 50):
	count = get_articles(url, author_t, all_coauthors)
	url = url + page_iter + str(count)

coauthors_dict = count_values(all_coauthors)
for key, value in sorted(coauthors_dict.items()):
	print(key, value)