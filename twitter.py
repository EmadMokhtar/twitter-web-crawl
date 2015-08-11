import requests
import time
from lxml import html

class TwitterCrawler:

	def __init__(self, starting_url, depth=0):
		self.starting_url = starting_url
		self.depth = depth
		self.current_depth = 0
		self.depth_links = []
		self.profiles = []

	def crawl(self):
		profile = self.get_twitter_profile_from_link(self.starting_url)
		self.profiles.append(profile)
		self.depth_links.append(profile.followed)

		while self.current_depth < self.depth:
			current_links = []
			for link in self.depth_links[self.current_depth]:
			    current_profile = self.get_twitter_profile_from_link(link)
			    current_links.extend(current_profile.followed)
			    self.profiles.append(current_profile)
			    time.sleep(5)
			self.current_depth += 1
			self.depth_links.append(current_links)

	def get_twitter_profile_from_link(self, link):
		start_page = requests.get(link)
		tree = html.fromstring(start_page.text)
		followed = []

		name = tree.xpath('//h1[@class="ProfileHeaderCard-name"]/a/text()')[0]
		username = tree.xpath('//h2[@class="ProfileHeaderCard-screenname u-inlineBlock u-dir"]/a/@href')[0]
		bio = tree.xpath('//p[@class="ProfileHeaderCard-bio u-dir"]/text()')[0]
		join_date = tree.xpath('//div[@class="ProfileHeaderCard-joinDate"]/span[@class="ProfileHeaderCard-joinDateText js-tooltip u-dir"]/text()')[0]
		followed_accounts = tree.xpath('//a[@class="js-user-profile-link"]/@href')
		followed = ['https://www.twitter.com{0}'.format(f) for f in followed_accounts]

		profile = TwitterProfile(name, username, bio, followed, join_date)

		return profile

class TwitterProfile:

	def __init__(self, name, username, bio, followed, join_date):
		self.name = name
		self.username = username.replace('/','@')
		self.bio = bio
		self.followed = followed
		self.join_date = join_date

	def __str__(self):
		return "Fullname: {0}, Username: {1}, Join Date: {2} Bio: {3} \n\r".format(self.name, self.username, self.join_date, self.bio)

crawler = TwitterCrawler('http://twitter.com/emadmokhtar', 1)
crawler.crawl()

for profile in crawler.profiles:
	print profile