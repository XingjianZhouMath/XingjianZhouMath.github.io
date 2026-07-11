# Xingjian Zhou — Academic Website

A Quarto academic website for geometric analysis, configured to publish from `docs/` on GitHub Pages.

## Preview and build

```powershell
quarto preview
quarto render
```

## Add a note

1. Copy `notes/_note-template.qmd` to a descriptive filename such as `notes/mean-curvature-flow.qmd`.
2. Edit its title, description, date, categories, and content.
3. Remove `draft: true` when ready.
4. Add a matching entry under `website.navbar.left` → `Notes` → `menu` in `_quarto.yml` only if you want the note directly in the top dropdown. The Notes index itself updates automatically.

Markdown files (`.md`) are also discovered automatically. Put standalone LaTeX sources in `notes/tex/` and link to them from a web note.

## Publish

After rendering, configure GitHub Pages to deploy from the `main` branch and `/docs` folder.

