# 计算机视觉学习笔记

这是一个系统的计算机视觉实践学习项目，通过Jupyter Notebook形式提供从基础到进阶的计算机视觉算法实现。

## 项目概述

本项目通过一系列精心设计的实验和代码示例，帮助学习者深入理解计算机视觉的核心概念和算法。每个章节都包含理论讲解和实际代码实现。

## 环境配置

### 创建虚拟环境

```bash
conda create -n cv_env python=3.10 -y
conda activate cv_env
```

### 安装依赖包

```bash
conda install numpy matplotlib pandas scipy -y
conda install -c conda-forge scikit-image -y
pip install opencv-contrib-python -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install jupyter ipykernel -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### 启动Jupyter Notebook

```bash
jupyter notebook
```

## 课程内容

### 1. 卷积操作 (Convolution)

- **1.1 一维卷积**: 理解卷积的基本概念和数学原理
- **1.2 二维卷积**: 掌握图像卷积操作和滤波器应用

### 2. 图像滤波 (Image Filtering)

- **2.1-2.2 均值滤波**: 平滑图像和噪声消除
- **2.3 中值滤波**: 处理椒盐噪声
- **2.4 双边滤波**: 保持边缘的平滑滤波
- **2.5 导向滤波**: 高级边缘保持滤波技术

### 3. 灰度变换与阈值化 (Grayscale Transformation & Thresholding)

- **3.1 灰度变换**: 对比度增强和直方图均衡化
- **3.2 图像阈值化与二值化**: 图像分割基础

### 4. 形态学与多尺度处理 (Morphology & Multi-scale Processing)

- **4.1 数学形态学**: 膨胀、腐蚀、开运算、闭运算
- **4.2 多尺度处理**: 图像金字塔和多分辨率分析

### 5. 模板匹配 (Template Matching)

- **5.1 平方差类匹配**: 基本的模板匹配算法
- **5.2 多目标模板匹配**: 复杂场景下的模板识别

### 6. 边缘检测 (Edge Detection)

- **6.1 Roberts算子**: 简单的边缘检测方法
- **6.2 一阶算子对比实验**: Sobel、Prewitt算子比较
- **6.3 Laplacian算子**: 二阶微分边缘检测
- **6.4 Canny边缘检测**: 经典的多阶段边缘检测算法

### 7. 角点检测 (Corner Detection)

- **7.1 Harris角点检测**: 经典的角点检测算法
- **7.2 图像拼接**: 基于特征点的图像配准和拼接

## 数据集

项目包含多个测试图像：

- `img/` 目录包含各种测试图像
- 每个章节都有对应的测试图像文件
- 主要使用经典的Lena图像和其他测试图像

## 项目结构

```
Learning/
├── 1卷积/                    # 卷积操作
├── 2图像滤波/                # 图像滤波技术
├── 3灰度变换与阈值化/        # 图像增强与分割
├── 4形态学与多尺度处理/      # 形态学操作
├── 5模板匹配/                # 模板匹配算法
├── 6边缘检测/                # 边缘检测方法
├── 7角点检测/                # 角点检测与图像拼接
├── img/                      # 图像资源
├── environment.txt           # 环境配置说明
└── README.md                 # 项目说明文档
```

## 学习建议

1. **按顺序学习**: 建议按照章节顺序进行学习，因为后面的内容会依赖前面的基础知识
2. **动手实践**: 每个Notebook都包含代码实现，建议自己运行并修改参数观察效果
3. **理解原理**: 不仅要会运行代码，更要理解每个算法背后的数学原理
4. **扩展实验**: 可以尝试使用自己的图像进行实验，或者修改算法参数观察不同效果

## 技术栈

- **编程语言**: Python 3.10
- **核心库**: OpenCV, NumPy, Matplotlib, SciPy
- **图像处理**: scikit-image
- **开发环境**: Jupyter Notebook
- **包管理**: Conda

### 博客文章

以下是我在学习过程中撰写的计算机视觉相关博客文章，记录了更深入的理论理解和实践心得：

- [卷积：彻底搞懂卷积核怎么扫图和计算【计算机视觉】](https://blog.csdn.net/R_Feynman_/article/details/156833752)
- [图像滤波：手撕五大经典滤波（均值 / 高斯 / 中值 / 双边 / 导向）【计算机视觉】](https://blog.csdn.net/R_Feynman_/article/details/156872829)
- [灰度变换与阈值化：从像素映射到图像二值化的核心操作【计算机视觉】](https://blog.csdn.net/R_Feynman_/article/details/157647806)
- [形态学与多尺度处理：图像形状与尺度的基础处理框架【计算机视觉】](https://blog.csdn.net/R_Feynman_/article/details/157617875)
- [单 / 多目标模板匹配：相似度度量与阈值优化【计算机视觉】](https://blog.csdn.net/R_Feynman_/article/details/156995021)
- [边缘检测：基础算子到高级边缘提取【计算机视觉】](https://blog.csdn.net/R_Feynman_/article/details/157186376)
- [角点检测：基础原理到高精度特征定位拼接图像【计算机视觉】](https://blog.csdn.net/R_Feynman_/article/details/157584387)

## 参考资料

- **《动手学计算机视觉》** - 系统学习计算机视觉理论和实践的优秀教材
  - 官方网站：[https://hcv.boyuai.com/](https://hcv.boyuai.com/)

## 版权声明

本项目为个人学习笔记，主要用于计算机视觉算法的学习和实践。

- 项目中的代码和实验内容均为学习过程中的实践实现
- 博客文章为作者的学习总结和心得
- 参考书籍链接仅用于学习参考目的
- 使用的测试图像包括标准测试图像和教材示例图像

## 贡献

欢迎提交问题和改进建议！

> **声明**：由于本人水平有限，难免存在疏忽和错误，恳请批评指正。

## 许可证

本项目仅供学习交流使用。
