"""
A file observer that automatically perform hex extractions as new 
raw-data files are being dumped into hex\raw-data
"""

import os
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from hex_extractor import do_extract

logging.basicConfig(level=logging.INFO, filename='fantech.log', format='%(levelname)s - %(message)s')

# Create a stream handler to log messages to the console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(logging.Formatter('%(levelname)s - %(message)s'))

# Add the console handler to the root logger
logging.getLogger().addHandler(console_handler)

# Event handler for filesystem events
class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        # file_extension = os.path.splitext(event.src_path)[1]
        filename, file_extension = os.path.splitext(os.path.basename(event.src_path))
        if file_extension.lower() == '.json':
            logging.info("New Data file detected: [%s]",filename)
            do_extract(event.src_path)
            logging.info("Awaiting next file...")

if __name__ == "__main__":
    # Directory to watch
    path = r"hex\raw-data"

    try:
        # Create the directory if it doesn't exist
        os.makedirs(path, exist_ok=True)
    except OSError as e:
        logging.error(f"Error creating directory: {e}")
        exit(1)

    # Create the observer and event handler
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)

    # Start the observer
    observer.start()
    logging.info("Auto-extractor Started - Awaiting new data files at hex/raw-data")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        logging.warning("Auto-extractor Terminated")
        observer.stop()

    observer.join()