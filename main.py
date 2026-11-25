"""Have You Tried Turning It Off?

One line a hopeless tech support agent tells a desperate customer.
The punchline lands on the last words — that is where the judge reads
the laugh. Limit: 200 characters. Writes one line to /output/entry.txt.
"""
import os

LINE = (
    "Okay sir I've unplugged it, rebooted it, held it gently and even "
    "said sorry to it — at this point I'm starting to think the "
    "problem might be you."
)

LIMIT = 200


def build_line() -> str:
    text = LINE.strip()
    if len(text) > LIMIT:
        raise ValueError(f"line too long: {len(text)} chars (limit {LIMIT})")
    if len(text) < 1:
        raise ValueError("line is empty")
    return text


def main() -> int:
    line = build_line()
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(line)
    # readback assert — the file must round-trip byte for byte
    with open(path, "r", encoding="utf-8") as fh:
        readback = fh.read()
    assert readback == line, "readback mismatch"
    assert 1 <= len(readback) <= LIMIT, "length out of range"
    print(f"line ({len(readback)} chars): {readback}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
