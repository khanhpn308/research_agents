#!/usr/bin/env python3
"""
CLI Chat & Prompt tool using Antigravity Tools Proxy (127.0.0.1:8045)
Supports streaming, single-prompt mode, interactive conversation mode, and model selection.
"""

import sys
import argparse
from openai import OpenAI

DEFAULT_BASE_URL = "http://127.0.0.1:8045/v1"
DEFAULT_API_KEY = "sk-2da2bafe75404d8690664334e18fa9b3"
DEFAULT_MODEL = "gemini-3.8-flash-high"

def get_client(base_url=DEFAULT_BASE_URL, api_key=DEFAULT_API_KEY):
    return OpenAI(base_url=base_url, api_key=api_key)

def ask_single(client, model, prompt):
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            stream=True
        )
        for chunk in response:
            delta = chunk.choices[0].delta.content
            if delta:
                print(delta, end="", flush=True)
        print()
    except Exception as e:
        print(f"\n[Lỗi kết nối / Quota]: {e}", file=sys.stderr)

def interactive_chat(client, model):
    print(f"==================================================")
    print(f"🤖 Antigravity Chat CLI (Model: {model})")
    print(f"📌 Endpoint: {client.base_url}")
    print(f"💡 Nhập câu hỏi bình thường. Gõ 'exit' hoặc 'quit' để thoát.")
    print(f"==================================================\n")

    history = []
    while True:
        try:
            user_input = input("You: ").strip()
            if not user_input:
                continue
            if user_input.lower() in ("exit", "quit", "q"):
                print("Tạm biệt!")
                break

            history.append({"role": "user", "content": user_input})
            print("\nAI: ", end="", flush=True)

            response = client.chat.completions.create(
                model=model,
                messages=history,
                stream=True
            )

            assistant_reply = []
            for chunk in response:
                delta = chunk.choices[0].delta.content
                if delta:
                    print(delta, end="", flush=True)
                    assistant_reply.append(delta)
            print("\n" + "-"*50)

            full_reply = "".join(assistant_reply)
            history.append({"role": "assistant", "content": full_reply})

        except KeyboardInterrupt:
            print("\nĐã hủy lệnh.")
            break
        except Exception as e:
            print(f"\n[Lỗi]: {e}\n", file=sys.stderr)

def main():
    parser = argparse.ArgumentParser(description="Antigravity Tools AI Runner")
    parser.add_argument("prompt", nargs="*", help="Câu hỏi đơn lẻ (nếu không truyền sẽ mở chat tương tác)")
    parser.add_argument("--model", "-m", default=DEFAULT_MODEL, help=f"Tên model (mặc định: {DEFAULT_MODEL})")
    parser.add_argument("--list-models", action="store_true", help="Liệt kê danh sách model khả dụng")
    args = parser.parse_args()

    client = get_client()

    if args.list_models:
        try:
            models = client.models.list()
            print("Các model khả dụng:")
            for m in models.data:
                print(f" - {m.id}")
        except Exception as e:
            print(f"Không lấy được danh sách model: {e}", file=sys.stderr)
        return

    if args.prompt:
        prompt_text = " ".join(args.prompt)
        ask_single(client, args.model, prompt_text)
    else:
        interactive_chat(client, args.model)

if __name__ == "__main__":
    main()
