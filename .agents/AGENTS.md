# Workspace Guidelines

## Documentation Style & Formatting Rules

- **GitHub Compatibility**: All Markdown documentation (`README.md`, `notes.md`) must be written using simple, GitHub-friendly Markdown.
- **Math Formatting**: Prefer plain Markdown and inline code (e.g. `current_sum - k`, `prefix[R + 1] - prefix[L] = k`) over LaTeX. Use LaTeX only when genuinely necessary and only in syntax known to render correctly on GitHub (e.g. `$O(n)$`, `$O(1)$`).
- **No Unnecessary LaTeX**: Avoid using `\text{...}`, `\mathrm{...}`, `\begin{...}`, `\end{...}`, or complex LaTeX environments for variable names. Use inline code for algorithm variables (e.g. `current_sum`, `prefix_sum`, `balance`, `freq`, `first_index`).
