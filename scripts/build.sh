#!/usr/bin/env bash
# Render the slides and refresh the published copy in docs/ (served by GitHub Pages).
#
#   bash scripts/build.sh
#
# Needs Quarto 1.10 or newer on the PATH (https://quarto.org/docs/get-started/).
# No Python or R is required: the deck has no executable code cells.
set -euo pipefail
cd "$(dirname "$0")/.."

quarto render index.qmd            # writes index.html + index_files/ (both git-ignored)

rm -rf docs
mkdir -p docs/figures
cp index.html docs/
cp -R index_files docs/
cp -R assets docs/
# Only the figures the slides show travel with the published copy: image lines
# of the form ![](figures/name.png){...}. Paths quoted inside speaker notes are
# deliberately not matched.
grep -oE '^!\[[^]]*\]\(figures/[^)]+\)' index.qmd | sed -E 's/.*\((figures\/[^)]+)\).*/\1/' | sort -u | while read -r f; do
  cp "$f" "docs/$f"
done
touch docs/.nojekyll               # GitHub Pages: serve the files as they are
if [ -f output/workshop-2026-09-11.pdf ]; then
  cp output/workshop-2026-09-11.pdf docs/
fi

echo "rendered: docs/index.html ($(grep -c '<section id=' docs/index.html) slides)"
