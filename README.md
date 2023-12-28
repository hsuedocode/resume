# resume.md

![Resume](resume.png)

Write your resume in
[Markdown](https://raw.githubusercontent.com/mikepqr/resume.md/main/resume.md),
style it with [CSS](resume.css), output to [PDF](resume.pdf) or [HTML](resume.html)


## Prerequisites

 - Python ≥ 3.6
 - Install dependencies in virtual env 
   - Add virtual env - `python3 -m venv venv`
   - Activate venv `source venv/bin/activate`
   - Install dependencies `pip3 install -r requirements.txt`
 - Optional, required for PDF output: Google Chrome or Chromium

## Usage
 1. Activate venv `source venv/bin/activate` 
 2. Run `python3 main.py {file_name}.md` to export markdown to pdf by default
     - Hardcoded to output to `resume_martin_hsueh.pdf`
     - Use `--html` to also output to `resume.html`
     - Use `--chrome-path=/path/to/chrome` if resume.py cannot find your Chrome
       or Chromium executable.

## Customization

Edit [resume.css](resume.css) to change the appearance of your resume. The
default style is extremely generic, which is perhaps what you want in a resume,
but CSS gives you a lot of flexibility. See, e.g. [The Tech Resume
Inside-Out](https://www.thetechinterview.com/) for good advice about what a
resume should look like (and what it should say).

Change the appearance of the PDF version (without affecting the HTML version) by
adding rules under the `@media print` CSS selector.

Change the margins and paper size of the PDF version by editing the [`@page` CSS
rule](https://developer.mozilla.org/en-US/docs/Web/CSS/%40page/size).

[python-markdown](https://python-markdown.github.io/) is by default a very basic
markdown compiler, but it has a number of optional extensions that you may want
to enable (by adding to [the list of extensions
here](https://github.com/mikepqr/resume.md/blob/f1b0699a9b66833cb67bb59111f45a09ed3c0f7e/resume.py#L112)).
<code><a
href="https://python-markdown.github.io/extensions/attr_list/">attr_list</a></code>
in particular may by useful if you are editing the CSS.
[abbreviations](https://python-markdown.github.io/extensions/abbreviations/)
extension is already enabled.
