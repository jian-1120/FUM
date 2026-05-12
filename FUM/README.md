# FUM Addon Folder

这是一个可直接安装到 Blender 的 **FUM 插件文件夹**。本目录包含 `__init__.py`、`operators/` 与 `ui/`，因此它是用户从 GitHub ZIP 解压后应当安装或复制到 Blender `addons` 目录中的内层插件目录。

## Version

| Field | Value |
|---|---|
| Addon | FUM |
| Version | v1.6 |
| Update | Export Preflight Workflow |
| Blender Target | Blender 4.x |

## v1.6 Export Preflight Workflow

FUM v1.6 将插件从单项网格检查工具扩展为面向导出流程的预检助手。用户可以在 FUM 面板中点击 **Run Export Check**，一次性运行非流形边、重复顶点、翻转法线、N-Gons 与孤立顶点检测，并在界面中获得 **PASS**、**WARNING** 或 **FAIL** 的导出状态摘要。

| Status | Meaning |
|---|---|
| PASS | 未发现已知网格问题，模型可以进入导出流程。 |
| WARNING | 检测到非阻断问题，例如重复顶点、N-Gons 或孤立顶点；建议在导出前复查。 |
| FAIL | 检测到阻断问题，例如非流形边或翻转法线；建议修复后再导出。 |

## Installation

1. 将整个 `FUM` 文件夹复制到 Blender 的 `addons` 目录，或通过 Blender 的插件安装界面选择包含 `__init__.py` 的这一层目录。
2. 在 Blender 中进入 `Edit -> Preferences -> Add-ons`。
3. 搜索并启用 `FUM`。
4. 在 3D Viewport 中按 `N` 打开右侧栏，并进入 **FUM** 面板。

> 注意：如果你是通过 GitHub 的 `Download ZIP` 下载仓库，请确保安装的是包含 `__init__.py` 的内层 `FUM` 文件夹，而不是外层仓库文件夹。
