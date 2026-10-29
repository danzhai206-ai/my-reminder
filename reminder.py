import json
import datetime
today = datetime.date.today()
print(today)
tasks={
    "2026-10-29": ["pythonの勉強", "ITパスポート勉強"]
}
with open("tasks.json", "w", encoding="utf-8") as f:
    json.dump(tasks,f,ensure_ascii=False)
with open("tasks.json", "r", encoding="utf-8") as f:
    loaded_tasks=json.load(f)
print(loaded_tasks)
print("ファイルの保存先:", __import__("os").getcwd())