# Maliye ve Vergi Mevzuatı Türkçe Domain Corpus v1.0

## Amaç
Bu veri seti, maliye bölümü öğrencilerinin ve profesyonellerin vergi kanunları konusunda Türkçe sorularını cevaplayabilen alana özel bir dil modelinin continued pretraining (CPT) aşamasında kullanılmak üzere hazırlanmıştır. 

## Kapsam
- **Kapsam içi:** Türk vergi sisteminin temelini oluşturan kanunlar (Vergi Usul Kanunu, Gelir Vergisi, Kurumlar Vergisi, KDV, Amme Alacaklarının Tahsil Usulü).
- **Kapsam dışı:** Uluslararası vergi anlaşmaları, SGK mevzuatı, Türk Ticaret Kanunu ve gümrük mevzuatı.

## Veri Kaynakları
| Kaynak | Tür | Dil | Doküman | Lisans / Kullanım |
| :--- | :--- | :--- | :--- | :--- |
| Mevzuat.gov.tr (T.C. Cumhurbaşkanlığı) | PDF | tr | 5 | Kamuya açık resmi mevzuat |
| **Toplam (Ham)** | | | **5** | |

## Veri Toplama
Dokümanlar doğrudan Mevzuat Bilgi Sistemi (mevzuat.gov.tr) üzerinden PDF formatında indirilmiş olup, orijinal halleriyle `data/raw/` klasöründe saklanmaktadır. 

## İşleme Adımları
1. **Extraction:** Tüm PDF'ler `scripts/01_extract.py` kullanılarak `PyMuPDF` kütüphanesi ile yüksek doğrulukla düz metne (TXT) çevrildi.
2. **Cleaning:** `scripts/02_clean.py` ile Regex kullanılarak; ardışık boşluklar teke indirildi, sayfa sonlarındaki tek başına duran sayfa numaraları temizlendi ve "Mevzuat Bilgi Sistemi" gibi header/footer kalıntıları silindi.
3. **Filtering & Deduplication:** Kullanılan 5 temel kaynak tamamen birbirinden bağımsız kanun metinleri olduğu için exact (tam) veya near (yakın) duplicate tespit edilmedi ve veri kaybı yaşanmadı.

## Format
JSONL. Her satır bir dokümandır ve şu alanları içerir: `document_id`, `title`, `source`, `language`, `document_type`, `char_count`, `text`.

## İstatistikler
- **Final doküman sayısı:** 5
- **Türkçe Oranı:** %100
- **Manuel kalite kontrolü:** 5 dosyanın tamamı işlem sonrası manuel kontrolden geçirilmiş, metin bozulması tespit edilmemiştir.

## Sürüm Geçmişi
- v1.0 (Ekim 2026): İlk extraction, cleaning ve JSONL dönüştürme işlemleri tamamlanarak vize teslimi için hazırlandı.

## Hazırlayanlar
Hilmi Sinan Kaplan (Bilgisayar Mühendisliği Öğrencisi). Danışman: Asım Sinan Yüksel.