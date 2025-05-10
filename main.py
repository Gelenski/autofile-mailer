from watchdog.observers import Observer # type: ignore
from watchdog.events import FileSystemEventHandler # type: ignore
from pathlib import Path
import time
import os
from dotenv import load_dotenv # type: ignore
from app.utils import is_extension_valid, extract_client, extract_file_number

load_dotenv()

tracked_dir = Path(os.getenv("CLIENTS_DIR", "clients/"))

class FileHandler(FileSystemEventHandler):
    def on_created(self, event):
        """
        Handle the creation of a new file in the tracked directory.
        """

        if not event.is_directory:
            trace = Path(event.src_path)
            if is_extension_valid(trace):
                    client = extract_client(trace)
                    file_number = extract_file_number(trace)
                    print("New file detected:", trace, "| Client:", client, "| File_number:", file_number)
            else:
                    print("Directory ignored, invalid file type:", trace)


if __name__ == "__main__":
    observer = Observer()
    handler = FileHandler()
    # Start watching the tracked directory for new files.
    observer.schedule(handler, str(tracked_dir), recursive=True)
    observer.start()
    print("Watching directory:", tracked_dir)
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()