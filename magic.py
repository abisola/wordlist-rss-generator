#!/usr/bin/python
import time
import random
import os
import sys

from email.Utils import formatdate

##open translation file
try: 
	path = os.getenv('TRANSLATOR_PROJECT_ROOT_DIR', '')

	f_german_words = open(path.strip()+'german-word-list.txt', 'r')

	file_contents = f_german_words.readlines()

	##create RSS file
	f_rss = open(path+'list.xml','w')

	pubdate = formatdate()

	#set up templates
	container_template = '<rss version="2.0"><channel><description>Common German words compiled by myself</description>	<link>http://www.fatokun.com</link>	<title>Common German Words</title><pubDate>{{pubdate}}</pubDate><lastBuildDate>{{pubdate}}</lastBuildDate>{{items}}</channel></rss>'
	item_template = '<item> <guid isPermaLink="false">http://www.fatokun.com/id/100{{guid}}</guid> <pubDate>{{pubdate}}</pubDate> <title>{{title}}</title><description>{{description}}</description> <link> http://www.fatokun.com/</link> <author>noreply@fatokun.com (Site Admin)</author> </item>'


	items = ''
	counter = 0

	for num in range(0,20):
		random_number = random.randrange(473) #generate random number to use 
		word_of_interest = file_contents[random_number]

		entry_items = word_of_interest.rstrip('\n').split(';')
		english_translation = entry_items[1]
		german_word = entry_items[0]

		items = items + item_template.replace("{{title}}", german_word).replace("{{description}}", english_translation).replace("{{pubdate}}", pubdate).replace("{{guid}}", str(random_number))


	rss = container_template.replace("{{items}}", items).replace("{{pubdate}}", pubdate)

except IOError:
	# do nothing
	print "There has been an error with reading or writing to the file. Sorrry"
else: 
	#write rss to file
	# print rss
	f_rss.write(rss)
	
	#tidy up
	f_german_words.close()
	f_rss.close()