---
name: startup-blueprint
description: Generates a comprehensive 14-section blueprint for a startup app idea, from market analysis to development roadmap.
---

# Startup Blueprint Generation

Use this skill to generate a structured blueprint for any app idea. The goal is to provide a developer with everything they need to start building and a designer with everything they need to start mockup creation.

## Core Principles
- **Free-First Tooling**: Recommend ONLY tools with genuinely usable free tiers.
- **Realism**: No placeholders. Use real domain names, fields, and logic.
- **Coherence**: Every section must build upon the previous ones.
- **Speed to Launch**: Favor options that minimize time to MVP.

## Output Variants

- **Full Blueprint**: Sections 1 through 14 in order.
- **Quick Blueprint**: Sections 1, 2, 7, and 14 only.
- **Design Focus**: Sections 3, 4, 5, and 6 only.
- **Code Focus**: Sections 7, 8, 9, and 10 only.

---

## Section 1 — Idea Analysis
- **Problem Statement**: What specific pain point is being solved?
- **Target Audience**: Who is the primary persona?
- **Value Proposition**: Why will they use THIS app over others?
- **Competitive Landscape**: List 3 competitors and our "Unfair Advantage".

## Section 2 — Feature List
- **MVP Tier**: Absolute minimum features for a usable end-to-end flow.
- **V2 Tier**: High-impact retention features for post-launch.
- **Future Backlog**: "Nice-to-have" features for scaling.

## Section 3 — User Flow
- **Happy Path**: Step-by-step walkthrough of the core user journey (e.g., from landing to purchase).
- **Edge Cases**: Handling common alternative paths (e.g., forgotten password, empty search).

## Section 4 — Screen Structure
- **Sitemap**: High-level map of all screens and their hierarchy.
- **Navigation Model**: Tab bar vs. Drawer vs. Linear flow.

## Section 5 — Design System
- **Color Palette**: 3-5 harmonious HEX codes with usage roles (Primary, Secondary, Background).
- **Typography**: Chosen Google Font and scale (H1, Body, Caption).
- **UI Mood**: Descriptive terms (e.g., "Minimal & Clean", "Vibrant & Dynamic").

## Section 6 — Wireframes + Stitch Prompts
- **Wireframe Descriptions**: Text-based layout for the 3 main screens.
- **6B — Stitch Prompts**: specific prompts for Google Stitch to generate usable mockups on the first try.

## Section 7 — Technology Stack
- **Frontend**: Flutter (Dart) or React Native (TS) - justify based on complexity.
- **Backend/Database**: Supabase vs. Firebase.
- **External APIs**: Necessary 3rd party services (all with free tiers).

## Section 8 — Backend Architecture
- **Infrastructure**: Hosting (Railway/Render/Fly.io).
- **Auth Strategy**: Supabase/Firebase Auth setup.
- **Edge Functions**: Where to use serverless logic.

## Section 9 — Database Schema
- **ER Diagram**: Mermaid diagram of tables and relationships.
- **Table Definitions**: Column names, types, and constraints (UUIDs, Foreign Keys).

## Section 10 — Starter Code
Generate all three using real domain names and logic:
1. **Primary data model**: The core entity (e.g., `Order`, `Property`, `Workout`).
2. **Core feature screen**: Real UI logic, state management (loading/error), and theme integration.
3. **Primary service class**: Fetch/Post calls with error handling.

## Section 11 — Monetization Strategy
- **Chosen Model**: Freemium / Subscription / One-time / IAP / Ads / Marketplace.
- **Free vs. Paid**: Specific feature gates.
- **Pricing Tiers**: Concrete points (e.g., Free / $4.99/mo / $9.99/mo).
- **Metric to Optimize**: (e.g., trial-to-paid conversion, DAU, ARPU).
- **Implementation**: Stripe or RevenueCat free tier.

## Section 12 — Growth Strategy
Suggest 3–5 mechanisms (e.g., referrals, gamification, content loops). Include:
- **Name & Mechanics**: How it works for this app.
- **Fit**: Why it works for this audience.
- **Complexity**: Low / Medium / High.

## Section 13 — App Store Launch Plan
- **Asset Checklist**: Icon style, 5 Key Screenshots (what they communicate).
- **Copy**: App Name, Subtitle/Short Desc, Long Desc (~200 words).
- **ASO**: 10-15 keywords.
- **Sequence**: Soft launch -> Reviews -> Public launch -> ASO iteration.

## Section 14 — Development Roadmap
- **Phase 1 (MVP)**: Weeks 1-6. Focus on end-to-end usability.
- **Phase 2 (Beta)**: Weeks 7-10. Internal testing, bug fixes, 10 real users.
- **Phase 3 (Launch)**: Weeks 11-12. Submission & Marketing.
- **Phase 4 (V2)**: Months 4-6. Feedback-driven priority.
- **Phase 5 (Scale)**: Month 6+. Future features & optimization.

---

## Success Criteria
The output succeeds if a developer can start the code and a designer can generate mockups from the prompts immediately.
