# 多维敏捷工作空间设计方案 (Multi-Dimensional Agile Workspace)

## 1. 核心理念 (The Vision)
针对复杂项目（如基于 Tauri 的跨平台应用），通过 **Git Flow** 与 **Git Worktree** 的深度结合，将单一的代码仓库演变为一个具有“专业分工”的多维物理空间。每个空间代表一个特定的角色视角，旨在解决单人开发中的“角色混淆”与“上下文切换开销”问题。

## 2. 技术栈与工具
- **核心流控**: Git Flow (AVH Edition) - 提供严格的分支管理规范。
- **物理隔离**: Git Worktree - 提供瞬间切换、无需 `stash` 的隔离环境。
- **环境**: Windows / PowerShell / VS Code。

## 3. 空间布局与角色定义 (Workspace Roles)

| 物理路径 | 对应分支 | 角色 (Role) | 核心职责 | 推荐策略 |
| :--- | :--- | :--- | :--- | :--- |
| `pyart/` | `develop` | **Main** | 核心开发、代码集成中心。 | 常驻 |
| `pyart-architect/` | `feature/architect` | **Architect** | 架构规划、解耦设计。 | **常驻** |
| `pyart-product/` | `feature/product` | **Product Owner** | 需求分析、功能定义 (Spec)、验收 (UAT)。 | **常驻** |
| `pyart-scrum/` | `feature/scrum-master` | **Scrum Master** | 任务管理、Sprint 规划。 | **常驻** |
| `pyart-docs/` | `feature/knowledge` | **Knowledge Manager** | 文档维护、技术债管理。 | **常驻** |
| `pyart-qa/` | `feature/testing` | **Testing/QA** | 测试用例编写、回归测试。 | **常驻** |
| `pyart-devops/` | `feature/devops` | **DevOps** | 发布流程、构建脚本、打包与签名。 | **常驻 (强烈推荐)** |

## 4. 关键价值 (Key Benefits)
1. **零成本上下文切换**: 无需 `git stash` 或 `git commit -m "wip"`，直接切换文件夹即可进入另一个工作状态。
2. **物理级的视角转换**: 空间的变换暗示大脑进行“角色换位”。在 `testing` 文件夹里，你的心态是“找茬”；在 `architect` 文件夹里，你的心态是“全局规划”。
3. **并行构建与运行**: 在 Rust 编译庞大的后端时，你可以直接在 Web 空间继续打磨 UI，互不阻塞。
4. **单人敏捷 (Solo-Agile) 的具象化**: 将抽象的敏捷角色转化为可见的物理存在，确保每一个角色（如文档、测试）都不会被忽视。

## 5. 工作流与生命周期管理 (Workflow & Lifecycle)

为了维持“角色空间”的长期存在，我们不能简单使用 `git flow feature finish`（默认会删除分支）。需采用以下“常驻分支策略”：

### A. 常驻角色分支 (Permanent Role Branches)
适用于 Architect, Scrum Master, Knowledge Manager, Testing 等长期职能。

1.  **日常工作**: 在各自的工作树（Worktree）中正常 `commit`。
2.  **成果交付 (Merge)**:
    - 切换回主空间: `cd ../pyart`
    - 手动合并（保留分支）:
      ```powershell
      git checkout develop
      git merge feature/architect
      # 可选: git push origin develop
      ```
3.  **反向同步 (Update)**:
    - 切换回角色空间: `cd ../pyart-architect`
    - 拉取主干更新: `git pull origin develop` (或 `git merge develop`)
    - *目的: 确保架构师基于最新的代码库进行设计。*

### B. 临时特性分支 (Transient Feature Branches)
适用于开发特定功能（如 `feature/login-page`），做完即走。

1.  **开始**: `git flow feature start login-page`
2.  **开发**: 可以在主空间，或创建一个临时的 Worktree。
3.  **结束**:
    - `git flow feature finish login-page`
    - 分支被自动删除。
    - 如果创建了 Worktree，需手动清理: `git worktree remove ../pyart-login-page`

---
*修订于 2026-01-06 — 增加“常驻分支策略”以适配长期角色分工。*
