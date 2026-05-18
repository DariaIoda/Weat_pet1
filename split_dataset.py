import pandas as pd
from sklearn.model_selection import train_test_split

# Настройки
csv_file = r"d:\6 semester\coursework\peat_wet\labels.csv"
train_size = 0.8          # 80% на обучение, 20% на проверку

# Загружаем метки
df = pd.read_csv(csv_file)

# Разделяем с сохранением пропорций классов
train_df, val_df = train_test_split(df, test_size=1-train_size, 
                                    stratify=df['class'], random_state=42)

# Сохраняем
train_df.to_csv("train_labels.csv", index=False)
val_df.to_csv("val_labels.csv", index=False)

print(f"Всего изображений: {len(df)}")
print(f"Train: {len(train_df)} изображений")
print(f"Validation: {len(val_df)} изображений")

# Показываем распределение классов
print("\nРаспределение классов в train:")
print(train_df['class'].value_counts().sort_index())
print("\nРаспределение классов в val:")
print(val_df['class'].value_counts().sort_index())