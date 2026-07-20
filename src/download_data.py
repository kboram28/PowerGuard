# UCI 데이터 다운로드

"""
UCI Individual Household Electric Power Consumption 데이터셋 다운로드 스크립트

사용법:
    python src/download_data.py
"""

import os
import zipfile
import urllib.request

# UCI 데이터셋 URL
URL = "https://archive.ics.uci.edu/static/public/235/individual+household+electric+power+consumption.zip"

# 저장 경로
RAW_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "raw")
ZIP_PATH = os.path.join(RAW_DIR, "household_power_consumption.zip")
TXT_PATH = os.path.join(RAW_DIR, "household_power_consumption.txt")


def download_and_extract():
    os.makedirs(RAW_DIR, exist_ok=True)

    if os.path.exists(TXT_PATH):
        print(f"이미 존재합니다: {TXT_PATH}")
        return

    print("UCI 데이터셋 다운로드 중...")
    urllib.request.urlretrieve(URL, ZIP_PATH)
    print(f"다운로드 완료: {ZIP_PATH}")

    print("압축 해제 중...")
    with zipfile.ZipFile(ZIP_PATH, "r") as zf:
        zf.extractall(RAW_DIR)
    print(f"압축 해제 완료: {TXT_PATH}")

    # zip 파일은 정리 (원본 txt만 남김)
    os.remove(ZIP_PATH)


if __name__ == "__main__":
    download_and_extract()