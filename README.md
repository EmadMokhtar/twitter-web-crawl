#Twitter Profile Crawler
Twitter Profile Crawler will crawl a Twitter profile to extract profile's

* 	Full name.
* 	Username.
* 	Bio.
*  Joining Date.
* 	Recent followed accounts.

And if there are recent followed account and according to crawl depth, it will crawl the recent followed Twitter accounts.

##Installation
```
pip install lxml 
pip install requests
```

#How to use?
From terminal:

```
python twitter.py <username> <depth>
```

###Example:
If I want to get profile of @EmadMokhtar for depth = 1

```
python twitter.py emadmokhtar 1
```
