from requests_html import HTML, HTMLSession

session = HTMLSession()

r = session.get("https://klopotenko.com/en/breakfast/")
for html in r.html:
    print(html)
all = r.html.find('.js-post-container', first=True)
posts = all.find('.rtin-single-post')


def get_recipe():
    for post in posts:
        link = post.find(".rtin-img", first=True).find('a', first=True).attrs['href']
        r2 = session.get(link)
        article = r2.html.find('main', first=True)
        try:
            headline = article.find('.item-title', first=True).text
        except:
            headline = None
        try:
            cuisine = article.find('.recipe-cuisine', first=True).text
        except:
            cuisine = None
        try:
            ingredients = article.find('.ingredient-list', first=True).text
        except:
            ingredients = None
        try:
            steps = article.find('.direction-wrap-layout1', first=True).text
        except:
            steps = None
        print(headline, cuisine, ingredients, steps)
        try:
            time = article.find('.feature-sub-title.total_time', first=True).text
            time = time.replace("total_time_text", "")
        except:
            time = None
        print(headline, cuisine, ingredients, steps, time)


get_recipe()