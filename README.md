# FUM 🛠️

**Fix Your Mesh — A Blender Modeling Assistant**

一个用于检测和高亮非流形边的 Blender 建模辅助插件。

A lightweight Blender addon for detecting and highlighting non-manifold edges in mesh objects.

---

## ✨ Features | 功能

* 🔍 检测模型中的非流形边
  Detect non-manifold edges in the active mesh
* 🔺 检测模型中的重复顶点 (支持阈值调节)
  Detect duplicate vertices in the active mesh (with adjustable threshold)

* 🎯 自动高亮问题边
  Highlight problematic edges in Edit Mode

* 📊 在UI面板中显示检测结果
  Display detection results in a simple UI panel

* ⚡ 轻量快速，无需额外依赖
  Lightweight and fast, no external dependencies

---

## 📦 Installation | 安装方法

1. 下载 `.py` 文件（例如 `model_doctor.py`）
   Download the `.py` file (e.g. `model_doctor.py`)

2. 打开 Blender
   Open Blender

3. 进入：
   Go to:
   `Edit → Preferences → Add-ons`

4. 点击 **Install** 并选择插件文件
   Click **Install** and select the addon file

5. 勾选启用插件
   Enable the addon

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

> <img width="841" height="727" alt="image" src="https://github.com/user-attachments/assets/35e47d0a-22c7-4797-b23a-11cbe4743970" />


```id="demo_path"
images/demo.png
```

---

## 📁 Project Structure | 项目结构

```id="proj_struct"
fum/
│
├── __init__.py
├── operators/
│   ├── __init__.py
│   ├── non_manifold_edges.py
│   └── duplicate_vertices.py
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
* [ ] 法线方向检测
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
