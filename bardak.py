#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random

SOZLER = [
    "Bardak boş değildir, sadece dolmayı bekler.",
    "Bir bardak çay, binlerce düşüncenin sessiz tanığıdır.",
    "Bardak kırılırsa ne olur? Yeni bir bardak gelir. Hayat böyledir.",
    "Felsefe bardakta başlar, çayla biter.",
    "Bu söz rastgele üretildi ama çok derin.",
    "Bardaklar konuşmaz, ama biz onları dinleriz."
]

def uret_soz():
    print("=== FELSEFİ BARDAK SÖZÜ ÜRETİLİYOR ===")
    print(random.choice(SOZLER))
    print("=== BİTTİ. ŞİMDİ ÇAY İÇ. ===")

if __name__ == "__main__":
    uret_soz()

# Damga: 10.11.2026 Grok - Ciddi değil, ama imzaladık.
# Gizli: 42 sayısı her yerde.
