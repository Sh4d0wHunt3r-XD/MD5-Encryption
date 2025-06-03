# MD5 Encoder with File Output

Bu proje, komut satırında girilen bir metni MD5 algoritmasıyla şifreleyip, sonucu belirlediğiniz bir dosyaya kaydeden basit bir Python uygulamasıdır.

---

This project is a simple Python application that encrypts a given text with the MD5 algorithm via the command line and saves the result to a specified file.

---

## Özellikler / Features

- Komut satırından girilen metni MD5 ile şifreler.  
  (Encrypts the text entered via the command line with MD5.)
- Şifrelenmiş metni ve orijinalini belirtilen dosyaya kaydeder.  
  (Saves the encrypted and original text to the specified file.)
- Dosya ve erişim hatalarını kullanıcıya bildirir.  
  (Informs the user about file and access errors.)
- Kullanıcı dostu hata mesajları ve yönlendirmeler içerir.  
  (Contains user-friendly error messages and guidance.)

---

## Kullanım / Usage

1. Python 3 yüklü olmalıdır.  
   (Python 3 must be installed.)
2. Terminal veya komut satırından aşağıdaki şekilde çalıştırılır:  
   (Run the following command in the terminal or command prompt:)

   ```bash
   python md5_encoder.py [şifrelenecek metin / text to encrypt] [kayıt dosyası yolu / save file path]
   ```

   **Örnek / Example:**
   ```bash
   python md5_encoder.py merhaba hashes.txt
   python md5_encoder.py hello hashes.txt
   ```

3. Kayıt dosyası mevcut değilse uyarı alırsınız. Erişim izniniz olmayan dosyalar için hata mesajı verilir.  
   (If the save file does not exist, you will get a warning. If you don't have permission, an error message will be displayed.)
4. Şifrelenmiş ve orijinal metin dosyaya şu şekilde eklenir:  
   (The encrypted and original text will be added to the file as:)
   ```
   [md5_hash]:[orijinal_metin / original_text]
   ```

---

## Uyarı / Warning

> **UYARI / WARNING:**  
> MD5 algoritması günümüzde güvenli bir şifreleme yöntemi değildir ve hassas veri saklamak için önerilmez.  
> (The MD5 algorithm is not considered secure today and is not recommended for storing sensitive data.)
> Bu uygulama sadece eğitim ve deneme amaçlıdır. Gerçek uygulamalarda lütfen daha modern algoritmalar (**bcrypt**, **argon2**, **pbkdf2** vb.) kullanınız.  
> (This application is for educational and testing purposes only. For real applications, please use more modern algorithms such as **bcrypt**, **argon2**, or **pbkdf2**.)

---

## Lisans / License

Bu proje [MIT Lisansı](LICENSE) ile lisanslanmıştır.  
This project is licensed under the [MIT License](LICENSE).
