from myparsers import prom
from myutils.saver import savetoc, savetoj

def main():
    caturl = "https://prom.ua/ua/Domashnyaya-odezhda-zhenskaya"

    maxpages = 4

    products = prom.parse_prom(caturl, maxpages)

    if not products:
        print("Error")
        return

    filef = input("В каком формате сохранить данные? (csv/json): ").strip().lower()

    if filef == "json":
        savetoj(products, "output/prom_products.json")
    else:
        savetoc(products, "output/prom_products.csv")

if __name__ == "__main__":
    main()
