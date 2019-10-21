def check_structure_base_data(data):
    assert sorted(list(data.keys())) == [
        "data_zakonczenia_dzialalnosci",
        "gmina",
        "kod_pocztowy",
        "miejscowosc",
        "nazwa",
        "nip",
        "nr_lokalu",
        "nr_nieruchomosci",
        "powiat",
        "regon",
        "silos_id",
        "status_nip",
        "typ",
        "ulica",
        "wojewodztwo",
    ]


def check_structure_address(address):
    assert sorted(list(address)) == [
        "adres",
        "gmina",
        "kod_pocztowy",
        "miejscowosc",
        "nr_lokalu",
        "nr_nieruchomosci",
        "powiat",
        "ulica",
        "wojewodztwo",
    ]


def check_structure_pkd(pkd):
    assert sorted(list(pkd)) == ["kod", "nazwa", "przewazajace"]


def check_structure_contact(contact):
    assert sorted(list(contact)) == ["email", "nr_faksu", "nr_telefonu", "nr_wewnetrzny_telefonu", "www"]


def check_structure_report_f1(details):
    assert sorted(list(details)) == [
        "ad_siedz_gmina_nazwa",
        "ad_siedz_gmina_symbol",
        "ad_siedz_kod_pocztowy",
        "ad_siedz_kraj_nazwa",
        "ad_siedz_kraj_symbol",
        "ad_siedz_miejscowosc_nazwa",
        "ad_siedz_miejscowosc_poczty_nazwa",
        "ad_siedz_miejscowosc_poczty_symbol",
        "ad_siedz_miejscowosc_symbol",
        "ad_siedz_nietypowe_miejsce_lokalizacji",
        "ad_siedz_numer_lokalu",
        "ad_siedz_numer_nieruchomosci",
        "ad_siedz_powiat_nazwa",
        "ad_siedz_powiat_symbol",
        "ad_siedz_ulica_nazwa",
        "ad_siedz_ulica_symbol",
        "ad_siedz_wojewodztwo_nazwa",
        "ad_siedz_wojewodztwo_symbol",
        "adres_email",
        "adres_stronyinternetowej",
        "data_orzeczenia_o_upadlosci",
        "data_powstania",
        "data_rozpoczecia_dzialalnosci",
        "data_skreslenia_dzialalnosci_z_regon",
        "data_skreslenia_z_rejestru_ewidencji",
        "data_wpisu_do_rejestru_ewidencji",
        "data_wpisu_dzialalnosci_do_regon",
        "data_wznowienia_dzialalnosci",
        "data_zaistnienia_zmiany_dzialalnosci",
        "data_zakonczenia_dzialalnosci",
        "data_zakonczenia_postepowania_upadlosciowego",
        "data_zawieszenia_dzialalnosci",
        "nazwa",
        "nazwa_skrocona",
        "nie_podjeto_dzialalnosci",
        "numer_faksu",
        "numer_telefonu",
        "numer_w_rejestrze_ewidencji",
        "numer_wewnetrzny_telefonu",
        "organ_rejestrowy_nazwa",
        "organ_rejestrowy_symbol",
        "regon9",
        "rodzaj_rejestru_nazwa",
        "rodzaj_rejestru_symbol",
    ]


def check_structure_report_f2(details):
    assert sorted(list(details)) == [
        "ad_siedz_gmina_nazwa",
        "ad_siedz_gmina_symbol",
        "ad_siedz_kod_pocztowy",
        "ad_siedz_kraj_nazwa",
        "ad_siedz_kraj_symbol",
        "ad_siedz_miejscowosc_nazwa",
        "ad_siedz_miejscowosc_poczty_nazwa",
        "ad_siedz_miejscowosc_poczty_symbol",
        "ad_siedz_miejscowosc_symbol",
        "ad_siedz_nietypowe_miejsce_lokalizacji",
        "ad_siedz_numer_lokalu",
        "ad_siedz_numer_nieruchomosci",
        "ad_siedz_powiat_nazwa",
        "ad_siedz_powiat_symbol",
        "ad_siedz_ulica_nazwa",
        "ad_siedz_ulica_symbol",
        "ad_siedz_wojewodztwo_nazwa",
        "ad_siedz_wojewodztwo_symbol",
        "adres_email",
        "adres_stronyinternetowej",
        "data_orzeczenia_o_upadlosci",
        "data_powstania",
        "data_rozpoczecia_dzialalnosci",
        "data_skreslenia_dzialalanosci_z_regon",
        "data_wpisu_dzialalnosci_do_regon",
        "data_wznowienia_dzialalnosci",
        "data_zaistnienia_zmiany_dzialalnosci",
        "data_zakonczenia_dzialalnosci",
        "data_zakonczenia_postepowania_upadlosciowego",
        "data_zawieszenia_dzialalnosci",
        "nazwa",
        "nazwa_skrocona",
        "numer_faksu",
        "numer_telefonu",
        "numer_wewnetrzny_telefonu",
        "regon9",
    ]


