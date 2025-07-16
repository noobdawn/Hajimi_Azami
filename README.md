# Hajimi_Azami

![](GIF/bustup_asami_laugh.gif)

福来蓟很可爱，所以创建了这个项目 | 福来あざみが可愛いから、このプロジェクトを作りました | Created this project because Azami Fukurai is adorable

## 目录结构 | ディレクトリ構成 | Directory Structure
Atlas/: Renderdoc捕获的图集，子文件夹名表示分划图集使用的尺寸 | Renderdocから取得したアトラス。サブフォルダ名は分割サイズを指定 | Atlas captured from Renderdoc, subfolder names indicate slicing size  
GIFs/: 制作完成的福来蓟动态表情 | 作成済みの福来あざみGIF表情 | Pre-made Azami Fukurai animated GIFs

## 定制表情 | カスタムGIF作成 | Customize GIFs
执行 main.py 重新生成表情 | main.pyを実行してGIFを再生成 | Run main.py to regenerate GIFs  
需要配置以下参数 | 以下のパラメータを設定する必要があります | Requires setting these parameters:

`BACKGROUND_COLOR` : 背景颜色 | 背景色 | Background color
`INTERVAL` : 帧间隔/毫秒 (例: `100`) | フレーム間隔/ミリ秒 (例: `100`) | Frame interval in milliseconds (e.g. `100`)  
`SCALE` : GIF缩放比例 (例: `4`) | GIFスケール係数 (例: `4`) | GIF scaling factor (e.g. `4`)

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