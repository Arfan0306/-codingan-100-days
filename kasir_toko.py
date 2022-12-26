# dictionary untuk menyimpan informasi produk
products = {
    "item1": {"name": "Shampoo", "price": 10000},
    "item2": {"name": "Sabun", "price": 5000},
    "item3": {"name": "Pembalut", "price": 7000},
}

# variabel untuk menyimpan informasi transaksi
transaction_items = []
total_price = 0

while True:
    # menampilkan menu dan meminta input dari user
    print("Selamat datang di toko kami!")
    print("Produk yang tersedia:")
    for item_id, item_info in products.items():
        print(f"{item_id}: {item_info['name']} ({item_info['price']} IDR)")
    print("\n")
    print("Silakan masukkan kode produk yang ingin dibeli (atau 'q' untuk mengakhiri transaksi)")
    item_id = input()
    
    # jika user memasukkan 'q', maka transaksi diakhiri
    if item_id == "q":
        break
    
    # jika produk yang diminta tersedia, maka tambahkan produk ke daftar transaksi
    if item_id in products:
        item = products[item_id]
        transaction_items.append(item)
        total_price += item["price"]
        print(f"{item['name']} ditambahkan ke daftar transaksi")
    else:
        print("Maaf, produk yang diminta tidak tersedia")

# menampilkan rincian transaksi
print("\nRincian transaksi:")
for item in transaction_items:
    print(f"- {item['name']} ({item['price']} IDR)")
print(f"Total: {total_price} IDR")
