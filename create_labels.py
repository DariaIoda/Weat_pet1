import os
import csv
import re

# ================== НАСТРОЙКИ ==================
image_folder = r"d:/6 semester/coursework/peat_wet/images"   # ← убедись, что путь правильный!
output_csv = "labels.csv"

# Диапазоны: (начальный номер, конечный номер, класс)
ranges = [
    (6212, 6260, 1),    # DSC06212 - DSC06260 → класс 1 (сухие)
    (6102, 6210, 2),    # DSC06102 - DSC06210 → класс 2
    (6262, 6393, 3),    # DSC06262 - DSC06391 → класс 3
    (6395, 6494, 4),    # DSC06395 - DSC06494 → класс 4
    (6496, 6553, 5),    # DSC06496 - DSC06553 → класс 5
    (6597, 6657, 6),    # DSC06597 - DSC06657 → класс 6
    (6659, 6720, 7),    # DSC06659 - DSC06720 → класс 7
    (6090, 6101, 0),    # DSC06090 - DSC06101 → класс 0 (не торф)
]

# =============================================

data = []
image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.jpg', '.jpeg'))]

print(f"Найдено JPG файлов: {len(image_files)}")

for filename in sorted(image_files):
    # Извлекаем число из имени (например, из DSC06243.JPG → 6243)
    match = re.search(r'DSC0*(\d+)', filename, re.IGNORECASE)
    if not match:
        continue
    num = int(match.group(1))
    
    assigned = False
    for start_num, end_num, class_id in ranges:
        if start_num <= num <= end_num:
            data.append([filename, class_id])
            assigned = True
            break
    
    if not assigned:
        print(f"Предупреждение: файл {filename} (номер {num}) не попал ни в один диапазон")

# Записываем в CSV
with open(output_csv, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['filename', 'class'])
    writer.writerows(data)

print(f"\nГотово! Создано {len(data)} записей в {output_csv}")
if len(data) == 0:
    print("Внимание: ни один файл не попал в диапазоны. Проверь номера!")

full_path = os.path.abspath(output_csv)
print(f"\n✅ Файл создан по пути: {full_path}")