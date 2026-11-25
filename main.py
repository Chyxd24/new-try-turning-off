"""Have You Tried Turning It Off?

One line a hopeless tech support agent tells a desperate customer who
swears the gadget is broken. The laugh lands on the last words - the
judge reads the end. Limit: 200 chars. Writes one line to /output/entry.txt.
"""
import os

ENTRY_PATH = "/output/entry.txt"
LIMIT = 200

LINE = (
    "Sir, I've unplugged it, rebooted it, hugged it, apologised to it, "
    "read it your emails and shown it family photos - at this point I'm "
    "100% sure the device is fine and the problem is you."
)


def build_line():
    """Return the single joke line, validated against the character budget."""
    text = LINE.strip()
    if not text:
        raise ValueError("line is empty")
    if len(text) > LIMIT:
        raise ValueError(f"line too long: {len(text)} > {LIMIT}")
    return text


def write_entry(line, path=ENTRY_PATH):
    """Write one line to `path`, then read it back byte for byte."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(line)
    with open(path, "r", encoding="utf-8") as fh:
        readback = fh.read()
    if readback != line:
        raise AssertionError("readback mismatch")
    if not 1 <= len(readback) <= LIMIT:
        raise AssertionError("length out of range")
    return readback


def main():
    line = build_line()
    saved = write_entry(line)
    print(f"line ({len(saved)} chars): {saved}")
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
