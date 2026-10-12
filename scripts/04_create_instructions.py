import os
import json

# Klasör yollarını otomatik bulma
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
FINAL_DIR = os.path.join(PROJECT_ROOT, "data", "final")

def create_instruction_dataset():
    print("Instruction Dataset v1.0 oluşturuluyor...\n")
    
    if not os.path.exists(FINAL_DIR):
        os.makedirs(FINAL_DIR)
        
    output_file = os.path.join(FINAL_DIR, "instruction_v1.0.jsonl")
    
    # Asım Hoca'nın taksonomisine (görev türlerine) uygun maliye soru-cevap örneklerimiz
    ornek_sorular = [
        {
            "id": "INS_0001",
            "source_document": "DOC_1001", # Gelir Vergisi Kanunu referansı
            "task_type": "tanim_ve_aciklama",
            "generation_method": "manuel_hazirlanmis",
            "messages": [
                {"role": "user", "content": "Gelir Vergisi Kanunu'na göre ticari kazanç nedir?"},
                {"role": "assistant", "content": "Gelir Vergisi Kanunu Madde 37'ye göre, her türlü ticari ve sınai faaliyetlerden doğan kazançlar ticari kazançtır. Örneğin; maden işletmeleri, taş ocakları, özel okul ve hastanelerin işletilmesinden elde edilen kazançlar bu kapsama girer."}
            ]
        },
        {
            "id": "INS_0002",
            "source_document": "DOC_1004", # Vergi Usul Kanunu referansı
            "task_type": "uygulama_adimlari",
            "generation_method": "manuel_hazirlanmis",
            "messages": [
                {"role": "user", "content": "İşe başlama bildirimi vergi dairesine kaç gün içinde yapılmalıdır?"},
                {"role": "assistant", "content": "Vergi Usul Kanunu'na göre tüccarlar, serbest meslek erbabı ve kurumlar vergisi mükellefleri, işe başlama keyfiyetini vergi dairesine bildirmek zorundadır. Bu bildirim, işe başlama tarihinden itibaren 10 gün içinde yapılmalıdır."}
            ]
        },
        {
            "id": "INS_0003",
            "source_document": "DOC_1002", # KDV Kanunu referansı
            "task_type": "karsilastirma",
            "generation_method": "manuel_hazirlanmis",
            "messages": [
                {"role": "user", "content": "KDV'de tam istisna ile kısmi istisna arasındaki fark nedir?"},
                {"role": "assistant", "content": "Tam istisnada (örneğin ihracat teslimleri), mükellefler bu işlemler için yüklendikleri KDV'yi indirim konusu yapabilir ve indiremedikleri kısmı iade alabilirler. Kısmi istisnada ise (örneğin eğitim ve sağlık istisnaları), yüklenilen KDV'nin indirimi veya iadesi mümkün değildir, gider veya maliyet unsuru olarak dikkate alınır."}
            ]
        },
        {
            "id": "INS_0004",
            "source_document": "genel_bilgi",
            "task_type": "bilgi_yetersizligi", # Hocanın özellikle ekleyin dediği, yapay zekanın sınırını bilmesi gereken durum
            "generation_method": "manuel_hazirlanmis",
            "messages": [
                {"role": "user", "content": "2026 yılı enflasyon oranı yüzde kaç olacak?"},
                {"role": "assistant", "content": "Bu soruya cevap veremem. Ben maliye mevzuatı ve vergi kanunları konularında yardımcı olmak üzere tasarlanmış bir asistanım; makroekonomik piyasa tahminleri yapacak verilere sahip değilim. Vergi kanunlarıyla ilgili bir sorunuz olursa yardımcı olabilirim."}
            ]
        }
    ]

    islenen = 0
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for ornek in ornek_sorular:
            json_line = json.dumps(ornek, ensure_ascii=False)
            outfile.write(json_line + '\n')
            islenen += 1
            
    print("--- İŞLEM ÖZETİ ---")
    print(f"Toplam {islenen} adet yüksek kaliteli instruction (Soru-Cevap) örneği oluşturuldu.")
    print(f"Dosyanız 'data/final/instruction_v1.0.jsonl' konumunda hazır!")

if __name__ == "__main__":
    create_instruction_dataset()