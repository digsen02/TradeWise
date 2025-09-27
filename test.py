from datetime import datetime

from Shareholder import Shareholder
from Company import Company, Market

digsen = Shareholder("digsen")
digsen.portfolio.set_cash(10000000)

testMarket = Market("테스트 시장")

testMarket.add_company(Company("apple", 24, 1000, 10000))
testMarket.add_shareholder(digsen)

apple = testMarket.get_company("apple")
apple.add_order_sell(
    id="asd",
    quantity=10,
    price=1000
)
apple.add_order_sell(
    id="asd",
    quantity=10,
    price=10000
)

is_stop = False

while not is_stop:
    user_input = input("선택: ")

    if user_input == "1":
        is_stop = True

    elif user_input == "2":
        testMarket.show_companies()

    elif user_input == "3":
        testMarket.add_company(Company(input("회사 명: "), int(input("회사 나이: ")), int(input("발행 주: ")), int(input("발행 가: "))))

    elif user_input == "4":
        digsen.buy_stock(market= testMarket, name= input("회사 명: "), quantity= int(input("갯수: ")), price= int(input("가격: ")))

    elif user_input == "5":
        print(digsen.portfolio)

    elif user_input == "6":
        testMarket.get_company("apple").show_order(is_sell = True)
        testMarket.get_company("apple").show_order()

print("종료됨")