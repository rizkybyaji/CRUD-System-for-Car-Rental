data_mobil = [{'Tipe Mobil' : 'Gtr', 'Merk Mobil' : 'Nissan', 'Transmisi' : 'MT', 'Tahun' : '2013', 'Harga Sewa' : '2.000.000'},
              {'Tipe Mobil' : 'F90', 'Merk Mobil' : 'Bmw', 'Transmisi' : 'AT', 'Tahun' : '2016', 'Harga Sewa' : '1.500.000'}]

def confirmation():
    # Fungsi untuk mengkonfirmasi tindakan kepada pengguna
    while True:
        jawaban = input('Apakah Anda yakin? (Y:Ya / T:Tidak) : ').upper()
        if jawaban in ('Y', 'T'):
            return jawaban
        else:
            print('\nMasukkan jawaban yang valid (Y/T)')

def rollback_menu():
    # Fungsi untuk kembali ke menu utama
    while True:
        balik_menu = input('\nKembali ke menu utama? (Y:Ya / T:Tidak) : ').upper()
        if balik_menu == 'T':
            list_cars()
        elif balik_menu == 'Y':
            main()
        else:
            print('\nMasukkan jawaban yang valid (Y/T)')
            list_cars()

def cars_type():
    # Fungsi untuk menambahkan data tipe mobil
    while True:
        tipe_mobil = input('Masukkan tipe mobil : ').title()
        if not all(idx.isalnum() or idx.isspace() for idx in tipe_mobil):
            print ('\nInput hanya dapat berupa alfabet, angka, dan spasi\n')
        else:
            return tipe_mobil
        
def cars_brand():
    # Fungsi untuk menambahkan data merk mobil
    while True:
        merk_mobil = input('Masukkan merk mobil : ').title()
        if not all(idx.isalnum() or idx.isspace() for idx in merk_mobil):
            print('\nInput hanya dapat berupa alfabet, angka, dan spasi\n')
        else:
            return merk_mobil

def transmision():
    # Fungsi untuk menambahkan data transmisi mobil
    while True:
        transmisi = input('Masukkan transmisi mobil (AT/MT) : ').upper()
        if transmisi in ('AT', 'MT'):
            return transmisi
        else:
            print('\nMasukkan jawaban yang valid (AT/MT)\n')

def year():
    # Fungsi untuk menambahkan data tahun mobil
    while True:
        tahun = input('Masukkan tahun mobil : ')
        if len(tahun) != 4 or not tahun.isdigit():
            print('\nInput harus berupa angka dan berjumlah 4 karakter, silahkan masukkan lagi\n')
        else:
            return tahun
        
def price():
    # Fungsi untuk menambahkan data harga sewa mobil
    while True:
        harga = input('Masukkan harga sewa per hari : ')
        if not harga.isdigit():
            print('\nInput harus berupa angka\n')
        else:
            harga_sewa = f'{int(harga):,}'.replace(',', '.')
            return harga_sewa

def add_cars():
    # Fungsi untuk menambahkan data mobil
    tipe_mobil = cars_type()
    merk_mobil = cars_brand()
    transmisi = transmision()
    tahun = year()
    harga_sewa = price()

    print('\nAnda akan menambahkan data mobil dengan detail :')
    print(f'Tipe Mobil : {tipe_mobil} \nMerk Mobil : {merk_mobil} \nTransmisi : {transmisi} \nTahun : {tahun} \nHarga Sewa : {harga_sewa}')

    if confirmation() == 'Y':
        data_mobil.append({'Tipe Mobil' : tipe_mobil, 'Merk Mobil' : merk_mobil, 'Transmisi' : transmisi, 'Tahun' : tahun, 'Harga Sewa' : harga_sewa})
        print('\nData mobil berhasil ditambahkan')
    else:
        print('\nPenambahan data mobil dibatalkan')

def list_cars():
    # Fungsi untuk menampilkan data mobil
    if not data_mobil:
        print('\nTidak ada data mobil yang tersedia untuk ditampilkan')
    else:
        print('===============================================================================')
        print('| No |    Tipe Mobil    |    Merk Mobil    | Transmisi | Tahun |  Harga Sewa  |')
        print('===============================================================================')
        for idx, data in enumerate(data_mobil, start=1):
            tipe = data['Tipe Mobil'].title().ljust(16)  # Justifikasi ke kiri, maksimal 16 karakter
            merk = data['Merk Mobil'].title().ljust(16)  # Justifikasi ke kiri, maksimal 16 karakter
            transmisi = data['Transmisi'].upper().center(9)  # Pusatkan, maksimal 9 karakter
            tahun = data['Tahun'].center(5)  # Pusatkan, maksimal 5 karakter
            sewa = data['Harga Sewa'].rjust(12)  # Justifikasi ke kanan, maksimal 12 karakter
            print(f"| {idx:2d} | {tipe} | {merk} | {transmisi} | {tahun} | {sewa} |")
        print("===============================================================================")
        
