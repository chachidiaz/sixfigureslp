// @ts-check
import { defineConfig } from 'astro/config';

export default defineConfig({
  // The site lives in a folder of the main website: thesixfigureslp.com/insider
  site: 'https://thesixfigureslp.com',
  base: '/insider',
  trailingSlash: 'ignore',
});
