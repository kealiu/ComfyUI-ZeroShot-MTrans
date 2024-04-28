# ComfyUI-ZeroShot-MTrans: 零样本单图像材质迁移

[English](README.md)

一个适用于 [ZeST（零样本单图像材质迁移）](https://github.com/ttchengab/zest_code/)的非官方 ComfyUI 自定义节点

![Zero-Shot Material Transfer from a Single Image](https://github.com/ttchengab/zest_code/raw/main/fig/method.jpg)

给定一张输入图像（例如，一个苹果的照片）和一张单独的材质样例图像（例如，一个金碗），ZeST 可以将金材质从样例图像转移到苹果上，同时具有准确的光照线索，并保持其他部分的细节一致。

## 安装

在 `ComfyUI Manager` 中安装或将代码克隆至 `ComfyUI/custom_nodes`

重启`ComfyUI`后即可使用如下节点

![ZestNode](images/ZeSTNode.png)

## 依赖项

- ControlNet
- IP 适配器
- 任意分割模型

## 输入/输出

- 输入:
    - `target_image` ：用于重绘的原始图像
    - `subject_mask` ：用于重绘的蒙版。改蒙版同时也作为inpaint节点的输入。
    - `brighter` ：默认为 1，表示不改变亮度
        - 值小于 1，表示使目标变暗，当目标处于高光时有用
        - 值大于 1，表示使目标变亮，当目标处于黑暗时有用
        - 提示：尽量让主体颜色处于中间灰状态
- 输出:
    - IMAGE ：亮度模式（灰度）下的目标图像。 作为 inpaint节点的输入

## 工作流程

![ZeST Simple Workflow](ZeSTSimpleWorkflow.png)

### 输入图片
![pumpkin](images/pumpkin.png)

### 材质图片
![cpu_material](images/cpu_material.png)

### 中间图片

#### 蒙版

![pumpkin_mask](images/pumpkin_mask.png)

#### 主体明度化

![pumpkin_zest](images/pumpkin_zest.png)

### 输出图片

![pumpkin_output](images/pumpkin_output.png)

# 致谢
- ZeST: 零样本单图像材质迁移论文: https://arxiv.org/abs/2404.06425
- ZeST 官方演示: https://github.com/ttchengab/zest_code/
- ZeST 网站: https://ttchengab.github.io/zest/
- ZeST 官方视频: https://www.youtube.com/watch?v=atG1VvgeG_g

```bibtex
@article{cheng2024zest,
  title={ZeST: 零样本单图像材质迁移},
  author={程泰颖, Prafull Sharma, Andrew Markham, Niki Trigoni, Varun Jampani},
  journal={arXiv 预印本 arXiv:2404.06425},
  year={2024}
}
```