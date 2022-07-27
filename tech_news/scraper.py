import requests
from time import sleep
from parsel import Selector
from tech_news.database import create_news
# Requisito 1


def fetch(url):
    sleep(1)
    try:
        response = requests.get(
            url,
            timeout=3,
            headers={"user-agent": "Fake user-agent"},
        )
        if(response.status_code != 200):
            return None
        return response.text
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)

    return [
        link
        for link in selector.css('a.cs-overlay-link::attr(href)').getall()
    ]


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)

    return selector.css('a.next::attr(href)').get()


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(text=html_content)

    new_info = dict()
    new_info['url'] = selector.xpath('//link[@rel="canonical"]/@href').get()
    new_info['title'] = selector.css('.entry-title::text').get().strip()
    new_info['timestamp'] = selector.css('.meta-date::text').get()
    new_info['writer'] = selector.css('.author a::text').get()
    new_info['summary'] = ''.join(
        selector.css('div.entry-content > p:nth-of-type(1) *::text').getall()
    ).strip()
    new_info['tags'] = selector.xpath('//a[@rel="tag"]/text()').getall()
    new_info['category'] = selector.css('.category-style .label::text').get()
    new_info['comments_count'] = len(
        selector.css("ol.comment-list li").getall()
    ) or 0
    return new_info


# Requisito 5


def get_tech_news(amount):
    data = fetch('https://blog.betrybe.com/')
    page_news = scrape_novidades(data)
    news = []
    while len(news) < amount:
        for link in page_news:
            news_data = fetch(link)
            news.append(scrape_noticia(news_data))

        try:
            data = fetch(scrape_next_page_link(data))
            page_news = scrape_novidades(data)
        except FileNotFoundError:
            break

    news = news[:amount]
    create_news(news)

    return news
