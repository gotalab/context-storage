# TODOリストCLIアプリケーション

## 概要

このプロジェクトには、コマンドラインインターフェースから使用できるシンプルなTODOリスト管理アプリケーションが含まれています。Pythonで実装されており、JSON形式でのデータ永続化を提供します。

## ファイル構成

- `src/todo.py`: メインのアプリケーションファイル（134行）
- `src/README.md`: 基本的な使用方法のドキュメント（53行）

## 主要機能

### 1. TODOの管理操作
- **追加**: 新しいTODOアイテムの作成
- **表示**: TODOリストの表示（未完了のみまたは全て）
- **完了**: TODOアイテムを完了としてマーク
- **削除**: TODOアイテムの削除
- **更新**: 既存のTODOアイテムの編集

### 2. データ構造
各TODOアイテムには以下の情報が含まれます：
- `id`: 一意識別子
- `title`: タイトル
- `description`: 詳細説明（オプション）
- `completed`: 完了状態（真偽値）
- `created_at`: 作成日時
- `completed_at`: 完了日時（完了時のみ）

### 3. データ永続化
- JSONファイル（`todo.json`）による永続化
- UTF-8エンコーディングによる日本語サポート
- 自動的なファイル作成と更新

## 使用方法

### 前提条件
- Python 3.x
- uvパッケージマネージャー（推奨）

### コマンド一覧

#### TODOの追加
```bash
uv run src/todo.py add "タスクのタイトル" -d "詳細説明"
```

例:
```bash
uv run src/todo.py add "買い物に行く" -d "牛乳とパンを買う"
```

#### TODOリストの表示
未完了のTODOのみ表示：
```bash
uv run src/todo.py list
```

全てのTODO（完了済みを含む）を表示：
```bash
uv run src/todo.py list -a
```

#### TODOの完了
```bash
uv run src/todo.py complete [ID]
```

例:
```bash
uv run src/todo.py complete 1
```

#### TODOの削除
```bash
uv run src/todo.py delete [ID]
```

例:
```bash
uv run src/todo.py delete 1
```

#### TODOの更新
```bash
uv run src/todo.py update [ID] -t "新しいタイトル" -d "新しい説明"
```

例:
```bash
uv run src/todo.py update 1 -t "修正されたタスク" -d "更新された説明"
```

#### ヘルプの表示
```bash
uv run src/todo.py --help
```

## 技術的詳細

### アーキテクチャ
- **TodoListクラス**: メインのロジックを担当
- **argparse**: コマンドライン引数の解析
- **JSON**: データのシリアライゼーション

### エラーハンドリング
- JSONファイルの破損検出
- 存在しないTODO IDの処理
- 適切なエラーメッセージの表示

### 日本語対応
- UTF-8エンコーディングによる完全な日本語サポート
- 日本語でのユーザーメッセージ
- 日本語でのヘルプテキスト

## ファイルの場所
- メインアプリケーション: [`src/todo.py`](../src/todo.py)
- 使用方法ドキュメント: [`src/README.md`](../src/README.md)

## 今後の拡張可能性
- カテゴリ機能の追加
- 優先度レベルの実装
- 期限設定機能
- 検索・フィルタリング機能
- エクスポート機能（CSV、XML等）

---

このドキュメントは、プルリクエスト #13 で追加されたTODOリストCLIアプリケーションについて説明しています。