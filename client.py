import requests

# آدرس سرورت روی Railway (بعد از deploy عوضش کن)
SERVER_URL = "https://your-app.up.railway.app/save"

print("📝 هر چیزی بنویس تا به سرور بفرسته. برای خروج بنویس: exit\n")

while True:
    text = input(">> ")
    
    if text.strip().lower() == "exit":
        print("👋 خداحافظ!")
        break
    
    if not text.strip():
        continue
    
    try:
        response = requests.post(SERVER_URL, json={"text": text}, timeout=10)
        
        if response.status_code == 200:
            print("✅ ارسال شد و ذخیره گردید")
        else:
            print(f"❌ خطا: {response.status_code} - {response.text}")
    
    except Exception as e:
        print(f"❌ خطای اتصال: {e}")