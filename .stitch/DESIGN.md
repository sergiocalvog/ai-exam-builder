# AI Exam Builder - Semantic Design System

This document serves as the "Source of Truth" for the visual and behavioral personality of the AI Exam Builder project. It is optimized for alignment during AI generation of new screens.

## 1. Atmosphere & Vibe
- **Scholarly & Professional**: Designs should feel trustworthy, academic, and modern.
- **Glassmorphism**: Subtle use of transparency and blur to create depth without clutter.
- **Responsive & Dynamic**: Use micro-animations to indicate AI processing and state changes.

## 2. Color Palette
| Token | HEX | Role |
| :--- | :--- | :--- |
| `primary` | `#2563EB` | Global actions, focus states, brand identity. |
| `success` | `#10B981` | Validation, exam completion, correct answers. |
| `surface` | `#F8FAFC` | Main workspace background. |
| `glass-bg` | `rgba(255, 255, 255, 0.05)` | Card backgrounds with 12px blur. |
| `text-high` | `#0F172A` | Primary readability, headings. |
| `text-low` | `#64748B` | Labels, metadata, empty states. |

## 3. Typography
- **Headings**: `Outfit` (Weight 800) - For impactful, high-tech branding.
- **Body**: `Inter` (Weight 400-600) - For maximum legibility in exam content.
- **Code/Data**: `JetBrains Mono` - For technical details or JSON views.

## 4. Geometry & Shape
- **Border Radius**: `24px` for main cards, `12px` for buttons.
- **Borders**: `1px` solid `rgba(255, 255, 255, 0.1)` on glass elements.
- **Shadows**: Deep but subtle shadows (e.g., `0 20px 50px rgba(0, 0, 0, 0.1)`) to lift cards off the background.

## 5. Component Patterns
- **Cards**: Large, rounded, glass-textured cards for each question.
- **Uploader**: Dotted border with active pulse animation when file is over it.
- **Inputs**: Transparent backgrounds with bottom-border focus states.
