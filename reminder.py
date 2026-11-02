import json
import datetime
from winotify import Notification

today = datetime.date.today().isoformat()
print(today)

tasks = {
    today: ["pythonの勉強", "ITパスポート勉強"]
}
with open("tasks.json", "w", encoding="utf-8") as f:
    json.dump(tasks,f,ensure_ascii=False)
with open("tasks.json", "r", encoding="utf-8") as f:
    loaded_tasks=json.load(f)
print(loaded_tasks)
today_tasks=loaded_tasks.get(today, [])
if today_tasks:
   message = "\n".join(today_tasks)
   notification=Notification(
    app_id="リマインダー",
     title="今日のタスク",
     msg=message,
   )
   notification.show()