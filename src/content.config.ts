import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

// One Markdown file per issue in content/issues/. The file name becomes the URL slug.
const issues = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './content/issues' }),
  schema: z.object({
    number: z.coerce.string(),
    title: z.string(),
    summary: z.string(),
    date: z.coerce.date(),
    readTime: z.number().int().positive(),
    author: z.string().default('The Insider team'),
  }),
});

export const collections = { issues };
