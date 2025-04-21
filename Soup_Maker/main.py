from bs4 import BeautifulSoup
import requests

words_list = []

for page in range(1,27):
    if page == 1:
        url = "https://www.bestwordlist.com/5letterwords.htm"
    else:
        url = f"https://www.bestwordlist.com/5letterwordspage{page}.htm"
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the specific span element with class "mt"
    mt_span = soup.find('span', class_='mt')

    # Extract all words as text and split them into a list
    for word in mt_span.get_text(separator=" ").split():
        words_list.append(word)

print(words_list)
print(len(words_list))
