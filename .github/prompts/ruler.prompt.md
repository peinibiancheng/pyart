---
agent: agent
---
# Storage Rules
- Always save implementation plans, task lists, and draft artifacts to the project-local directory: ./github/plan/.
- Do not use the global user directory for project-specific plans.
- Ensure ./.github/ is added to .gitignore.

# 工作模式
- 按.github\mdaw\MultiDimensionalAgileWorkspace.md 说明的多维工作空间模式工作。

# Multi-Dimensional Workspace Commands
- **Save (保存)**: Stage and commit all changes in the current active worktree.
  - Operation: git add ., git commit -m "update: <context>" 
- **Deliver (交付/提交)**: Merge current permanent role branch into develop.
  - Operation: 
    1. Commit current changes in role workspace.
    2. cd <main-workspace-path> (e.g.,E:/code/pyart/)
    3. git pull (ensure develop is latest)
    4. git merge <role-branch-name>
    5. git push origin develop
    6. cd <role-workspace-path>
    7. git merge develop (Sync back)
- 执行git flow feature finish 时，要让我确认一下。

# 术语表
1：需要，是的。
0：不需要，不。
同步代码：将主工作区的develop分支的最新更改合并到各个角色工作区。
提交代码：将当前角色工作区的更改提交到对应的本地角色分支,然后合并到develop，然后把develop合并回角色工作区。
保存代码：将当前角色工作区的更改提交到对应的本地角色分支。
推送代码：将当前角色工作区的本地角色分支推送到远程仓库，将develop分支推送到远程仓库。
站会：每日站会，简短汇报昨天做了什么，今天计划做什么，有没有阻碍。由Scrum Master主持。
归档：将已完成的任务从任务列表中移除，并存档到历史记录文件中。
任务列表：.github/mdaw/tasks.md 文件，包含当前待办任务。
角色工作区：每个角色对应的独立工作区目录，如 PyPixel-architect/。
主工作区：包含主代码库的工作区目录，如 PyPixel/。
发布：将 develop 分支的最新代码打包发布，通常由 DevOps 负责。
阻碍：影响任务完成的任何问题或障碍，需要及时报告给 Scrum Master。
知识库：.github/knowledge/ 目录，存放项目相关的文档和知识资源。
任务分解：将大任务拆分为更小、更易管理的子任务，便于分配和跟踪进度。
总结：由 Knowledge Manager 定期编写的项目进展和经验总结文档。
更新文档：由 Knowledge Manager 负责，确保项目文档的及时更新和维护。

# 沟通规范
- 使用简洁明了的语言描述问题和需求。
- 遇到阻碍时，及时向 Scrum Master 报告。
- 定期更新任务状态，确保团队成员了解进展。
- 尊重他人意见，积极参与讨论和决策。
- 保持专业态度，遵守团队约定的工作流程和规范。
# 角色职责
- **Architect (架构师)**: 负责系统设计、目录结构和核心引擎开发。
- **Product Owner (产品负责人)**: 负责需求分析、功能定义 (Spec)、背靠背验收 (UAT)。
- **Scrum Master (敏捷主管)**: 负责冲刺规划、任务分解和每日站会主持。
- **Knowledge Manager (知识管理员)**: 负责项目文档编写和维护。
- **Testing/QA (测试/质量保证)**: 负责单元测试、集成测试和CI测试脚本编写。
- **DevOps (开发运维)**: 负责GitHub Actions、打包和部署。
# 立即目标
1. 定义项目架构。
2. 设置基本的CI/CD流程。
3. 开始编写项目文档。
4. 制定详细的任务列表并分配给各角色。
5. 确保所有角色理解并遵守多维工作空间模式。
# 长期目标
1. 完成核心功能开发。
2. 实现全面的测试覆盖。
3. 优化CI/CD流程，实现自动化部署。
4. 建立完善的知识库，方便团队成员查阅。
5. 持续改进工作流程，提高团队协作效率。
# 注意事项
- 遵守多维工作空间模式，确保各角色工作区与主工作区同步。
- 定期检查任务列表，确保任务按时完成。
- 保持良好的沟通，及时解决阻碍。
- 关注项目进展，确保长期目标的实现。
# 参考资料
- .github/mdaw/MultiDimensionalAgileWorkspace.md
- .github/mdaw/architecture.md
- .github/mdaw/roadmap.md
- .github/mdaw/tasks.md
- docs/spec.md