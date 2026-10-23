import { getCollection, type CollectionEntry } from 'astro:content';

export type Issue = CollectionEntry<'issues'> & {
  /** Two-digit issue number, e.g. "08" */
  number: string;
  /** Minutes to read */
  readTime: number;
};

const WORDS_PER_MINUTE = 230;

/** All issues, newest first, with number and read time filled in. */
export async function getIssues(): Promise<Issue[]> {
  const entries = await getCollection('issues');
  const oldestFirst = entries.sort((a, b) => a.data.date.getTime() - b.data.date.getTime() || a.id.localeCompare(b.id));
  const issues = oldestFirst.map((entry, i) => {
    const words = (entry.body ?? '').split(/\s+/).filter(Boolean).length;
    return {
      ...entry,
      number: entry.data.number ?? String(i + 1).padStart(2, '0'),
      readTime: entry.data.readTime ?? Math.max(1, Math.round(words / WORDS_PER_MINUTE)),
    };
  });
  return issues.reverse();
}

/** Home of the archive, e.g. /insider/ */
export const homeUrl = import.meta.env.BASE_URL.replace(/\/?$/, '/');

export const issueUrl = (issue: Issue) => `${homeUrl}issues/${issue.id}/`;

// Dates are written without a time, so they parse as UTC midnight. Format in UTC
// so the day never shifts with the build machine's time zone.
const longFmt = new Intl.DateTimeFormat('en-US', { month: 'long', day: 'numeric', year: 'numeric', timeZone: 'UTC' });
const shortFmt = new Intl.DateTimeFormat('en-US', { month: 'short', day: 'numeric', year: 'numeric', timeZone: 'UTC' });

export const longDate = (d: Date) => longFmt.format(d); // October 14, 2026
export const shortDate = (d: Date) => shortFmt.format(d); // Oct 14, 2026
export const isoDate = (d: Date) => d.toISOString().slice(0, 10);
export const readLabel = (minutes: number) => `${minutes} min read`;
export const countLabel = (n: number) => `${n} ${n === 1 ? 'issue' : 'issues'}`;
