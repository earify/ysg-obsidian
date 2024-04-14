import os
import shutil

def delete_folder(folder_path):
    try:
        # 주어진 경로의 폴더를 삭제합니다.
        os.system(f"rmdir /s /q {folder_path}")
        print(f"{folder_path} removed.")
    except FileNotFoundError:
        print(f"주어진 경로에 폴더가 없습니다: {folder_path}")
    except OSError as e:
        print(f"폴더 삭제 중 오류가 발생했습니다: {e}")


def copy_folders_to_destination(source_folders, dest_dir):
    # 대상 폴더가 이미 존재하면 삭제
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
    
    # 대상 폴더 생성
    os.makedirs(dest_dir)

    # 각 소스 폴더를 대상 폴더로 복사
    for source_folder in source_folders:
        # 소스 폴더의 전체 경로를 가져옴
        source_folder_path = os.path.join(source_folder)
        # 대상 폴더의 전체 경로를 가져옴
        dest_folder_path = os.path.join(dest_dir, os.path.basename(source_folder_path))

        # 소스 폴더를 대상 폴더로 복사
        shutil.copytree(source_folder_path, dest_folder_path)

# 사용자가 직접 폴더의 경로를 입력합니다.
source_folders = [
    "D:/earify/Gdrive/obsidian/ysg/_여수고 자료",
    "D:/earify/Gdrive/obsidian/ysg/.obsidian",
    "D:/earify/Gdrive/obsidian/ysg/수업 자료"
]


# 폴더를 삭제할 경로를 지정합니다.
folder_to_delete = "D:\\earify\\coding\\github\\ysg-obsidian\\ysg_study"

# 폴더 삭제 함수 호출
delete_folder(folder_to_delete)

# 사용자로부터 대상 폴더의 경로를 입력 받기
# 입력 받은 폴더들을 대상 폴더로 복사
destination_directory = "D:/earify/coding/github/ysg-obsidian/ysg_study/"
copy_folders_to_destination(source_folders, destination_directory)

print("Folders copied successfully!")

input("Press enter to left.")