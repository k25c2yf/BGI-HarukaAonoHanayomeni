import os

directory = './big5'  # 設定目錄路徑

for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        file_path = os.path.join(directory, filename)
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        content = content.replace("竜", "龍")
        
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)