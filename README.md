# Maliye Öğrencileri İçin RAG Destekli Akıllı Mevzuat Asistanı

Bu proje, maliye bölümü öğrencilerinin ve profesyonellerin karmaşık vergi kanunları içinde aradıkları spesifik bilgilere hızlı ve doğru bir şekilde ulaşmalarını sağlamak amacıyla geliştirilmektedir. 

Vize dönemi kapsamında, model eğitiminde (CPT ve SFT aşamaları) kullanılacak olan "Domain Corpus" ve "Instruction Dataset" veri setleri, resmi mevzuat kaynaklarından elde edilerek yapay zeka eğitimine uygun hale getirilmiştir.

## Klasör Yapısı
- `data/raw/`: İndirilen orijinal PDF kanun metinleri.
- `data/extracted/`: PDF'lerden çıkarılan ham metin dosyaları (TXT).
- `data/cleaned/`: Gereksiz boşluklardan ve sayfa numaralarından arındırılmış metinler.
- `data/final/`: Model eğitimine hazır JSONL formatındaki final veri setleri.
- `scripts/`: Veri işleme, temizleme ve dönüştürme işlemlerini otomatize eden Python kodları.

## Kodların Çalıştırılma Sırası
Projeyi sıfırdan derlemek için `scripts` klasöründeki kodları şu sırayla çalıştırabilirsiniz:
1. `python scripts/01_extract.py` (PDF'leri metne çevirir)
2. `python scripts/02_clean.py` (Metinleri temizler)
3. `python scripts/03_to_jsonl.py` (Domain Corpus JSONL dosyasını oluşturur)
4. `python scripts/04_create_instructions.py` (Instruction JSONL dosyasını oluşturur)

## Veri Seti Raporları
Veri setlerinin detaylı istatistikleri, kaynakları ve kalite kontrol raporları için lütfen `DATASET_CARD.md` ve `INSTRUCTION_CARD.md` dosyalarını inceleyiniz.