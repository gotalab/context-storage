# Context Storage

新規プロジェクト作成時のAI開発環境初期セットアップを劇的に簡素化するテンプレート集です。

## 概要

新しいプロジェクトを作成する度に、Claude Code、Cursor、Windsurf などの AI 対応 IDE の初期設定を一から行うのは非常に面倒です。このリポジトリは、技術スタック別に最適化された設定ファイル、ルール、フック、コマンドなどを事前に用意し、**ディレクトリをコピーするだけで、すぐに実運用レベルで AI IDE を使い始められる**ことを目的としています。

## ディレクトリ構成

```
context-storage/
├── python/                   # Python プロジェクト用テンプレート
│   ├── .cursorrules         # Cursor 用ルール（Python特化）
│   ├── CLAUDE.md            # Claude Code 用設定
│   ├── .windsurf/           # Windsurf 用設定
│   │   ├── rules/           # Python コーディングルール
│   │   └── workflows/       # Python ワークフロー
│   ├── .github/             # GitHub Actions テンプレート
│   │   └── workflows/       # Python CI/CD
│   ├── pyproject.toml       # Python 設定ファイル
│   ├── .gitignore           # Python 用 gitignore
│   └── setup-commands.md    # 初期セットアップコマンド集
│
├── typescript/              # TypeScript プロジェクト用テンプレート
│   ├── .cursorrules         # TypeScript/Node.js ルール
│   ├── CLAUDE.md            # Claude Code 設定
│   ├── .windsurf/           # Windsurf 設定
│   ├── package.json         # npm 設定テンプレート
│   ├── tsconfig.json        # TypeScript 設定
│   ├── .gitignore           # Node.js 用 gitignore
│   └── setup-commands.md    # セットアップ手順
│
├── react/                   # React プロジェクト用テンプレート
│   ├── .cursorrules         # React/Next.js ルール
│   ├── CLAUDE.md            # フロントエンド特化設定
│   ├── .windsurf/           # React ワークフロー
│   └── setup-commands.md    # React セットアップ
│
├── data-science/            # データサイエンス用テンプレート
│   ├── .cursorrules         # Jupyter/pandas ルール
│   ├── CLAUDE.md            # ML/AI 開発設定
│   ├── .windsurf/           # データ分析ワークフロー
│   └── requirements.txt     # データサイエンス用ライブラリ
│
└── shared/                  # 共通設定・ユーティリティ
    ├── hooks/               # Git hooks テンプレート
    ├── github-actions/      # 再利用可能な Actions
    └── common-configs/      # 共通設定ファイル

```

### 現在の構成（移行準備中）

現在は Windsurf 用の汎用ルールが配置されています。今後、技術スタック別のテンプレートに再編成予定：

```
.windsurf/rules/     # → shared/ や各技術スタックに移行予定
.windsurf/workflows/ # → 技術スタック別ワークフローに分割予定
```

## 解決する問題

### 😫 現在の問題
- 新規プロジェクト作成の度に AI IDE の初期設定を一から行う必要がある
- 技術スタックごとに最適な `.cursorrules` や `CLAUDE.md` を毎回作成する手間
- プロジェクト固有のフック、設定ファイル、GitHub Actions の設定が面倒
- チーム間で AI IDE の設定が統一されていない

### ✨ このリポジトリで実現すること
- **1分で完了**: `cp -r python/* /your-new-project/` でセットアップ完了
- **即実運用**: コピー直後から AI IDE が最適な状態で動作
- **技術スタック特化**: Python、TypeScript、React など、各技術に最適化済み
- **チーム標準化**: 組織全体で一貫した AI 開発環境

## 主な特徴

### 1. ワンコマンドセットアップ

```bash
# 新しい Python プロジェクトの場合
cp -r context-storage/python/* /your-new-project/
cd /your-new-project
# → 即座に Claude Code、Cursor、Windsurf が最適化状態で利用可能！
```

### 2. 技術スタック別最適化

各技術スタックに特化した設定：

- **Python**: データサイエンス、Web開発、CLI ツール向けルール
- **TypeScript**: Node.js、フロントエンド、フルスタック向け設定
- **React**: コンポーネント設計、状態管理、パフォーマンス最適化
- **データサイエンス**: Jupyter、pandas、機械学習向け環境

### 3. 全IDE対応済み

各テンプレートには以下が含まれます：

- **`.cursorrules`**: Cursor 用のプロジェクト固有ルール
- **`CLAUDE.md`**: Claude Code 用のコンテキストとコマンド
- **`.windsurf/`**: Windsurf 用のルールとワークフロー
- **設定ファイル**: `tsconfig.json`、`pyproject.toml` など

## 使用方法

### 🚀 Step 1: 新規プロジェクト作成

