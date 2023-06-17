import wikipediaapi

def get_article(title):
    w_api = wikipediaapi.Wikipedia('en')
    page = w_api.page(title)
    if page.exists():
        return page.text
    else:
        return ""
def read_titles(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line.strip()

def calculate(filename):
    titles = read_titles(filename)
    sum_of_letters = 0
    sum_of_articles = 0
    for title in titles:
        article = get_article(title)
        letters = len([char for char in article if char.isalpha()] )
        sum_of_letters += letters
        sum_of_articles += 1
    if sum_of_articles > 0:
        print(sum_of_letters)
        print(sum_of_articles)
        return sum_of_letters/sum_of_articles
    return 0
print(f"Srednia liczba liter/artykul: {calculate('small.txt')}")