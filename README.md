# Hajimi_Azami

![](GIF/x2/bustup_asami_laugh.gif)

因《都市传说解体中心》的主人公福来蓟非常可爱，特创建此项目
『都市伝説解体センター』の主人公・福来あざみの可愛さに惹かれて、このリポジトリを作成しました
Created this repository due to the adorable protagonist Azami Fukurai from "Urban Myth Dissolution Center"

## 目录结构 | ディレクトリ構成 | Directory Structure

GIF目录包含预生成的福来蓟动态表情，按不同缩放比例组织
GIFディレクトリには、事前に生成された福来あざみの動きのあるスタンプが拡大率別に整理されています
The GIFs directory contains pre-generated animated stickers of Azami Fukurai organized by different scaling factors

## 定制表情 | カスタムGIF作成 | Customize GIFs

如果想重新定制，则执行main.py，需要设定的参数为：  
カスタマイズしたい場合は、main.pyを実行します。設定する必要があるパラメータは次のとおりです：  
To create custom versions, run main.py with the following configurable parameters:

```python
BACKGROUND_COLOR = (0, 0, 0, 255) # 背景颜色 / 背景色 / Background color (RGBA)
INTERVAL = 100                  # 每帧持续时间(ms) / フレーム間隔(ミリ秒) / Frame interval (milliseconds)
```

## 注意事项 | 注意事項 | Note

注意，若执行时Python的Pillow库报错，且信息为`ValueError: invalid palette size`，则考虑更新Pillow库，该报错已在[此处](https://github.com/python-pillow/Pillow/pull/8494/files#diff-dcacc75af03647f068da2f14ab22643cc7d92cc7bf790b80244ae58e3e3debb2)修复  
実行時にPillowライブラリが`ValueError: invalid palette size`エラーを報告した場合、Pillowライブラリを更新してください。この問題は[こちら](https://github.com/python-pillow/Pillow/pull/8494/files#diff-dcacc75af03647f068da2f14ab22643cc7d92cc7bf790b80244ae58e3e3debb2)で修正されています  
If you encounter `ValueError: invalid palette size` from Pillow library during execution, consider updating Pillow. This issue was fixed [here](https://github.com/python-pillow/Pillow/pull/8494/files#diff-dcacc75af03647f068da2f14ab22643cc7d92cc7bf790b80244ae58e3e3debb2)