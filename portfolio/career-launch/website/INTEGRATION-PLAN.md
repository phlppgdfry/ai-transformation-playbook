# Minimal integration plan

## Identified source and owned scope

Existing repository: `phlppgdfry/pgosprive`, base `704815a`. Actual source files: `src/data/projects.json`, `src/data/projects.ts`, `src/pages/ProjectDetail.tsx`, `src/components/portfolio/ProjectLinks.tsx`; existing build generates `public/sitemap.xml`. No new framework/component is needed.

Owned proposal on local branch `portfolio/career-launch-catalogue-isolated-2026-11-05`, isolated worktree `/private/tmp/enterprise-ai-career-website`:

1. Add only the `enterprise-ai-accounting-case` data object from [project-entry.json](project-entry.json).
2. Copy the authentic accounting PNG to `public/work/enterprise-ai-accounting.png`; preserve its hash/caption provenance.
3. Include the new route in the existing sitemap, preserving unrelated entries.
4. Reuse `/work/:slug` rendering, EN/NL text, image semantics and Code link. `links` stays empty so the app does not count a Markdown case as a live interactive demo.
5. Keep existing six-item audience feature selections unchanged. The case is available through the all-project catalogue/search and its direct route.

Preview route: `http://127.0.0.1:4178/work/enterprise-ai-accounting-case`. Proposed public route after owner approval: `https://www.philippegodfroy.com/work/enterprise-ai-accounting-case` (not claimed deployed).

## Concurrent work

The original checkout on `portfolio/enterprise-ai-career-launch-2026-11-05` acquired unrelated edits in `SiteNav.tsx`, `Home.tsx`, a different enterprise-AI section and Noordwerk assets during this task. They were not authored, reverted or committed by this task. The original checkout also holds the initial uncommitted copy of this catalogue proposal/build sitemap; it is left intact to avoid damaging concurrent work. Integrate the isolated commit selectively after comparing it with those edits. Do not blindly merge two overlapping presentation branches.

## Review and publish later

Run existing tests and production build, inspect the new route in both languages at desktop/mobile widths, and check the Code link points to the public playbook. Review role/AI-assistance wording. The build's pre-existing sitemap generator stamps every entry with the build date; this proposal preserves prior entry dates and adds only the new route in the committed sitemap. No generator redesign is included.

Only after explicit approval should you push/merge the website and career-launch branches and run the normal deployment process. No DNS, domain, contact form, global metadata, paid service or deployment setting is changed here.
