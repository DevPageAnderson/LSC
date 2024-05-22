import os
import shutil

# 지정된 디렉토리 경로
directory = r'C:\Users\Public\Documents\Photon Kinetics\PKSL\Archived Data'

# 디렉토리 내의 모든 파일과 폴더를 삭제합니다
for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
        print(f'Deleted: {file_path}')
    except Exception as e:
        print(f'Error deleting {file_path}: {e}')
