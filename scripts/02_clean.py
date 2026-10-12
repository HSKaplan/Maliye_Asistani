import os
import re

# Klasör yollarını otomatik bulma
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)

EXTRACTED_DIR = os.path.join(PROJECT_ROOT, "data", "extracted")
CLEANED_DIR = os.path.join(PROJECT_ROOT, "data", "cleaned")

def clean_text(text):
    # 1. Boşluk (Whitespace) Normalizasyonu: Yan yana birden fazla boşluğu tek boşluğa indirir
    text = re.sub(r'[ \t]+', ' ', text)
    
    # 2. Üst üste binen çoklu satır sonlarını (enter) teke/ikiye indirir
    text = re.sub(r'\n{3,}', '\n\n', text)
    
    # 3. Sadece sayılardan oluşan satırları (sayfa numaralarını) siler.
    # Not: Madde 15 gibi içinde yazı olan sayıları silmez, sadece tek başına duran sayıları siler.
    text = re.sub(r'^\s*\d+\s*$', '', text, flags=re.MULTILINE)
    
    # 4. Mevzuat sistemindeki standart header kalıntılarını temizler (Eğer varsa)
    text = re.sub(r'Mevzuat Bilgi Sistemi', '', text, flags=re.IGNORECASE)
    
    return text.strip()

def process_cleaning():
    print("Metin temizleme işlemi (Cleaning) başlatılıyor...\n")
    
    # Klasör kontrolü
    if not os.path.exists(CLEANED_DIR):
        print(f"HATA: '{CLEANED_DIR}' klasörü bulunamadı. Lütfen data klasörünün içinde 'cleaned' adında bir klasör aç.")
        return

    islenen = 0
    
    # extracted klasöründeki txt dosyalarını sırayla okuyoruz
    for filename in os.listdir(EXTRACTED_DIR):
        if filename.endswith(".txt"):
            input_path = os.path.join(EXTRACTED_DIR, filename)
            output_path = os.path.join(CLEANED_DIR, filename)
            
            with open(input_path, 'r', encoding='utf-8') as f:
                raw_text = f.read()
                
            # Temizleme fonksiyonumuzu çalıştırıyoruz
            cleaned_text = clean_text(raw_text)
            
            # Temizlenmiş metni cleaned klasörüne kaydediyoruz
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(cleaned_text)
                
            print(f"TEMİZLENDİ: {filename}")
            islenen += 1

    print("\n--- İŞLEM ÖZETİ ---")
    print(f"Başarıyla temizlenen dosya sayısı: {islenen}")
    print("Veriler yapay zeka eğitimine bir adım daha yaklaştı!")

if __name__ == "__main__":
    process_cleaning()