from requests_html import HTML, HTMLSession

session = HTMLSession()

r = session.get("https://klopotenko.com/en/breakfast/")
all = r.html.find('.js-post-container', first=True)
posts = all.find('.rtin-single-post')
for post in posts:
    link = post.find(".rtin-img", first=True).find('a', first=True).attrs['href']
    r2 = session.get(link)
    article = r2.html.find('main', first=True)
    try:

        headline = article.find('.item-title', first=True).text
    except:
        headline = None
    print(headline)
    try:
        cuisine = article.find('.recipe-cuisine', first=True).text
    except:
        cuisine = None
    print(cuisine)