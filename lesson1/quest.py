import time
import sys
import os
import shutil
import tkinter as tk
from tkinter import filedialog


def iteratively_display_text(text_list, delay=1):
    for text in text_list:
        print(text)
        time.sleep(delay)


def simulate_loading(text):
    for i in range(3):
        sys.stdout.write(f"\r{text}" + "." * i)
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write(f"\r{text}" + "." * 3 + " 完成!\n")


iteratively_display_text(
    [
        "恭喜你 正確的執行了第一堂課的練習",
        "你接下來會用這個小遊戲更熟戲Terminal的操作",
        "在接下來的小遊戲中 你會扮演一個貨物公司的倉儲管理員",
        "你需要在完全不離開終端機的前提下 完成系統的種種挑戰",
        "要進行這個小遊戲 我們需要一個空的資料夾",
        "接下來會跳出一個視窗 請你選擇一個空的資料夾進行遊戲",
        "如果資料夾不是空的，遊戲將會刪除資料夾內的所有檔案，所以請務必選擇一個空的資料夾！",
    ]
)

input("如果你已經想好了要用哪一個空的資料夾 請按Enter鍵繼續")

root = tk.Tk()
root.withdraw()
quest_path = filedialog.askdirectory()

while (not len(quest_path)) or not os.access(quest_path, os.W_OK):
    print("\n要能進行遊戲 你需要選擇一個這個程式能夠編輯的資料夾")
    print("通常在桌面上建立一個資料夾並選擇他即可")
    print("請選擇一個不同的資料夾")
    quest_path = filedialog.askdirectory()

print(f"\n將在 {quest_path} 進行遊戲！\n")

# Delete all files and folders in the quest_path
for root, dirs, files in os.walk(quest_path, topdown=False):
    for file in files:
        os.remove(os.path.join(root, file))
    for dir in dirs:
        shutil.rmtree(os.path.join(root, dir))

os.mkdir(os.path.join(quest_path, "load_intake"))
with open(os.path.join(quest_path, "load_intake", "practice.txt"), "w") as f:
    f.write("""很棒 你成功讀取了貨物資訊!""")
os.mkdir(os.path.join(quest_path, "food"))
os.mkdir(os.path.join(quest_path, "coffee"))
os.mkdir(os.path.join(quest_path, "computers"))

simulate_loading("正在準備遊戲")

print("首先 請另開一個終端機視窗 並將那個視窗切換到遊戲的資料夾")
input("完成後請按enter \n")

print("請告訴我你在遊戲資料夾中看到幾個子資料夾")
num_of_folders = input("請輸入數字: ")
while num_of_folders != "4":
    print("答錯了! 請再次確認你的答案")
    num_of_folders = input("請輸入數字: ")

iteratively_display_text(
    [
        "正確，現在讓我們說明遊戲規則",
        "現在開始每回合會都會有一系列新的貨物進入你的倉庫 他們會被放到load_intake資料夾中",
        "請你將這些貨物分類到適當的資料夾中",
        "現在請你將load_intake中的practice.txt移動到food資料夾中",
    ]
)

while True:
    input("完成後請按enter \n")
    intake = os.listdir(os.path.join(quest_path, "load_intake"))
    food = os.listdir(os.path.join(quest_path, "food"))
    if len(intake) == 0 and "practice.txt" in food:
        break
    print("檢查失敗！請再試一次")

# Clear all folders
for folder in ["load_intake", "food", "coffee", "computers"]:
    for file in os.listdir(os.path.join(quest_path, folder)):
        os.remove(os.path.join(quest_path, folder, file))

# Create 4 food files (burger, spaghetti, salad, pizza) in the  load_intake folder
for food in ["burger", "spaghetti", "salad", "pizza"]:
    with open(os.path.join(quest_path, "load_intake", f"{food}.txt"), "w") as f:
        f.write(f"{food}!")
# Create 4 coffee files (latte, cappuccino, espresso, americano) in the  load_intake folder
for coffee in ["latte", "cappuccino", "espresso", "americano"]:
    with open(os.path.join(quest_path, "load_intake", f"{coffee}.txt"), "w") as f:
        f.write(f"{coffee}!")
# Create 3 computer files (macbook, surface, thinkpad, xps) in the  load_intake folder
for computer in ["macbook", "surface", "xps"]:
    with open(os.path.join(quest_path, "load_intake", f"{computer}.txt"), "w") as f:
        f.write(f"這是{computer}的電腦")
    os.chmod(os.path.join(quest_path, "load_intake", f"{computer}.txt"), 0o777)


iteratively_display_text(
    [
        "恭喜你完成了第一個任務!",
        "接下來你會進行正式的遊戲",
        "現在，請你將load_intake資料夾中的所有檔案分類到適當的資料夾中",
    ]
)


error = False

