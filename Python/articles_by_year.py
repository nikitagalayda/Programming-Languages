# Graphs the number of articles written by a desired author for every year for
# which the author wrote at least 1 paper

import urllib.request
import matplotlib.pyplot as plt
import re
from coauthors import *

def count_values(val_list):
	val_list.reverse()
	values_dict = dict()
	for val in val_list:
		if val in values_dict:
			values_dict[val] += 1
		else:
			values_dict[val] = 1
	return values_dict

def graph_years(val_dict):
	plt.bar(range(len(val_dict)), val_dict.values(), align='center')
	plt.yticks(range(max(val_dict.values())+1))
	plt.xticks(range(len(val_dict)), val_dict.keys())
	plt.show()

def visit_page_count_papers(url, val_list):
	res_num = 0
	# Get HTML content
	content = urllib.request.urlopen(url)
	html_str = content.read().decode('utf-8')

	# Distinguishing date from other information
	pattern_date = 'p class="is-size-7"><span class="[\s\S]*?</p>'

	# Get all matching date strings
	result_date = re.findall(pattern_date, html_str)
	for r in result_date:
		res_num += 1
		# Separate the year from the rest of information
		find_num_pattern = '[0-9][0-9][0-9][0-9]'
		val_list.append(re.findall(find_num_pattern, r)[1])
	return res_num

# def get_article_title(article):
# 	pattern = 'title is-5 mathjax[\s\S]*?</p>'
# 	result = re.findall(pattern, article)
# 	return result


def get_articles(url, author, years):
	art_num = 0
	pattern_article = 'li class="arxiv-result">[\s\S]*?</li>'
	content = urllib.request.urlopen(url)
	html_str = content.read().decode('utf-8')
	result_article = re.findall(pattern_article, html_str)
	for article in result_article:
		if(author_in_article_coauthors(article, author, 0)):
			year = get_year(article)
			years.append(year)
		else:
			year = get_year(article)
		art_num += 1
	
	return art_num




author_t = input("Input Author: ")
author = author_t.strip().replace(" ", "+")
base_url = "https://arxiv.org"
page_iter = '&start='
url = "https://arxiv.org/search/?query=" + author + "&searchtype=author"
pattern_page = 'a href="/search/?[\s]*[\S]*start=[\d]+"[\s]*class="pagination-link'
years = []
pages = []

count = 50
i = 0
while(count >= 50):
	count = get_articles(url, author_t, years)
	url = url + page_iter + str(count)

year_counts = count_values(years)
graph_years(year_counts)