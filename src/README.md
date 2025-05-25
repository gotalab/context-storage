# シンプルTODOリストアプリケーション

このアプリケーションは、コマンドラインから使用できるシンプルなTODOリスト管理ツールです。

## 機能

- TODOの追加
- TODOリストの表示（未完了のみまたはすべて）
- TODOの完了としてマーク
- TODOの削除
- TODOの更新（タイトルと説明）

## 使い方

### TODOの追加

```bash
uv run todo.py add "買い物に行く" -d "牛乳とパンを買う"
```

### TODOリストの表示

未完了のTODOのみを表示：
```bash
uv run todo.py list
```

すべてのTODO（完了済みを含む）を表示：
```bash
uv run todo.py list -a
```

### TODOを完了としてマーク

```bash
uv run todo.py complete 1  # IDが1のTODOを完了としてマーク
```

### TODOの削除

```bash
uv run todo.py delete 1  # IDが1のTODOを削除
```

### TODOの更新

```bash
uv run todo.py update 1 -t "新しいタイトル" -d "新しい説明"
```

## データ保存

TODOデータは `todo.json` ファイルに保存されます。このファイルは自動的に作成・更新されます。
