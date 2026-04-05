import re

def process_line(text):
    """1行のテキストを変換するメインロジック"""
    def replace_with_hint(match):
        content = match.group(1)
        
        def hide_word(word_match):
            word = word_match.group(0)
            if len(word) > 1:
                # 1文字目 + 残りの数だけアンダーバー
                return word[0] + "　_" * (len(word) - 1)
            return word

        return re.sub(r'[a-zA-Z\']+', hide_word, content)

    # カッコの中身を置換
    return re.sub(r'\((.*?)\)', replace_with_hint, text)

def main():
    input_file = "input.txt"   # 読み込むファイル名
    output_file = "output.txt" # 書き出すファイル名

    try:
        with open(input_file, "r", encoding="utf-8") as f_in, \
             open(output_file, "w", encoding="utf-8") as f_out:
            
            for line in f_in:
                # 1行ずつ読み込んで変換
                converted_line = process_line(line.strip())
                # 結果をファイルに書き出し（改行付き）
                f_out.write(converted_line + "\n")
        
        print(f"完了！ {output_file} を確認してください。")

    except FileNotFoundError:
        print(f"エラー: {input_file} が見つかりません。")

if __name__ == "__main__":
    main()