def check_structure_report_f3(details):
    assert sorted(list(details)) == [
        "ad_siedz_gmina_nazwa",
        "ad_siedz_gmina_symbol",
        "ad_siedz_kod_pocztowy",
        "ad_siedz_kraj_nazwa",
        "ad_siedz_kraj_symbol",
        "ad_siedz_miejscowosc_nazwa",
        "ad_siedz_miejscowosc_poczty_nazwa",
        "ad_siedz_miejscowosc_poczty_symbol",
        "ad_siedz_miejscowosc_symbol",
        "ad_siedz_nietypowe_miejsce_lokalizacji",
        "ad_siedz_numer_lokalu",
        "ad_siedz_numer_nieruchomosci",
        "ad_siedz_powiat_nazwa",
        "ad_siedz_powiat_symbol",
        "ad_siedz_ulica_nazwa",
        "ad_siedz_ulica_symbol",
        "ad_siedz_wojewodztwo_nazwa",
        "ad_siedz_wojewodztwo_symbol",
        "adres_email",
        "adres_stronyinternetowej",
        "data_orzeczenia_o_upadlosci",
        "data_powstania",
        "data_rozpoczecia_dzialalnosci",
        "data_skreslenia_dzialalnosci_z_regon",
        "data_wpisu_do_rejestru_ewidencji",
        "data_wpisu_dzialalnosci_do_regon",
        "data_wznowienia_dzialalnosci",
        "data_zaistnienia_zmiany_dzialalnosci",
        "data_zakonczenia_dzialalnosci",
        "data_zakonczenia_postepowania_upadlosciowego",
        "data_zawieszenia_dzialalnosci",
        "nazwa",
        "nazwa_skrocona",
        "numer_faksu",
        "numer_telefonu",
        "numer_w_rejestrze_ewidencji",
        "numer_wewnetrzny_telefonu",
        "organ_rejestrowy_nazwa",
        "organ_rejestrowy_symbol",
        "regon9",
        "rodzaj_rejestru_nazwa",
        "rodzaj_rejestru_symbol",
    ]


def check_structure_report_p(details):
    assert sorted(list(details)) == [
        "ad_siedz_gmina_nazwa",
        "ad_siedz_gmina_symbol",
        "ad_siedz_kod_pocztowy",
        "ad_siedz_kraj_nazwa",
        "ad_siedz_kraj_symbol",
        "ad_siedz_miejscowosc_nazwa",
        "ad_siedz_miejscowosc_poczty_nazwa",
        "ad_siedz_miejscowosc_poczty_symbol",
        "ad_siedz_miejscowosc_symbol",
        "ad_siedz_nietypowe_miejsce_lokalizacji",
        "ad_siedz_numer_lokalu",
        "ad_siedz_numer_nieruchomosci",
        "ad_siedz_powiat_nazwa",
        "ad_siedz_powiat_symbol",
        "ad_siedz_ulica_nazwa",
        "ad_siedz_ulica_symbol",
        "ad_siedz_wojewodztwo_nazwa",
        "ad_siedz_wojewodztwo_symbol",
        "adres_email",
        "adres_stronyinternetowej",
        "data_orzeczenia_o_upadlosci",
        "data_powstania",
        "data_rozpoczecia_dzialalnosci",
        "data_skreslenia_z_regon",
        "data_wpisu_do_regon",
        "data_wpisu_do_rejestru_ewidencji",
        "data_wznowienia_dzialalnosci",
        "data_zaistnienia_zmiany",
        "data_zakonczenia_dzialalnosci",
        "data_zakonczenia_postepowania_upadlosciowego",
        "data_zawieszenia_dzialalnosci",
        "forma_finansowania_nazwa",
        "forma_finansowania_symbol",
        "forma_wlasnosci_nazwa",
        "forma_wlasnosci_symbol",
        "liczba_jedn_lokalnych",
        "nazwa",
        "nazwa_skrocona",
        "nip",
        "numer_faksu",
        "numer_telefonu",
        "numer_w_rejestrze_ewidencji",
        "numer_wewnetrzny_telefonu",
        "organ_rejestrowy_nazwa",
        "organ_rejestrowy_symbol",
        "organ_zalozycielski_nazwa",
        "organ_zalozycielski_symbol",
        "podstawowa_forma_prawna_nazwa",
        "podstawowa_forma_prawna_symbol",
        "regon9",
        "rodzaj_rejestru_ewidencji_nazwa",
        "rodzaj_rejestru_ewidencji_symbol",
        "status_nip",
        "szczegolna_forma_prawna_nazwa",
        "szczegolna_forma_prawna_symbol",
    ]


