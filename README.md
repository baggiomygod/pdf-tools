一个可以通过命令行模式调用的给PDF打水印的简单应用

# 使用

`$ python simplePdfWatermark.py [OPTIONS] FILENAME`

参数`--help` 查看详细参数介绍

## 提示

暂时没有去水印功能

## pdfWatermark

**固定文字水印**

`python simplePdfWatermark.py -w "WATERMARK" demo.pdf`

**设置水印文字颜色 透明度 位置**

`python simplePdfWatermark.py -w "WATERMARK" -c "#FF0000" -o 0.3 -x 200 -y 150  demo.pdf`

**输出新文件**

`python pdfwatermark.py -c "#FF0000" -o 0.3 -x 200 -y 150  -w "watermark-2021" -d out.pdf demo.pdf`

# 打包

1. `pip install pyinstaller`
2. `pyinstaller.exe ./simplePdfWater.py`
3. 打包后输出在`dist`文件夹下
4. 测试打包应用`.\dist\simplePdfWatermark\simplePdfWatermark.exe  -c "#FF0000" -o 0.3 -s 20 -x 180 -y 0 -w "zbd-watermark" -d D:\work\jyjs-projects\examples\pdfwatermark\files\water2.pdf D:\work\jyjs-projects\examples\pdfwatermark\files\1.pdf`


## pdfSplit

pdf 拆分

DEV:

`python ./tools/pdfSplit/pdfSplit.py -s 146 -e 199 -t D:\work\jyjs-projects\examples\pdfToolsPy\files\2012-2021.pdf D:\work\jyjs-projects\examples\pdfToolsPy\files\2021.pdf`


## 打包


1. `pip install pyinstaller`
2. `pyinstaller.exe ./tools/pdfSplit/pdfSplit.py`
3. 打包后输出在`dist`文件夹下
4. 测试打包应用`.\dist\simplePdfWatermark\simplePdfWatermark.exe  -c "#FF0000" -o 0.3 -s 20 -x 180 -y 0 -w "zbd-watermark" -d D:\work\jyjs-projects\examples\pdfwatermark\files\water2.pdf D:\work\jyjs-projects\examples\pdfwatermark\files\1.pdf`



<!-- C:\\Users\\admin\\Desktop\\exmple.docx C:\\Users\\admin\\Desktop\\exmple.pdf -->