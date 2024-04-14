import os
import shutil

def copy_folders_to_destination(source_folders, dest_dir):
    # 대상 폴더가 없으면 생성
    if not os.path.exists(dest_dir):
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

# 사용자로부터 대상 폴더의 경로를 입력 받기
# 입력 받은 폴더들을 대상 폴더로 복사
destination_directory = "G:/공유 드라이브/fyz/ysg_study"
copy_folders_to_destination(source_folders, destination_directory)

# 한 번 더
destination_directory = "D:/earify/coding/github/ysg-obsidian/ysg study/"
copy_folders_to_destination(source_folders, destination_directory)


print("Folders copied successfully!")
