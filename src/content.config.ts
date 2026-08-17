import { z, defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';

const blogCollection = defineCollection({
  loader: glob({ pattern: "*.md", base: "./src/content/blog" }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    pubDate: z.date().or(z.string()).optional(),
    tags: z.array(z.string()).optional(),
    author: z.string().default('Dr. Ubirajara Barroso, Jr.'),
    schemas: z.array(z.string()).optional(),
  }),
});

export const collections = {
  'blog': blogCollection,
};
