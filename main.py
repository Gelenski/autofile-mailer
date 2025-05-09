from watchdog.observers import Observer # type: ignore
from watchdog.events import FileSystemEventHandler # type: ignore
from pathlib import Path
import time
import os
from dotenv import load_dotenv # type: ignore

load_dotenv()

tracked_dir = Path(os.getenv("CLIENTS_DIR", "clients/"))

class FileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            trace = Path(event.src_path)
            print(f"File detected: {event.src_path}")

if __name__ == "__main__":
    observer = Observer()
    handler = FileHandler()
    observer.schedule(handler, str(tracked_dir), recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()