def check_structure_report_lf(details):
    assert sorted(list(details)) == [
        "ad_siedz_gmina_nazwa",
        "ad_siedz_gmina_symbol",
        "ad_siedz_kod_pocztowy",
        "ad_siedz_kraj_nazwa",
        "ad_siedz_kraj_symbol",
        "ad_siedz_miejscowosc_nazwa",
        "ad_siedz_miejscowosc_poczty_nazwa",
        "ad_siedz_miejscowosc_poczty_symbol",
        "ad_siedz_miejscowosc_symbol",
        "ad_siedz_nietypowe_miejsce_lokalizacji",
        "ad_siedz_numer_lokalu",
        "ad_siedz_numer_nieruchomosci",
        "ad_siedz_powiat_nazwa",
        "ad_siedz_powiat_symbol",
        "ad_siedz_ulica_nazwa",
        "ad_siedz_ulica_symbol",
        "ad_siedz_wojewodztwo_nazwa",
        "ad_siedz_wojewodztwo_symbol",
        "data_powstania",
        "data_rozpoczecia_dzialalnosci",
        "data_skreslenia_z_regon",
        "data_wpisu_do_regon",
        "data_wpisu_do_rejestru_ewidencji",
        "data_wznowienia_dzialalnosci",
        "data_zaistnienia_zmiany",
        "data_zakonczenia_dzialalnosci",
        "data_zawieszenia_dzialalnosci",
        "forma_finansowania_nazwa",
        "forma_finansowania_symbol",
        "nazwa",
        "nie_podjeto_dzialalnosci",
        "numerw_rejestrze_ewidencji",
        "organ_rejestrowy_nazwa",
        "organ_rejestrowy_symbol",
        "regon14",
        "rodzaj_rejestru_nazwa",
        "rodzaj_rejestru_symbol",
        "silos_id",
        "silos_nazwa",
    ]


def check_structure_report_lp(details):
    assert sorted(list(details)) == [
        "ad_siedz_gmina_nazwa",
        "ad_siedz_gmina_symbol",
        "ad_siedz_kod_pocztowy",
        "ad_siedz_kraj_nazwa",
        "ad_siedz_kraj_symbol",
        "ad_siedz_miejscowosc_nazwa",
        "ad_siedz_miejscowosc_poczty_nazwa",
        "ad_siedz_miejscowosc_poczty_symbol",
        "ad_siedz_miejscowosc_symbol",
        "ad_siedz_nietypowe_miejsce_lokalizacji",
        "ad_siedz_numer_lokalu",
        "ad_siedz_numer_nieruchomosci",
        "ad_siedz_powiat_nazwa",
        "ad_siedz_powiat_symbol",
        "ad_siedz_ulica_nazwa",
        "ad_siedz_ulica_symbol",
        "ad_siedz_wojewodztwo_nazwa",
        "ad_siedz_wojewodztwo_symbol",
        "data_powstania",
        "data_rozpoczecia_dzialalnosci",
        "data_skreslenia_z_regon",
        "data_wpisu_do_regon",
        "data_wpisu_do_rejestru_ewidencji",
        "data_wznowienia_dzialalnosci",
        "data_zaistnienia_zmiany",
        "data_zakonczenia_dzialalnosci",
        "data_zawieszenia_dzialalnosci",
        "forma_finansowania_nazwa",
        "forma_finansowania_symbol",
        "nazwa",
        "numer_wrejestrze_ewidencji",
        "organ_rejestrowy_nazwa",
        "organ_rejestrowy_symbol",
        "regon14",
        "rodzaj_rejestru_ewidencji_nazwa",
        "rodzaj_rejestru_ewidencji_symbol",
    ]
