# Xingjian Zhou — Academic Website

A Quarto academic website for geometric analysis, configured to publish from `docs/` on GitHub Pages.

## Preview and build

```powershell
quarto preview
quarto render
```

## Add a note

The Notes page links directly to GitHub's upload screen for the repository's `notes/` directory.

1. Download `files/note-template.md` from the Notes page.
2. Edit the title, description, date, categories, and content.
3. Rename it with lowercase letters, numbers, and hyphens, for example `mean-curvature-flow.md`.
4. Upload it through the Notes page and confirm the commit on GitHub.

The `Render and publish notes` workflow validates the note, renders the website, and commits the updated `docs/` output. New notes appear automatically on the Notes index after a few minutes. Add an entry to the Notes menu in `_quarto.yml` only when a note should be featured in the top navigation.

Markdown files (`.md`) are also discovered automatically. Put standalone LaTeX sources in `notes/tex/` and link to them from a web note.

## Publish

After rendering, configure GitHub Pages to deploy from the `main` branch and `/docs` folder.

For automatic note publishing, open **Settings → Actions → General → Workflow permissions** and enable **Read and write permissions**. Do not grant repository write access to other accounts if only the owner should be able to publish notes.
