import { defineConfig } from "astro/config";
import tailwindcss from "@tailwindcss/vite";
import nimbus, {
  defineConfig as defineNimbusConfig,
} from "@cloudflare/nimbus-docs";
import { tableScroll } from "@cloudflare/nimbus-docs/markdown";

export default defineConfig({
  output: "static",
  server: { host: "127.0.0.1", port: 4328 },
  vite: { plugins: [tailwindcss()] },
  integrations: [
    nimbus(
      defineNimbusConfig({
        site: "https://sandpapergate.callumflack-97f.workers.dev",
        title: "Sandpapergate",
        description:
          "The documents, the accounts, and the questions that remain.",
        locale: "en-AU",
        socialImageAlt: "Sandpapergate — the public record",
        sidebar: { items: ["index", { autogenerate: { collection: "docs" } }] },
      }),
      {
        rules: {
          "nimbus/frontmatter-shape": "error",
          "nimbus/internal-link": "error",
        },
        markdown: {
          hastPlugins: [tableScroll()],
          features: { headingAttributes: true, smartPunctuation: false },
        },
      },
    ),
  ],
});
