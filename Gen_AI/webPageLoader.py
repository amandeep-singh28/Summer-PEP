# pip install bs4
from langchain_community.document_loaders import WebBaseLoader

URL = "https://www.flipkart.com/apple-macbook-neo-a18-pro-2026-pro-8-gb-256-gb-ssd-tahoe-mhff4hn-a/p/itm8c46a289d349a?pid=COMHH8C5GRDQYNCY&lid=LSTCOMHH8C5GRDQYNCYMNIDDD&marketplace=FLIPKART&q=macbook&store=6bo%2Fb5g&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&fm=organic&iid=17b74cb3-5e92-41d1-9b3f-2f3c09cd76cc.COMHH8C5GRDQYNCY.SEARCH&ppt=None&ppn=None&ssid=wa15lnug5c0000001783665056352&qH=864faee128623e2f&ov_redirect=true"

loader = WebBaseLoader(URL)
documents = loader.load()

# print(documents)
print(f"Actual Data:\n{documents[0].page_content}")

print(f"Meta Data:\n{documents[0].metadata}\n")