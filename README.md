# FUM 🛠️

**Fix Your Mesh — A Blender Mesh Inspection Plugin**

FUM 是一个专业的 Blender 模型拓扑检测与诊断插件，旨在帮助 3D 艺术家快速定位并修复模型中的几何问题。

A professional Blender mesh inspection and diagnostic plugin designed to help 3D artists quickly locate and fix geometric issues in their models.

---

## 📥 Download Latest Version | 下载最新版本

👉 **[点击这里下载 FUM 最新版本 (Download FUM Latest Release)](https://github.com/jian-1120/FUM/releases/latest)**

---

## ✨ Features | 功能

* 🔍 检测模型中的非流形边
  Detect non-manifold edges in the active mesh
* 🔺 检测模型中的重复顶点 (支持阈值调节)
  Detect duplicate vertices in the active mesh (with adjustable threshold)
* 🔄 检测模型中的翻转法线面
  Detect flipped normals faces in the active mesh
* 🎨 自动高亮问题面
  Highlight problematic faces in Edit Mode
* 🔲 检测 N-Gons (边数 > 4 的面)
  Detect N-Gons (faces with more than 4 edges)

* 🎯 自动高亮问题边
  Highlight problematic edges in Edit Mode

* 📊 在UI面板中显示检测结果
  Display detection results in a simple UI panel

* ⚡ 轻量快速，无需额外依赖
  Lightweight and fast, no external dependencies

---

## 📦 Installation | 安装方法

⚠️ **重要：下载后请先检查文件夹结构！**
从 GitHub 下载的 ZIP 解压后，会出现一个 `FUM-main` 文件夹。点击进入后，你会看到 `FUM`、`release`、`README.md` 等文件。

其中只有 `FUM` 文件夹是真正的插件包，里面有 `__init__.py`、`operators/`、`ui/` 等文件。

请根据你的安装方式，将正确的 `FUM` 文件夹提供给 Blender。

---

### 方法一：Blender 内安装（推荐）

1. 下载并解压 ZIP 文件。
2. 进入 `FUM-main` 文件夹，找到里面的 `FUM` 文件夹。
3. 打开 Blender → `编辑(Edit)` → `偏好设置(Preferences)` → `插件(Add-ons)` → `安装...`。
4. **选中里层的 `FUM` 文件夹**（不是 `FUM-main`），点击“安装插件”。
5. 在插件列表搜索 `FUM`，勾选启用。

### 方法二：手动复制到 `addons` 目录（备用方案，适合安装器不稳定时使用）

1. 下载并解压 ZIP 文件，进入 `FUM-main`，找到里面的 `FUM` 文件夹。
2. 打开 Blender 的插件目录（通常是 `C:\Users\[你的用户名]\AppData\Roaming\Blender Foundation\Blender\[版本号]\scripts\addons\`）。
3. 将**里层的 `FUM` 文件夹**整个复制到该目录下。
4. 重启 Blender → `偏好设置(Preferences)` → `插件(Add-ons)` → 搜索 `FUM` → 勾选启用。

---

## 🚀 Usage | 使用方法

1. 选择一个模型对象
   Select a mesh object

2. 按 `N` 打开右侧栏
   Press `N` to open the sidebar

3. 打开 **FUM / Model Doctor** 面板
   Go to the **FUM / Model Doctor** tab

4. 点击按钮：
   Click:
   **Detect Non-Manifold Edges**

👉 插件会自动：
👉 The addon will:

* 进入编辑模式
  Switch to Edit Mode

* 高亮所有非流形边
  Highlight all non-manifold edges

* 显示问题数量
  Display the number of issues

---

## 🧠 What is Non-Manifold Geometry? | 什么是非流形结构？

非流形边是指不符合标准拓扑规则的几何结构，例如：

Non-manifold geometry refers to topology issues such as:

* 被超过两个面共享的边
  Edges shared by more than two faces

* 开放边（模型破洞）
  Open edges (holes)

* 内部面或重叠几何
  Internal faces or overlapping geometry

这些问题可能导致：

These issues can cause problems in:

* 游戏引擎

* Game engines

* 渲染流程

* Rendering pipelines

* 3D打印

* 3D printing

---

## 📸 Preview | 效果展示

> <img width="841" height="727" alt="image" src="https://github.com/user-attachments/assets/35e47d0a-22c7-4797-b23a-11cbe4743970" /><img width="621" height="749" alt="TU" src="https://github.com/user-attachments/assets/c433c826-61c4-4891-a5dc-32acee7e1a27" />

```id="demo_path"
images/demo.png
```

---

## 🖼️ Screenshots | 截图展示

*(预留区域：未来将在此添加更多功能演示 GIF 与截图)*

---

## 📁 Project Structure | 项目结构

```id="proj_struct"
fum/
│
├── __init__.py
├── operators/
│   ├── __init__.py
│   ├── non_manifold_edges.py
│   ├── duplicate_vertices.py
│   ├── flipped_normals.py
│   └── ngons.py
├── ui/
│   ├── __init__.py
│   └── panel.py
├── README.md
├── LICENSE
└── images/
```

---

## 🛠️ Roadmap | 开发计划

* [x] 重复顶点检测（Merge by Distance问题）
* [x] 法线方向检测
* [x] N-Gon 检测
* [ ] 模型质量评分系统
* [ ] AI辅助优化建议

---

## 🤝 Contributing | 参与贡献

欢迎提出建议或参与开发！

Contributions, ideas, and feedback are welcome.

---

## 📄 License | 开源协议

MIT License

---

## 👤 Author | 作者

环境艺术专业学生，正在探索 AI + 建模工作流工具。

An environment design student exploring AI-assisted modeling tools.

---

## ⭐ Support | 支持

如果你觉得这个项目有用：

If you find this project useful:

* ⭐ 给项目点个星

* ⭐ Star this repository

* 📢 分享给其他建模师

* 📢 Share with other 3D artists

---
