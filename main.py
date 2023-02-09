from classes.store import Store
from classes.shop import Shop
from classes.request import Request


def main():
    store = Store()
    shop = Shop()

    store.add("хлеб", 20)
    store.add("творог", 20)
    store.add("мясо", 20)

    shop.add("хлеб", 3)
    shop.add("творог", 3)
    shop.add("мясо", 3)

    stop_words = ["стоп", "выход"]

    while True:
        user_input = input()

        if user_input in stop_words:
            exit()

        request = Request(user_input)

        if request.product not in store.get_items().keys():
            print("Такой товар отсутствует, попробуйте ввести другой")
            continue
        if store.get_items().get(request.product) >= request.amount and shop.get_free_space() >= request.amount:
            print("Нужное количество есть на складе и в магазине достаточно места")
        elif store.get_items().get(request.product) >= request.amount and shop.get_free_space() <= request.amount:
            print("Нужное количество есть на складе, но в магазине недостаточно места, попробуйте заказать меньше")
            continue
        else:
            print("Выбранного товара не хватает на складе, попробуйте заказать меньше")
            continue

        store.remove(request.product, request.amount)
        print(f"Курьер забрал {request.amount} {request.product} со склад")
        print(f"Курьер везет {request.amount} {request.product} со склад в магазин")
        shop.add(request.product, request.amount)
        print(f"Курьер доставил {request.amount} {request.product} в магазин")

        print("В склад хранится:")
        for k, v in store.get_items().items():
            print(v, k)

        print("В магазин хранится:")
        for k, v in shop.get_items().items():
            print(v, k)


if __name__ == "__main__":
    main()
