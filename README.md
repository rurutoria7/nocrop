No Crop
===

No Crop 可以把任何尺寸的影像填充成固定長寬比的新影像。

這個工具可以協助你在 Instagram 或者其他平台發布照片，而免於被失去原有的照片比例。

## Installation

```
mkdir ~/Scripts && git clone ~/Scripts
pip install -r requirements.txt
```

## Add Automator (Only for MacOS)

如果要加到 Automator，請確保該 Repo 放在 `~/Scripts` 下

1. 打開 Automator，新增一個 "快速動作" 服務
2. 新增一個 "執行 Shell 工序" 動作
3. 上方設定如下：
![img.png](img.png)
4. 在"執行 Shell 工序指令裡"貼上：
```
python3 ~/Scripts/nocrop/nocrop.py >& ~/Scripts/nocrop/log
osascript -e 'display alert "Done"'
```
