class Item:
    """Kelas untuk menyimpan detail barang"""
    def __init__(self, id_item, nama, stok, harga):
        self.id_item = id_item
        self.nama = nama
        self.stok = stok
        self.harga = harga

    def distribusi(self, jumlah):
        """Mengurangi stok barang untuk didistribusikan"""
        if jumlah > self.stok:
            print(f"Stok tidak cukup untuk mendistribusikan {jumlah} unit {self.nama}.")
        else:
            self.stok -= jumlah
            print(f"{jumlah} unit {self.nama} berhasil didistribusikan.")

    def __str__(self):
        return f"{self.id_item}: {self.nama} - Stok: {self.stok}, Harga: Rp{self.harga}"


class InventoryManager:
    """Kelas untuk mengelola daftar barang dalam inventaris"""
    def __init__(self):
        self.items = {}

    def tambah_item(self, id_item, nama, stok, harga):
        """Menambahkan barang ke inventaris"""
        if id_item in self.items:
            print(f"Barang dengan ID {id_item} sudah ada.")
        else:
            self.items[id_item] = Item(id_item, nama, stok, harga)
            print(f"Barang '{nama}' berhasil ditambahkan.")

    def edit_item(self, id_item, nama=None, stok=None, harga=None):
        """Mengedit barang dalam inventaris"""
        if id_item in self.items:
            if nama:
                self.items[id_item].nama = nama
            if stok is not None:
                self.items[id_item].stok = stok
            if harga is not None:
                self.items[id_item].harga = harga
            print(f"Barang dengan ID {id_item} berhasil diperbarui.")
        else:
            print(f"Barang dengan ID {id_item} tidak ditemukan.")

    def hapus_item(self, id_item):
        """Menghapus barang dari inventaris"""
        if id_item in self.items:
            del self.items[id_item]
            print(f"Barang dengan ID {id_item} berhasil dihapus.")
        else:
            print(f"Barang dengan ID {id_item} tidak ditemukan.")

    def distribusi_barang(self, id_item, jumlah):
        """Mendistribusikan barang kepada konsumen"""
        if id_item in self.items:
            self.items[id_item].distribusi(jumlah)
        else:
            print(f"Barang dengan ID {id_item} tidak ditemukan.")

    def laporan(self):
        """Menampilkan laporan semua barang dalam inventaris"""
        if not self.items:
            print("Tidak ada barang dalam inventaris.")
        else:
            print("\n=== Laporan Inventaris ===")
            for item in self.items.values():
                print(item)
            print("=========================")


def main():
    manager = InventoryManager()

    while True:
        print("\n=== Sistem Manajemen Inventaris ===")
        ("1print. Tambah Barang")
        print("2. Edit Barang")
        print("3. Hapus Barang")
        print("4. Distribusi Barang")
        print("5. Lihat Laporan")
        print("6. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            id_item = input("Masukkan ID Barang: ")
            nama = input("Masukkan Nama Barang: ")
            stok = int(input("Masukkan Stok Barang: "))
            harga = int(input("Masukkan Harga Barang: "))
            manager.tambah_item(id_item, nama, stok, harga)

        elif pilihan == "2":
            id_item = input("Masukkan ID Barang yang akan diedit: ")
            nama = input("Masukkan Nama Baru (kosongkan jika tidak ingin mengubah): ") or None
            stok = input("Masukkan Stok Baru (kosongkan jika tidak ingin mengubah): ")
            harga = input("Masukkan Harga Baru (kosongkan jika tidak ingin mengubah): ")
            stok = int(stok) if stok else None
            harga = int(harga) if harga else None
            manager.edit_item(id_item, nama, stok, harga)

        elif pilihan == "3":
            id_item = input("Masukkan ID Barang yang akan dihapus: ")
            manager.hapus_item(id_item)

        elif pilihan == "4":
            id_item = input("Masukkan ID Barang yang akan didistribusikan: ")
            jumlah = int(input("Masukkan jumlah barang yang akan didistribusikan: "))
            manager.distribusi_barang(id_item, jumlah)

        elif pilihan == "5":
            manager.laporan()

        elif pilihan == "6":
            print("Keluar dari aplikasi. Terima kasih!")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    main()