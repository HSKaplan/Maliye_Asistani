import os
import json

# Klasör yollarını otomatik bulma
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)

CLEANED_DIR = os.path.join(PROJECT_ROOT, "data", "cleaned")
FINAL_DIR = os.path.join(PROJECT_ROOT, "data", "final") # Hocanın istediği final klasörü

def create_jsonl():
    print("JSONL formatına dönüştürme işlemi başlatılıyor...\n")
    
    # Final klasörü yoksa otomatik açıyoruz
    if not os.path.exists(FINAL_DIR):
        os.makedirs(FINAL_DIR)
        
    # Çıktı dosyamızın adı (Hocanın beklediği isim)
    output_file = os.path.join(FINAL_DIR, "domain_corpus_v1.jsonl")
    
    islenen = 0
    
    # JSONL dosyasını yazma modunda açıyoruz
    with open(output_file, 'w', encoding='utf-8') as outfile:
        # cleaned klasöründeki temiz txt dosyalarını okuyoruz
        for i, filename in enumerate(os.listdir(CLEANED_DIR)):
            if filename.endswith(".txt"):
                filepath = os.path.join(CLEANED_DIR, filename)
                
                with open(filepath, 'r', encoding='utf-8') as f:
                    text = f.read()
                    
                # Dosya adından başlık üretiyoruz (Örn: "gelir vergisi kanunu.txt" -> "Gelir Vergisi Kanunu")
                title = filename.replace(".txt", "").replace("_", " ").title()
                char_count = len(text)
                
                # Asım Hoca'nın istediği metadata (kimlik) formatı
                metadata = {
                    "document_id": f"DOC_{1000 + i}",
                    "title": title,
                    "source": "mevzuat.gov.tr",
                    "language": "tr",
                    "document_type": "kanun_metni",
                    "char_count": char_count,
                    "text": text
                }
                
                # Bu kimlik bilgilerini ve metni tek bir JSON satırına çeviriyoruz
                json_line = json.dumps(metadata, ensure_ascii=False)
                
                # Çıktı dosyasına satır olarak yazıp alt satıra geçiyoruz
                outfile.write(json_line + '\n')
                
                print(f"EKLENDİ: {title} (Karakter Sayısı: {char_count})")
                islenen += 1

    print("\n--- İŞLEM ÖZETİ ---")
    print(f"Toplam {islenen} kanun başarıyla JSONL formatına dönüştürüldü.")
    print(f"Dosyanız 'data/final/domain_corpus_v1.jsonl' konumunda hazır!")

if __name__ == "__main__":
    create_jsonl()