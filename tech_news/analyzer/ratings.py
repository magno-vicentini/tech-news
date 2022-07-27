from tech_news.database import get_collection
# Requisito 10


def top_5_news():
    all_news = get_collection()
    news_list = list(all_news.find({}).sort([
        ('comments_count', -1),
        ('title', 1)
    ]).limit(5))

    return [(news['title'], news['url']) for news in news_list]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
