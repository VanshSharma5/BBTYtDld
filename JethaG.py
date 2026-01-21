import cloudscraper
from bs4 import BeautifulSoup
import re

# requirements
#    cloudscraper
#    beautifulsoup4

# this is only for educational purpose.😇

# sanfoundry MCQs urls
urls = [
    "https://www.sanfoundry.com/c-programming-questions-answers-variable-names-1/",
    "https://www.sanfoundry.com/c-programming-questions-answers-variable-names-2/",
    "https://www.sanfoundry.com/c-programming-questions-answers-data-types-sizes-1/",
    "https://www.sanfoundry.com/c-programming-questions-answers-data-types-sizes-2/",
    "https://www.sanfoundry.com/c-programming-questions-answers-constants-1/",
    "https://www.sanfoundry.com/c-programming-interview-questions-answers-constants/",
    "https://www.sanfoundry.com/interview-questions-answers-c-declarations/"
]

# filter regex
garbage = r"<script\b[^>]*>[\s\S]*?</script>|<span\b[^>]*>|</span>|<li\b[^>]*>|</li>|<pre\b[^>]*>|</pre>|<div class=\"sf-desktop-ads\">[\s\S]*?</script>|<div class=\"sf-mobile-ads\" style=\"padding-bottom: 20px;\">[\s\S]*?</script>|</div>|<div\b[^>]*>|<br/>"



# this take the url of page and return the needed section as string by level 1 filteration
def parse_page(url):
    # create scrapper
    req= cloudscraper.create_scraper()
    res = req.get(url).text
    soup = BeautifulSoup(res, "html.parser")
    need = str(soup.find_all(class_="entry-content"))
    need = re.sub(garbage, "", need)
    need = need.split('\n')[2:-12] # dont touch it
    return "\n".join(need)

# split the ques
def parse_ques(page):
    ques = page.split("<p>")
    return ques

file_name = "CMCQs.txt"

with open(file_name, "w") as file:
    for url in urls:
        ques = parse_ques(parse_page(url))
        for q in ques:
            file.write(q)

print("Ho gai")