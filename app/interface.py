from typing import TypedDict


class ResultInterface(TypedDict):
    agir_hasta_sayisi: int
    gunluk_iyilesen: int
    gunluk_test: int
    gunluk_vaka: int
    gunluk_vefat: int
    hastalarda_zaturre_oran: float
    tarih: str
    toplam_entube: int
    toplam_iyilesen: int
    toplam_test: int
    toplam_vaka: int
    toplam_vefat: int
    toplam_yogun_bakim: int
