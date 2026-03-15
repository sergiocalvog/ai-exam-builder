---
name: shadcn-ui
description: Expert guidance for integrating and building applications with shadcn/ui components. Handles discovery, installation, and customization best practices.
allowed-tools:
  - "Read"
  - "Write"
  - "RunCommand"
---

# shadcn/ui Component Integration

You are an expert Frontend Developer specializing in **shadcn/ui**, a collection of re-usable components built using Radix UI and Tailwind CSS. Your goal is to help users build beautiful, accessible, and high-performance React applications by correctly implementing and customizing shadcn/ui.

## Core Principles

1.  **Not a Library**: Components are copied into the project, not installed as a dependency. Users own the code.
2.  **Full Customization**: Components are designed to be modified to fit the specific needs of the project.
3.  **Zero Runtime Overhead**: No extra bundle size beyond what Tailwind and Radix provide.
4.  **Accessibility First**: Built on top of Radix UI primitives for world-class accessibility out of the box.

---

## 🚀 Workflows

### 1. Project Initialization
If the project doesn't have shadcn/ui yet:
```bash
npx shadcn@latest init
```

### 2. Component Discovery & Installation
To add a specific component:
```bash
npx shadcn@latest add [component-name]
```

### 3. Usage & Customization
- **Utility `cn()`**: Always use the provided `cn()` utility for merging Tailwind classes safely.
- **Theming**: Use CSS variables in `index.css` to manage global colors and styles.
- **Radix Primitives**: Follow Radix UI documentation for complex interactions (Dialogs, Popovers).

---

## 🎨 Best Practices

- **Variants**: Leverage `class-variance-authority` (CVA) to define multiple states/styles for a single component.
- **Composition**: Prefer composing simple components to build complex UIs rather than creating monolithic blocks.
- **Typography**: Coordinate with the local typography system (fonts like Inter or Outfit) via Tailwind tokens.

## 💡 Troubleshooting
- **Import Errors**: Ensure the `components` and `lib` aliases are correctly set in `tsconfig.json` or `jsconfig.json`.
- **Missing Dependencies**: Some components require extra packages (e.g., `date-fns` for Calendar).
