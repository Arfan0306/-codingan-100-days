#latihan logika dan komperasi

#membuat gabungan rentang dari angka

#+++++++3----------10++++++

inputUser = int(input("masukan angka yang bernilai\nkurang dari 3 \natau \nlebih dari 10 \n:"))

#+++++++3----------------
#memeriksa angka kurang dari 3
kurang_dari = (inputUser < 3)
print( "kurang dari 3 :",kurang_dari)

#----------10+++++++++
#memeriksa angka lebih dari 10
lebih_dari = ("lebih dari 10 :",inputUser > 10)


#+++++++3----------10++++++
benar = kurang_dari or lebih_dari
print("angka yg anda masukan :",benar)

#-----3+++++10------
#irisan
print("\n",10*"=","\n")
inputUser = int(input("masukan angka yang bernilai\nlebih dari 3 \ndan \nkurang dari 10 \n:"))

#-----3++++++++++++
lebih_drai = (inputUser > 3)
print("lebih dari 3 :",lebih_dari)


#++++++++10----------
kurang_dari = (inputUser < 10)
print("kurang dari 10 :",kurang_dari)
