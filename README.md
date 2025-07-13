# Context Storage

AI対応IDEの**コンテキストエンジニアリング初期作業を完全にスキップ**し、新規プロジェクトで即座に最適化されたAI開発環境を実現するリポジトリです。

## 概要

新規プロジェクトを開始する度に、AI アシスタントに適切なコンテキストを与えるための**コンテキストエンジニアリング**作業が必要になります。Claude Code、Cursor、Windsurf などの AI 対応 IDE で効果的な開発を行うには、プロジェクトの性質、コーディング規約、ベストプラクティスなどの文脈を正確に伝える必要がありますが、この初期設定は非常に時間がかかる作業です。

このリポジトリは、**IDE別に最適化された汎用的なコンテキスト設定**を提供し、**ファイルをコピーするだけで、コンテキストエンジニアリングの初期段階を完全にスキップ**できることを目的としています。

## ディレクトリ構成

```
context-storage/
├── Claude-Code/              # Claude Code 用コンテキスト設定
│   ├── CLAUDE.md            # メインコンテキストファイル
│   ├── commands.md          # よく使うコマンド集
│   ├── hooks/               # Claude Code 用フック設定
│   ├── settings.json        # Claude Code 設定ファイル
│   └── templates/           # 汎用的なファイルテンプレート
│       ├── python-context.md
│       ├── typescript-context.md
│       └── web-context.md
│
├── Windsurf/                # Windsurf 用コンテキスト設定
│   ├── rules/               # 汎用コーディングルール
│   │   ├── general.md       # 一般的なコーディング原則
│   │   ├── best-practices.md # ベストプラクティス
│   │   └── code-quality.md  # コード品質ガイドライン
│   ├── workflows/           # 汎用ワークフロー
│   │   ├── development.md   # 開発フロー
│   │   ├── testing.md       # テスト戦略
│   │   └── deployment.md    # デプロイメント
│   └── contexts/            # プロジェクトタイプ別コンテキスト
│       ├── web-app.md
│       ├── api-server.md
│       └── data-analysis.md
│
├── Cursor/                  # Cursor 用コンテキスト設定
│   ├── .cursorrules         # メインルールファイル
│   ├── project-templates/   # プロジェクトタイプ別ルール
│   │   ├── .cursorrules-python
│   │   ├── .cursorrules-typescript
│   │   └── .cursorrules-react
│   ├── extensions.json      # 推奨拡張機能設定
│   └── snippets/            # コードスニペット集
│
└── shared/                  # IDE共通設定
    ├── gitignore-templates/ # 技術別gitignoreテンプレート
    ├── github-actions/      # 汎用GitHub Actions
    ├── docker-templates/    # Dockerファイルテンプレート
    └── docs/                # 設定方法・使い方ドキュメント

```

### 現在の構成（移行中）

現在は主にWindsurf用の設定が配置されており、Claude Code、Cursor用の構成に順次展開予定：

```
.windsurf/rules/     # → Windsurf/ に移行済み
.windsurf/workflows/ # → Windsurf/ に移行済み
.github/workflows/   # → shared/github-actions/ に移行予定
```

## 解決する問題

### 😫 コンテキストエンジニアリングの初期作業が面倒
- **新規プロジェクトの度に発生**: AI アシスタントに適切なコンテキストを与えるための設定作業
- **時間がかかる**: `.cursorrules`、`CLAUDE.md`、ワークフロー設定を一から考える必要
- **ベストプラクティスがわからない**: 効果的なコンテキスト設計の知識不足
- **設定忘れ**: プロジェクト途中でAI支援が不十分になる問題
- **チーム不統一**: メンバー間でAIアシスタントの設定品質にばらつき

### ✨ このリポジトリで実現すること
- **初期作業を完全スキップ**: コンテキストエンジニアリングの初期段階を0秒で完了
- **即座に高品質なAI支援**: コピー直後から最適化されたAIアシスタントが利用可能
- **IDE別最適化**: Claude Code、Cursor、Windsurf それぞれに特化した設定
- **ベストプラクティス適用済み**: 実績のあるコンテキスト設計パターンを標準装備
- **チーム統一**: 組織全体で一貫したAI開発体験を実現

