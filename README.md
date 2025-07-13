# Context Storage

様々なIDE、AI コーディングアシスタント、AIエージェント用のプロジェクト固有ルールとワークフローを管理するリポジトリです。

## 概要

このリポジトリは、Windsurf、Cursor、Claude Code などの AI 対応 IDE や、各種 AI エージェント・コーディングエージェントで使用するプロジェクト固有のルールやワークフローを一元管理します。プロジェクトごとにディレクトリを作成し、そのディレクトリを読み込むだけで、AI アシスタントがプロジェクトの文脈を理解し、適切なコーディング支援を行えるようにすることを目的としています。

## ディレクトリ構成

```
context-storage/
├── project-name/              # プロジェクト固有のコンテキスト
│   ├── .cursorrules          # Cursor用ルール
│   ├── .claude               # Claude Code用設定
│   ├── .windsurf/            # Windsurf用設定
│   │   ├── rules/            # プロジェクト固有ルール
│   │   └── workflows/        # プロジェクト固有ワークフロー
│   ├── context.md            # プロジェクト概要とコンテキスト
│   └── setup.md              # 初期セットアップ手順
│
├── shared/                    # 共通ルール・ワークフロー
│   ├── rules/                # 汎用コーディングルール
│   │   ├── dbt.md           # DBTベストプラクティス
│   │   ├── typescript.md    # TypeScriptスタイルガイド
│   │   └── python.md        # Pythonコーディング規約
│   │
│   └── workflows/            # 汎用ワークフロー
│       ├── git-operations.md # Git操作標準化
│       └── ci-cd.md         # CI/CDパイプライン
│
└── templates/                # プロジェクトテンプレート
    ├── web-app/             # Webアプリケーション用
    ├── data-pipeline/       # データパイプライン用
    └── ml-project/          # 機械学習プロジェクト用

```

### 現在の構成（移行中）

現在は Windsurf 向けの構成となっていますが、今後は上記の構成に移行予定です：

```
.windsurf/
├── rules/          # コーディングルールとベストプラクティス
└── workflows/      # 自動化ワークフロー

.github/
└── workflows/      # GitHub Actions（Claude AI統合）

docs/              # プロジェクトドキュメント
```

## 主な特徴

### 1. マルチ IDE/エージェント対応

単一のリポジトリで複数の AI コーディングツールをサポート：

- **Windsurf**: `.windsurf/` ディレクトリ
- **Cursor**: `.cursorrules` ファイル
- **Claude Code**: `.claude` 設定、`CLAUDE.md` ファイル
- **その他 AI エージェント**: カスタム設定ファイル

### 2. プロジェクト固有のコンテキスト管理

各プロジェクトディレクトリに含まれる情報：

- **context.md**: プロジェクトの背景、技術スタック、アーキテクチャ
- **setup.md**: 開発環境のセットアップ手順
- **IDE固有ルール**: 各IDEに最適化されたコーディングルール
- **カスタムワークフロー**: プロジェクト特有の作業フロー

### 3. 再利用可能なコンポーネント

- **共通ルール**: 言語やフレームワーク別のベストプラクティス
- **汎用ワークフロー**: Git操作、CI/CD、テストなどの標準化
- **プロジェクトテンプレート**: 新規プロジェクトの迅速な立ち上げ

## 使用方法

### 1. 既存プロジェクトのコンテキストを利用

```bash
# プロジェクトのコンテキストをIDEに読み込む
cp -r context-storage/project-name/.windsurf /your-project/     # Windsurf用
cp context-storage/project-name/.cursorrules /your-project/     # Cursor用
cp context-storage/project-name/CLAUDE.md /your-project/        # Claude Code用
```

### 2. 新規プロジェクトのセットアップ

```bash
# テンプレートからプロジェクトを初期化
cp -r context-storage/templates/web-app/* /your-new-project/
# プロジェクト固有の設定をカスタマイズ
```

### 3. AI アシスタントでの活用

1. IDE でプロジェクトを開く
2. 該当するコンテキストファイルが自動的に読み込まれる
3. AI アシスタントがプロジェクトの文脈を理解して適切な支援を提供

## 貢献方法

### プロジェクトコンテキストの追加

1. `project-name/` ディレクトリを作成
2. 各 IDE 用の設定ファイルを配置
3. `context.md` と `setup.md` を記述
4. プルリクエストを作成

### 共通ルール・ワークフローの改善

1. `shared/` ディレクトリ内の該当ファイルを編集
2. 実プロジェクトでの検証を実施
3. プルリクエストで変更を提案

## 想定される利用シーン

- **チーム開発**: 新メンバーが参加時、プロジェクトのコンテキストを即座に AI アシスタントに理解させる
- **マルチプロジェクト**: 複数プロジェクト間を移動する際、各プロジェクトの文脈を素早く切り替え
- **技術標準化**: 組織全体でコーディング規約やワークフローを統一
- **AI 活用最大化**: 各 IDE の AI 機能を最大限に活用するための最適な設定

## 今後の展望

- プロジェクトテンプレートの充実
- より多くの IDE/AI ツールへの対応
- コミュニティによるベストプラクティスの共有
- 自動コンテキスト生成ツールの開発

## ライセンス

このプロジェクトのライセンスについては、各ファイルのヘッダーを参照してください。

---

🔗 **GitHub**: [https://github.com/gotalab/context-storage](https://github.com/gotalab/context-storage)