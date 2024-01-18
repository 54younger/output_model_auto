# 功能介绍
-- blender.py 将专辑封面材质绑定至黑胶唱片,并将唱片机模型导出为.glb
-- image_processing.py 改变专辑封面大小,使其贴合黑胶唱片(因为我也不知道怎么改材质大小,用一个笨方法)
-- model.blend 唱片机模型,未添加专辑封面
-- new.blend 卡片上唱片机模型,未添加专辑封面
-- img 专辑封面文件夹
  -- resize 处理后的专辑封面文件夹
-- temp.blend 添加封面时临时文件,删除blender.py文件最后一行代码可保留
-- model.glb 最终成品

# 使用方法
## 1
先运行image_process.py,得到处理后的专辑封面.
*注意更改代码内路径*

## 2
  #### 运行blender.py命令为:
  你的blender安装路径(不要有空格)(这个应该不用强调吧)/blender.exe -b -P *该文件夹绝对路径*/blender.py -- --parent_dir *该文件夹绝对路径* --pic_name 专辑封面名(只有名字,无需要加后缀)

*example*: blender.exe -b -P C:/Users/younger/Desktop/output_model_auto/for_card/blender.py -- --parent_dir C:/Users/younger/Desktop/output_model_auto/for_card/ --pic_name 2

## 3
得到目标文件
