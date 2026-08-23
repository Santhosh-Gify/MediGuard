/**
 * Semantic design tokens for the mobile app.
 *
 * These tokens mirror the naming conventions used in web artifacts (index.css)
 * so that multi-artifact projects share a cohesive visual identity.
 *
 * Replace the placeholder values below with values that match the project's
 * brand. If a sibling web artifact exists, read its index.css and convert the
 * HSL values to hex so both artifacts use the same palette.
 *
 * To add dark mode, add a `dark` key with the same token names.
 * The useColors() hook will automatically pick it up.
 */

const colors = {
  light: {
    // Legacy aliases (kept for backward compatibility)
    text: '#35233a',
    tint: '#c84b78',

    // Core surfaces
    background: '#fff8fb',
    foreground: '#35233a',

    // Cards / elevated surfaces
    card: '#ffffff',
    cardForeground: '#35233a',

    // Primary action color (buttons, links, active states)
    primary: '#c84b78',
    primaryForeground: '#ffffff',

    // Secondary / less-emphasis interactive surfaces
    secondary: '#f9e3ec',
    secondaryForeground: '#6d2949',

    // Muted / subdued elements (dividers, timestamps, placeholders)
    muted: '#f6eaf0',
    mutedForeground: '#8b7281',

    // Accent highlights (badges, selected items, focus rings)
    accent: '#ffe8b8',
    accentForeground: '#704516',

    // Destructive actions (delete, error states)
    destructive: '#c83e58',
    destructiveForeground: '#ffffff',

    // Borders and input outlines
    border: '#ead8e1',
    input: '#ead8e1',
  },

  // Border radius (in px). Sync from the sibling web artifact's --radius
  // CSS variable. This value applies to cards, buttons, inputs, and modals.
  radius: 8,
};

export default colors;
