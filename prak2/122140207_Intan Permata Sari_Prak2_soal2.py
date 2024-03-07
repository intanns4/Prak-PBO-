class Kamar:
    def __init__(self, no_kamar, items, total):
        self.no_kamar = no_kamar
        self.items = items
        self.total = total

    def tampilkan_kamar(self):
        print(f"Nomor kamar : {self.no_kamar}")
        print("Items:")
        for item in self.items:
            print(f"- {item}")
        print(f"Harga Total: Rp{self.total}")

    def __del__(self):
        print(f"Kamar {self.no_kamar} Telah check in!")

def pesanan_decorator(func):
    def wrapper(self, no_kamar, items, total):
        print(f"Pemesanan baru diterima: Pemesanan {no_kamar}")
        func(self, no_kamar, items, total)
    return wrapper

class Redbluehotel:
    def __init__(self, nama):
        self.nama = nama
        self.orders = []

    @pesanan_decorator
    def place_order(self, no_kamar, items, total):
        new_order = Kamar(no_kamar, items, total)
        self.orders.append(new_order)

    def tampilkan_Kamar(self):
        print(f"Orders at {self.nama}:")
        for order in self.orders:
            order.tampilkan_kamar()
            print()



hotel = Redbluehotel("QuickBite")


hotel.place_order(1, ["Deluxe Room", "Superior Twin", "Superior Double"], 26000000)
hotel.place_order(2, ["Suite Room", "Elmi Suite"], 20000000)

hotel.tampilkan_Kamar()

