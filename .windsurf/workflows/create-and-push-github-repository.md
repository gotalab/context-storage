---
description: Push an Existing Local Project to a New Repository
---

# GitHub Push Workflow *(MCP‑enabled)*

This guide shows you how to push **an existing local project folder to a brand‑new GitHub repository**, with repository creation handled by the **Model Context Protocol (MCP) GitHub Server tool**. The GitHub repository will automatically inherit the **same name as your local folder**.

> **Note on MCP** — Your environment is already authenticated to GitHub through the MCP GitHub Server tool. You do **not** need to open the GitHub Web UI; the tool creates the repository and handles pushes behind the scenes.

---

## Prerequisites

* **Git ≥ 2.x** installed (`git --version`).
* A **GitHub account** with SSH **or** HTTPS access configured.
* Use **MCP GitHub Server**

---

## Action 1 — Navigate to Your Project Folder

```bash
cd /path/to/your/project            # e.g. my-project
```

---

## Action 2 — Initialize the Local Git Repository

```bash
if [ ! -d .git ]; then
  git init                           # create .git if it doesn’t exist
fi
git branch -M main                   # optional: use main as default branch
```

---

## Action 3 — Generate `.gitignore` Automatically and Review

The agent model inspects your project files and **auto‑generates an appropriate `.gitignore`** (languages, build outputs, editor folders, etc.).

1. **Agent generates** the file.
2. **You review & tweak** any patterns if needed.
3. **Stage the file** once it looks correct:

   ```bash
   git add .gitignore
   ```

---

## Action 4 — Stage and Commit Your Code — Stage and Commit Your Code — Stage and Commit Your Code — Stage and Commit Your Code

```bash
git add .
git commit -m "Initial commit"
```

---

## Action 5 — Create the Matching Repository via MCP GitHub Server Tool

When your first push (next action) hits GitHub, the create_repository tool automatically provisions a repository named $(basename "$PWD") under your account/organization with the chosen visibility (default private). No Web UI interaction is required.

> Skip if your workflow auto‑creates on push.

---

## Action 6 — Add the Remote Origin

```bash
# replace YOUR-USER with your GitHub username
# choose SSH or HTTPS depending on your config

git remote add origin git@github.com:YOUR-USER/$(basename "$PWD").git
# or
# git remote add origin https://github.com/YOUR-USER/$(basename "$PWD").git
```

---

## Action 7 — Push to GitHub


```bash
git push -u origin main   # first push sets upstream
```

---

## Action 8 — Verify

* Refresh or open the repository URL printed by the push output.
* Ensure files and the **main** branch are present.


---

## Troubleshooting & Tips

* **Auth error:** confirm SSH key or PAT; MCP needs valid credentials.
* **`fatal: remote origin already exists`:** you added the remote earlier; update with `git remote set-url origin <new-url>`.
* **Large files (> 100 MB):** enable Git LFS → `git lfs install && git lfs track "*.zip"`.
* **Sensitive data pushed:** rotate secrets, then clean history with `git filter-repo` or use GitHub secret‑scanning.

---

Happy pushing (cleanly)! 🚀