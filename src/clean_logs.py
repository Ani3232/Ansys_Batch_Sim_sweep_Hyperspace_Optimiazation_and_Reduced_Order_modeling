import os
import sys

# -------- CONFIGURE LOG DIRECTORY --------
log_directory   = r"C:\Users\Administrator\Desktop\Thesis\root\logs"
root_directory  = r"C:\Users\Administrator\Desktop\Thesis\root\src"
# -----------------------------------------

def delete_log_files(directory):
    if not os.path.exists(directory):
        print(f"[ x ] Directory not found: {directory}")
        return

    deleted_count = 0

    for file in os.listdir(directory):
        if file.endswith(".log"):
            file_path = os.path.join(directory, file)
            try:
                os.remove(file_path)
                print(f"[ x ] Deleted: {file}")
                deleted_count += 1
            except Exception as e:
                print(f"[ x ] Failed to delete {file}: {e}")

    print(f"\n[ x ] Total log files deleted: {deleted_count}")

if __name__ == "__main__":
    delete_log_files(log_directory)
    delete_log_files(root_directory)
