import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title, search_by_date, search_by_tag, search_by_category
)
from tech_news.analyzer.ratings import (
    top_5_news, top_5_categories
)
# Requisito 12


def analyzer_menu():
    options = input(
        'Selecione uma das opções a seguir:'
        '\n 0 - Popular o banco com notícias;'
        '\n 1 - Buscar notícias por título;'
        '\n 2 - Buscar notícias por data;'
        '\n 3 - Buscar notícias por tag;'
        '\n 4 - Buscar notícias por categoria;'
        '\n 5 - Listar top 5 notícias;'
        '\n 6 - Listar top 5 categorias;'
        '\n 7 - Sair.'
    )

    try:
        options = int(options)
    except ValueError:
        return options

    chose_option(options)


def chose_option(option):

    if (option == 0):
        get_tech_news(input('Digite quantas notícias serão buscadas:'))
    elif (option in range(1, 5)):
        filter_options(option)
    elif (option in range(5, 7)):
        rating_options(option)
    elif (option == 7):
        print('Encerrando script\n')
    else:
        print('Opção inválida', file=sys.stderr)


def filter_options(option):

    if (option == 1):
        print(search_by_title(input('Digite o título que deseja buscar:')))
    elif (option == 2):
        print(search_by_date(input('Digite a data que deseja buscar:')))
    elif (option == 3):
        print(search_by_tag(input('Digite a tag que deseja buscar:')))
    elif (option == 4):
        print(
            search_by_category(input('Digite a categoria que deseja buscar:'))
            )


def rating_options(option):

    if (option == 5):
        print(top_5_news())
    elif (option == 6):
        print(top_5_categories())
