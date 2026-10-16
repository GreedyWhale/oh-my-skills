# oh-my-skills

个人维护的 AI skills 集合。每个技能独立存放在 `skills/<skill-name>/`，包含自己的 `SKILL.md` 和所需资源，可以单独安装、使用和维护。

## 技能目录

| 技能 | 用途 | 版本 |
|---|---|---|
| [project-rules-init](skills/project-rules-init/SKILL.md) | 为新项目或已有项目初始化通用 AI 总则与项目专项规则，保留已有约束，区分已配置、不适用和尚未配置的要求 | 1.1.0 |

## 安装与使用

选择需要的技能，将对应的整个目录安装到工具的技能目录；不要把仓库根目录作为一个技能安装。

例如，使用 Codex 的 skill-installer：

```text
使用 $skill-installer，从 GreedyWhale/oh-my-skills 安装 skills/project-rules-init。
```

也可以克隆本仓库后，将 `skills/project-rules-init/` 完整复制到个人技能目录，例如 `~/.agents/skills/project-rules-init/`。保留技能自带的所有子目录；如果目标已存在，先检查版本和本地修改，不要直接覆盖。

安装后，在目标项目中调用：

```text
使用 $project-rules-init，为当前项目初始化总则与项目专项规则，按现有项目证据完成适用项配置。
```

具体运行要求、边界和验证方式以各技能的 `SKILL.md` 为准。安装技能与在项目中执行技能是两个步骤。

## 集合维护

- 新技能放入独立的 `skills/<skill-name>/` 目录，并更新上方目录表。
- 技能的脚本、模板、参考资料和界面元数据随技能存放，不将单个技能的内容展开到仓库根目录。
- 每个技能自行说明依赖和验证入口；集合不预设所有技能使用相同技术栈或规则。
- 更新已有技能时保留其版本、用户定制及兼容性边界，不自动影响其他技能或已安装副本。

当前 `project-rules-init` 的受控验证命令（在仓库根目录执行，要求 POSIX 环境和 Python 3.10+）：

```sh
python3 skills/project-rules-init/scripts/validate.py
```

该命令仅验证此技能，不代表整个集合未来新增的技能都已验证。
