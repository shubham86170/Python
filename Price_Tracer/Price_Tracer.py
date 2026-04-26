import requests
from bs4 import BeautifulSoup

class PriceTracer:
    def __init__(self, url, target_price):
        self.url = url
        self.target_price = target_price
        self.user_agent = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36"}
        self.response = requests.get(url = self.url , headers = self.user_agent).text
        self.soup = None

    def fetch_page(self):       # This method handle network of page not found error
       
        try:        # Check if request was successful
            response = requests.get(self.url, headers=self.user_agent)
            
            if response.status_code == 200:
                self.soup = BeautifulSoup(response.text, "lxml")
            else:
                print("Error: Unable to fetch page (Status Code:", response.status_code, ")")

        except requests.exceptions.RequestException as e:
            print("Network Error:", e)


    def product_title(self):        # This method 
        title = self.soup.find("span", {"id":"productTitle"})
        if title is not None:
            return title.text.strip()
        else:
            return "Tag Not Found"

    def product_price(self):        # This method get the product price
       
        try:
            product_price = self.soup.find("span", {"class": "a-price-whole"})

            if product_price:
                price_text = product_price.text.strip()
                return price_text
            else:
                print("Price not found on page")
                return None

        except Exception as e:
            print("Error while extracting price:", e)
            return None
        
    def convert_price(self, price_in_number):   # This method convert the price into numeric value
        
        try:
            price_in_number = price_in_number.replace(",", "").replace(".", "")
            return int(price_in_number)

        except Exception as e:
            print("Error converting price:", e)
            return None
        
    def compare_price(self, current_price):     # This method compare the price with target price
        
        if current_price <= self.target_price:
            print("Good deal! Price is within your target. You can buy it.")
        else:
            print("Price is too high. Better wait or see something other.")
        
    def run(self):              # This method helps to run in sequence way
        self.fetch_page()

        if self.soup:
            price_in_number = self.product_price()

            if price_in_number:
                numeric_price = self.convert_price(price_in_number)

                if numeric_price:
                    print(self.product_title(), "\nCurrent Price:", numeric_price)
                    self.compare_price(numeric_price)


url = "https://www.amazon.in/Samsung-Creative-ProVisual-Customized-Processor/dp/B0GL8BF2X2/ref=pd_sbs_d_sccl_1_4/523-5531168-6586900?pd_rd_w=o26ig&content-id=amzn1.sym.d1406b44-aa69-47e4-9270-f613e12d52dc&pf_rd_p=d1406b44-aa69-47e4-9270-f613e12d52dc&pf_rd_r=FZXFD5WACSFPGZQ12JPT&pd_rd_wg=ljZBk&pd_rd_r=dc512926-9d9e-4e63-b7c3-6d311c665e76&pd_rd_i=B0GL8BF2X2&psc=1"
target_price = 100000
tracker = PriceTracer(url, target_price)
tracker.run()