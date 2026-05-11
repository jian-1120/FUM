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
* 孤立顶点检测 (无连接边或面的顶点)
  Detect isolated vertices (vertices with no connected edges or faces)

* 🎯 自动高亮问题边
  Highlight problematic edges in Edit Mode

* 📊 在UI面板中显示检测结果
  Display detection results in a simple UI panel

* ⚡ 轻量快速，无需额外依赖
  Lightweight and fast, no external dependencies

---

## 📥 安装指南 | Installation Guide

### ⚠️ 重要提示 | Important Note

从 GitHub 下载的 ZIP 文件（例如 `FUM-main.zip`）解压后，通常会得到一个名为 `FUM-main` 的文件夹。进入该文件夹后，你会发现真正的插件本体是**内层的 `FUM` 文件夹**，其中包含 `__init__.py`、`operators/`、`ui/` 等文件。请务必将这个内层的 `FUM` 文件夹提供给 Blender 进行安装。

⚠️ **Please make sure you install the INNER "FUM" folder, not the outer folder with the "-main" suffix.**

---

### 步骤一：下载插件 ZIP 包 | Step 1: Download the Addon ZIP Package

从 GitHub Releases 页面下载最新版插件 ZIP 文件（例如 `FUM_vx.x.x.zip`）：
Download the latest addon ZIP file from the GitHub Releases page (e.g., `FUM_vx.x.x.zip`):

👉 **[下载 FUM 最新版本 (Download FUM Latest Release)](https://github.com/jian-1120/FUM/releases/latest)**

---

### 步骤二：解压并找到真正的插件文件夹 | Step 2: Unzip and Locate the Actual Addon Folder

解压下载的 ZIP 文件。你会看到一个名为 `FUM-main` 的文件夹（这是 GitHub 默认行为）。进入该文件夹，找到**内层的 `FUM` 文件夹**。

Unzip the downloaded ZIP file. You will find a folder named `FUM-main` (this is GitHub's default behavior). Navigate into this folder to locate the **inner `FUM` folder**.

---

### 步骤三：复制到 Blender `addons` 目录 | Step 3: Copy to Blender `addons` Directory

将步骤二中找到的**内层 `FUM` 文件夹**整体复制到 Blender 的 `addons` 插件目录。该目录通常位于：
Copy the **inner `FUM` folder** found in Step 2 directly into Blender's `addons` directory. This directory is typically located at:

*   **Windows**: `C:\Users\[你的用户名]\AppData\Roaming\Blender Foundation\Blender\[版本号]\scripts\addons\`
*   **macOS**: `/Users/[你的用户名]/Library/Application Support/Blender/[版本号]/scripts/addons/`
*   **Linux**: `~/.config/blender/[版本号]/scripts/addons/`

---

### 步骤四：在 Blender 中启用插件 | Step 4: Enable the Addon in Blender

1.  打开 Blender。
    Open Blender.
2.  进入 `编辑(Edit)` → `偏好设置(Preferences)` → `插件(Add-ons)`。
    Go to `Edit` → `Preferences` → `Add-ons`.
3.  在搜索框中输入 `FUM`，找到插件。
    Search for `FUM` in the search bar.
4.  勾选插件旁边的复选框以启用它。
    Check the box next to the addon to enable it.

---

## 🔄 更新旧版本插件 | Updating an Existing Version

⚠️ **重要警告：在安装新版本前，务必彻底移除旧版本，否则可能导致插件功能异常或 Blender 崩溃。**
⚠️ **Important Warning: Before installing a new version, you MUST completely remove the old version to prevent unexpected behavior or Blender crashes.**

1.  **关闭 Blender**。
    **Close Blender**.
2.  进入 Blender 的 `addons` 目录（参考上方“步骤三”）。
    Navigate to Blender's `addons` directory (refer to "Step 3" above).
3.  **删除旧版本 `FUM` 文件夹**。确保该目录中不再有任何旧的 `FUM` 文件。
    **Delete the old `FUM` folder**. Ensure no old `FUM` files remain in this directory.
4.  如果存在 `__pycache__` 文件夹，要保留。
    If a `__pycache__` folder exists, you may keep.
5.  按照上述“安装指南”的步骤，将新版**内层 `FUM` 文件夹**复制到 `addons` 目录。
    Follow the "Installation Guide" steps above to copy the new **inner `FUM` folder** into the `addons` directory.
6.  重新打开 Blender。
    Restart Blender.
7.  进入 `编辑(Edit)` → `偏好设置(Preferences)` → `插件(Add-ons)`，搜索 `FUM` 并勾选启用。
    Go to `Edit` → `Preferences` → `Add-ons`, search for `FUM`, and enable it.

---

## 💡 未来计划 | Future Plan

我们正在积极探索优化插件打包和安装流程，目标是实现：
We are actively exploring ways to optimize the addon packaging and installation process, aiming for:

*   **标准 Blender ZIP 打包**: 允许用户直接通过 Blender 的 `Install from ZIP` 功能安装。
    **Standard Blender ZIP Packaging**: Enable direct installation via Blender's `Install from ZIP` feature.
*   **自动化 Release 打包**: 自动生成符合 Blender 规范的 ZIP 包，减少手动操作。
    **Automated Release Packaging**: Automatically generate Blender-compliant ZIP packages to minimize manual steps.

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
FUM/
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
└── CHANGELOG.md
```

---

## 🛠️ Roadmap | 开发计划

* [x] 重复顶点检测（Merge by Distance问题）
* [x] 法线方向检测
* [x] N-Gon 检测
* [x] 孤立顶点检测
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
