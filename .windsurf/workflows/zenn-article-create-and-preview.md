---
description: Zenn CLIで記事を新規作成しプレビューする方法
---

# Zenn CLIを使って記事を新規作成し、プレビューするワークフロー

このワークフローは、[Zenn CLI公式ガイド](https://zenn.dev/zenn/articles/zenn-cli-guide) を基に、Zennで新しい記事を作成しローカルでプレビューする手順をまとめたものです。

## 手順

1. 新しい記事を作成する
   ```sh
   npx zenn new:article
   ```
   - 対話形式でタイトルや公開設定などを入力します。
   - `articles/` 配下にMarkdownファイルが生成されます。

2. ローカルサーバーでプレビューする
   ```sh
   npx zenn preview
   ```
   - `http://localhost:8000` で記事をプレビューできます。

3. ブラウザで `http://localhost:8000` にアクセスし、記事内容を確認します。

## 参考
- [Zenn CLI公式ガイド](https://zenn.dev/zenn/articles/zenn-cli-guide)

// turbo-all
