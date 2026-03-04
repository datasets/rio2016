import csv
from pathlib import Path

import requests


SOURCES = {
    "athletes.csv": "https://raw.githubusercontent.com/flother/rio2016/master/athletes.csv",
    "events.csv": "https://raw.githubusercontent.com/flother/rio2016/master/events.csv",
}


def header(path: Path):
    with path.open(newline="", encoding="utf-8") as fh:
        reader = csv.reader(fh)
        return next(reader)


def download(url: str, target: Path):
    response = requests.get(url, timeout=60)
    response.raise_for_status()
    text = response.text
    if not text.strip():
        raise RuntimeError(f"Downloaded empty payload from {url}")
    target.write_text(text, encoding="utf-8")


def main():
    repo_root = Path(__file__).resolve().parents[1]
    for filename, url in SOURCES.items():
        output = repo_root / filename
        temp = repo_root / f".{filename}.tmp"
        download(url, temp)
        if output.exists() and header(output) != header(temp):
            raise RuntimeError(f"Header mismatch for {filename}; refusing overwrite")
        temp.replace(output)
        print(f"Updated {filename}")


if __name__ == "__main__":
    main()
