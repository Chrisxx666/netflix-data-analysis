import os
import sys
import time
import subprocess
from datetime import datetime

"""
這是一個主腳本，用於執行整個 Netflix 資料分析流程，
從資料清洗、載入到資料庫，到生成圖表和網站資源。
"""


def print_step(message):
    """打印帶有時間戳的步驟訊息"""
    current_time = datetime.now().strftime('%H:%M:%S')
    print(f"\n[{current_time}] {message}")
    print("=" * 50)


def run_script(script_name):
    """執行指定的 Python 腳本"""
    print_step(f"執行: {script_name}")
    script_path = os.path.join(os.path.dirname(__file__), script_name)
    # 使用 subprocess 代替 os.system
    subprocess.run([sys.executable, script_path], check=True)


def main():
    """主流程"""
    start_time = time.time()

    print("\n📊 開始執行 Netflix 資料分析流程 📊")
    print("=" * 50)

    # 步驟 1: 載入與預覽原始資料
    run_script("01_load_and_preview.py")

    # 步驟 2: 清洗與格式化資料
    run_script("02_clean_and_format.py")

    # 步驟 3: 將資料載入 MySQL
    run_script("load_to_mysql.py")

    # 步驟 4: CSV 資料分析
    run_script("03_exploratory_analysis(csv).py")

    # 步驟 5: SQL 資料分析
    run_script("04_sql_analysis.py")

    # 步驟 6: 生成並保存圖表 (新增步驟)
    run_script("save_charts.py")

    # 計算執行時間
    execution_time = time.time() - start_time
    print(f"\n✅ 全部流程已完成! 總執行時間: {execution_time:.2f} 秒")
    print("\n📊 分析結果可以在 'website' 目錄中查看")
    print("💡 提示: 您可以使用瀏覽器開啟 website/index.html 查看網頁版結果")


if __name__ == "__main__":
    main()