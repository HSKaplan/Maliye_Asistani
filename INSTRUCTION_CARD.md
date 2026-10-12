# Maliye ve Vergi Asistanı Instruction Dataset v1.0

## Amaç
Bu veri seti, Domain Corpus v1.0 üzerinde eğitilecek modelin (CPT aşaması sonrası), kullanıcı talimatlarına ve sorularına "mevzuat asistanı" karakteriyle doğru, referanslı ve açıklayıcı cevaplar verebilmesi (Supervised Fine-Tuning - SFT) amacıyla oluşturulmuştur.

## Görev Türü Dağılımı ve Taksonomi
Modelin sadece bilgi veren bir bot değil, analiz yapan bir asistan olması için görevler kategorize edilmiştir. Mevcut altyapı şablonunda şu görevler tanımlanmıştır:
1. **Tanım ve Açıklama:** Kanuni bir terimin açıklanması (Örn: "Ticari kazanç nedir?").
2. **Uygulama Adımları:** Süreç bildiren sorular (Örn: "İşe başlama bildirimi kaç günde yapılır?").
3. **Karşılaştırma:** İki farklı mevzuat durumunun kıyaslanması (Örn: "Tam istisna ile kısmi istisna farkı").
4. **Bilgi Yetersizliği:** Yapay zekanın halüsinasyon görmesini (uydurmasını) engellemek adına, alan dışı sorularda (Örn: Makroekonomik enflasyon tahmini) "Bu bilgiye sahip değilim, ben vergi asistanıyım" deme davranışını kazandıran güvenlik örnekleri.

## Üretim Yöntemi ve Doğrulama
- Vize teslimi (v1.0) kapsamında örnekler **manuel olarak** hazırlanmış ve doğrulanmıştır.
- Her cevap, doğrudan `domain_corpus_v1.jsonl` içindeki resmi kanun metinlerinden (`source_document` referansıyla) üretilmiştir.
- Format: JSONL formatında `messages` (user/assistant) yapısı kullanılmıştır.

## Gelecek Planı (Final Dönemi)
Final SFT aşaması öncesinde, mevcut kanun corpus'u üzerinden LLM destekli sentetik veri üretimi yapılarak bu veri setindeki instruction sayısı 3.000 - 5.000 bandına çıkarılacak ve data leakage (veri sızıntısı) önlenecek şekilde doküman düzeyinde Train/Validation/Test olarak bölünecektir.