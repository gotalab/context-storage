# Context Storage

Windsurf AI アシスタント用のルールとワークフローを管理するリポジトリです。

## 概要

このリポジトリは、Windsurf（AIコードエディタ）で使用する各種ルールやワークフローを一元管理し、開発の一貫性と効率性を向上させることを目的としています。

## ディレクトリ構成

```
context-storage/
├── .windsurf/
│   ├── rules/          # コーディングルールとベストプラクティス
│   │   ├── dbt.md                    # DBTテストのベストプラクティス
│   │   ├── dbt-implementation.md     # DBT実装ガイド
│   │   ├── code-style-typescript.md  # TypeScriptコーディングスタイル
│   │   ├── data-scientist.md         # データサイエンティスト向けルール
│   │   └── cs-tutor.md              # CSチューター用ルール
│   │
│   └── workflows/      # 自動化ワークフロー
│       ├── python-project-setup.md               # Pythonプロジェクトセットアップ
│       ├── git-create-and-push-github-repository.md  # GitHubリポジトリ作成
│       ├── git-pr-branch‑commit‑push.md          # PR作成ワークフロー
│       ├── build-and-deploy-mytarget.md          # ビルド＆デプロイ
│       ├── zenn-article-create-and-preview.md    # Zenn記事作成
│       └── test.md                              # テストワークフロー
│
├── .github/
│   └── workflows/      # GitHub Actions
│       ├── claude.yml               # Claude PR アシスタント
│       ├── claude-code-review.yml   # Claude コードレビュー
│       └── claude_docs.yml          # Claude ドキュメント生成
│
└── docs/              # プロジェクトドキュメント
    └── dbt-rules.md   # DBTルールの日本語説明

```

## 主な機能

### 1. コーディングルール (`.windsurf/rules/`)

各技術スタックに対するベストプラクティスとコーディング規約を定義：

- **DBT**: データ変換ツールのテスト手法とベストプラクティス
- **TypeScript**: 型安全なコーディングスタイルガイド
- **データサイエンス**: 機械学習プロジェクトのガイドライン

### 2. ワークフロー (`.windsurf/workflows/`)

頻繁に行う作業を自動化するためのワークフロー定義：

- プロジェクトセットアップの自動化
- Git操作の効率化
- ビルド・デプロイプロセスの標準化

### 3. GitHub Actions統合

Claude AIを活用した自動化：

- プルリクエストの自動レビュー
- コード品質チェック
- ドキュメント自動生成

## 使用方法

1. Windsurfエディタでプロジェクトを開く
2. 必要なルールやワークフローを`.windsurf`ディレクトリから選択
3. AIアシスタントがこれらのルールに基づいてコード生成・レビューを実行

## 貢献方法

1. 新しいルールやワークフローの追加は、適切なディレクトリに配置
2. 日本語ドキュメントは`docs/`ディレクトリに追加
3. プルリクエストを作成し、Claude AIによる自動レビューを受ける

## ライセンス

このプロジェクトのライセンスについては、各ファイルのヘッダーを参照してください。

---

🔗 **GitHub**: [https://github.com/gotalab/context-storage](https://github.com/gotalab/context-storage)