import { getCollection, type CollectionEntry } from 'astro:content';

export type Issue = CollectionEntry<'issues'>;

/** All issues, newest first. */
export async function getIssues(): Promise<Issue[]> {
  const issues = await getCollection('issues');
  return issues.sort((a, b) => b.data.date.getTime() - a.data.date.getTime());
}

export const issueUrl = (issue: Issue) => `/issues/${issue.id}/`;

// Dates are written without a time, so they parse as UTC midnight. Format in UTC
// so the day never shifts with the build machine's time zone.
const longFmt = new Intl.DateTimeFormat('en-US', { month: 'long', day: 'numeric', year: 'numeric', timeZone: 'UTC' });
const shortFmt = new Intl.DateTimeFormat('en-US', { month: 'short', day: 'numeric', year: 'numeric', timeZone: 'UTC' });

export const longDate = (d: Date) => longFmt.format(d); // October 14, 2026
export const shortDate = (d: Date) => shortFmt.format(d); // Oct 14, 2026
export const isoDate = (d: Date) => d.toISOString().slice(0, 10);
export const readLabel = (minutes: number) => `${minutes} min read`;
export const countLabel = (n: number) => `${n} ${n === 1 ? 'issue' : 'issues'}`;
