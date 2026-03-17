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

项目包含多个测试图像：

- `img/` 目录包含各种测试图像
- 每个章节都有对应的测试图像文件
- 主要使用经典的Lena图像和其他测试图像


## 技术栈

- **编程语言**: Python 3.10
- **核心库**: OpenCV, NumPy, Matplotlib, SciPy
- **图像处理**: scikit-image
- **开发环境**: Jupyter Notebook
- **包管理**: Conda

### 博客文章

以下是我在学习过程中撰写的计算机视觉相关博客文章，记录了更深入的理论理解和实践心得：

- [灰度变换与阈值化：从像素映射到图像二值化的核心操作【计算机视觉】](https://blog.csdn.net/R_Feynman_/article/details/157647806)
- [卷积：彻底搞懂卷积核怎么扫图和计算【计算机视觉】](https://blog.csdn.net/R_Feynman_/article/details/156833752)
- [图像滤波：手撕五大经典滤波（均值 / 高斯 / 中值 / 双边 / 导向）【计算机视觉】](https://blog.csdn.net/R_Feynman_/article/details/156872829)
- [形态学与多尺度处理：图像形状与尺度的基础处理框架【计算机视觉】](https://blog.csdn.net/R_Feynman_/article/details/157617875)
- [单 / 多目标模板匹配：相似度度量与阈值优化【计算机视觉】](https://blog.csdn.net/R_Feynman_/article/details/156995021)
- [边缘检测：基础算子到高级边缘提取【计算机视觉】](https://blog.csdn.net/R_Feynman_/article/details/157186376)
- [角点检测：基础原理到高精度特征定位拼接图像【计算机视觉】](https://blog.csdn.net/R_Feynman_/article/details/157584387)
- [特征检测：SIFT 与 SURF（尺度不变 / 加速稳健特征）【计算机视觉】](https://blog.csdn.net/R_Feynman_/article/details/157720209)
- [傅里叶变换：从空域到频域的图像分析【计算机视觉】](https://blog.csdn.net/R_Feynman_/article/details/158626321)
- [小波变换：多分辨率分析与图像小波去噪 / 增强 / 融合【计算机视觉】](https://blog.csdn.net/R_Feynman_/article/details/158892445)
- [图像去雾：从直方图增强到暗通道先验【计算机视觉】](https://blog.csdn.net/R_Feynman_/article/details/158807328)


## 参考资料

- **《动手学计算机视觉》** 
  - 官方网站：[https://hcv.boyuai.com/](https://hcv.boyuai.com/)
- **《Python计算机视觉与应用案例》**

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
