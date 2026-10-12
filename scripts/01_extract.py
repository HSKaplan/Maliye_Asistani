import os
import pymupdf  # Eski 'fitz' yerine güncel kullanımı ekledik

# Kodun nerede çalıştığına bakılmaksızın klasörlerin yerini otomatik bulmasını sağlıyoruz
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__)) # Bu dosyanın (scripts) konumu
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR) # Ana klasör (Maliye_Asistani) konumu

# Hedef klasörlerimizin kesin ve net yolları (Bilgisayarına göre otomatik ayarlanır)
RAW_DIR = os.path.join(PROJECT_ROOT, "data", "raw")
EXTRACTED_DIR = os.path.join(PROJECT_ROOT, "data", "extracted")

def extract_text_from_pdfs():
    print("Metin çıkarma işlemi başlatılıyor...\n")
    
    basarili_sayisi = 0
    hatali_sayisi = 0

    # Eğer raw klasörü yoksa veya adını yanlış yazdıysak bizi uyarsın
    if not os.path.exists(RAW_DIR):
        print(f"HATA: {RAW_DIR} klasörü bulunamadı! Lütfen 'data' ve 'raw' klasörlerini doğru açtığından emin ol.")
        return

    # raw klasöründeki tüm dosyaları tek tek dönüyoruz
    for filename in os.listdir(RAW_DIR):
        if filename.endswith(".pdf"):
            pdf_yolu = os.path.join(RAW_DIR, filename)
            # Kaydedeceğimiz txt dosyasının adını ayarlıyoruz (Örn: kanun.pdf -> kanun.txt)
            txt_adi = filename.replace(".pdf", ".txt")
            txt_yolu = os.path.join(EXTRACTED_DIR, txt_adi)

            try:
                # PDF dosyasını güncel kütüphane ile açıyoruz
                doc = pymupdf.open(pdf_yolu)
                tum_metin = ""

                # PDF'in tüm sayfalarını dönüp metinleri birleştiriyoruz
                for sayfa in doc:
                    tum_metin += sayfa.get_text()

                # Çıkardığımız metni utf-8 formatında txt olarak kaydediyoruz
                with open(txt_yolu, "w", encoding="utf-8") as f:
                    f.write(tum_metin)

                print(f"BAŞARILI: {filename} -> {txt_adi}")
                basarili_sayisi += 1

            except Exception as e:
                print(f"HATA: {filename} okunamadı. Sebep: {e}")
                hatali_sayisi += 1

    # İşlem Özeti
    print("\n--- İŞLEM ÖZETİ ---")
    print(f"Başarıyla çıkarılan dosya: {basarili_sayisi}")
    print(f"Hatalı (Okunamayan) dosya: {hatali_sayisi}")

if __name__ == "__main__":
    extract_text_from_pdfs()