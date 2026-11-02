import { defineConfig, UserConfig } from "vitepress";
import { withSidebar } from "vitepress-sidebar";
import {
  mermaidPlugin,
  taskCheckboxPlugin,
  obsidianWikilinksPlugin,
} from "primary-vitepress/config";
import mdItTaskLists from "markdown-it-task-lists";
import mdItObsidianCallouts from "markdown-it-obsidian-callouts";
import path from "node:path";
import fs from "node:fs";

// https://vitepress.dev/reference/site-config
const vitePressConfigs: UserConfig<any> = {
  title: "📑 FICHES.ME CPES2",
  description: "La deuxième édition de Guigui qui sauve ton année de CPES.",
  base: '/cpes2/',
  cleanUrls: true,
  lastUpdated: true,
  ignoreDeadLinks: true,
  markdown: {
    math: true,
    toc: { level: [1, 2] },
    lineNumbers: true,
    languageAlias: {
      "pseudo-code": "python",
      conf: "yaml",
    },
    config(md) {
      md.use(mermaidPlugin);
      md.use(taskCheckboxPlugin);
      md.use(mdItObsidianCallouts);
      md.use(obsidianWikilinksPlugin, {
        resolveLink(target: string, fromFile?: string) {
          if (fromFile && !target.startsWith("/")) {
            const fromDir = path.dirname(fromFile.replace(/\\/g, "/"));
            const resolved = path.join(fromDir, target).replace(/\\/g, "/");
            if (fs.existsSync(resolved)) {
              return "/" + resolved;
            }
            if (fs.existsSync(resolved + ".md")) {
              return "/" + resolved;
            }
          }
        },
      });
      md.use(mdItTaskLists, { enabled: true });
    },
  },
  vite: {
    ssr: {
      noExternal: ["primary-vitepress", "mermaid"],
    },
  },
  titleTemplate: ":title - FICHES V2",
  lang: "fr-FR",
  head: [["link", { rel: "icon", type: "image/png", href: "/cpes2/logo.png" }]],
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    logo: "/logo.png",
    editLink: {
      pattern: "https://github.com/fiches-me/cpes2/edit/main/:path",
    },
    nav: [
      { text: "🖥️ POO", link: "/poo" },
      { text: "🍃 Santé", link: "/bio" },
      { text: "💸 Eco", link: "/eco" },
      { text: "💖 Nous Aider", link: "https://fiches.funa.dev/contribution" },
    ],
    footer: {
      message: "Publié sous licence GPL-3.0.",
      copyright: "Copyright © 2019-2026 FUNASITIEN, Guilhem C.",
    },
    socialLinks: [
      { icon: "github", link: "https://github.com/fiches-me/cpes2" },
      { icon: "discord", link: "https://dsc.gg/drmcld" },
    ],
    search: {
      provider: 'local'
    }
  },
  sitemap: {
    hostname: "https://fiches.funa.dev/cpes2",
  },
  transformPageData(ctx) {
    const canonicalUrl = `https://fiches.funa.dev/cpes2/${ctx.relativePath.replace(/\.(md|html)$/, "").replace(/\index$/, "")}`;
    ctx.frontmatter.head = ctx.frontmatter.head || [];
    ctx.frontmatter.head.push([
      "link",
      { rel: "canonical", href: canonicalUrl },
    ]);
  },
};

const sections = [
  "eco",
  "info",
  "maths",
  "poo",
  "bio",
  "misc",
  "ens",
  "sdd",
];

const sidebarOptions = sections.map((section) => ({
  documentRootPath: "/",
  scanStartPath: section,
  resolvePath: `/${section}/`,
  useTitleFromFrontmatter: true,
  useFolderTitleFromIndexFile: true,
  sortMenusByFrontmatterOrder: true,
  excludeFilesByFrontmatterFieldName: "draft",
  hyphenToSpace: true,
  underscoreToSpace: true,
}));

export default defineConfig(withSidebar(vitePressConfigs, sidebarOptions));
