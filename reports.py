import sqlite3
from datetime import datetime

class ReportManager:
    def __init__(self, db_name="compliance_reports.db"):
        self.db_name = db_name
        self._initialize_db()

    def _initialize_db(self):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS reports (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        bucket_name TEXT,
                        issue TEXT,
                        timestamp TEXT
                    )''')
        conn.commit()
        conn.close()

    def store_report(self, bucket_name, issues):
        if not issues:
            return

        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        for issue in issues:
            c.execute(
                "INSERT INTO reports (bucket_name, issue, timestamp) VALUES (?, ?, ?)",
                (bucket_name, issue, timestamp)
            )

        conn.commit()
        conn.close()
        print(f" Stored {len(issues)} issues for '{bucket_name}' in {self.db_name}.")
