这是一个练手项目

1.实现的是vlooup中提炼表一信息到表二的功能

2.点名程序

逐步完善把

ps:打包：1.pip pyinstaller 2.pyinstaller 路径（若是不想让生成的exe打开时有命令行，那就把文件后缀名改成pyw） 3.生成（1kb的打包成了8m）

3.pycharm运行时，no module named cv2错误的解决办法:在cmd中输入：pip install opencv-python  打开PyCharm，选择file-settings-project-project interpreter,如下图所示。如果打开之后没看到opencv-python 的package，则选择右上角的“+”号搜索opencv-python. 最后记得点击右下角的应用。Apply+OK即可，如果还不行重启pycharm

4.模块下载Pillow，代码写PIL！即再将from Pillow import Image改成from PIL import Image

5.截图 代码是抄的，只希望以后能写出自己的代码

6.识别程序需要先用微信截图
