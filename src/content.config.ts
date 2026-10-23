import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

// One Markdown file per issue in content/issues/. The file name becomes the URL slug.
// Only title, summary and date are required: the issue number and read time are
// worked out from the publish date and the word count unless set here.
const issues = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './content/issues' }),
  schema: z.object({
    title: z.string(),
    summary: z.string(),
    date: z.coerce.date(),
    number: z.coerce.string().optional(),
    readTime: z.number().int().positive().optional(),
    author: z.string().default('The Insider team'),
  }),
});

export const collections = { issues };
