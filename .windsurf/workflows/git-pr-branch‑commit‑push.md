---
description: creating a new branch, committing your work, pushing the branch to GitHub, and opening a Pull Request (PR).
---

````markdown
# Fast Branch‑Commit‑Push‑PR Workflow

Follow these exact commands in order. Replace placeholders `<...>` with your values.

---

## 1. Create a feature branch
Please automatically generate an appropriate branch name for the task and create the branch.

```bash
git switch -c feature/<short‑slug>
```

---

## 2. Work, stage, and commit

```bash
git add <changes files>

# ✅ Commit with an imperative Conventional‑Commit message
git commit -m "<type>(<scope>): <short summary>"
```

**Example**

```bash
git commit -m "feat(auth): add JWT middleware"
```

| Field       | Purpose                     | Examples                                           |
| ----------- | --------------------------- | -------------------------------------------------- |
| **`type`**  | what changed                | `feat`, `fix`, `docs`, `refactor`, `test`, `chore`, etc... |
| **`scope`** | module / feature (optional) | `auth`, `api`, `db`                                |
| **summary** | ≤ 50 chars, no period       | `add JWT middleware`                               |
| **body**    | why / background            | “Adds token validation…”                           |

---

## 3. Push the branch (Standard Git)

```bash
git push -u origin feature/<short‑slug>
```

---

## 4. Open a Pull Request (MCP tool)
Open a pull request using the create_pull_request mcp tool.

---

## 5. Merge & clean up

```bash
# After approvals & green CI
git checkout main
git pull origin main
git branch -d feature/<short‑slug>
git push origin --delete feature/<short‑slug>
```

Done! 🚀