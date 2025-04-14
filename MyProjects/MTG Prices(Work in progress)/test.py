# # import cloudscraper
# #
# # cookies = {
# #     '_fbp': 'fb.1.1726329987305.686354820688884247',
# #     '_uetvid': '4c21b40072b311ef934a4f02a22642b3',
# #     'PHPSESSID': 'juuvndu58cpqb76n4b8cshg8jj',
# #     '_cfuvid': '6M3cBzmxv_jn5NNCP_mkRf1tcDZxzySRICGHr.gUGwQ-1744375357316-0.0.1.1-604800000',
# #     '__cf_bm': 'fDLLv6D4PsDOYuF5QXzCgcvfSwNTNg2hgEPBKvOOrJ8-1744383413-1.0.1.1-8Lnnmk.sMvRX9WwRL76ZvWoexUQxnYhUDfbm9DOMzOcoCxk.v4F2HbNNFpInSZKUmrHj7hwiF.kIcRJhuFnXuU8nDJfGTcfIOvKnowZLrOM',
# # }
# #
# # headers = {
# #     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
# #     'accept-language': 'en-US,en;q=0.9',
# #     'cache-control': 'max-age=0',
# #     'priority': 'u=0, i',
# #     'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
# #     'sec-ch-ua-mobile': '?0',
# #     'sec-ch-ua-platform': '"Windows"',
# #     'sec-fetch-dest': 'document',
# #     'sec-fetch-mode': 'navigate',
# #     'sec-fetch-site': 'none',
# #     'sec-fetch-user': '?1',
# #     'upgrade-insecure-requests': '1',
# #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
# #     # 'cookie': '_fbp=fb.1.1726329987305.686354820688884247; _uetvid=4c21b40072b311ef934a4f02a22642b3; PHPSESSID=juuvndu58cpqb76n4b8cshg8jj; _cfuvid=6M3cBzmxv_jn5NNCP_mkRf1tcDZxzySRICGHr.gUGwQ-1744375357316-0.0.1.1-604800000; __cf_bm=fDLLv6D4PsDOYuF5QXzCgcvfSwNTNg2hgEPBKvOOrJ8-1744383413-1.0.1.1-8Lnnmk.sMvRX9WwRL76ZvWoexUQxnYhUDfbm9DOMzOcoCxk.v4F2HbNNFpInSZKUmrHj7hwiF.kIcRJhuFnXuU8nDJfGTcfIOvKnowZLrOM',
# # }
# #
# # params = {
# #     'utm_campaign': 'card_prices',
# #     'utm_medium': 'text',
# #     'utm_source': 'scryfall',
# # }
# #
# # scraper = cloudscraper.create_scraper()
# #
# # response = scraper.get(
# #     'https://www.cardmarket.com/en/Magic/Products/Singles/Innistrad-Remastered/Edgar-Markov',
# #     params=params,
# #     cookies=cookies,
# #     headers=headers,
# # )
# #
# # print(response.status_code)
# import undetected_chromedriver as uc
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from time import sleep
# from bs4 import BeautifulSoup
#
# options = uc.ChromeOptions()
# # options.headless = True
# options.add_argument("--disable-extensions")
# options.add_argument("--disable-gpu")
#
# driver = uc.Chrome(options=options)
# driver.get("https://www.cardmarket.com/en/Magic/Products/Singles/Innistrad-Remastered/Edgar-Markov?referrer=scryfall")
#
#
# sleep(10)
#
# try:
#     accept_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Accept')]")
#     accept_button.click()  # Click the accept button to allow cookies
#     sleep(2)  # Wait for a moment to ensure cookies are accepted
# except:
#     print("No cookie consent modal found or already accepted.")
#
# prices = driver.find_elements(By.TAG_NAME, "dd")[4:7]
# # prices = driver.page_source
# # soup = BeautifulSoup(prices, "lxml")
# for x in prices:
#     print(x.text)
#
# driver.quit()

# from prices import cardmarket_price
#
# print(cardmarket_price("https://www.cardmarket.com/en/Magic/Products/Singles/Innistrad-Remastered/Edgar-Markov?referrer=scryfall&utm_campaign=card_prices&utm_medium=text&utm_source=scryfall"))