## 主な特徴

### 1. IDE別コンテキスト最適化

各AIツールの特性に合わせた専用コンテキスト設定：

```bash
# Claude Code の場合
cp context-storage/Claude-Code/CLAUDE.md /your-project/
cp context-storage/Claude-Code/commands.md /your-project/

# Cursor の場合  
cp context-storage/Cursor/.cursorrules /your-project/

# Windsurf の場合
cp -r context-storage/Windsurf/ /your-project/.windsurf/
```

### 2. コンテキストエンジニアリング不要

事前に最適化された汎用コンテキストを提供：

- **汎用性と専門性のバランス**: どのプロジェクトでも適用可能な設定
- **実績ベース**: 実際の開発で効果が実証されたパターン
- **継続的改善**: コミュニティフィードバックによる品質向上
- **学習効果**: 設定内容を通じてベストプラクティスを学習可能

### 3. 即座に実運用レベル

コピー直後から以下が利用可能：

- **Claude Code**: 適切なコンテキスト理解、効果的なコマンド補完
- **Cursor**: 最適化されたコード生成、リファクタリング支援
- **Windsurf**: 体系化されたワークフロー、品質管理ルール
- **共通設定**: Git hooks、GitHub Actions、Docker設定など

## 使用方法

### 🚀 Step 1: プロジェクト準備とIDE選択

```bash
# 1. 新しいプロジェクトディレクトリを作成
mkdir my-awesome-project
cd my-awesome-project

# 2. 使用するAI IDEに応じてコンテキストをコピー
```

### ⚡ Step 2: IDE別コンテキスト設定

#### Claude Code を使用する場合
```bash
cp /path/to/context-storage/Claude-Code/CLAUDE.md .
cp /path/to/context-storage/Claude-Code/commands.md .
cp /path/to/context-storage/Claude-Code/settings.json .

# 必要に応じてプロジェクトタイプ別テンプレートも追加
cp /path/to/context-storage/Claude-Code/templates/python-context.md ./CONTEXT.md
```

#### Cursor を使用する場合
```bash
cp /path/to/context-storage/Cursor/.cursorrules .

# プロジェクトタイプに応じてより具体的なルールも選択可能
cp /path/to/context-storage/Cursor/project-templates/.cursorrules-python ./.cursorrules
```

#### Windsurf を使用する場合
```bash
cp -r /path/to/context-storage/Windsurf/ ./.windsurf/

# プロジェクトタイプ別コンテキストを選択
cp /path/to/context-storage/Windsurf/contexts/web-app.md ./.windsurf/project-context.md
```

### 🎯 Step 3: 即座にAI開発開始

```bash
# IDE を起動（コンテキストエンジニアリングは既に完了済み！）
cursor .        # Cursor の場合
code .          # Claude Code の場合  
# Windsurf でプロジェクトを開く
```

**これだけで完了！** AIアシスタントが最適化されたコンテキストで即座に高品質な支援を開始します。

## 具体的な効果例

### 🎯 コンテキストエンジニアリング効果の比較

#### 従来の方法（時間がかかる）
```bash
mkdir new-project && cd new-project

# 毎回これらの作業が必要：
# 1. .cursorrules を一から作成（30分）
# 2. CLAUDE.md でプロジェクト説明作成（20分）
# 3. Windsurf ワークフロー設定（15分）
# 4. 各IDE設定の調整・最適化（30分）
# 合計: 約95分の初期設定時間
```

#### Context Storage使用時（即座に完了）
```bash
mkdir new-project && cd new-project

# IDE別に選択してコピーするだけ：
cp context-storage/Claude-Code/CLAUDE.md .          # 5秒
cp context-storage/Cursor/.cursorrules .            # 5秒  
cp -r context-storage/Windsurf/ ./.windsurf/        # 10秒

# 合計: 20秒で最適化されたAI環境が完成
# → 95分の時間短縮！
```

### 🚀 実際の開発体験の違い

#### Context Storage 適用前
- AIが毎回プロジェクトの文脈を理解するのに時間がかかる
- コーディング規約やベストプラクティスを都度説明する必要
- IDE間でAI支援の品質にばらつきがある