while True:
    if error:
        print("分類失敗! 請再試一次")
    input("完成後請按enter \n")
    error = False
    intake = os.listdir(os.path.join(quest_path, "load_intake"))
    food = os.listdir(os.path.join(quest_path, "food"))
    coffee = os.listdir(os.path.join(quest_path, "coffee"))
    computers = os.listdir(os.path.join(quest_path, "computers"))
    # Remove any hidden files
    intake = [i for i in intake if not i.startswith(".")]
    food = [f for f in food if not f.startswith(".")]
    coffee = [c for c in coffee if not c.startswith(".")]
    computers = [c for c in computers if not c.startswith(".")]

    if len(intake) != 0 or len(food) != 4 or len(coffee) != 4 or len(computers) != 3:
        error = True
        continue
    food_expected = ["burger", "spaghetti", "salad", "pizza"]
    food_expected = [f"{food}.txt" for food in food_expected]
    for f in food:
        if f not in food_expected:
            error = True
            break
    if error:
        continue
    coffee_expected = ["latte", "cappuccino", "espresso", "americano"]
    coffee_expected = [f"{coffee}.txt" for coffee in coffee_expected]
    for c in coffee:
        if c not in coffee_expected:
            error = True
            break
    if error:
        continue
    computers_expected = ["macbook", "surface", "xps"]
    computers_expected = [f"{computer}.txt" for computer in computers_expected]
    for c in computers:
        if c not in computers_expected:
            error = True
            break
    if error:
        continue
    break


simulate_loading("正在檢查貨物")

iteratively_display_text(
    [
        "檢查錯誤！電腦區缺少一個檔案",
        "請再試一次",
        "[送貨小精靈] 嗨！是我！送貨小精靈！",
        "[送貨小精靈] 關於那個缺少的電腦... 我在送貨的路上把他弄丟了",
        "[送貨小精靈] 我原本以為系統會忘記有他的... 但是看來我錯了",
        "[送貨小精靈] 你能幫我在電腦區裡新增一個'zephyrus.txt'的檔案嗎？",
    ]
)


while True:
    input("完成後請按enter \n")
    error = False
    computers = os.listdir(os.path.join(quest_path, "computers"))
    if "zephyrus.txt" not in computers:
        error = True
    if error:
        print("檢查錯誤！電腦區缺少一個檔案")
    else:
        break

simulate_loading("正在檢查貨物")

# Write a file called "suspecious_activity.txt" in the game root folder
with open(os.path.join(quest_path, "suspecious_activity.txt"), "w") as f:
    f.write(
        """貨物檢查失敗！zephyrus型號不符合格式！
[系統註記]在解決此問題後，請刪除此檔案"""
    )

iteratively_display_text(
    [
        "貨物檢查失敗！",
        "zephyrus型號不符合格式！",
        "[送貨小精靈] 可惡！被系統發現檔案不對了！",
        "[送貨小精靈] 看來只能從現有的檔案中找一個來改一改了",
        "[送貨小精靈] 你能試試看刪除掉原本的Zepharus檔案後",
        "[送貨小精靈] 複製一個其他電腦的檔案並將他改名成zephyrus.txt嗎？",
        "[送貨小精靈] 記得將檔案內容改成'這是zephyrus的電腦'",
        "[送貨小精靈] 這樣應該就不會被發現了",
        "[系統註記] 因為遊戲設計的小瑕疵 在此使用cp時 請使用cp -p來複製檔案 這樣後續的檢查才不會出錯 謝謝",
    ]
)


while True:
    input("完成後請按enter \n")
    error = False
    computers = os.listdir(os.path.join(quest_path, "computers"))
    if "zephyrus.txt" not in computers:
        print("檢查錯誤！電腦區缺少一個檔案")
        continue
    with open(os.path.join(quest_path, "computers", "zephyrus.txt"), "r") as f:
        content = f.read()
        content = content.strip()
        file_name_match = (
            content == "這是zephyrus的電腦" or content == "'這是zephyrus的電腦'"
        )
        op_mode = (
            os.stat(os.path.join(quest_path, "computers", "zephyrus.txt")).st_mode
            & 0o777
        )
        if not file_name_match or op_mode != 0o777:
            print("檢查錯誤！zephyrus型號不符合格式！")
            continue
    break

simulate_loading("正在檢查貨物")
print("檢查成功！")

simulate_loading("正在驗收清單")

if os.path.exists(os.path.join(quest_path, "suspecious_activity.txt")):
    iteratively_display_text(
        [
            "驗收清單失敗！你的倉庫有可疑的活動！",
            "請打開suspecious_activity.txt檔案查看詳細資訊",
            "[送貨小精靈] 可惡！之前新增的檔案留下了痕跡！",
            "[送貨小精靈] 你能看看遊戲根目錄的suspecious_activity.txt檔案嗎？",
            "[送貨小精靈] 搞不好他能告訴你一些有用的資訊",
        ]
    )

    while True:
        input("完成後請按enter \n")
        if os.path.exists(os.path.join(quest_path, "suspecious_activity.txt")):
            print("驗收清單失敗！ 你的倉庫有可疑的活動！")
            continue
        break

iteratively_display_text(
    [
        "驗收清單成功！",
        "在結束遊戲之前，你能重複一次你在哪個資料夾進行這個遊戲嗎？",
        "[系統提示] 有個指令能讓你不用往上滑也可以回答這個問題",
    ]
)

while True:
    user_input = input("你在哪個資料夾進行呢？ ")
    if user_input == quest_path:
        break
    print("回答錯誤！")

iteratively_display_text(
    [
        "恭喜你完成了所有的任務",
        "你已經完成了第一堂課的所有練習！",
    ]
)
