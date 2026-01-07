# 🚀 MDAW 环境恢复指南 (MDAW Environment Restoration Guide)

假设你在新电脑的根目录是 `E:\Code\` (或者 Mac/Linux 的 `~/Code/`)。

## 第 1 步：克隆主修罗场 (Main Workspace)
首先拉取主仓库，确立 `pyart` 为集成中心。

```bash
cd E:\Code
git clone https://github.com/peinibiancheng/pyart.git pyart
cd pyart
```

## 第 2 步：恢复多维空间 (Reconstruct Worktrees)
进入主目录后，运行以下命令。这会从远程拉取各角色分支，并在物理上重建所有平行文件夹。

> **注意**：由于分支已在远程存在，`git worktree` 会自动建立追踪关系，无需手动 checkout。

```bash
# 1. 确保获取所有远程信息
git fetch --all
# 创建分支
git checkout develop

# 2. 一键重建 5 个角色空间
git worktree add ../pyart-architect feature/architect
git worktree add ../pyart-scrum feature/scrum-master
git worktree add ../pyart-docs feature/knowledge
git worktree add ../pyart-qa feature/testing
git worktree add ../pyart-devops feature/devops
```

## 第 3 步：初始化 Git Flow (可选)
为了让工具链完整，建议重新初始化 git flow 配置。

```bash
git flow init -d
```

---

## 验证结果
执行完上述步骤后，你的文件夹结构将完美复刻：

```text
E:\Code\
├── pyart/           (Main - develop)
├── pyart-architect/ (Architect)
├── pyart-devops/    (DevOps)
├── pyart-docs/      (Docs)
├── pyart-qa/        (QA)
└── pyart-scrum/     (Scrum)
```
