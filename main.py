from watchdog.observers import Observer # type: ignore
from watchdog.events import FileSystemEventHandler # type: ignore
from pathlib import Path
import time
import os
from dotenv import load_dotenv # type: ignore
from app.utils import is_extension_valid, extract_client

load_dotenv()

tracked_dir = Path(os.getenv("CLIENTS_DIR", "clients/"))

class FileHandler(FileSystemEventHandler):
    def on_created(self, event):
        trace = Path(event.src_path)
        if not event.is_directory:
            client = extract_client(trace)
            print("New file detected:", trace, "Client:", client)
        else:
            print("Directory ignored, invalid file type:", trace)

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