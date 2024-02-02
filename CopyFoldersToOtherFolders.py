# -*- coding: utf-8 -*-

import os
import shutil

plik_ze_sciezkami = r'sciezki.txt'
sciezka_bazowa_docelowa = r'kopiowanie_plikow_z_1_do_2_folderu\x'

with open(plik_ze_sciezkami, 'r', encoding='utf-8') as plik:
    for sciezka_zrodlowa in plik:
        sciezka_zrodlowa = sciezka_zrodlowa.strip()  
        if os.path.exists(sciezka_zrodlowa) and os.path.isdir(sciezka_zrodlowa):
            
            ostatni_folder = os.path.basename(os.path.normpath(sciezka_zrodlowa))
            sciezka_docelowa = os.path.join(sciezka_bazowa_docelowa, ostatni_folder)
            
            if not os.path.exists(sciezka_docelowa):
                os.makedirs(sciezka_docelowa)
            
            for plik in os.listdir(sciezka_zrodlowa):
                pelna_sciezka_zrodlowa = os.path.join(sciezka_zrodlowa, plik)
                if os.path.isfile(pelna_sciezka_zrodlowa):
                    shutil.copy(pelna_sciezka_zrodlowa, sciezka_docelowa)
        else:
            print(f"Ścieżka {sciezka_zrodlowa} nie istnieje lub nie jest folderem.")
