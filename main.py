from lib import crawler

crawler = crawler.IMDB()
crawler.get_id('tt1631867')
#crawler.get_list('https://www.imdb.com/search/title/?count=100&groups=top_1000&sort=user_rating')
out = crawler.print_json()
print(out)
crawler.driver.quit()