#### Context Storage 適用後  
- プロジェクト開始時点でAIが適切な文脈を理解済み
- 一貫したコーディング規約とベストプラクティスが自動適用
- どのIDEでも同等の高品質なAI支援を即座に利用可能

## 貢献方法

### IDE別コンテキスト改善

#### Claude Code コンテキストの改善
1. `Claude-Code/` ディレクトリで設定を改善
2. 以下の観点で最適化：
   - CLAUDE.md の文脈説明の明確性
   - commands.md のコマンド網羅性
   - hooks/ の実用性
3. 実際のプロジェクトで効果を検証
4. プルリクエストで改善提案

#### Cursor ルールの改善  
1. `Cursor/` ディレクトリで.cursorrulesを改善
2. 以下を重視：
   - より効果的なコード生成のためのルール
   - プロジェクトタイプ別テンプレートの拡充
   - 推奨拡張機能の最適化
3. 複数のプロジェクトタイプで検証
4. プルリクエストで改善提案

#### Windsurf ワークフロー改善
1. `Windsurf/` ディレクトリで設定を改善  
2. 以下の領域で改善：
   - rules/ の汎用性と実用性
   - workflows/ の効率性
   - contexts/ のプロジェクトタイプ網羅
3. 実開発での効果測定
4. プルリクエストで改善提案

### 新しいAIツール対応

新しいAI対応IDEやコーディングエージェントへの対応：

1. `New-Tool/` ディレクトリを作成
2. そのツールの特性に合わせたコンテキスト設計
3. 既存IDE設定との整合性確認  
4. ドキュメント作成とテスト
5. プルリクエストで提案

### コンテキスト設計のガイドライン

効果的なコンテキスト設計の原則：

- **汎用性**: 特定プロジェクトに依存しない設定
- **即効性**: コピー直後から効果を発揮する設定
- **学習効果**: 設定内容からベストプラクティスを学べる構成
- **継続性**: プロジェクトの成長に合わせて拡張可能な設計

## 想定される利用シーン

### 🏢 チーム・組織でのコンテキストエンジニアリング効率化
- **新人オンボーディング**: 初日からベテランと同等のAI開発環境を提供
- **プロジェクト間移動**: チームメンバーが異なるプロジェクトに参加する際の即座の環境構築
- **AI活用標準化**: 組織全体でAIアシスタントの効果を最大化する統一基準
- **知識の蓄積**: 効果的なコンテキスト設計ノウハウの組織内共有

### 🚀 個人開発でのコンテキスト作業削減
- **アイデア検証**: プロトタイプ作成時のセットアップ時間を最小化
- **マルチプロジェクト**: 複数の個人プロジェクト間でのコンテキスト切り替え
- **学習加速**: 新技術習得時にコンテキスト作成ではなく学習に集中
- **フリーランス効率化**: クライアントワーク開始時の迅速な環境構築

### 💡 教育・研修でのAI活用最大化
- **プログラミング教育**: 学習者がコンテキスト設計を学ぶ前からAI支援を活用
- **企業研修**: 統一されたAI環境での技術研修実施
- **ハッカソン**: 参加者が開発のコアに集中できる環境即座提供
- **コンテキストエンジニアリング教育**: 効果的な設定例を通じた学習機会

## 今後の展望

### 短期目標（コンテキスト品質向上）
- **IDE別最適化の深化**: Claude Code、Cursor、Windsurf それぞれの特性を活かした設定
- **プロジェクトタイプ別テンプレート**: Web、API、CLI、データ分析など用途別コンテキスト
- **効果測定機能**: AI支援効果を定量的に評価できる仕組み

### 中長期目標（エコシステム拡張）
- **新AIツール対応**: GitHub Copilot、Tabnine、その他新興AIツールへの拡張
- **自動コンテキスト生成**: プロジェクト分析による最適コンテキストの自動作成
- **コミュニティ知見集約**: ユーザー投稿による効果的なコンテキストパターンの共有
- **IDE間連携**: 複数IDE使用時の一貫したコンテキスト管理

## ライセンス

このプロジェクトのライセンスについては、各ファイルのヘッダーを参照してください。

---

🔗 **GitHub**: [https://github.com/gotalab/context-storage](https://github.com/gotalab/context-storage)