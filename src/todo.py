#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
from datetime import datetime
import argparse

class TodoList:
    def __init__(self, file_path="todo.json"):
        self.file_path = file_path
        self.todos = []
        self.load_todos()

    def load_todos(self):
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, 'r', encoding='utf-8') as f:
                    self.todos = json.load(f)
            except json.JSONDecodeError:
                print("警告: TODOファイルが破損しています。新しいTODOリストを作成します。")
                self.todos = []

    def save_todos(self):
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(self.todos, f, ensure_ascii=False, indent=2)

    def add_todo(self, title, description=""):
        todo = {
            "id": len(self.todos) + 1,
            "title": title,
            "description": description,
            "completed": False,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "completed_at": None
        }
        self.todos.append(todo)
        self.save_todos()
        print(f"追加しました: {title}")

    def list_todos(self, show_completed=False):
        if not self.todos:
            print("TODOリストは空です。")
            return

        print("\nTODOリスト:")
        print("-" * 50)
        for todo in self.todos:
            if show_completed or not todo["completed"]:
                status = "[完了]" if todo["completed"] else "[未完了]"
                print(f"{todo['id']}. {status} {todo['title']}")
                if todo["description"]:
                    print(f"   説明: {todo['description']}")
                print(f"   作成日時: {todo['created_at']}")
                if todo["completed_at"]:
                    print(f"   完了日時: {todo['completed_at']}")
                print("-" * 50)

    def complete_todo(self, todo_id):
        for todo in self.todos:
            if todo["id"] == todo_id and not todo["completed"]:
                todo["completed"] = True
                todo["completed_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.save_todos()
                print(f"完了としてマークしました: {todo['title']}")
                return
        print(f"ID {todo_id} のTODOが見つからないか、すでに完了しています。")

    def delete_todo(self, todo_id):
        for i, todo in enumerate(self.todos):
            if todo["id"] == todo_id:
                deleted = self.todos.pop(i)
                self.save_todos()
                print(f"削除しました: {deleted['title']}")
                return
        print(f"ID {todo_id} のTODOが見つかりません。")

    def update_todo(self, todo_id, title=None, description=None):
        for todo in self.todos:
            if todo["id"] == todo_id:
                if title:
                    todo["title"] = title
                if description is not None:
                    todo["description"] = description
                self.save_todos()
                print(f"更新しました: ID {todo_id}")
                return
        print(f"ID {todo_id} のTODOが見つかりません。")

def main():
    parser = argparse.ArgumentParser(description="シンプルなTODOリストアプリケーション")
    subparsers = parser.add_subparsers(dest="command", help="コマンド")

    # add コマンド
    add_parser = subparsers.add_parser("add", help="新しいTODOを追加")
    add_parser.add_argument("title", help="TODOのタイトル")
    add_parser.add_argument("-d", "--description", help="TODOの詳細説明", default="")

    # list コマンド
    list_parser = subparsers.add_parser("list", help="TODOリストを表示")
    list_parser.add_argument("-a", "--all", action="store_true", help="完了したTODOも表示")

    # complete コマンド
    complete_parser = subparsers.add_parser("complete", help="TODOを完了としてマーク")
    complete_parser.add_argument("id", type=int, help="完了としてマークするTODOのID")

    # delete コマンド
    delete_parser = subparsers.add_parser("delete", help="TODOを削除")
    delete_parser.add_argument("id", type=int, help="削除するTODOのID")

    # update コマンド
    update_parser = subparsers.add_parser("update", help="TODOを更新")
    update_parser.add_argument("id", type=int, help="更新するTODOのID")
    update_parser.add_argument("-t", "--title", help="新しいタイトル")
    update_parser.add_argument("-d", "--description", help="新しい説明")

    args = parser.parse_args()
    todo_list = TodoList()

    if args.command == "add":
        todo_list.add_todo(args.title, args.description)
    elif args.command == "list":
        todo_list.list_todos(args.all)
    elif args.command == "complete":
        todo_list.complete_todo(args.id)
    elif args.command == "delete":
        todo_list.delete_todo(args.id)
    elif args.command == "update":
        todo_list.update_todo(args.id, args.title, args.description)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
