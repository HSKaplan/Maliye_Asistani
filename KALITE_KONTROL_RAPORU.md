# Maliye Asistanı - Manuel Kalite Kontrol Raporu

## 1. Domain Corpus v1.0 Kontrolü
Veri setimiz 5 adet temel vergi kanunundan oluştuğu için rastgele örneklem seçilmemiş, **5 dosyanın tamamı (%100) manuel kontrole tabi tutulmuştur**.

| Kontrol Kriteri | Başarı Oranı | Açıklama |
| :--- | :--- | :--- |
| **Okunabilir metin** | %100 | Tüm PDF'ler karakter bozulması olmadan TXT'ye aktarıldı. |
| **Doğru domain** | %100 | Tüm belgeler doğrudan mevzuat.gov.tr'den alınan vergi kanunlarıdır. |
| **Header/footer temiz** | %100 | Sayfa sonlarındaki "Mevzuat Bilgi Sistemi" yazıları ve yalnız duran sayfa numaraları Regex ile başarıyla temizlendi. |
| **Metadata doğru** | %100 | JSONL formatındaki `document_id`, `title` ve `source` alanları hatasız eşleşti. |

*Hata Sınıflandırması:* Veri seti dar ve resmi formatta olduğu için ekstra bir `extraction_error` veya `out_of_domain` hatası tespit edilmemiştir.

---

## 2. Instruction Dataset v1.0 Kontrolü
Hazırlanan Soru-Cevap (Instruction) setindeki tüm örnekler manuel olarak incelenmiştir.

| Kontrol Kriteri | Durum |
| :--- | :--- |
| **Talimat anlaşılırlığı** | Başarılı. Sorular öğrenci ve mükellef diline uygun sorulmuştur. |
| **Kaynakla tutarlılık** | Başarılı. Cevapların tamamı `source_document` ile belirtilen kanun metnindeki maddelerden teyit edilmiştir. Halüsinasyon engellenmiştir. |
| **Görev türü doğruluğu** | Başarılı. Karşılaştırma, Tanım ve Bilgi Yetersizliği görevleri doğru kategorize edilmiştir. |

**Sonuç:** Her iki veri seti de eğitim (CPT ve SFT) aşamaları için yapısal olarak uygun ve temizdir.