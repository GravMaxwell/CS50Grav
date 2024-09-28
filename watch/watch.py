import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    # regular expression to match src attribute of an iframe with YT url.
    pattern = r'src="https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)"'
    match = re.search(pattern, s)
    if match:
        video_id = match.group(1)
        return f"https://youtu.be/{video_id}"
    return None

if __name__ == "__main__":
    main()
