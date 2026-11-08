# Career Launch — final production delivery, 8 November 2026

## Release decision: SUCCESS / GO within the documented showcase scope

The Career Launch materials are merged into the public playbook. The existing private website is integrated, deployed to its existing Vercel project and verified on the actual public domain. No repository visibility, historical milestone tag, DNS or database schema was changed. No cloud AI capability, professional client engagement or personal technical mastery is inferred from this release.

**Live case:** [English](https://www.philippegodfroy.com/work/enterprise-ai-accounting-case) · [Dutch](https://www.philippegodfroy.com/nl/work/enterprise-ai-accounting-case). [Central showcase](../SHOWCASE.md) · [exact machine-readable evidence](evidence/production-2026-11-08/release-verification.json).

## GitHub and deployment

| Component | Exact code revision | Integration and hosted checks |
|---|---|---|
| Public playbook content | `ab6ac7dde28cdc7b4cdc5111af6204287d0293af` | [PR 1 merged](https://github.com/phlppgdfry/ai-transformation-playbook/pull/1), [main CI success](https://github.com/phlppgdfry/ai-transformation-playbook/actions/runs/42481934852) |
| Private website main | `9d4bc72f8c8b77ea2b7a333ac78e2ebaa0c2b346` | [PR 2 merged — owner access](https://github.com/phlppgdfry/pgosprive/pull/2), [main CI success — owner access](https://github.com/phlppgdfry/pgosprive/actions/runs/42482315807) |

Vercel production deployment `dpl_AbwWH3fiNGzDiZNrzpWFYAnFqcz6` is READY at [the deployment URL](https://pgosprive-10yk0dkz6-kippiegs-projects.vercel.app), aliased to `www.philippegodfroy.com` and the apex domain. GitHub deployment `7636110820` records that exact website main SHA with success. Public browser verification additionally required the built `index-Ce7QG8Eq.js` asset, rather than assuming a push meant deployment. This report-only follow-up has its own GitHub commit/review record; the code SHAs above identify the deployed implementation, not a self-referential report hash.

## Completed changes

- Central narrative, thirteen requested supporting documents, recruiter/CV/LinkedIn drafts, recording package, website copy, 24 interview questions and 10 ownership exercises with a 14-day plan are delivered. [Reader index](README.md), [audit/rubric](PORTFOLIO-AUDIT.md), [original changed-file manifest](evidence/changed-files.json).
- Preserved independently developed website navigation, Dutch URLs, language/document metadata, project catalogue, branding and documentation. The current catalogue already contained the prepared case; exactly one honest fictional entry and authentic screenshot remain. Merge-marker repair was verified before release; no overlapping work was discarded.
- Reproduced the current language fix instead of introducing a second implementation. Added regression tests for case identity, disclosure, explicit Dutch routes and legacy query-language navigation.
- Standardized on Node 24 and one npm lockfile. Removed stale Bun locks, fixed test Node typings, and added CI typecheck, lint and high-severity audit checks. Compatible security updates plus reviewed Vite 6.4.5 / Vitest 4.1.12 updates remove critical/high audit findings. Removed unused Zod; tested patched transitive build/lint dependencies.
- Merged both PRs after hosted success and verified the existing automatic Vercel production workflow. No paid resource, database migration or new hosting architecture was introduced.

## Actual verification

| Gate | Result and limits |
|---|---|
| Playbook | 9 unittest tests passed locally; content main CI passed. |
| Clean installation | npm ci from final package-lock.json passed; no undocumented global application package required. |
| Website tests | 31 Vitest tests passed, including 3 release regression tests; hosted main suite passed. |
| Typecheck / lint | Both passed. Lint has 0 errors and 8 inherited Fast Refresh warnings; no rule disabled for this release. |
| Production build | Vite build and 128-route prerender passed locally and hosted. Main bundle remains over 500 kB: a performance warning, not a broken build. |
| Links | Hosted full catalogue link job passed. Local career-document file targets validated. Private CI/source links are labelled owner-only, rather than falsely presented as anonymous evidence. |
| Preview | Vercel READY and authenticated EN/NL HTML requests returned 200 with correct title/language. Direct browser preview remained protected; no protection was disabled. Local browser verification preceded merge. |
| Actual public browser | Chrome, 375/768/1024/1440 px; homepage, work catalogue, EN/NL case; 20 checks passed, 0 console/page errors. Tested exact production bundle, loaded image, overflow, EN→NL→EN with preserved query/anchor, GitHub link, keyboard focus and alt presence. [Executed record](evidence/production-2026-11-08/browser.json). |
| Contact safety | Empty JSON POST returned 400; no real contact message or email was sent. Delivery to a real inbox was not retested. |
| Security | New staged content and central reachable-history Gitleaks scans found no secret. Private website history retains the previously classified anon client key; no privileged key added. Current code/bundle does not initialize Supabase or depend on RLS. RLS itself was not assessed. |
| Dependencies | npm audit: 0 critical, 0 high, 2 moderate package findings. GitHub independently recalculated from 69 alerts to 2 medium Router advisories. [Exact audit](evidence/production-2026-11-08/dependency-audit.json). No alert manually dismissed. |

[Desktop screenshot](evidence/production-2026-11-08/case-1440.png) · [mobile screenshot](evidence/production-2026-11-08/case-375.png). These are actual production captures, not conceptual mockups. Basic checks are not a WCAG certification or a complete screen-reader/contrast audit. Historical 172 repository tests, 27 deterministic/27 Qwen checks and 26 integration browser checks remain retained release evidence; they were not misrepresented as new runtime runs in this presentation release.

## Remaining issues

**BLOCKER:** none confirmed within the documented Career Launch showcase scope.

**Non-blocking security:** GHSA-wrjc-x8rr-h8h6 affects untrusted backslash Link/useNavigate destinations; this site uses authored static destinations. GHSA-337j-9hxr-rhxg affects React Router SSR error hydration; this client BrowserRouter app does not use it. Build-time metadata prerendering is not Router SSR. Retain the explicit risk assessment; a separately tested Router 7.18+ migration is recommended when touching routing or adding either exposure. Scanner success alone would not prove security.

**OPTIONAL:** eight Fast Refresh warnings, large bundle warning, broader accessibility and browser coverage. No feature expansion is required to finish this release.

**FUTURE LEARNING / human tasks:** complete ownership exercises, personally review career claims, record an actual video, update CV/LinkedIn and apply to real roles. These were prepared, not performed on the author's behalf. Azure inference/OCR, complete Copilot Studio runtime and personal mastery remain unverified; no customer savings or deployments are invented.

## Operations and freeze

Previous known-good deployment: `dpl_B1DssNkGShTgvuuEdW17BL7Z762V`. If a confirmed production regression occurs, use the existing authorized Vercel rollback mechanism with that exact target, then verify the domain. Rollback was not needed or executed.

The code release can now be frozen. Preserve existing branches and milestone tags. Further work is personal learning, recording and external review, or a concrete new defect—not another portfolio feature cycle. Final report publication is documentation-only and must retain passing CI. The final merged report revision is visible in GitHub history and recorded in the delivery response.
