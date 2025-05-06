import requests
from bs4 import BeautifulSoup
import re
from pathlib import Path
from datetime import datetime

# === CONFIGURATION ===
ROOT_DIR = Path("content")  # or "." for full site
SECTION_HEADER = "Aktueller Zinssatz"

def fetch_ecb_rate():
    url = "https://www.ecb.europa.eu/stats/financial_markets_and_interest_rates/euro_short-term_rate/html/index.en.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    rate_str = soup.select_one(".table td strong").text.strip()  # "2.167"
    return rate_str.replace(".", ",")

def build_new_block(rate):
    today = datetime.today().strftime("%d.%m.%Y")
    return (
        f"## {SECTION_HEADER}\n\n"
        f"**Stand {today}:**\\\n"
        f"**➔ {rate} % p.a.**\n\n"
        f"*(Zins ändert sich täglich mit dem EZB-Leitzins.)*\n"
    )

def update_markdown(file_path: Path, header: str, new_block: str):
    original = file_path.read_text(encoding="utf-8")
    pattern = rf"(## {re.escape(header)}\n\n)(.*?)(?=\n## |\Z)"  # header followed by content
    updated = re.sub(pattern, new_block, original, flags=re.DOTALL)

    if original != updated:
        file_path.write_text(updated, encoding="utf-8")
        print(f"✅ Updated: {file_path}")

def find_md_files_with_header(root_dir: Path, header: str):
    return [f for f in root_dir.rglob("*.md") if f.read_text(encoding="utf-8").find(f"## {header}") != -1]

def main():
    print("⏳ Fetching ECB rate...")
    rate = fetch_ecb_rate()
    block = build_new_block(rate)

    print("🔍 Searching for markdown files...")
    files = find_md_files_with_header(ROOT_DIR, SECTION_HEADER)
    for f in files:
        update_markdown(f, SECTION_HEADER, block)

    if not files:
        print("⚠️ No files with the header found.")

if __name__ == "__main__":
    main()

