# 医学图像增强软件

中文名称：医学图像增强软件

英文名称：Medical-Image-Enhancement-Software

---
> createTime: 2023-11-13  
> updateTime: 2023-11-27  
---

## 介绍

软件名称：**基于pydicom与cv2的PET医学图像增强系统**

### 软件功能

1、图像读取：

- 使用 Pydicom 库读取 DICOM 格式的 PET 图像。

2、初始图像评估：

- 对动态范围、噪声水平等进行评估。

3、图像分析：

- 进行直方图均衡化处理。

4、图像增强：

- 利用自适应增强技术，应用频域滤波器，包括高通和低通滤波器，以及锐化技术。还可以考虑使用cv2库提供的其他增强方法或技术。

5、增强效果评估：

- 定量评估：计算增强后图像的对比度、锐度等参数。
- 定性评估：基于医生或放射科专家的反馈，评估增强图像在医学应用中的可读性和实用性。

6、软件典型使用流程：

- 图像读取
- 图像增强处理
- 结果展示

## 技术

### 软件技术架构

- PyQt6
- OpenCV
- PyDICOM

### 运行方法

```shell
# 创建python虚拟环境
python -m virtualenv venv

# 在当前终端会话中启用python虚拟环境（在cmd命令提示符下）
venv\Scripts\activate

# 安装所需依赖
pip install -r requirements.txt

# 如果要把当前已安装的pip包写入到文本文件
pip freeze > requirements.txt

# 使用pyuic，这要求安装PyQt6
python -m PyQt6.uic.pyuic .\src\widgets\widget_01.ui -o .\src\widgets\widget_01.py
```

### 目录结构

`src/main.py`：主程序

`src/widgets/`：QtWidget控件实例

`build.py`：构建脚本

`qt6-tools`：Qt6工具

## 更新日志

### 2023-11-13

- 初始发布

### 2023-11-27

- 集成 PyQt6-tools 到项目中，方便使用
- 新增计算灰度直方图功能

### 2023-11-30

- 新增：直方图均衡化功能
- 修复：requirement.txt
- 修复：build.py构建脚本
- 第一次交付