```bash
# 1. 新しいプロジェクトディレクトリを作成
mkdir my-awesome-project
cd my-awesome-project

# 2. 技術スタックに応じたテンプレートをコピー
cp -r /path/to/context-storage/python/* .        # Python プロジェクトの場合
# または
cp -r /path/to/context-storage/typescript/* .    # TypeScript プロジェクトの場合
# または  
cp -r /path/to/context-storage/react/* .         # React プロジェクトの場合
```

### ⚡ Step 2: 即座に AI IDE で開発開始

```bash
# IDE を起動（設定は既に最適化済み）
cursor .        # Cursor の場合
code .          # Claude Code の場合
# Windsurf でプロジェクトを開く
```

**これだけで完了！** AI アシスタントが最適化された状態で利用可能になります。

### 🛠️ Step 3: 必要に応じてカスタマイズ

各テンプレートの `setup-commands.md` を参照して、追加のセットアップを実行：

```bash
# Python の場合の例
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## 具体的な使用例

### Python データサイエンスプロジェクトの場合

```bash
mkdir ml-analysis
cd ml-analysis
cp -r context-storage/data-science/* .

# IDE で開くと、以下が自動で設定済み：
# - Jupyter notebook 向けのルール
# - pandas/numpy 最適化設定  
# - ML ライブラリのインポート補完
# - データ可視化のベストプラクティス
```

### TypeScript Web アプリの場合

```bash
mkdir my-web-app  
cd my-web-app
cp -r context-storage/typescript/* .
npm install

# IDE で開くと、以下が自動で設定済み：
# - TypeScript 厳格設定
# - ESLint/Prettier ルール
# - フロントエンド向けのコード補完
# - パフォーマンス最適化のガイドライン
```

## 貢献方法

### 新しい技術スタックテンプレートの追加

1. `technology-name/` ディレクトリを作成（例：`go/`, `rust/`, `vue/`）
2. 以下のファイルを作成：
   ```
   technology-name/
   ├── .cursorrules          # Cursor 用ルール
   ├── CLAUDE.md             # Claude Code 用設定
   ├── .windsurf/            # Windsurf 用設定
   ├── .gitignore            # 技術固有の gitignore
   ├── 設定ファイル           # その技術の標準設定
   └── setup-commands.md     # セットアップ手順
   ```
3. 実際のプロジェクトで検証
4. プルリクエストを作成

### 既存テンプレートの改善

1. 該当する技術スタックディレクトリで改善を実施
2. AI IDE での動作確認
3. `setup-commands.md` の更新（必要に応じて）
4. プルリクエストで改善を提案

### テンプレート作成のガイドライン

各テンプレートには以下を含めてください：

- **`.cursorrules`**: 技術特化のコーディングルール、ベストプラクティス
- **`CLAUDE.md`**: プロジェクト構成説明、よく使うコマンド、注意点
- **`.windsurf/`**: ワークフロー、自動化ルール
- **設定ファイル**: その技術の標準的な設定（厳格めに設定）
- **`setup-commands.md`**: 初期セットアップの具体的手順

## 想定される利用シーン

### 🏢 チーム・組織での活用
- **新人オンボーディング**: 新メンバーが初日から最適化されたAI環境で開発開始
- **プロジェクト標準化**: チーム全体で一貫したAI設定とコーディング規約
- **技術移行**: 新しい技術スタックの学習時に最適な環境を即座に構築

### 🚀 個人開発での活用  
- **プロトタイピング**: アイデアを素早く形にするための最適化された環境
- **学習効率化**: 新しい技術の学習時にベストプラクティスが適用された状態から開始
- **副業・個人案件**: 案件ごとに技術スタックが変わる場合の迅速な環境構築

### 💡 教育・研修での活用
- **プログラミング教育**: 学習者が環境設定に時間を取られることなく学習に集中
- **技術研修**: 企業研修で統一された環境を素早く提供
- **ハッカソン**: 参加者が開発に集中できる環境を即座に提供

## 今後の展望

### 短期目標
- **主要技術スタックの網羅**: Go, Rust, Vue.js, Swift, Kotlin など
- **より詳細な設定**: フレームワーク別、用途別のサブテンプレート
- **セットアップ自動化**: シェルスクリプトによるワンコマンドセットアップ

### 中長期目標  
- **AIツール拡張**: GitHub Copilot、Tabnine などへの対応
- **クラウド統合**: GitHub Codespaces、GitPod への対応
- **設定同期ツール**: 複数プロジェクト間での設定同期機能
- **コミュニティ主導**: ユーザー投稿による設定テンプレートの拡充

## ライセンス

このプロジェクトのライセンスについては、各ファイルのヘッダーを参照してください。

---

🔗 **GitHub**: [https://github.com/gotalab/context-storage](https://github.com/gotalab/context-storage)