# Hajimi_Azami

![](GIF/bustup_asami_laugh.gif)

因为福来蓟很可爱，所以有了这个库。  
福来あざみが可愛いから、このライブラリを作りました。  
Because Azami Fukurai is cute, I created this library.

## 目录结构 | ディレクトリ構成 | Directory Structure

```
プロジェクト構造 | Project Structure
.
├── Atlas/
│   ├── 128x128/    # 分划尺寸 | 分割サイズ | Slice size
│   ├── 240x135/
│   └── ... 
├── GIFs/
│   ├── bustup_asami_amazed_g.gif
│   ├── bustup_asami_amazed.gif
│   └── ...
├── main.py          # 主生成脚本 | メインスクリプト | Main generator
```

Atlas目录下是我从Renderdoc中获取的图集，子文件夹名则制定了分划图集时使用的size；  
Atlasディレクトリには、Renderdocから取得したアトラスが含まれています。サブフォルダ名は、アトラスを分割する際に使用するサイズを指定しています；  
The Atlas directory contains atlas data captured from Renderdoc. Subfolder names indicate the size used for splitting the atlas.

GIF目录下则是我已经制作好的福来蓟动态表情；  
GIFディレクトリには、私が既に作成した福来あざみの動くスタンプが含まれています；  
The GIF directory contains pre-made animated stickers of Azami Fukurai.

## 定制表情 | カスタムGIF作成 | Customize GIFs

如果想重新定制，则执行main.py，需要设定的参数为：  
カスタマイズしたい場合は、main.pyを実行します。設定する必要があるパラメータは次のとおりです：  
To create custom versions, run main.py with the following configurable parameters:

```python
BACKGROUND_COLOR = (0, 0, 0, 0) # 背景颜色 / 背景色 / Background color (RGBA)
INTERVAL = 100                  # 每帧持续时间(ms) / フレーム間隔(ミリ秒) / Frame interval (milliseconds)
SCALE = 4                       # GIF缩放比例 / GIFスケール / GIF scale factor
```

## 注意事项 | 注意事項 | Note

注意，若执行时Python的Pillow库报错，且信息为`ValueError: invalid palette size`，则考虑更新Pillow库，该报错已在[此处](https://github.com/python-pillow/Pillow/pull/8494/files#diff-dcacc75af03647f068da2f14ab22643cc7d92cc7bf790b80244ae58e3e3debb2)修复  
実行時にPillowライブラリが`ValueError: invalid palette size`エラーを報告した場合、Pillowライブラリを更新してください。この問題は[こちら](https://github.com/python-pillow/Pillow/pull/8494/files#diff-dcacc75af03647f068da2f14ab22643cc7d92cc7bf790b80244ae58e3e3debb2)で修正されています  
If you encounter `ValueError: invalid palette size` from Pillow library during execution, consider updating Pillow. This issue was fixed [here](https://github.com/python-pillow/Pillow/pull/8494/files#diff-dcacc75af03647f068da2f14ab22643cc7d92cc7bf790b80244ae58e3e3debb2)