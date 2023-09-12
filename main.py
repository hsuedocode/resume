#!/usr/bin/env/python3
import argparse
import base64
import itertools
import logging
import os
import re
import subprocess
import sys

import markdown

preamble = """\
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{title}</title>
<style>
{css}
</style>
</head>
<body>
<div id="resume">
"""

postamble = """\
</div>
</body>
</html>
"""

CHROME_GUESSES_MACOS = (
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    "/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
)

# https://stackoverflow.com/a/40674915/409879
CHROME_GUESSES_WINDOWS = (
    # Windows 10
    os.path.expandvars(r"%ProgramFiles(x86)%\Google\Chrome\Application\chrome.exe"),
    os.path.expandvars(r"%ProgramFiles%\Google\Chrome\Application\chrome.exe"),
    os.path.expandvars(r"%LocalAppData%\Google\Chrome\Application\chrome.exe"),
    # Windows 7
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    # Vista
    r"C:\Users\UserName\AppDataLocal\Google\Chrome",
    # XP
    r"C:\Documents and Settings\UserName\Local Settings\Application Data\Google\Chrome",
)

# https://unix.stackexchange.com/a/439956/20079
CHROME_GUESSES_LINUX = [
    "/".join((path, executable))
    for path, executable in itertools.product(
        (
            "/usr/local/sbin",
            "/usr/local/bin",
            "/usr/sbin",
            "/usr/bin",
            "/sbin",
            "/bin",
            "/opt/google/chrome",
        ),
        ("google-chrome", "chrome", "chromium", "chromium-browser"),
    )
]


def guess_chrome_path() -> str:
    if sys.platform == "darwin":
        guesses = CHROME_GUESSES_MACOS
    elif sys.platform == "win32":
        guesses = CHROME_GUESSES_WINDOWS
    else:
        guesses = CHROME_GUESSES_LINUX
    for guess in guesses:
        if os.path.exists(guess):
            logging.info("Found Chrome or Chromium at " + guess)
            return guess
    raise ValueError("Could not find Chrome. Please set CHROME_PATH.")


def title(md: str) -> str:
    """
    Return the contents of the first markdown heading in md, which we
    assume to be the title of the document.
    """
    for line in md.splitlines():
        if re.match("^#[^#]", line):  # starts with exactly one '#'
            return line.lstrip("#").strip()
    raise ValueError(
        "Cannot find any lines that look like markdown h1 headings to use as the title"
    )


def make_html(md: str) -> str:
    """
    Compile md to HTML and prepend/append preamble/postamble.
    """
    try:
        with open("index.css") as cssfp:
            css = cssfp.read()
    except FileNotFoundError:
        print("index.css not found. Output will by unstyled.")
        css = ""
    return "".join(
        (
            preamble.format(title=title(md), css=css),
            markdown.markdown(md, extensions=["smarty", "abbr"]),
            postamble,
        )
    )


def write_pdf(html: str, output_name: str = "resume", chrome: str = "") -> None:
    """
    Write html to {output_name}.pdf
    """
    chrome = chrome or guess_chrome_path()
    html64 = base64.b64encode(html.encode("utf-8"))
    options = [
        "--no-sandbox",
        "--headless",
        "--print-to-pdf-no-header",
        "--enable-logging=stderr",
        "--log-level=2",
        "--in-process-gpu",
        "--disable-gpu",
    ]

    pdf_output = f"{output_name}.pdf"
    try:
        subprocess.run(
            [
                chrome,
                *options,
                f"--print-to-pdf={pdf_output}",
                "data:text/html;base64," + html64.decode("utf-8"),
            ],
            check=True,
        )
        logging.info(f"Wrote {pdf_output}")
    except subprocess.CalledProcessError as exc:
        if exc.returncode == -6:
            logging.warning(
                "Chrome died with <Signals.SIGABRT: 6> "
                f"but you may find {output_name}.pdf was created successfully."
            )
        else:
            raise exc

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "file",
        help="markdown input file [resume.md]",
    )
    parser.add_argument(
        "--html",
        help="Also write html output",
        action="store_true",
    )
    parser.add_argument(
        "--chrome-path",
        help="Path to Chrome or Chromium executable",
    )
    parser.add_argument("-q", "--quiet", action="store_true")
    parser.add_argument("--debug", action="store_true")
    args = parser.parse_args()

    if args.quiet:
        logging.basicConfig(level=logging.WARN, format="%(message)s")
    elif args.debug:
        logging.basicConfig(level=logging.DEBUG, format="%(message)s")
    else:
        logging.basicConfig(level=logging.INFO, format="%(message)s")

    FILE_NAME = {
        'backend.md': 'resume_MartinHsueh',
        'fullstack.md': 'resume_martin_hsueh'
    }
    dir = os.getcwd()
    output_name = os.path.join(dir,FILE_NAME.get(args.file, 'resume'))
    with open(args.file, encoding="utf-8") as mdfp:
        md = mdfp.read()
    html = make_html(md)

    if args.html:
        with open(output_name + ".html", "w", encoding="utf-8") as htmlfp:
            htmlfp.write(html)
            logging.info(f"Wrote {htmlfp.name}")

    write_pdf(html, output_name=output_name, chrome=args.chrome_path)
