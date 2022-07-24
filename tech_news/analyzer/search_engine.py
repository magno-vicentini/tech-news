import re
from datetime import datetime
from tech_news.database import search_news

# Requisito 6
def search_by_title(title):
    title_regex = re.compile(title, re.IGNORECASE)
    news_by_title = search_news({'title': {'$regex': title_regex}})

    return [(news['title'], news['url']) for news in news_by_title]


# Requisito 7
def search_by_date(date):
    try:
        date = datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        raise ValueError('Data inválida')
    else:
        news_by_date = search_news({'timestamp': date.strftime("%d/%m/%Y")})

    return [(news['title'], news['url']) for news in news_by_date]


# Requisito 8
def search_by_tag(tag):
    tag_regex = re.compile(tag, re.IGNORECASE)
    news_by_tag = search_news({'tags': {'$elemMatch': {'$regex': tag_regex}}})
    return [(news['title'], news['url']) for news in news_by_tag]


# Requisito 9
def search_by_category(category):
    category_regex = re.compile(category, re.IGNORECASE)
    news_by_category = search_news({'category': {'$regex': category_regex}})

    return [(news['title'], news['url']) for news in news_by_category]
