# XPath Playbook — Examples & Demo

This repository contains small runnable examples and a short Selenium script demonstrating robust XPath techniques discussed in the blog post:
- Blog: https://inderpsingh.blogspot.com/2026/01/xpath-techniques.html
- Video: https://youtu.be/ags-f80bne0

## Quick steps

1. Open the sample HTML in Chrome:
   - Open `examples/sample.html` in Chrome (drag-and-drop into the browser).
   - Open DevTools Console (F12) and evaluate example XPaths using:
     ```
     $x("//label[normalize-space()='Username']/following-sibling::input[1]")
     ```

2. Try the brittle example (to show failure):
```
$x("//html/body/div[2]/div[1]/form/input[2]")
```

Observe how small DOM changes will break absolute paths.

3. Run the Selenium example (requires Python, Chrome and ChromeDriver)
- Install requirements:
  ```
  pip install selenium webdriver-manager
  ```
- Run:
  ```
  python code/selenium_example.py
  ```
- Output: the script will print which XPaths matched and sample values.

## Files included

- `examples/sample.html` — small demo page to try XPaths interactively
- `examples/xpath_examples.txt` — XPaths and expected results
- `code/selenium_example.py` — runnable script demonstrating robust XPaths
- `notes/troubleshooting.md` — common problems and fixes

## Demo script (60 seconds) — suggested video intro
1. Evaluate brittle absolute path (`$x("//html/body/...")`) — show break.
2. Evaluate anchor + axis (`$x("//label[normalize-space()='Username']/following-sibling::input[1]")`) — show success.
3. Evaluate partial match (`$x("//input[starts-with(@id,'user_')]")`) — show success.
4. End with: "Full Playbook & runnable examples — link in the description."

## License & attribution
Use these examples freely in talks, training, blog posts. If you republish, please attribute back to the blog post and the video.

---

