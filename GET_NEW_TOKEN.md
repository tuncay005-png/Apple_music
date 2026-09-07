# ⚠️ YANDEX MUSIC TOKEN YENİLƏMƏK LAZIMDIR

Token-ınız işləmir və ya vaxtı keçib. Yeni token əldə etməlisiniz.

---

## 🔑 ÜSUL 1: Brauzerdə (Ən asan)

1. **Yandex Music**-ə daxil olun:
   https://music.yandex.ru/

2. **F12** basın (Developer Console açılacaq)

3. **Console** tabına keçin

4. Bu kodu **kopyalayıb yapışdırın** və Enter basın:

```javascript
console.log(localStorage.getItem('access_token'));
```

5. Çıxan token-i kopyalayın (uzun hərflər və rəqəmlər)

6. Token belə görünəcək:
   ```
   y0_AgA...uzun_string...xyz
   ```

7. `.env` faylında `YANDEX_TOKEN=` hissəsini yeni token ilə əvəz edin

---

## 🔑 ÜSUL 2: Python ilə (Username və Password lazımdır)

```powershell
pip install yandex-music-token
yandex-music-token
```

Username və password soruşacaq, token verəcək.

---

## ✅ YENİ TOKEN-I ƏLAVƏ ETMƏK:

### Lokal istifadə üçün (.env faylı):

1. `.env` faylını açın (Notepad ilə)

2. Bu sətrı tapın:
   ```
   YANDEX_TOKEN=y0__wgBENiDg8cHGIqPSSD86ff5GDDLm_ifCJZV9IbpHhSps_glxbeGg9EVMtzc
   ```

3. Yeni token ilə əvəz edin:
   ```
   YANDEX_TOKEN=YENI_TOKEN_BURAYA
   ```

4. Saxlayın

### GitHub Actions üçün (GitHub Secrets):

1. https://github.com/tuncay005-png/Apple_music/settings/secrets/actions

2. **YANDEX_TOKEN** secret-ini tapın

3. **Update** düyməsi

4. Yeni token-i yapışdırın

5. **Update secret**

---

## 🧪 TEST ETMƏK:

```powershell
cd c:\Users\Tuncay\Desktop\Apple_music
python test_config.py
```

Əgər ✅ görürsüzsə - token işləyir!

---

## 📝 QEYD:

Yandex Music token-ları **müvəqqətidir** və vaxtaşırı yeniləmək lazımdır.
Token-ı hər dəfə yeniləməli olsanız, bu normaldır.

Alternativ olaraq, Yandex Plus abunəliyi ilə daha uzun müddətli token-lar əldə edə bilərsiniz.
