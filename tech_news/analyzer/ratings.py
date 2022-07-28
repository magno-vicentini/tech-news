from tech_news.database import get_collection, find_news
from collections import Counter
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
    count_common_categories = Counter(
        news["category"] for news in find_news()
    ).most_common(5)

    sort_categories = sorted(
        sorted(
            count_common_categories,
            key=lambda x: x[0],
        ),
        key=lambda x: x[1],
        reverse=True,
    )

    return [category[0] for category in sort_categories]
