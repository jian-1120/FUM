# FUM — Fix Your Mesh

**专业级 Blender 网格验证工具包。**

FUM 是一款专业的 Blender 插件，专注于网格检查和导出预检验证。它帮助艺术家、环境设计师、技术艺术家和资产管线团队在模型导出到游戏引擎、渲染工作流或其他下游生产工具之前，识别常见的几何问题。

## 版本信息

| 字段 | 值 |
|---|---|
| 当前版本 | v2.2 |
| 发布主题 | Public Release Polish Update |
| Blender 目标版本 | Blender 4.x |
| 许可证 | MIT 许可证 |
| 仓库 | <https://github.com/jian-1120/FUM> |

## 🚀 功能概览

FUM 专注于在导出前进行实用的网格质量检查。该插件提供独立的检查工具，以及一个统一的 **导出预检** 工作流，将活动网格总结为 **PASS**、**WARNING** 或 **FAIL**。

| 检查项 | 目的 | 预检严重性 |
|---|---|---|
| 非流形边 | 查找可能破坏拓扑、碰撞、着色或导出工作流的边。 | FAIL |
| 重复顶点 | 查找距离小于可配置阈值的顶点。 | WARNING |
| 翻转法线 | 查找与重新计算的法线相比，法线方向反转的面。 | FAIL |
| N-Gons | 查找具有四个以上顶点的面。 | WARNING |
| 孤立顶点 | 查找没有连接边的游离顶点。 | WARNING |

## 🛠️ 导出预检工作流

**导出预检** 工作流旨在作为资产交付前的最终检查。点击 FUM 面板中的 **运行导出预检**，即可运行所有检查，更新问题计数器，并显示清晰的导出就绪性摘要。

| 状态 | 含义 | 建议操作 |
|---|---|---|
| PASS | 未检测到已知网格问题。 | 网格已准备好导出。 |
| WARNING | 检测到非阻塞性问题。 | 导出前请检查高亮显示的几何体。 |
| FAIL | 检测到阻塞性导出问题。 | 导出前请修复报告的问题。 |

> FUM 不会自动修改您的网格。它检测、高亮显示并总结潜在问题，以便艺术家能够控制最终的清理过程。

## ⬇️ 安装指南

从 [GitHub Releases 页面](https://github.com/jian-1120/FUM/releases/latest) 下载最新版本。如果您从 GitHub 下载源代码 ZIP，请安装包含 `__init__.py`、`operators/`、`ui/` 和 `blender_manifest.toml` 的内部 `FUM` 文件夹。

1.  下载或克隆仓库。
2.  找到内部的 `FUM` 插件文件夹。
3.  将 `FUM` 文件夹复制到 Blender 的插件目录中，或通过 Blender 的插件偏好设置进行安装。
4.  在 `编辑 > 偏好设置 > 插件` 中启用 **FUM - Fix Your Mesh**。
5.  使用 `N` 键打开 3D 视口侧边栏，然后选择 **FUM** 选项卡。

## 🗺️ 路线图

*   当前：Blender 插件 (开源, MIT)
*   2026 年夏季：Blender 版 FUM Pro (包含修复指导)
*   探索中：Maya、3ds Max 和移动版本

## 🖼️ 视觉资产

### 宣传图

<!-- Placeholder for Banner Image -->

### 演示 GIF

<!-- Placeholder for Demo GIF -->

### 功能截图

<!-- Placeholder for Feature Screenshots -->

## 仓库结构

```text
FUM/
├── FUM/
│   ├── __init__.py
│   ├── blender_manifest.toml
│   ├── operators/
│   │   ├── duplicate_vertices.py
│   │   ├── export_preflight.py
│   │   ├── flipped_normals.py
│   │   ├── isolated_vertices.py
│   │   ├── ngons.py
│   │   └── non_manifold_edges.py
│   └── ui/
│       └── panel.py
├── docs/
│   └── ENGINEERING_NOTES.md
├── images/
│   ├── banners/
│   ├── gifs/
│   └── screenshots/
├── CHANGELOG.md
├── LICENSE
├── README.md
└── RELEASE_NOTES_v2.1.md
```

## 发布打包说明

对于手动安装，内部的 `FUM` 文件夹就是 Blender 插件文件夹。对于未来的市场打包，包应保留 `__init__.py`、`blender_manifest.toml`、`operators/`、`ui/` 和 MIT `LICENSE` 文件。内部工作流文件和生成的构建产物通过 `.gitignore` 排除。

## 许可证

FUM 根据 MIT 许可证发布。请参阅 [`LICENSE`](LICENSE) 获取完整的许可证文本。

## 作者

FUM 由 **Jian** 开发，他是一名环境设计学生，致力于探索 AI 辅助建模工作流和实用的 3D 生产工具。
