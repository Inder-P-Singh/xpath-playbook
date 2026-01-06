# XPath Playbook — Troubleshooting & Quick Fixes

This note lists common XPath issues you will see when evaluating locators and the simplest fixes.

1. XPath returns nothing (empty array)
   - Cause: wrong context or timing; element not yet in DOM.
   - Fix:
     - In DevTools Console, try `$x("...")` to verify.
     - Ensure correct frame: if inside iframe, use the frame's DOM or switch frames in automation.
     - Add waits in automation (explicit wait for element presence).

2. Locator works in DevTools but fails in automation
   - Cause: timing / dynamic rendering / race condition.
   - Fix:
     - Use explicit waits (WebDriverWait until element located or visible).
     - Wait for network requests or JS initialization (use MutationObserver pattern if needed).

3. Attribute values change each load (dynamic ids/classes)
   - Cause: framework-generated tokens (e.g., React keys, server timestamps).
   - Fix:
     - Use `starts-with(@id,'prefix_')` or `contains(@class,'static-part')`.
     - Prefer semantic anchors: labels, aria-labels, data-* attributes if available.

4. Invisible whitespace or line breaks breaking text matches
   - Use `normalize-space()` around text content: `normalize-space()='Submit'`.

5. Multiple matches returned where you expect one
   - Cause: selector too generic.
   - Fix:
     - Add context: anchor with label or parent container.
     - Combine conditions: `and` / `or`.
     - Use positional index only when stable: `[...]` but prefer unique attributes.

6. Locator brittle due to DOM structure changes (absolute paths)
   - Always prefer relative XPath and attribute-based selection over absolute index paths.

7. Shadow DOM / Web Components
   - Standard XPath / querySelector cannot pierce shadow DOM.
   - Use framework-specific approaches or Chrome DevTools `pierce` selectors, or expose testing hooks.

8. XPath in XML vs HTML nuances
   - Functions like `text()` behavior may differ for HTML; prefer `normalize-space()` for visible text.

9. Performance issues
   - Very complex XPath (deep descendant and many predicates) can be slower.
   - Use simpler predicates and anchors; test in a real environment.

10. Debugging tips
   - Use Chrome DevTools Console: `$x("<xpath>")` to quickly evaluate.
   - Use `document.evaluate()` for programmatic evaluation.
   - Print outerHTML of nearby nodes to inspect structure: `console.log($x("//label[1]")[0].outerHTML)`

11. When all else fails: add stable data attributes
   - If you control app code or can negotiate test hooks, ask devs to add `data-test-id="login-username"` attributes — these are the least brittle solution.

Keep a short checklist to validate a candidate XPath:
- Does it avoid absolute indices? (Yes/No)
- Does it use stable attributes/anchors? (Yes/No)
- Is text matching using normalize-space()? (Yes/No)
- Does it avoid fragile framework-only props? (Yes/No)
