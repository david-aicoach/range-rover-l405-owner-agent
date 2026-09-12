#!/usr/bin/env bash
# This repo packages exactly one Skill at its root (range-rover-l405-owner-agent/,
# named after the repo — see BOOTSTRAP.md). Expose it through each agent's own
# native Skill path so Claude/Codex/agy working in this repo discover it too:
#   .claude/skills/<name>  Claude Code (symlink)
#   .codex/skills/<name>   Codex (symlink) — confirmed live via a `codex exec`
#                          discovery test that Codex reads a project-local
#                          .codex/skills/ in addition to $CODEX_HOME/skills.
#   .agents/skills.json    Antigravity (agy) — its documented per-repo manifest
#                          convention, scanning repo root for any SKILL.md dir.
#                          A live agy 1.2.1 test did not pick this up (only its
#                          global ~/.gemini/config/skills/ showed); written
#                          anyway as forward-compatible best-effort — verify
#                          live with `agy --print` before relying on it.
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"

mkdir -p .claude/skills .codex/skills .agents

for skill_dir in */; do
  [ -f "${skill_dir}SKILL.md" ] || continue
  name=$(basename "$skill_dir")
  target="../../${name}"
  for dst in .claude/skills .codex/skills; do
    link="${dst}/${name}"
    [ -L "$link" ] && rm "$link"
    ln -s "$target" "$link"
  done
done

for dst in .claude/skills .codex/skills; do
  for link in "$dst"/*; do
    [ -L "$link" ] || continue
    name=$(basename "$link")
    [ -f "${name}/SKILL.md" ] || rm "$link"
  done
done

cat > .agents/skills.json <<'EOF'
{
  "entries": [
    { "path": "." }
  ]
}
EOF

echo "skills exposed: claude=$(ls .claude/skills/ 2>/dev/null | tr '\n' ' ')| codex=$(ls .codex/skills/ 2>/dev/null | tr '\n' ' ')| agy=manifest"