def edit_cars():
    # Fungsi untuk mengubah data mobil
    if not data_mobil:
        print('\nTidak ada data mobil yang tersedia untuk diubah')
        return rollback_menu()
    else:
        list_cars()
        while True:
            edit = input('Masukkan nomor mobil yang ingin diubah : ')
            if not edit.isdigit():
                print('\nInput harus berupa angka, silahkkan pilih kembali\n')
                return edit_cars()
            else:
                idx_edit = int(edit) - 1
                if 0 <= idx_edit < len(data_mobil):
                    print('\nAnda akan mengubah data mobil dengan detail: ')
                    print(f'Tipe Mobil : {data_mobil[idx_edit]['Tipe Mobil']}\nMerk Mobil : {data_mobil[idx_edit]['Merk Mobil']}\nTransmisi : {data_mobil[idx_edit]['Transmisi']}\nTahun: {data_mobil[idx_edit]['Tahun']}\nHarga Sewa: {data_mobil[idx_edit]['Harga Sewa']}')
                    if confirmation() == 'Y':
                        while True:
                            print('\nMenu Ubah Data: \n1. Tipe Mobil\n2. Merk Mobil\n3. Transmisi\n4. Tahun\n5. Harga Sewa\n0. Kembali')
                            jenis_edit = (input('\nMasukkan data yang ingin diubah : '))
                            tipe_edit = ''
                            data_penampung = ''
                            batal = ('Data batal diubah')

                            if not jenis_edit.isdigit():
                                print('Input tidak valid, silahkan pilih kembali')
                                continue
                            elif jenis_edit == '1':
                                tipe_edit = 'Tipe Mobil'
                                data_penampung = cars_type()
                            elif jenis_edit == '2':
                                tipe_edit = 'Merk Mobil'
                                data_penampung = cars_brand()
                            elif jenis_edit == '3':
                                tipe_edit = 'Transmisi'
                                data_penampung = transmision()
                            elif jenis_edit == '4':
                                tipe_edit = 'Tahun'
                                data_penampung = year()
                            elif jenis_edit == '5':
                                tipe_edit = 'Harga Sewa'
                                data_penampung = price()
                            elif jenis_edit == '0':
                                edit_cars()
                            else:
                                print('Pilihan tidak tersedia, silahkan pilih kembali')
                                continue

                            if confirmation() == 'Y':
                                data_baru = data_penampung
                                data_mobil[idx_edit][tipe_edit] = data_baru
                                print('\nData mobil berhasil diubah')
                                return main()
                            else:
                                print(batal)
                                return main()
                    else:
                        print('\nPengubahan data mobil dibatalkan')
                        return
                else:
                    print('\nNomor mobil tidak valid')
                    return edit_cars()

def delete_cars():
    # Fungsi untuk menghapus data mobil
    if not data_mobil:
        print('\nTidak ada data mobil yang tersedia untuk dihapus')
        rollback_menu()
    else:
        list_cars()
        while True:
            hapus = input('Masukkan nomor mobil yang ingin dihapus : ')
            if not hapus.isdigit():
                print('\nInput tidak valid, silahkkan pilih kembali\n')
                return delete_cars()
            else:
                idx_hapus = int(hapus) - 1
                if 0 <= idx_hapus < len(data_mobil):
                    print('\nAnda akan menghapus data mobil dengan detail :')
                    print(f'Tipe Mobil : {data_mobil[idx_hapus]['Tipe Mobil']}\nMerk Mobil : {data_mobil[idx_hapus]['Merk Mobil']}\nTransmisi : {data_mobil[idx_hapus]['Transmisi']}\nTahun: {data_mobil[idx_hapus]['Tahun']}\nHarga Sewa: {data_mobil[idx_hapus]['Harga Sewa']}')
                    if confirmation() == 'Y':
                        data_mobil.pop(idx_hapus)
                        print('\nData mobil berhasil dihapus')
                        return
                    else:
                        print('\nPenghapusan data mobil dibatalkan')
                        return
                else:
                    print('\nNomor mobil tidak valid')
                    return delete_cars()

def main():
    # Fungsi main menu
    while True:
        print('\n*****Selamat datang di Capstone Project Module 1 by M RIZKY BAYU AJI*****')
        print("\nPilihan Menu :\n")
        print("1. Tambah Mobil")
        print("2. Tampilkan Mobil")
        print("3. Edit Mobil")
        print("4. Hapus Mobil")
        print("5. Keluar")

        pilihan = input("\nPilih menu: ")
        
        if pilihan == "1":
            add_cars()
        elif pilihan == "2":
            list_cars()
            rollback_menu()
        elif pilihan == "3":
            edit_cars()
        elif pilihan == "4":
            delete_cars()
        elif pilihan == "5":
            print("\nTerima kasih!")
            raise SystemExit
        else:
            print("Pilihan tidak valid, silakan pilih kembali.")

if __name__ == "__main__":
    main()