import re

def get_year(article):
	# pattern_date = 'p class="is-size-7"><span class="[\s\S]*?</p>'
	pattern_date = 'announced</span>[\s\S]*?</p>'
	year = re.findall(pattern_date, article)[0]
	start = year.find('>')
	end = year.find('\n')
	year = year[start+1:end-1].strip().split()[1]
	return year

def author_in_article_coauthors(article, search_author, return_list):
	pattern_coauthors = 'Authors:</span>[\s\S]*?</p>'
	find_coauthor_pattern = '>.+?<'
	coauthor_list = []

	result_coauthors = re.findall(pattern_coauthors, article)
	for coauthor in result_coauthors:
		clean_authors = re.findall(find_coauthor_pattern, coauthor)
		for author in clean_authors:
			coauthor_list.append(author.replace('<', '').replace('>', ''))
	if search_author in coauthor_list:
		if return_list == 1:
			return True, coauthor_list
		return True
	else:
		if return_list == 1:
			return False, coauthor_list
		return False

def get_coauthors_all(article_list, search_author):
	final_authors = []
	pattern_coauthors = 'Authors:</span>[\s\S]*?</p>'
	find_coauthor_pattern = '>.+?<'

	for article in article_list:
		result_coauthor = re.findall(pattern_coauthors, article)
		for coauthor in result_coauthor:
			clean_authors = re.findall(find_coauthor_pattern, coauthor)
			loc_coauthor_list = []
			for author in clean_authors:
				loc_coauthor_list.append(author.replace('<', '').replace('>', ''))
			if search_author in loc_coauthor_list:
				final_authors = final_authors + loc_coauthor_list
	return final_authors