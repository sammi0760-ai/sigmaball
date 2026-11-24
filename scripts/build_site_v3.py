#!/usr/bin/env python3
"""
SigmaBall for Powerball — Site Generator v3.1 (Refined 2-Card Mockup Redesign)
- 2-Column Mockup Card Layout (#111827 ~ #1E293B, 16px radius, rgba(148,163,184,0.2) border, 24px padding)
- White balls (38px circle) + Red Powerball (#EF4444) horizontally aligned (flex-wrap: nowrap)
- 4-Box Summary Grid: Sum 195, Median 175, Odd/Even 3:2, High/Low 3:2
- Hot (Last 100): 21, 36, 61, 14 & Cold (Overdue): 04, 13, 49, 58 chips
- Right Card: 4 filter chips with checkmarks (flex-wrap: wrap)
- Pill action button with smooth roll animation
- Disclaimer caption: "Sample UI preview · Historical data simulation · Does not guarantee winning"
- Operator: Cho Yeon Planning & sammi0760@gmail.com with click-to-copy
- Segmented language switcher EN / ES / KO with localStorage
- Inlined CSS & base64 logo for immediate file:// local double-click rendering
"""

import os
import base64

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
LOGO_PATH = os.path.join(BASE_DIR, "assets", "images", "sigmaball-logo.png")

with open(LOGO_PATH, "rb") as f:
    LOGO_B64 = base64.b64encode(f.read()).decode("utf-8")
LOGO_DATA_URI = f"data:image/png;base64,{LOGO_B64}"

CSS_CONTENT = """/* ==========================================================================
   SigmaBall for Powerball — Official Responsive Dark Navy Design System v3.1
   Base: #0B1120 & Void #070B14 | Accents: Sigma White & Red Point #EF4444
   ========================================================================== */

:root {
  --bg-void: #070B14;
  --bg-primary: #0B1120;
  --bg-surface: #111827;
  --bg-card: rgba(17, 24, 39, 0.88);
  --bg-card-alt: #162033;

  --border-subtle: rgba(148, 163, 184, 0.2);
  --border-focus: rgba(239, 68, 68, 0.45);
  --border-card-hover: rgba(239, 68, 68, 0.38);

  --text-white: #FFFFFF;
  --text-primary: #F8FAFC;
  --text-secondary: #94A3B8;
  --text-muted: #64748B;

  --accent-red: #EF4444;
  --accent-red-hover: #F87171;
  --accent-red-dark: #DC2626;
  --accent-red-glow: rgba(239, 68, 68, 0.32);

  --accent-blue: #3B82F6;
  --accent-emerald: #10B981;
  --accent-amber: #F59E0B;

  --font-sans: -apple-system, BlinkMacSystemFont, "Inter", "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  --font-mono: ui-monospace, "SF Mono", "JetBrains Mono", Menlo, Consolas, monospace;

  --radius-sm: 6px;
  --radius-md: 10px;
  --radius-lg: 16px;
  --radius-xl: 24px;
  --radius-full: 9999px;

  --container-max: 1200px;
  --transition-fast: 0.18s ease-in-out;
  --transition-normal: 0.25s cubic-bezier(0.16, 1, 0.3, 1);
}

*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html {
  font-family: var(--font-sans);
  background-color: var(--bg-void);
  color: var(--text-primary);
  line-height: 1.6;
  scroll-behavior: smooth;
  -webkit-font-smoothing: antialiased;
}

body {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  background-color: var(--bg-void);
  background-image:
    radial-gradient(circle at 50% -10%, rgba(239, 68, 68, 0.15) 0%, rgba(11, 17, 32, 0.88) 45%, transparent 75%),
    radial-gradient(ellipse 60% 40% at 85% 20%, rgba(59, 130, 246, 0.07) 0%, transparent 60%),
    radial-gradient(ellipse 50% 35% at 15% 45%, rgba(239, 68, 68, 0.05) 0%, transparent 55%),
    radial-gradient(rgba(255, 255, 255, 0.025) 1px, transparent 1px);
  background-size: 100% 100%, 100% 100%, 100% 100%, 36px 36px;
  background-attachment: fixed;
  overflow-x: hidden;
}

a {
  color: var(--accent-red-hover);
  text-decoration: none;
  transition: all var(--transition-fast);
}

a:hover {
  color: #FFFFFF;
}

.container {
  width: 100%;
  max-width: var(--container-max);
  margin-left: auto;
  margin-right: auto;
  padding-left: 24px;
  padding-right: 24px;
}

/* --------------------------------------------------------------------------
   Floating Navigation & Language Switcher
   -------------------------------------------------------------------------- */
.site-header {
  position: sticky;
  top: 14px;
  z-index: 100;
  padding: 0 16px;
  margin-bottom: 24px;
}

.nav-shell {
  max-width: 1140px;
  margin: 0 auto;
  background: rgba(11, 17, 32, 0.85);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: var(--radius-full);
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.45);
}

.nav-container {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 64px;
  padding: 0 20px;
  gap: 16px;
}

.brand {
  display: flex;
  align-items: center;
  gap: 10px;
  text-decoration: none;
  flex-shrink: 0;
}

.brand-logo {
  width: 36px;
  height: 36px;
  border-radius: var(--radius-md);
  object-fit: cover;
  box-shadow: 0 0 14px rgba(239, 68, 68, 0.3);
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.brand-title {
  font-size: 1.05rem;
  font-weight: 800;
  color: #FFFFFF;
  letter-spacing: -0.02em;
}

.brand-subtitle {
  font-size: 0.6875rem;
  color: var(--text-muted);
  font-weight: 600;
  text-transform: uppercase;
}

.nav-links {
  display: flex;
  align-items: center;
  gap: 22px;
  list-style: none;
}

.nav-links a {
  font-size: 0.85rem;
  font-weight: 600;
  color: var(--text-secondary);
  transition: color var(--transition-fast);
}

.nav-links a:hover {
  color: #FFFFFF;
}

.nav-right-actions {
  display: flex;
  align-items: center;
  gap: 12px;
  flex-shrink: 0;
}

/* Segmented Language Switcher */
.lang-switcher {
  display: inline-flex;
  align-items: center;
  background: rgba(14, 23, 42, 0.85);
  border: 1px solid rgba(255, 255, 255, 0.14);
  border-radius: var(--radius-full);
  padding: 2px;
}

.lang-btn {
  background: transparent;
  border: none;
  color: #94A3B8;
  font-size: 0.75rem;
  font-weight: 700;
  padding: 5px 10px;
  border-radius: var(--radius-full);
  cursor: pointer;
  transition: all var(--transition-fast);
}

.lang-btn:hover {
  color: #FFFFFF;
}

.lang-btn.active {
  background: var(--accent-red);
  color: #FFFFFF;
  box-shadow: 0 0 10px rgba(239, 68, 68, 0.5);
}

.nav-policy-btn {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 7px 14px;
  font-size: 0.8rem;
  font-weight: 700;
  border-radius: var(--radius-full);
  background: rgba(239, 68, 68, 0.12);
  border: 1px solid rgba(239, 68, 68, 0.32);
  color: #FECACA;
  transition: all var(--transition-fast);
  text-decoration: none;
}

.nav-policy-btn:hover {
  background: rgba(239, 68, 68, 0.24);
  border-color: rgba(239, 68, 68, 0.55);
  color: #FFFFFF;
  transform: translateY(-1px);
}

/* --------------------------------------------------------------------------
   Hero Section
   -------------------------------------------------------------------------- */
.hero {
  padding: 44px 0 36px;
  text-align: center;
  position: relative;
}

.hero-pill-badge {
  display: inline-flex;
  align-items: center;
  gap: 9px;
  padding: 6px 16px;
  border-radius: var(--radius-full);
  background: rgba(239, 68, 68, 0.08);
  border: 1px solid rgba(239, 68, 68, 0.28);
  margin-bottom: 22px;
}

.pulse-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background-color: var(--accent-red);
  box-shadow: 0 0 10px var(--accent-red);
  animation: pulseDot 2s infinite ease-in-out;
}

@keyframes pulseDot {
  0%, 100% { opacity: 1; transform: scale(1); }
  50% { opacity: 0.5; transform: scale(1.2); }
}

.hero-pill-badge span {
  font-size: 0.78125rem;
  font-weight: 700;
  color: #FECACA;
  letter-spacing: 0.06em;
  text-transform: uppercase;
}

.hero-logo-large {
  width: 96px;
  height: 96px;
  border-radius: var(--radius-xl);
  margin: 0 auto 20px;
  display: block;
  box-shadow:
    0 12px 36px rgba(0, 0, 0, 0.8),
    0 0 0 1px rgba(255, 255, 255, 0.2),
    0 0 36px rgba(239, 68, 68, 0.35);
  border: 2px solid rgba(255, 255, 255, 0.22);
}

.hero-title {
  font-size: clamp(2.2rem, 5.5vw, 3.8rem);
  font-weight: 850;
  letter-spacing: -0.035em;
  line-height: 1.1;
  margin-bottom: 16px;
  color: #FFFFFF;
}

.hero-title-gradient {
  background: linear-gradient(135deg, #FFFFFF 20%, #FCA5A5 65%, #EF4444 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  display: inline-block;
}

.hero-subtitle {
  font-size: clamp(0.98rem, 2vw, 1.2rem);
  color: #CBD5E1;
  max-width: 740px;
  margin: 0 auto 28px;
  line-height: 1.7;
}

.package-pill-wrap {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  padding: 7px 16px;
  background: rgba(14, 23, 42, 0.85);
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: var(--radius-full);
  font-family: var(--font-mono);
  font-size: 0.85rem;
  color: #94A3B8;
  margin-bottom: 32px;
}

.package-pill-wrap code {
  color: #FFFFFF;
  font-weight: 700;
  background: rgba(239, 68, 68, 0.14);
  padding: 2px 8px;
  border-radius: var(--radius-sm);
  border: 1px solid rgba(239, 68, 68, 0.28);
}

.copy-btn {
  background: transparent;
  border: none;
  color: #94A3B8;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 4px;
  font-size: 0.75rem;
  font-family: var(--font-sans);
  font-weight: 600;
  padding: 3px 8px;
  border-radius: var(--radius-sm);
  transition: all var(--transition-fast);
}

.copy-btn:hover {
  color: #FFFFFF;
  background: rgba(255, 255, 255, 0.08);
}

.hero-actions {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 14px;
  flex-wrap: wrap;
  margin-bottom: 40px;
}

.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 13px 28px;
  border-radius: var(--radius-md);
  font-size: 0.92rem;
  font-weight: 700;
  cursor: pointer;
  transition: all var(--transition-fast);
  text-decoration: none;
  line-height: 1;
}

.btn-primary {
  background: linear-gradient(135deg, #EF4444 0%, #DC2626 60%, #B91C1C 100%);
  color: #FFFFFF;
  box-shadow: 0 4px 20px rgba(220, 38, 38, 0.45);
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.btn-primary:hover {
  background: linear-gradient(135deg, #F87171 0%, #EF4444 60%, #DC2626 100%);
  color: #FFFFFF;
  transform: translateY(-2px);
}

.btn-secondary {
  background: rgba(18, 28, 51, 0.8);
  color: #F8FAFC;
  border: 1px solid rgba(255, 255, 255, 0.12);
  backdrop-filter: blur(10px);
}

.btn-secondary:hover {
  background: rgba(26, 40, 72, 0.95);
  border-color: rgba(239, 68, 68, 0.4);
  color: #FFFFFF;
  transform: translateY(-2px);
}

/* Telemetry Strip */
.stat-ticker-strip {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 14px;
  max-width: 960px;
  margin: 0 auto;
  padding: 18px 20px;
  background: rgba(14, 23, 42, 0.6);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: var(--radius-lg);
  backdrop-filter: blur(10px);
}

.stat-ticker-item {
  text-align: center;
}

.stat-ticker-num {
  font-family: var(--font-mono);
  font-size: 1.2rem;
  font-weight: 800;
  color: #FFFFFF;
}

.stat-ticker-num.accent {
  color: var(--accent-red-hover);
}

.stat-ticker-lbl {
  font-size: 0.72rem;
  color: #94A3B8;
  font-weight: 600;
  margin-top: 3px;
  text-transform: uppercase;
}

/* --------------------------------------------------------------------------
   REFINED 2-CARD SIMULATION MOCKUP SECTION
   Theme: #111827 ~ #1E293B, 16px radius, rgba(148,163,184,0.2) border, 24px padding
   -------------------------------------------------------------------------- */
.section {
  padding: 68px 0;
}

.section-tag {
  font-size: 0.78125rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--accent-red);
  margin-bottom: 10px;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: rgba(239, 68, 68, 0.1);
  padding: 3px 12px;
  border-radius: var(--radius-full);
  border: 1px solid rgba(239, 68, 68, 0.25);
}

.section-title {
  font-size: clamp(1.85rem, 3.8vw, 2.5rem);
  font-weight: 800;
  letter-spacing: -0.025em;
  color: #FFFFFF;
  margin-bottom: 14px;
}

.section-desc {
  font-size: 1rem;
  color: var(--text-secondary);
  line-height: 1.7;
  max-width: 680px;
  margin: 0 auto;
}

.section-header {
  text-align: center;
  margin-bottom: 44px;
}

/* 2-Card Grid */
.sim-preview-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 24px;
}

.sim-mockup-card {
  background: linear-gradient(180deg, #111827 0%, #162033 100%);
  border: 1px solid rgba(148, 163, 184, 0.2);
  border-radius: 16px;
  padding: 24px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.45);
  display: flex;
  flex-direction: column;
  transition: transform 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease;
}

.sim-mockup-card:hover {
  transform: translateY(-3px);
  border-color: rgba(239, 68, 68, 0.4);
  box-shadow: 0 14px 38px rgba(0, 0, 0, 0.6), 0 0 20px rgba(239, 68, 68, 0.15);
}

.card-topbar-flex {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 12px;
  margin-bottom: 16px;
}

.card-title-group h3 {
  font-size: 1.2rem;
  font-weight: 800;
  color: #FFFFFF;
  letter-spacing: -0.015em;
  margin: 0 0 3px;
}

.card-title-group .sublabel {
  font-size: 0.72rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--accent-red);
}

.card-badge-group {
  display: flex;
  align-items: center;
  gap: 6px;
  flex-shrink: 0;
}

.badge-tag {
  font-size: 0.72rem;
  font-family: var(--font-mono);
  color: #CBD5E1;
  background: rgba(148, 163, 184, 0.12);
  padding: 3px 9px;
  border-radius: 999px;
  border: 1px solid rgba(148, 163, 184, 0.2);
  white-space: nowrap;
}

.badge-tag.accent {
  color: #FECACA;
  background: rgba(239, 68, 68, 0.15);
  border-color: rgba(239, 68, 68, 0.35);
  font-weight: 700;
}

/* Strictly Horizontal Ball Alignment (flex-wrap: nowrap) */
.balls-horizontal-row {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  flex-wrap: nowrap !important;
  width: 100%;
  margin: 16px 0 20px;
}

.ball-badge {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 38px;
  height: 38px;
  min-width: 38px;
  border-radius: 999px;
  font-size: 0.95rem;
  font-weight: 800;
  letter-spacing: -0.02em;
  user-select: none;
  flex-shrink: 0;
  transition: transform 0.15s ease;
}

.ball-badge:hover {
  transform: scale(1.1);
}

.ball-badge.white {
  background: #FFFFFF;
  color: #0B1120;
  border: 1px solid rgba(255, 255, 255, 0.9);
  box-shadow: 0 3px 8px rgba(0, 0, 0, 0.4), inset 0 -2px 3px rgba(0, 0, 0, 0.2);
}

.ball-badge.red {
  background: radial-gradient(circle at 35% 35%, #F87171 0%, #EF4444 60%, #DC2626 100%);
  color: #FFFFFF;
  border: 1px solid rgba(255, 255, 255, 0.4);
  box-shadow: 0 3px 12px rgba(239, 68, 68, 0.5), inset 0 -2px 3px rgba(0, 0, 0, 0.3);
}

.ball-divider-symbol {
  color: var(--text-muted);
  font-weight: 700;
  font-size: 1rem;
  user-select: none;
  padding: 0 2px;
  flex-shrink: 0;
}

/* 4-Box Summary Tiles */
.metric-summary-grid {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 8px;
  margin-bottom: 16px;
}

.metric-chip {
  background: rgba(14, 23, 42, 0.7);
  border: 1px solid rgba(148, 163, 184, 0.15);
  border-radius: 10px;
  padding: 10px 8px;
  text-align: center;
}

.metric-chip .chip-label {
  display: block;
  font-size: 0.6875rem;
  color: #94A3B8;
  text-transform: uppercase;
  font-weight: 600;
  margin-bottom: 3px;
  white-space: nowrap;
}

.metric-chip .chip-val {
  display: block;
  font-size: 1.05rem;
  color: #FFFFFF;
  font-weight: 800;
  line-height: 1.1;
}

/* Hot / Cold Information Bars */
.hot-cold-container {
  display: flex;
  flex-direction: column;
  gap: 8px;
  padding-top: 14px;
  border-top: 1px solid rgba(148, 163, 184, 0.12);
  margin-bottom: 16px;
}

.hot-cold-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 8px;
  background: rgba(14, 23, 42, 0.5);
  padding: 7px 12px;
  border-radius: 8px;
  border: 1px solid rgba(148, 163, 184, 0.1);
}

.hot-cold-row .label-tag {
  font-size: 0.72rem;
  font-weight: 700;
  display: flex;
  align-items: center;
  gap: 5px;
}

.hot-cold-row .label-tag.hot { color: #F87171; }
.hot-cold-row .label-tag.cold { color: #60A5FA; }

.mini-chips-group {
  display: flex;
  align-items: center;
  gap: 5px;
}

.mini-ball-chip {
  width: 24px;
  height: 24px;
  border-radius: 50%;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-size: 0.72rem;
  font-weight: 800;
  user-select: none;
}

.mini-ball-chip.hot {
  background: rgba(239, 68, 68, 0.18);
  border: 1px solid rgba(239, 68, 68, 0.45);
  color: #FECACA;
}

.mini-ball-chip.cold {
  background: rgba(59, 130, 246, 0.18);
  border: 1px solid rgba(59, 130, 246, 0.45);
  color: #BFDBFE;
}

/* Right Card: Filter Pills (flex-wrap: wrap) */
.filter-pills-wrap {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 16px;
}

.filter-pill-tag {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 6px 12px;
  border-radius: 999px;
  font-size: 0.74rem;
  font-weight: 700;
  background: rgba(239, 68, 68, 0.1);
  border: 1px solid rgba(239, 68, 68, 0.32);
  color: #FECACA;
}

.filter-pill-tag svg {
  color: var(--accent-red);
}

/* Shake Action Button */
.shake-action-btn {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 13px 20px;
  background: linear-gradient(135deg, #EF4444 0%, #DC2626 60%, #B91C1C 100%);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 999px;
  color: #FFFFFF;
  font-size: 0.85rem;
  font-weight: 800;
  letter-spacing: 0.03em;
  text-transform: uppercase;
  cursor: pointer;
  box-shadow: 0 4px 18px rgba(220, 38, 38, 0.45);
  transition: all 0.18s ease;
  margin-bottom: 14px;
}

.shake-action-btn:hover {
  background: linear-gradient(135deg, #F87171 0%, #EF4444 60%, #DC2626 100%);
  box-shadow: 0 6px 24px rgba(239, 68, 68, 0.65);
  transform: translateY(-2px);
}

/* Calm Disclaimer Caption at Card Bottom */
.card-disclaimer-caption {
  font-size: 0.74rem;
  color: #94A3B8;
  text-align: center;
  line-height: 1.45;
  margin-top: auto;
  padding-top: 12px;
  border-top: 1px solid rgba(148, 163, 184, 0.12);
}

/* --------------------------------------------------------------------------
   3-Step Workflow Section
   -------------------------------------------------------------------------- */
.workflow-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 24px;
}

.step-card {
  background: linear-gradient(180deg, #111827 0%, #162033 100%);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-lg);
  padding: 32px 24px;
  position: relative;
  display: flex;
  flex-direction: column;
  transition: all var(--transition-normal);
}

.step-card:hover {
  border-color: rgba(239, 68, 68, 0.4);
  transform: translateY(-3px);
  box-shadow: 0 16px 36px rgba(0, 0, 0, 0.6);
}

.step-num {
  font-family: var(--font-mono);
  font-size: 2rem;
  font-weight: 900;
  color: rgba(255, 255, 255, 0.12);
  line-height: 1;
  margin-bottom: 16px;
}

.step-title {
  font-size: 1.22rem;
  font-weight: 800;
  color: #FFFFFF;
  margin-bottom: 10px;
  letter-spacing: -0.015em;
}

.step-desc {
  font-size: 0.92rem;
  color: var(--text-secondary);
  line-height: 1.65;
  flex-grow: 1;
  margin-bottom: 18px;
}

.step-desc code {
  color: #93C5FD;
  font-family: var(--font-mono);
  font-size: 0.8rem;
}

.step-pill {
  align-self: flex-start;
  font-size: 0.72rem;
  font-weight: 700;
  padding: 4px 12px;
  border-radius: var(--radius-full);
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  color: #CBD5E1;
}

/* --------------------------------------------------------------------------
   Core Capabilities Grid
   -------------------------------------------------------------------------- */
.grid-3 {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 24px;
}

.feature-card {
  background: linear-gradient(180deg, #111827 0%, #162033 100%);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-lg);
  padding: 28px 24px;
  display: flex;
  flex-direction: column;
  transition: all var(--transition-normal);
  position: relative;
  overflow: hidden;
}

.feature-card::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 2px;
  background: linear-gradient(90deg, transparent, rgba(239, 68, 68, 0.8), transparent);
  opacity: 0;
  transition: opacity var(--transition-normal);
}

.feature-card:hover {
  border-color: rgba(239, 68, 68, 0.38);
  transform: translateY(-3px);
  box-shadow: 0 16px 36px rgba(0, 0, 0, 0.6);
}

.feature-card:hover::before {
  opacity: 1;
}

.feature-icon-box {
  width: 48px;
  height: 48px;
  border-radius: var(--radius-md);
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 18px;
}

.feature-icon-blue { background-color: rgba(59, 130, 246, 0.12); color: #60A5FA; border: 1px solid rgba(59, 130, 246, 0.28); }
.feature-icon-red { background-color: rgba(239, 68, 68, 0.14); color: #F87171; border: 1px solid rgba(239, 68, 68, 0.38); }
.feature-icon-purple { background-color: rgba(139, 92, 246, 0.12); color: #A78BFA; border: 1px solid rgba(139, 92, 246, 0.28); }
.feature-icon-emerald { background-color: rgba(16, 185, 129, 0.12); color: #34D399; border: 1px solid rgba(16, 185, 129, 0.28); }
.feature-icon-amber { background-color: rgba(245, 158, 11, 0.12); color: #FBBF24; border: 1px solid rgba(245, 158, 11, 0.28); }

.feature-title {
  font-size: 1.18rem;
  font-weight: 800;
  color: #FFFFFF;
  margin-bottom: 8px;
  letter-spacing: -0.015em;
}

.feature-desc {
  font-size: 0.9rem;
  color: var(--text-secondary);
  line-height: 1.65;
  margin-bottom: 18px;
  flex-grow: 1;
}

.feature-list {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 8px;
  padding-top: 14px;
  border-top: 1px solid rgba(255, 255, 255, 0.07);
}

.feature-list-item {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 0.8rem;
  color: #CBD5E1;
}

.feature-list-item svg {
  color: var(--accent-red);
  flex-shrink: 0;
}

/* --------------------------------------------------------------------------
   Mandatory Disclaimer Box
   -------------------------------------------------------------------------- */
.disclaimer-section {
  padding: 24px 0 44px;
}

.disclaimer-box {
  background: linear-gradient(180deg, rgba(239, 68, 68, 0.09) 0%, rgba(14, 23, 42, 0.92) 100%);
  border: 1px solid rgba(239, 68, 68, 0.45);
  border-left: 5px solid var(--accent-red);
  border-radius: var(--radius-lg);
  padding: 26px 30px;
  box-shadow: 0 10px 32px rgba(0, 0, 0, 0.5);
}

.disclaimer-header {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 14px;
}

.disclaimer-badge {
  padding: 3px 9px;
  border-radius: var(--radius-sm);
  background: rgba(239, 68, 68, 0.25);
  border: 1px solid rgba(239, 68, 68, 0.45);
  color: #FECACA;
  font-size: 0.72rem;
  font-weight: 800;
  text-transform: uppercase;
}

.disclaimer-title {
  font-size: 1.08rem;
  font-weight: 800;
  color: #F87171;
}

.disclaimer-text {
  font-size: 0.94rem;
  color: #F1F5F9;
  line-height: 1.75;
}

.disclaimer-note {
  margin-top: 12px;
  font-size: 0.8rem;
  color: #94A3B8;
  line-height: 1.6;
}

/* --------------------------------------------------------------------------
   FAQ Accordion
   -------------------------------------------------------------------------- */
.faq-wrap {
  max-width: 900px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.faq-item {
  background: linear-gradient(180deg, #111827 0%, #162033 100%);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-lg);
  overflow: hidden;
  transition: all var(--transition-fast);
}

.faq-item:hover {
  border-color: rgba(239, 68, 68, 0.35);
}

.faq-item[open] {
  border-color: rgba(239, 68, 68, 0.48);
}

.faq-question {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  padding: 20px 24px;
  cursor: pointer;
  user-select: none;
  list-style: none;
}

.faq-question::-webkit-details-marker { display: none; }

.faq-question-text {
  font-size: 1.05rem;
  font-weight: 800;
  color: #FFFFFF;
}

.faq-chevron {
  color: var(--accent-red);
  transition: transform var(--transition-fast);
  flex-shrink: 0;
}

.faq-item[open] .faq-chevron {
  transform: rotate(180deg);
}

.faq-answer {
  padding: 0 24px 20px;
  font-size: 0.92rem;
  color: #CBD5E1;
  line-height: 1.75;
  border-top: 1px solid rgba(255, 255, 255, 0.06);
  padding-top: 16px;
}

.faq-answer code {
  color: #93C5FD;
  font-family: var(--font-mono);
  font-size: 0.8rem;
}

/* --------------------------------------------------------------------------
   Specifications Matrix
   -------------------------------------------------------------------------- */
.specs-panel {
  background: linear-gradient(180deg, #111827 0%, #162033 100%);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-xl);
  padding: 38px;
  box-shadow: 0 10px 32px rgba(0, 0, 0, 0.5);
}

.specs-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 18px;
  margin-top: 30px;
}

.spec-item {
  background: rgba(11, 17, 32, 0.7);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: var(--radius-md);
  padding: 18px 16px;
}

.spec-label {
  font-size: 0.72rem;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: #94A3B8;
  margin-bottom: 6px;
  font-weight: 700;
}

.spec-value {
  font-size: 1.05rem;
  font-weight: 800;
  color: #FFFFFF;
}

.spec-sub {
  font-size: 0.78rem;
  color: var(--text-muted);
  margin-top: 3px;
}

/* --------------------------------------------------------------------------
   Footer & Contact Area (Cho Yeon Planning)
   -------------------------------------------------------------------------- */
.site-footer {
  margin-top: auto;
  background-color: #060912;
  border-top: 1px solid var(--border-subtle);
  padding: 56px 0 36px;
}

.footer-top {
  display: grid;
  grid-template-columns: 2fr 1fr 1fr;
  gap: 44px;
  padding-bottom: 40px;
  border-bottom: 1px solid var(--border-subtle);
}

.footer-brand-desc {
  font-size: 0.88rem;
  color: var(--text-secondary);
  line-height: 1.65;
  margin: 14px 0 20px;
  max-width: 440px;
}

.footer-col-title {
  font-size: 0.85rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: #FFFFFF;
  margin-bottom: 18px;
}

.footer-links {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.footer-links a {
  font-size: 0.88rem;
  color: var(--text-secondary);
  text-decoration: none;
  transition: color var(--transition-fast);
}

.footer-links a:hover {
  color: #FFFFFF;
}

.contact-highlight-card {
  background: rgba(14, 23, 42, 0.85);
  border: 1px solid rgba(148, 163, 184, 0.2);
  border-radius: var(--radius-md);
  padding: 16px 18px;
  margin-top: 12px;
}

.contact-email-row {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-top: 6px;
}

.email-copy-pill {
  background: rgba(239, 68, 68, 0.15);
  border: 1px solid rgba(239, 68, 68, 0.35);
  color: #FECACA;
  font-family: var(--font-mono);
  font-size: 0.78rem;
  padding: 3px 8px;
  border-radius: var(--radius-sm);
  cursor: pointer;
  transition: all var(--transition-fast);
}

.email-copy-pill:hover {
  background: rgba(239, 68, 68, 0.28);
  color: #FFFFFF;
}

.footer-bottom {
  padding-top: 28px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 16px;
  font-size: 0.8125rem;
  color: var(--text-muted);
}

.operator-badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 4px 10px;
  background-color: rgba(14, 23, 42, 0.85);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-sm);
  font-family: var(--font-mono);
  font-size: 0.75rem;
  color: #FECACA;
}

/* --------------------------------------------------------------------------
   Responsive Layouts (360px ~ 1280px)
   -------------------------------------------------------------------------- */
@media (max-width: 1040px) {
  .sim-preview-grid { grid-template-columns: 1fr; }
  .workflow-grid { grid-template-columns: 1fr; }
  .grid-3 { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .specs-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .stat-ticker-strip { grid-template-columns: repeat(2, 1fr); }
  .footer-top { grid-template-columns: 1fr 1fr; }
}

@media (max-width: 868px) {
  .nav-links { display: none; }
  .grid-3 { grid-template-columns: 1fr; }
  .specs-grid { grid-template-columns: 1fr; }
  .footer-top { grid-template-columns: 1fr; }
}

@media (max-width: 640px) {
  .container { padding-left: 16px; padding-right: 16px; }
  .hero { padding: 36px 0 28px; }
  .hero-actions { flex-direction: column; width: 100%; }
  .hero-actions .btn { width: 100%; }
  .stat-ticker-strip { grid-template-columns: 1fr 1fr; gap: 10px; padding: 14px; }
  .sim-mockup-card { padding: 20px 16px; }
  .metric-summary-grid { grid-template-columns: repeat(2, 1fr); gap: 6px; }
  .specs-panel { padding: 24px 18px; }
  .disclaimer-box { padding: 20px 18px; }
  .balls-horizontal-row { gap: 6px; }
  .ball-badge { width: 36px; height: 36px; min-width: 36px; font-size: 0.9rem; }
}

@media (max-width: 420px) {
  .container { padding-left: 12px; padding-right: 12px; }
  .site-header { padding: 0 6px; top: 6px; }
  .nav-container { height: 56px; padding: 0 12px; }
  .brand-logo { width: 30px; height: 30px; }
  .brand-title { font-size: 0.92rem; }
  .lang-btn { padding: 4px 7px; font-size: 0.7rem; }
  .nav-policy-btn { display: none; }
  .hero-title { font-size: 2rem; }
  .balls-horizontal-row { gap: 4px; }
  .ball-badge { width: 32px; height: 32px; min-width: 32px; font-size: 0.8rem; }
  .faq-question { padding: 16px 18px; }
  .faq-question-text { font-size: 0.95rem; }
  .faq-answer { padding: 0 18px 16px; font-size: 0.875rem; }
}
"""

with open(os.path.join(BASE_DIR, "assets", "css", "style.css"), "w", encoding="utf-8") as f:
    f.write(CSS_CONTENT)

HTML_CONTENT = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>SigmaBall for Powerball — Statistical Analysis & Combination Simulator</title>
  
  <meta name="description" content="SigmaBall for Powerball (com.sigmaball.app), operated by Cho Yeon Planning. Independent Android statistical utility offering historical draw statistics, filter-based combination generation, shake simulation, and backtesting.">
  <meta name="keywords" content="SigmaBall, Powerball statistics, lottery analysis, combination generator, backtesting, probability simulator, com.sigmaball.app, Cho Yeon Planning">
  <meta name="author" content="Cho Yeon Planning">
  
  <!-- Open Graph / Meta -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="YOUR_SITE_URL/">
  <meta property="og:title" content="SigmaBall for Powerball — Statistical Analysis Utility">
  <meta property="og:description" content="Independent statistical analysis and combinatorial simulation utility for Powerball. Historical draw archives, mathematical filters, shake picker, and backtesting. Operated by Cho Yeon Planning.">
  <meta property="og:image" content="{LOGO_DATA_URI}">

  <!-- Favicon -->
  <link rel="icon" type="image/svg+xml" href="assets/images/favicon.svg">
  <link rel="alternate icon" type="image/png" href="{LOGO_DATA_URI}">
  <link rel="canonical" href="YOUR_SITE_URL/">

  <!-- External Stylesheet for web servers -->
  <link rel="stylesheet" href="assets/css/style.css">

  <!-- Self-Contained Stylesheet (Guarantees immediate styling when double-clicked locally on desktop via file://) -->
  <style>
{CSS_CONTENT}
  </style>
</head>
<body>

  <!-- Floating Navigation Shell -->
  <header class="site-header">
    <div class="nav-shell">
      <div class="nav-container">
        <a href="#hero" class="brand" aria-label="SigmaBall for Powerball Home">
          <img src="{LOGO_DATA_URI}" alt="SigmaBall Logo" class="brand-logo" width="36" height="36">
          <div>
            <div class="brand-title">SigmaBall</div>
            <div class="brand-subtitle">for Powerball</div>
          </div>
        </a>

        <nav aria-label="Primary Navigation">
          <ul class="nav-links">
            <li><a href="#preview" data-i18n="nav_preview">Simulator</a></li>
            <li><a href="#workflow" data-i18n="nav_workflow">Workflow</a></li>
            <li><a href="#features" data-i18n="nav_features">Capabilities</a></li>
            <li><a href="#faq" data-i18n="nav_faq">FAQ</a></li>
            <li><a href="#disclaimer" data-i18n="nav_disclaimer">Disclaimer</a></li>
            <li><a href="privacy/sigmaball/index.html" data-href="/privacy/sigmaball" data-i18n="nav_privacy">Privacy Policy</a></li>
          </ul>
        </nav>

        <div class="nav-right-actions">
          <!-- Segmented Language Switcher (EN / ES / KO) -->
          <div class="lang-switcher" role="group" aria-label="Language Selector">
            <button class="lang-btn active" data-lang="en" type="button">EN</button>
            <button class="lang-btn" data-lang="es" type="button">ES</button>
            <button class="lang-btn" data-lang="ko" type="button">KO</button>
          </div>

          <a href="privacy/sigmaball/index.html" class="nav-policy-btn" data-href="/privacy/sigmaball">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
            <span data-i18n="btn_privacy">Privacy</span>
          </a>
        </div>
      </div>
    </div>
  </header>

  <main>
    <!-- Hero Section -->
    <section class="hero" id="hero">
      <div class="container">
        
        <div class="hero-pill-badge">
          <span class="pulse-dot"></span>
          <span data-i18n="hero_badge">Independent Android Statistical Tool · 2026 Edition</span>
        </div>

        <img src="{LOGO_DATA_URI}" alt="SigmaBall for Powerball Application Icon" class="hero-logo-large" width="96" height="96">

        <h1 class="hero-title">
          SigmaBall <span class="hero-title-gradient" data-i18n="hero_title_gradient">for Powerball</span>
        </h1>

        <p class="hero-subtitle" data-i18n="hero_subtitle">
          An objective, mathematical toolkit for Powerball enthusiasts. Analyze historical draw distributions, define custom statistical constraints, simulate combinations via shake motion, and backtest hypotheses against public records.
        </p>

        <!-- Interactive Package ID Pill -->
        <div class="package-pill-wrap" title="Google Play Package ID (Click to copy)">
          <span>Package ID:</span>
          <code>com.sigmaball.app</code>
          <button class="copy-btn" id="copyPkgBtn" type="button" aria-label="Copy package ID">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
            <span id="copyPkgText">Copy</span>
          </button>
        </div>

        <div class="hero-actions">
          <a href="#preview" class="btn btn-primary">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><polygon points="10 8 16 12 10 16 10 8"/></svg>
            <span data-i18n="btn_hero_sim">Explore Live Simulator</span>
          </a>
          <a href="privacy/sigmaball/index.html" class="btn btn-secondary">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
            <span data-i18n="btn_hero_privacy">Privacy Policy</span>
          </a>
        </div>

        <!-- Telemetry Strip -->
        <div class="stat-ticker-strip">
          <div class="stat-ticker-item">
            <div class="stat-ticker-num">292,201,338</div>
            <div class="stat-ticker-lbl" data-i18n="stat_space">Sample Space</div>
          </div>
          <div class="stat-ticker-item">
            <div class="stat-ticker-num accent">15+ Years</div>
            <div class="stat-ticker-lbl" data-i18n="stat_years">Public Archive (2010–Now)</div>
          </div>
          <div class="stat-ticker-item">
            <div class="stat-ticker-num">100% Local</div>
            <div class="stat-ticker-lbl" data-i18n="stat_local">On-Device SQLite Storage</div>
          </div>
          <div class="stat-ticker-item">
            <div class="stat-ticker-num accent">0.00%</div>
            <div class="stat-ticker-lbl" data-i18n="stat_gambling">Zero Gambling Alteration</div>
          </div>
        </div>

      </div>
    </section>

    <!-- SECTION 1: Clean 2-Card Mockup Redesign -->
    <section class="section" id="preview">
      <div class="container">
        
        <div class="section-header">
          <div class="section-tag">
            <span class="pulse-dot"></span>
            <span data-i18n="sim_tag">Interactive Simulation Preview</span>
          </div>
          <h2 class="section-title" data-i18n="sim_title">Designed for Analytical Clarity</h2>
          <p class="section-desc" data-i18n="sim_desc">
            Explore authentic dark UI components inspired directly by the SigmaBall Android application. Test the interactive Monte-Carlo shake simulator below.
          </p>
        </div>

        <div class="sim-preview-grid">

          <!-- Left Card: Draw Frequency & Range Snapshot -->
          <div class="sim-mockup-card">
            <div class="card-topbar-flex">
              <div class="card-title-group">
                <div class="sublabel" data-i18n="card_a_sublabel">Latest Recorded Drawing</div>
                <h3 data-i18n="card_a_title">Draw Frequency & Range Snapshot</h3>
              </div>
              <div class="card-badge-group">
                <span class="badge-tag">Archive #3284</span>
                <span class="badge-tag accent">data.ny.gov</span>
              </div>
            </div>

            <!-- Strictly Horizontal Ball Row (flex-wrap: nowrap) -->
            <div class="balls-horizontal-row" aria-label="Winning draw numbers: 14, 22, 39, 53, 67, Powerball 18">
              <div class="ball-badge white">14</div>
              <div class="ball-badge white">22</div>
              <div class="ball-badge white">39</div>
              <div class="ball-badge white">53</div>
              <div class="ball-badge white">67</div>
              <span class="ball-divider-symbol">+</span>
              <div class="ball-badge red" title="Red Powerball">18</div>
            </div>

            <!-- 4-Box Summary Tiles (2x2 or 4-box) -->
            <div class="metric-summary-grid">
              <div class="metric-chip">
                <span class="chip-label" data-i18n="chip_sum_lbl">Sum</span>
                <span class="chip-val">195</span>
              </div>
              <div class="metric-chip">
                <span class="chip-label" data-i18n="chip_median_lbl">Median</span>
                <span class="chip-val">175</span>
              </div>
              <div class="metric-chip">
                <span class="chip-label" data-i18n="chip_oddeven_lbl">Odd/Even</span>
                <span class="chip-val">3 : 2</span>
              </div>
              <div class="metric-chip">
                <span class="chip-label" data-i18n="chip_highlow_lbl">High/Low</span>
                <span class="chip-val">3 : 2</span>
              </div>
            </div>

            <!-- Hot & Cold Small Number Chips -->
            <div class="hot-cold-container">
              <div class="hot-cold-row">
                <span class="label-tag hot">
                  <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.38-.5-2-1-3-1.072-2.143-.224-4.054 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.153.433-2.294 1-3a2.5 2.5 0 0 0 2.5 2.5z"/></svg>
                  <span data-i18n="lbl_hot_chip">Hot (Last 100):</span>
                </span>
                <div class="mini-chips-group">
                  <span class="mini-ball-chip hot">21</span>
                  <span class="mini-ball-chip hot">36</span>
                  <span class="mini-ball-chip hot">61</span>
                  <span class="mini-ball-chip hot">14</span>
                </div>
              </div>

              <div class="hot-cold-row">
                <span class="label-tag cold">
                  <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 2v20M2 12h20M4.93 4.93l14.14 14.14M4.93 19.07 19.07 4.93"/></svg>
                  <span data-i18n="lbl_cold_chip">Cold (Overdue):</span>
                </span>
                <div class="mini-chips-group">
                  <span class="mini-ball-chip cold">04</span>
                  <span class="mini-ball-chip cold">13</span>
                  <span class="mini-ball-chip cold">49</span>
                  <span class="mini-ball-chip cold">58</span>
                </div>
              </div>
            </div>

            <!-- Calm Disclaimer Caption -->
            <div class="card-disclaimer-caption" data-i18n="caption_disclaimer">
              Sample UI preview · Historical data simulation · Does not guarantee winning
            </div>
          </div>

          <!-- Right Card: Interactive Shake Picker -->
          <div class="sim-mockup-card">
            <div class="card-topbar-flex">
              <div class="card-title-group">
                <div class="sublabel" data-i18n="card_b_sublabel">Combinatorial Filter Engine</div>
                <h3 data-i18n="card_b_title">Interactive Shake Picker</h3>
              </div>
              <div class="card-badge-group">
                <span class="badge-tag accent" data-i18n="card_b_rules">4 Rules Active</span>
              </div>
            </div>

            <!-- 4 Filter Chips with Checkmarks (flex-wrap: wrap) -->
            <div class="filter-pills-wrap">
              <span class="filter-pill-tag">
                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
                <span data-i18n="chip_consec">Consecutive ≤ 2</span>
              </span>
              <span class="filter-pill-tag">
                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
                <span data-i18n="chip_sum">Sum 130–180</span>
              </span>
              <span class="filter-pill-tag">
                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
                <span data-i18n="chip_odd">Odd/Even 3:2</span>
              </span>
              <span class="filter-pill-tag">
                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
                <span data-i18n="chip_exclude">Exclude Prev Draw</span>
              </span>
            </div>

            <!-- Strictly Horizontal Simulated Balls Row (flex-wrap: nowrap) -->
            <div class="balls-horizontal-row" id="simBallsRow" aria-label="Simulated balls: 08, 19, 33, 47, 62, Powerball 09">
              <div class="ball-badge white" id="b1">08</div>
              <div class="ball-badge white" id="b2">19</div>
              <div class="ball-badge white" id="b3">33</div>
              <div class="ball-badge white" id="b4">47</div>
              <div class="ball-badge white" id="b5">62</div>
              <span class="ball-divider-symbol">+</span>
              <div class="ball-badge red" id="bp" title="Red Powerball">09</div>
            </div>

            <!-- Pill Action Button with Shake Motion Simulation -->
            <button class="shake-action-btn" id="shakeBtn" type="button">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><rect x="5" y="2" width="14" height="20" rx="2" ry="2"/><line x1="12" y1="18" x2="12.01" y2="18"/></svg>
              <span id="shakeBtnText" data-i18n="btn_shake">⚡ Simulate Shake Motion (Generate)</span>
            </button>

            <!-- Calm Disclaimer Caption -->
            <div class="card-disclaimer-caption" data-i18n="caption_disclaimer">
              Sample UI preview · Historical data simulation · Does not guarantee winning
            </div>
          </div>

        </div>

      </div>
    </section>

    <!-- SECTION 2: 3-Step Statistical Workflow -->
    <section class="section" id="workflow">
      <div class="container">
        <div class="section-header">
          <div class="section-tag" data-i18n="wf_tag">Analytical Workflow</div>
          <h2 class="section-title" data-i18n="wf_title">How SigmaBall Works</h2>
          <p class="section-desc" data-i18n="wf_desc">
            A transparent 3-step loop: examine public records, apply custom combinatorial logic, and test hypothetical sets locally.
          </p>
        </div>

        <div class="workflow-grid">
          <div class="step-card">
            <div class="step-num">01</div>
            <h3 class="step-title" data-i18n="wf_s1_title">Explore History</h3>
            <p class="step-desc" data-i18n="wf_s1_desc">
              Browse decades of official Powerball draw results sourced from public government datasets (<code>data.ny.gov</code>). Inspect hot and cold ball trends, sum medians, and frequency heatmaps.
            </p>
            <div class="step-pill" data-i18n="wf_s1_pill">Public Data Ingestion</div>
          </div>

          <div class="step-card">
            <div class="step-num" style="color: rgba(239, 68, 68, 0.25);">02</div>
            <h3 class="step-title" data-i18n="wf_s2_title">Filter & Shake</h3>
            <p class="step-desc" data-i18n="wf_s2_desc">
              Define your own mathematical constraints—such as odd/even splits, sum total intervals, and consecutive ball limits. Shake your device to generate combinations adhering strictly to your rules.
            </p>
            <div class="step-pill" style="color: #FECACA; border-color: rgba(239,68,68,0.3); background: rgba(239,68,68,0.1);" data-i18n="wf_s2_pill">
              Accelerometer Simulator
            </div>
          </div>

          <div class="step-card">
            <div class="step-num" style="color: rgba(16, 185, 129, 0.25);">03</div>
            <h3 class="step-title" data-i18n="wf_s3_title">Backtest & Save</h3>
            <p class="step-desc" data-i18n="wf_s3_desc">
              Save your generated sets to your device's isolated local SQLite storage. Backtest hypothetical combinations against years of past drawings to calculate historical match frequencies.
            </p>
            <div class="step-pill" style="color: #A7F3D0; border-color: rgba(16,185,129,0.3); background: rgba(16,185,129,0.1);" data-i18n="wf_s3_pill">
              100% On-Device Storage
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Mandatory Disclaimer Box (Official Notice) -->
    <section class="disclaimer-section" id="disclaimer">
      <div class="container">
        <div class="disclaimer-box" role="alert" aria-label="Important Disclaimer">
          <div class="disclaimer-header">
            <span class="disclaimer-badge" data-i18n="disc_badge">Official Notice</span>
            <h2 class="disclaimer-title" data-i18n="disc_title">Independent Tool Disclaimer & Public Notice</h2>
          </div>
          <!-- Verbatim snippet preserved for compliance check -->
          <p class="disclaimer-text">
            <strong>SigmaBall for Powerball</strong> is an independent statistical analysis and number-simulation tool. It is <strong>NOT affiliated with, endorsed by, or connected to Powerball, the Multi-State Lottery Association (MUSL), or any government or lottery authority</strong>. No tickets are sold and no real-money gambling is offered. Historical data is sourced from public datasets such as <code>data.ny.gov</code>.
          </p>
          <p class="disclaimer-note" data-i18n="disc_note">
            Mathematical simulation and statistical frequency tracking are purely educational and analytical. Previous draw distributions do not predict or guarantee future lottery draw results. Each lottery draw is an independent, mutually exclusive random trial.
          </p>
        </div>
      </div>
    </section>

    <!-- Core Capabilities (Features Grid) -->
    <section class="section" id="features">
      <div class="container">
        <div class="section-header">
          <div class="section-tag" data-i18n="feat_tag">Core Capabilities</div>
          <h2 class="section-title" data-i18n="feat_title">Engineered for Statistical Precision</h2>
          <p class="section-desc" data-i18n="feat_desc">
            SigmaBall provides deep statistical toolsets to analyze patterns, filter combinatorial spaces, and backtest strategies without misleading promises.
          </p>
        </div>

        <div class="grid-3">

          <!-- Feature 1: Historical Statistics -->
          <article class="feature-card">
            <div class="feature-icon-box feature-icon-blue">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 3v18h18"/><path d="m19 9-5 5-4-4-3 3"/></svg>
            </div>
            <h3 class="feature-title" data-i18n="f1_title">Historical Statistics</h3>
            <p class="feature-desc" data-i18n="f1_desc">
              Comprehensive frequency distribution and telemetry across decades of historical Powerball drawings. Track hot and cold numbers, overdue ball trends, and standard deviation curves.
            </p>
            <ul class="feature-list">
              <li class="feature-list-item">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
                <span data-i18n="f1_item1">White balls (1–69) & Powerball (1–26) heatmaps</span>
              </li>
              <li class="feature-list-item">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
                <span data-i18n="f1_item2">Sum total distribution & median charts</span>
              </li>
              <li class="feature-list-item">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
                <span data-i18n="f1_item3">Odd/Even and High/Low ratio tracking</span>
              </li>
            </ul>
          </article>

          <!-- Feature 2: Statistical Filters & Presets -->
          <article class="feature-card">
            <div class="feature-icon-box feature-icon-red">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="22 3 2 3 10 12.46 10 19 14 21 14 12.46 22 3"/></svg>
            </div>
            <h3 class="feature-title" data-i18n="f2_title">Statistical Filters & Presets</h3>
            <p class="feature-desc" data-i18n="f2_desc">
              Filter out mathematically improbable combinations before generation. Define combinatorial bounds such as consecutive number rules, range splits, and custom exclusions.
            </p>
            <ul class="feature-list">
              <li class="feature-list-item">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
                <span data-i18n="f2_item1">Consecutive number limits (e.g. max 2 adjacent)</span>
              </li>
              <li class="feature-list-item">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
                <span data-i18n="f2_item2">Target total sum intervals (e.g. 130–175)</span>
              </li>
              <li class="feature-list-item">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
                <span data-i18n="f2_item3">Save and export custom user filter presets</span>
              </li>
            </ul>
          </article>

          <!-- Feature 3: Quick Shake & Instant Pick -->
          <article class="feature-card">
            <div class="feature-icon-box feature-icon-purple">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="5" y="2" width="14" height="20" rx="2" ry="2"/><line x1="12" y1="18" x2="12.01" y2="18"/></svg>
            </div>
            <h3 class="feature-title" data-i18n="f3_title">Quick Shake & Instant Pick</h3>
            <p class="feature-desc" data-i18n="f3_desc">
              Harness your device's physical accelerometer. Give your phone a quick shake to trigger an organic Monte-Carlo random simulation that adheres strictly to your configured filters.
            </p>
            <ul class="feature-list">
              <li class="feature-list-item">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
                <span data-i18n="f3_item1">Accelerometer hardware shake sensor trigger</span>
              </li>
              <li class="feature-list-item">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
                <span data-i18n="f3_item2">Real-time validation against active rule sets</span>
              </li>
              <li class="feature-list-item">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
                <span data-i18n="f3_item3">Haptic vibration feedback on completion</span>
              </li>
            </ul>
          </article>

          <!-- Feature 4: Saved Sets & Backtesting -->
          <article class="feature-card">
            <div class="feature-icon-box feature-icon-emerald">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg>
            </div>
            <h3 class="feature-title" data-i18n="f4_title">Saved Sets & Backtesting</h3>
            <p class="feature-desc" data-i18n="f4_desc">
              Store custom combinations locally and run historical backtests. Simulate how your numbers would have matched against years of official Powerball draw results.
            </p>
            <ul class="feature-list">
              <li class="feature-list-item">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
                <span data-i18n="f4_item1">Multi-year historical backtest simulator</span>
              </li>
              <li class="feature-list-item">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
                <span data-i18n="f4_item2">Match tier metrics (Jackpot, Match 5, Match 4+PB)</span>
              </li>
              <li class="feature-list-item">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
                <span data-i18n="f4_item3">100% on-device private SQLite database</span>
              </li>
            </ul>
          </article>

          <!-- Feature 5: Multi-Language Support -->
          <article class="feature-card">
            <div class="feature-icon-box feature-icon-amber">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
            </div>
            <h3 class="feature-title" data-i18n="f5_title">Multi-Language Localization</h3>
            <p class="feature-desc" data-i18n="f5_desc">
              Built from the ground up for a global user base. Enjoy fully localized UI, statistical terminology, and instructions in English, Spanish (Español), and Korean (한국어).
            </p>
            <ul class="feature-list">
              <li class="feature-list-item">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
                <span data-i18n="f5_item1">English (EN) default international edition</span>
              </li>
              <li class="feature-list-item">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
                <span data-i18n="f5_item2">Spanish (ES) complete regional adaptation</span>
              </li>
              <li class="feature-list-item">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
                <span data-i18n="f5_item3">Korean (KO) localized terminology & UI</span>
              </li>
            </ul>
          </article>

          <!-- Feature 6: Privacy by Design -->
          <article class="feature-card">
            <div class="feature-icon-box feature-icon-blue">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
            </div>
            <h3 class="feature-title" data-i18n="f6_title">Privacy by Design</h3>
            <p class="feature-desc" data-i18n="f6_desc">
              Zero mandatory account registration, zero personal profile tracking. Your generated combinations and custom presets reside exclusively on your physical Android device.
            </p>
            <ul class="feature-list">
              <li class="feature-list-item">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
                <span data-i18n="f6_item1">No cloud account or login needed</span>
              </li>
              <li class="feature-list-item">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
                <span data-i18n="f6_item2">Google AdMob privacy policy compliant</span>
              </li>
              <li class="feature-list-item">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
                <span data-i18n="f6_item3">Clear all data anytime with one tap</span>
              </li>
            </ul>
          </article>

        </div>
      </div>
    </section>

    <!-- SECTION 3: Frequently Asked Questions (FAQ) -->
    <section class="section" id="faq">
      <div class="container">
        <div class="section-header">
          <div class="section-tag" data-i18n="faq_tag">Frequently Asked Questions</div>
          <h2 class="section-title" data-i18n="faq_title">Common Questions & Compliance</h2>
          <p class="section-desc" data-i18n="faq_desc">
            Direct, factual answers regarding data sourcing, mathematical models, and privacy.
          </p>
        </div>

        <div class="faq-wrap">

          <details class="faq-item" open>
            <summary class="faq-question">
              <span class="faq-question-text" data-i18n="faq_q1">Is this an official Powerball or government lottery application?</span>
              <svg class="faq-chevron" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
            </summary>
            <div class="faq-answer">
              <p data-i18n="faq_a1">
                <strong>No.</strong> SigmaBall for Powerball is an independent statistical analysis and number-simulation utility. It is <strong>NOT affiliated with, endorsed by, sponsored by, or connected to Powerball, the Multi-State Lottery Association (MUSL), or any government or lottery authority</strong>. No tickets are sold and no real-money gambling is offered.
              </p>
            </div>
          </details>

          <details class="faq-item">
            <summary class="faq-question">
              <span class="faq-question-text" data-i18n="faq_q2">Where does the historical lottery draw data come from?</span>
              <svg class="faq-chevron" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
            </summary>
            <div class="faq-answer">
              <p data-i18n="faq_a2">
                Historical draw records are retrieved from public open government repositories, specifically <code>data.ny.gov</code> ("Lottery Powerball Winning Numbers: Beginning 2010") published by the New York State Gaming Commission. The data is provided for objective educational, historical, and mathematical research purposes.
              </p>
            </div>
          </details>

          <details class="faq-item">
            <summary class="faq-question">
              <span class="faq-question-text" data-i18n="faq_q3">Does this application guarantee winning numbers or improve lottery odds?</span>
              <svg class="faq-chevron" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
            </summary>
            <div class="faq-answer">
              <p data-i18n="faq_a3">
                <strong>No.</strong> In true random lottery drawings, every number combination has an identical mathematical probability of being selected. Historical frequency analysis and combinatorial filters assist users in exploring statistical distributions and modeling custom sets, but they cannot predict future random outcomes or alter the underlying odds of the game. SigmaBall strictly avoids exaggerated claims.
              </p>
            </div>
          </details>

          <details class="faq-item">
            <summary class="faq-question">
              <span class="faq-question-text" data-i18n="faq_q4">How is my personal data and Google AdMob advertising handled?</span>
              <svg class="faq-chevron" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
            </summary>
            <div class="faq-answer">
              <p data-i18n="faq_a4_p1">
                SigmaBall follows a strict <strong>zero-cloud on-device storage</strong> architecture. Your saved combinations, filter presets, and settings remain solely within your device's local database (SQLite/SharedPreferences) and are never uploaded to developer servers.
              </p>
              <p style="margin-top: 10px;" data-i18n="faq_a4_p2">
                To support free development, the app integrates the <strong>Google AdMob SDK</strong>, which may process advertising identifiers (<code>AD_ID</code>), coarse IP-derived location, and ad performance diagnostics. For full disclosures, please review our <a href="privacy/sigmaball/index.html">English Privacy Policy</a> (/privacy/sigmaball) and developer <a href="app-ads.txt">app-ads.txt</a>.
              </p>
            </div>
          </details>

        </div>
      </div>
    </section>

    <!-- Specifications Matrix -->
    <section class="section" id="specifications" style="padding-top: 0;">
      <div class="container">
        <div class="specs-panel">
          <div class="section-tag" data-i18n="spec_tag">System Specifications</div>
          <h2 class="section-title" style="margin-bottom: 8px;" data-i18n="spec_title">Technical Information & Architecture</h2>
          <p class="section-desc" data-i18n="spec_desc">
            Detailed transparency for Google Play Console guidelines, developers, and users.
          </p>

          <div class="specs-grid">
            <div class="spec-item">
              <div class="spec-label" data-i18n="spec_app_name_lbl">Application Name</div>
              <div class="spec-value">SigmaBall for Powerball</div>
              <div class="spec-sub" data-i18n="spec_app_name_sub">Statistical Analysis Utility</div>
            </div>

            <div class="spec-item">
              <div class="spec-label" data-i18n="spec_pkg_lbl">Package Identifier</div>
              <div class="spec-value" style="font-family: var(--font-mono); font-size: 0.95rem;">com.sigmaball.app</div>
              <div class="spec-sub">Target: Android 8.0+ (API 26+)</div>
            </div>

            <div class="spec-item">
              <div class="spec-label" data-i18n="spec_data_lbl">Public Data Source</div>
              <div class="spec-value">data.ny.gov</div>
              <div class="spec-sub" data-i18n="spec_data_sub">State of NY Open Data (Lottery Powerball)</div>
            </div>

            <div class="spec-item">
              <div class="spec-label" data-i18n="spec_ads_lbl">Monetization & Ads</div>
              <div class="spec-value">Google AdMob SDK</div>
              <div class="spec-sub">Compliant with app-ads.txt standard</div>
            </div>

            <div class="spec-item">
              <div class="spec-label" data-i18n="spec_retention_lbl">Data Retention</div>
              <div class="spec-value">100% On-Device</div>
              <div class="spec-sub" data-i18n="spec_retention_sub">Encrypted Room/SQLite local database</div>
            </div>

            <div class="spec-item">
              <div class="spec-label" data-i18n="spec_lang_lbl">Supported Languages</div>
              <div class="spec-value">EN • ES • KO</div>
              <div class="spec-sub" data-i18n="spec_lang_sub">English, Spanish, Korean</div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </main>

  <!-- Site Footer (Cho Yeon Planning) -->
  <footer class="site-footer">
    <div class="container">
      <div class="footer-top">
        <div>
          <div class="brand" style="margin-bottom: 12px;">
            <img src="{LOGO_DATA_URI}" alt="SigmaBall Logo" class="brand-logo" width="34" height="34">
            <span class="brand-title">SigmaBall for Powerball</span>
          </div>
          <p class="footer-brand-desc" data-i18n="footer_desc">
            An independent, non-affiliated mathematical simulation and statistical utility for Android. Designed to provide transparent historical data analysis and combinatorial modeling.
          </p>
          <div style="display: flex; gap: 8px; flex-wrap: wrap;">
            <span class="operator-badge">com.sigmaball.app</span>
            <span class="operator-badge">v1.0 Release</span>
          </div>
        </div>

        <div>
          <div class="footer-col-title" data-i18n="footer_nav_title">Navigation</div>
          <ul class="footer-links">
            <li><a href="#preview" data-i18n="nav_preview">Simulator</a></li>
            <li><a href="#workflow" data-i18n="nav_workflow">3-Step Workflow</a></li>
            <li><a href="#features" data-i18n="nav_features">Key Features</a></li>
            <li><a href="#faq" data-i18n="nav_faq">Frequently Asked Questions</a></li>
            <li><a href="#disclaimer" data-i18n="nav_disclaimer">Disclaimer & Notice</a></li>
            <li><a href="privacy/sigmaball/index.html" data-href="/privacy/sigmaball" data-i18n="nav_privacy">Privacy Policy (English)</a></li>
            <li><a href="app-ads.txt" data-href="/app-ads.txt">AdMob app-ads.txt</a></li>
          </ul>
        </div>

        <div>
          <div class="footer-col-title" data-i18n="footer_contact_title">Operator & Contact</div>
          <div class="contact-highlight-card">
            <div style="font-size: 0.82rem; color: #94A3B8;"><strong style="color: #FFFFFF;" data-i18n="operator_lbl">Operator:</strong> Cho Yeon Planning</div>
            <div class="contact-email-row">
              <strong style="color: #FFFFFF; font-size: 0.82rem;" data-i18n="email_lbl">Email:</strong>
              <a href="mailto:sammi0760@gmail.com" style="color: #60A5FA; font-size: 0.82rem;">sammi0760@gmail.com</a>
              <button class="email-copy-pill" id="copyEmailBtn" type="button" title="Copy email address" aria-label="Copy Email">
                <span id="copyEmailText">Copy</span>
              </button>
            </div>
            <div style="margin-top: 10px; font-size: 0.82rem;">
              <a href="privacy/sigmaball/index.html" data-href="/privacy/sigmaball" style="color: #F87171; font-weight: 700;" data-i18n="footer_privacy_link">Privacy Policy Page &rarr;</a>
            </div>
          </div>
        </div>
      </div>

      <div class="footer-bottom">
        <div>
          &copy; 2026 Cho Yeon Planning. All rights reserved.
        </div>
        <div style="font-size: 0.75rem; color: #64748B;" data-i18n="footer_musl_note">
          SigmaBall for Powerball is NOT affiliated with, endorsed by, or sponsored by MUSL or Powerball.
        </div>
      </div>
    </div>
  </footer>

  <!-- Multilingual Engine & Interactive Simulator Script -->
  <script>
    // Multilingual Translations Dictionary (EN / ES / KO)
    const translations = {{
      en: {{
        nav_preview: "Simulator",
        nav_workflow: "Workflow",
        nav_features: "Capabilities",
        nav_faq: "FAQ",
        nav_disclaimer: "Disclaimer",
        nav_privacy: "Privacy Policy",
        btn_privacy: "Privacy",
        hero_badge: "Independent Android Statistical Tool · 2026 Edition",
        hero_title_gradient: "for Powerball",
        hero_subtitle: "An objective, mathematical toolkit for Powerball enthusiasts. Analyze historical draw distributions, define custom statistical constraints, simulate combinations via shake motion, and backtest hypotheses against public records.",
        btn_hero_sim: "Explore Live Simulator",
        btn_hero_privacy: "Privacy Policy",
        stat_space: "Sample Space",
        stat_years: "Public Archive (2010–Now)",
        stat_local: "On-Device SQLite Storage",
        stat_gambling: "Zero Gambling Alteration",
        sim_tag: "Interactive Simulation Preview",
        sim_title: "Designed for Analytical Clarity",
        sim_desc: "Explore authentic dark UI components inspired directly by the SigmaBall Android application. Test the interactive Monte-Carlo shake simulator below.",
        card_a_sublabel: "Latest Recorded Drawing",
        card_a_title: "Draw Frequency & Range Snapshot",
        chip_sum_lbl: "Sum",
        chip_median_lbl: "Median",
        chip_oddeven_lbl: "Odd/Even",
        chip_highlow_lbl: "High/Low",
        lbl_hot_chip: "Hot (Last 100):",
        lbl_cold_chip: "Cold (Overdue):",
        caption_disclaimer: "Sample UI preview · Historical data simulation · Does not guarantee winning",
        card_b_sublabel: "Combinatorial Filter Engine",
        card_b_title: "Interactive Shake Picker",
        card_b_rules: "4 Rules Active",
        chip_consec: "Consecutive ≤ 2",
        chip_sum: "Sum 130–180",
        chip_odd: "Odd/Even 3:2",
        chip_exclude: "Exclude Prev Draw",
        btn_shake: "⚡ Simulate Shake Motion (Generate)",
        wf_tag: "Analytical Workflow",
        wf_title: "How SigmaBall Works",
        wf_desc: "A transparent 3-step loop: examine public records, apply custom combinatorial logic, and test hypothetical sets locally.",
        wf_s1_title: "Explore History",
        wf_s1_desc: "Browse decades of official Powerball draw results sourced from public government datasets (data.ny.gov). Inspect hot and cold ball trends, sum medians, and frequency heatmaps.",
        wf_s1_pill: "Public Data Ingestion",
        wf_s2_title: "Filter & Shake",
        wf_s2_desc: "Define your own mathematical constraints—such as odd/even splits, sum total intervals, and consecutive ball limits. Shake your device to generate combinations adhering strictly to your rules.",
        wf_s2_pill: "Accelerometer Simulator",
        wf_s3_title: "Backtest & Save",
        wf_s3_desc: "Save your generated sets to your device's isolated local SQLite storage. Backtest hypothetical combinations against years of past drawings to calculate historical match frequencies.",
        wf_s3_pill: "100% On-Device Storage",
        disc_badge: "Official Notice",
        disc_title: "Independent Tool Disclaimer & Public Notice",
        disc_note: "Mathematical simulation and statistical frequency tracking are purely educational and analytical. Previous draw distributions do not predict or guarantee future lottery draw results. Each lottery draw is an independent, mutually exclusive random trial.",
        feat_tag: "Core Capabilities",
        feat_title: "Engineered for Statistical Precision",
        feat_desc: "SigmaBall provides deep statistical toolsets to analyze patterns, filter combinatorial spaces, and backtest strategies without misleading promises.",
        f1_title: "Historical Statistics",
        f1_desc: "Comprehensive frequency distribution and telemetry across decades of historical Powerball drawings. Track hot and cold numbers, overdue ball trends, and standard deviation curves.",
        f1_item1: "White balls (1–69) & Powerball (1–26) heatmaps",
        f1_item2: "Sum total distribution & median charts",
        f1_item3: "Odd/Even and High/Low ratio tracking",
        f2_title: "Statistical Filters & Presets",
        f2_desc: "Filter out mathematically improbable combinations before generation. Define combinatorial bounds such as consecutive number rules, range splits, and custom exclusions.",
        f2_item1: "Consecutive number limits (e.g. max 2 adjacent)",
        f2_item2: "Target total sum intervals (e.g. 130–175)",
        f2_item3: "Save and export custom user filter presets",
        f3_title: "Quick Shake & Instant Pick",
        f3_desc: "Harness your device's physical accelerometer. Give your phone a quick shake to trigger an organic Monte-Carlo random simulation that adheres strictly to your configured filters.",
        f3_item1: "Accelerometer hardware shake sensor trigger",
        f3_item2: "Real-time validation against active rule sets",
        f3_item3: "Haptic vibration feedback on completion",
        f4_title: "Saved Sets & Backtesting",
        f4_desc: "Store custom combinations locally and run historical backtests. Simulate how your numbers would have matched against years of official Powerball draw results.",
        f4_item1: "Multi-year historical backtest simulator",
        f4_item2: "Match tier metrics (Jackpot, Match 5, Match 4+PB)",
        f4_item3: "100% on-device private SQLite database",
        f5_title: "Multi-Language Localization",
        f5_desc: "Built from the ground up for a global user base. Enjoy fully localized UI, statistical terminology, and instructions in English, Spanish (Español), and Korean (한국어).",
        f5_item1: "English (EN) default international edition",
        f5_item2: "Spanish (ES) complete regional adaptation",
        f5_item3: "Korean (KO) localized terminology & UI",
        f6_title: "Privacy by Design",
        f6_desc: "Zero mandatory account registration, zero personal profile tracking. Your generated combinations and custom presets reside exclusively on your physical Android device.",
        f6_item1: "No cloud account or login needed",
        f6_item2: "Google AdMob privacy policy compliant",
        f6_item3: "Clear all data anytime with one tap",
        faq_tag: "Frequently Asked Questions",
        faq_title: "Common Questions & Compliance",
        faq_desc: "Direct, factual answers regarding data sourcing, mathematical models, and privacy.",
        faq_q1: "Is this an official Powerball or government lottery application?",
        faq_a1: "No. SigmaBall for Powerball is an independent statistical analysis and number-simulation utility. It is NOT affiliated with, endorsed by, sponsored by, or connected to Powerball, the Multi-State Lottery Association (MUSL), or any government or lottery authority. No tickets are sold and no real-money gambling is offered.",
        faq_q2: "Where does the historical lottery draw data come from?",
        faq_a2: "Historical draw records are retrieved from public open government repositories, specifically data.ny.gov ('Lottery Powerball Winning Numbers: Beginning 2010') published by the New York State Gaming Commission. The data is provided for objective educational, historical, and mathematical research purposes.",
        faq_q3: "Does this application guarantee winning numbers or improve lottery odds?",
        faq_a3: "No. In true random lottery drawings, every number combination has an identical mathematical probability of being selected. Historical frequency analysis and combinatorial filters assist users in exploring statistical distributions and modeling custom sets, but they cannot predict future random outcomes or alter the underlying odds of the game. SigmaBall strictly avoids exaggerated claims.",
        faq_q4: "How is my personal data and Google AdMob advertising handled?",
        faq_a4_p1: "SigmaBall follows a strict zero-cloud on-device storage architecture. Your saved combinations, filter presets, and settings remain solely within your device's local database (SQLite/SharedPreferences) and are never uploaded to developer servers.",
        faq_a4_p2: "To support free development, the app integrates the Google AdMob SDK, which may process advertising identifiers (AD_ID), coarse IP-derived location, and ad performance diagnostics. For full disclosures, please review our English Privacy Policy and developer app-ads.txt.",
        spec_tag: "System Specifications",
        spec_title: "Technical Information & Architecture",
        spec_desc: "Detailed transparency for Google Play Console guidelines, developers, and users.",
        spec_app_name_lbl: "Application Name",
        spec_app_name_sub: "Statistical Analysis Utility",
        spec_pkg_lbl: "Package Identifier",
        spec_data_lbl: "Public Data Source",
        spec_data_sub: "State of NY Open Data (Lottery Powerball)",
        spec_ads_lbl: "Monetization & Ads",
        spec_retention_lbl: "Data Retention",
        spec_retention_sub: "Encrypted Room/SQLite local database",
        spec_lang_lbl: "Supported Languages",
        spec_lang_sub: "English, Spanish, Korean",
        footer_desc: "An independent, non-affiliated mathematical simulation and statistical utility for Android. Designed to provide transparent historical data analysis and combinatorial modeling.",
        footer_nav_title: "Navigation",
        footer_contact_title: "Operator & Contact",
        operator_lbl: "Operator:",
        email_lbl: "Email:",
        footer_privacy_link: "Privacy Policy Page →",
        footer_musl_note: "SigmaBall for Powerball is NOT affiliated with, endorsed by, or sponsored by MUSL or Powerball."
      }},
      es: {{
        nav_preview: "Simulador",
        nav_workflow: "Flujo",
        nav_features: "Funciones",
        nav_faq: "Preguntas",
        nav_disclaimer: "Aviso",
        nav_privacy: "Privacidad",
        btn_privacy: "Privacidad",
        hero_badge: "Herramienta Estadística Independiente para Android · 2026",
        hero_title_gradient: "para Powerball",
        hero_subtitle: "Un conjunto de herramientas matemáticas y objetivas para entusiastas de Powerball. Analice distribuciones históricas de sorteos, defina restricciones estadísticas personalizadas, simule combinaciones mediante agitación y evalúe hipótesis con registros públicos.",
        btn_hero_sim: "Explorar Simulador",
        btn_hero_privacy: "Política de Privacidad",
        stat_space: "Espacio Muestral",
        stat_years: "Archivo Público (2010–Hoy)",
        stat_local: "Almacenamiento Local SQLite",
        stat_gambling: "Sin Alteración de Azar",
        sim_tag: "Vista Previa de Simulación",
        sim_title: "Diseñado para Claridad Analítica",
        sim_desc: "Explore componentes de interfaz oscura auténticos inspirados directamente en la aplicación Android SigmaBall. Pruebe el simulador interactivo Monte-Carlo.",
        card_a_sublabel: "Último Sorteo Registrado",
        card_a_title: "Instantánea de Frecuencia y Rango",
        chip_sum_lbl: "Suma",
        chip_median_lbl: "Mediana",
        chip_oddeven_lbl: "Impar/Par",
        chip_highlow_lbl: "Alto/Bajo",
        lbl_hot_chip: "Bolas Calientes (100):",
        lbl_cold_chip: "Bolas Frías (Atrasadas):",
        caption_disclaimer: "Vista previa de UI de muestra · Simulación de datos históricos · No garantiza premios",
        card_b_sublabel: "Motor de Filtros Combinatorios",
        card_b_title: "Selector Interactivo de Agitación",
        card_b_rules: "4 Reglas Activas",
        chip_consec: "Consecutivos ≤ 2",
        chip_sum: "Suma 130–180",
        chip_odd: "Impar/Par 3:2",
        chip_exclude: "Excluir Sorteo Ant.",
        btn_shake: "⚡ Simular Movimiento de Agitación (Generar)",
        wf_tag: "Flujo Analítico",
        wf_title: "Cómo Funciona SigmaBall",
        wf_desc: "Un ciclo transparente de 3 pasos: examine registros públicos, aplique lógica combinatoria personalizada y evalúe conjuntos hipotéticos localmente.",
        wf_s1_title: "Explorar Historial",
        wf_s1_desc: "Explore décadas de resultados oficiales de Powerball de fuentes públicas (data.ny.gov). Analice tendencias de bolas frías/calientes y medianas.",
        wf_s1_pill: "Ingesta de Datos Públicos",
        wf_s2_title: "Filtrar y Agitar",
        wf_s2_desc: "Defina límites matemáticos (ratios par/impar, suma total). Agite el dispositivo para generar combinaciones ajustadas a sus reglas.",
        wf_s2_pill: "Simulador por Acelerómetro",
        wf_s3_title: "Evaluar y Guardar",
        wf_s3_desc: "Guarde conjuntos en el almacenamiento local SQLite del dispositivo. Pruebe combinaciones contra sorteos pasados.",
        wf_s3_pill: "100% Almacenamiento Local",
        disc_badge: "Aviso Oficial",
        disc_title: "Descargo de Responsabilidad y Aviso Público",
        disc_note: "La simulación matemática y el seguimiento de frecuencias son puramente educativos y analíticos. Las distribuciones pasadas no predicen ni garantizan resultados futuros. Cada sorteo es un ensayo aleatorio independiente.",
        feat_tag: "Capacidades Clave",
        feat_title: "Diseñado para Precisión Estadística",
        feat_desc: "SigmaBall proporciona herramientas estadísticas avanzadas para analizar patrones y simular estrategias sin falsas promesas.",
        f1_title: "Estadísticas Históricas",
        f1_desc: "Distribución de frecuencias y telemetría de décadas de sorteos. Rastreo de números calientes y fríos, tendencias y desviaciones estándar.",
        f1_item1: "Mapas de calor de bolas blancas (1–69) y Powerball (1–26)",
        f1_item2: "Gráficos de distribución de suma total y mediana",
        f1_item3: "Seguimiento de ratios par/impar y alto/bajo",
        f2_title: "Filtros Estadísticos y Ajustes",
        f2_desc: "Filtre combinaciones matemáticamente improbables antes de la generación. Defina límites como reglas consecutivas y sumas.",
        f2_item1: "Límites de números consecutivos (máx. 2 contiguos)",
        f2_item2: "Intervalos de suma objetivo (ej. 130–175)",
        f2_item3: "Guarde y exporte filtros personalizados",
        f3_title: "Agitación Rápida y Selección Instantánea",
        f3_desc: "Aproveche el acelerómetro físico de su dispositivo. Agite el teléfono para generar números aleatorios Monte-Carlo bajo sus filtros.",
        f3_item1: "Disparador por sensor de movimiento de hardware",
        f3_item2: "Validación en tiempo real contra reglas activas",
        f3_item3: "Retroalimentación háptica por vibración",
        f4_title: "Conjuntos Guardados y Backtesting",
        f4_desc: "Almacene combinaciones localmente y realice pruebas retrospectivas contra años de sorteos oficiales de Powerball.",
        f4_item1: "Simulador retrospectivo de múltiples años",
        f4_item2: "Métricas de categorías de acierto (Jackpot, Match 5)",
        f4_item3: "Base de datos SQLite 100% privada en el dispositivo",
        f5_title: "Localización Multilingüe",
        f5_desc: "Diseñado globalmente. Disfrute de interfaz y terminología estadística completa en inglés, español y coreano.",
        f5_item1: "Inglés (EN) edición internacional predeterminada",
        f5_item2: "Español (ES) adaptación regional completa",
        f5_item3: "Coreano (KO) terminología y diseño localizado",
        f6_title: "Privacidad por Diseño",
        f6_desc: "Sin registro obligatorio, sin rastreo personal. Sus combinaciones y filtros residen exclusivamente en su dispositivo físico.",
        f6_item1: "Sin cuenta en la nube ni inicio de sesión",
        f6_item2: "Compatible con la política de privacidad de AdMob",
        f6_item3: "Borre todos los datos en cualquier momento con un toque",
        faq_tag: "Preguntas Frecuentes",
        faq_title: "Consultas Habituales y Cumplimiento",
        faq_desc: "Respuestas directas sobre fuentes de datos, modelos matemáticos y privacidad.",
        faq_q1: "¿Es esta una aplicación oficial de Powerball o del gobierno?",
        faq_a1: "No. SigmaBall for Powerball es una utilidad independiente de análisis y simulación. NO está afiliada, respaldada ni conectada con Powerball, MUSL ni ninguna autoridad de lotería. No se venden boletos ni se ofrece juego con dinero real.",
        faq_q2: "¿De dónde provienen los datos históricos de los sorteos?",
        faq_a2: "Los registros se obtienen de repositorios públicos abiertos del gobierno, específicamente data.ny.gov de la Comisión de Juego del Estado de Nueva York.",
        faq_q3: "¿Garantiza esta aplicación números ganadores o mejora las probabilidades?",
        faq_a3: "No. Cada sorteo de lotería aleatorio tiene probabilidades idénticas (1 en 292.2 millones para el premio mayor). Los filtros y análisis no alteran las probabilidades del juego.",
        faq_q4: "¿Cómo se manejan mis datos y la publicidad de Google AdMob?",
        faq_a4_p1: "SigmaBall no utiliza servidores en la nube. Todas sus combinaciones y filtros se almacenan exclusivamente en su dispositivo (SQLite).",
        faq_a4_p2: "Para mantener el acceso gratuito, se integra el SDK de Google AdMob, que procesa el identificador publicitario (AD_ID) y la ubicación aproximada según las políticas de Google.",
        spec_tag: "Especificaciones del Sistema",
        spec_title: "Información Técnica y Arquitectura",
        spec_desc: "Transparencia detallada para usuarios y pautas de Google Play Console.",
        spec_app_name_lbl: "Nombre de Aplicación",
        spec_app_name_sub: "Utilidad de Análisis Estadístico",
        spec_pkg_lbl: "Identificador de Paquete",
        spec_data_lbl: "Fuente de Datos Públicos",
        spec_data_sub: "Open Data del Estado de NY (Lottery Powerball)",
        spec_ads_lbl: "Monetización y Anuncios",
        spec_retention_lbl: "Retención de Datos",
        spec_retention_sub: "Base de datos local Room/SQLite encriptada",
        spec_lang_lbl: "Idiomas Disponibles",
        spec_lang_sub: "Inglés, Español, Coreano",
        footer_desc: "Utilidad matemática y estadística independiente para Android. Diseñada para proporcionar análisis de datos históricos y modelado combinatorio transparente.",
        footer_nav_title: "Navegación",
        footer_contact_title: "Operador y Contacto",
        operator_lbl: "Operador:",
        email_lbl: "Correo:",
        footer_privacy_link: "Política de Privacidad →",
        footer_musl_note: "SigmaBall for Powerball NO está afiliado, respaldado ni patrocinado por MUSL ni Powerball."
      }},
      ko: {{
        nav_preview: "시뮬레이터",
        nav_workflow: "워크플로우",
        nav_features: "주요 기능",
        nav_faq: "자주 묻는 질문",
        nav_disclaimer: "면책 공지",
        nav_privacy: "개인정보처리방침",
        btn_privacy: "정책",
        hero_badge: "독립 안드로이드 통계 분석 유틸리티 · 2026 최신판",
        hero_title_gradient: "for 파워볼",
        hero_subtitle: "파워볼 통계 분석 및 조합 시뮬레이션을 위한 객관적인 수학 유틸리티. 역대 추첨 빈도 분포를 분석하고, 필터 기반 번호를 생성하며, 가속도 흔들기 시뮬레이션 및 과거 회차 백테스팅을 제공합니다.",
        btn_hero_sim: "시뮬레이터 바로가기",
        btn_hero_privacy: "개인정보처리방침",
        stat_space: "전체 표본 공간",
        stat_years: "공공 데이터 아카이브 (2010–현재)",
        stat_local: "기기 로컬 안전 저장",
        stat_gambling: "사행성 변조 원천 차단",
        sim_tag: "인터랙티브 시뮬레이션 미리보기",
        sim_title: "정밀한 분석을 위한 직관적 설계",
        sim_desc: "시그마볼 안드로이드 앱의 실제 화면 구조를 웹에서 미리 확인하세요. 아래의 흔들기(Shake) 몬테카를로 시뮬레이터를 직접 테스트할 수 있습니다.",
        card_a_sublabel: "최근 기록된 당첨 회차",
        card_a_title: "추첨 빈도 및 구간 스냅샷",
        chip_sum_lbl: "합계",
        chip_median_lbl: "중위값",
        chip_oddeven_lbl: "홀짝 비율",
        chip_highlow_lbl: "고저 비율",
        lbl_hot_chip: "핫볼 (100회 최다):",
        lbl_cold_chip: "콜드볼 (미출현):",
        caption_disclaimer: "샘플 UI 미리보기 · 과거 데이터 기반 시뮬레이션 · 당첨을 보장하지 않음",
        card_b_sublabel: "필터 기반 조합 생성기",
        card_b_title: "인터랙티브 쉐이크 피커",
        card_b_rules: "4개 규칙 적용 중",
        chip_consec: "연속 번호 제한 (≤2)",
        chip_sum: "총합계 (130–180)",
        chip_odd: "홀짝 비율 (3:2)",
        chip_exclude: "직전 당첨 제외",
        btn_shake: "⚡ 흔들기 시뮬레이션 실행 (새 번호 생성)",
        wf_tag: "분석 워크플로우",
        wf_title: "시그마볼 이용 프로세스",
        wf_desc: "공공 데이터 확인, 맞춤형 수학 제약 조건 설정, 가상 조합 검증의 3단계 투명한 분석 구조를 제공합니다.",
        wf_s1_title: "01. 역대 통계 탐색",
        wf_s1_desc: "data.ny.gov 공공 데이터 기반 수십 년간의 공식 당첨 이력을 탐색하고, 핫·콜드 볼 및 합계 중위값을 분석합니다.",
        wf_s1_pill: "공공 데이터 수집",
        wf_s2_title: "02. 필터 설정 & 흔들기",
        wf_s2_desc: "홀짝 비율, 총합계 구간, 연속 번호 제한 등 수학적 제약 조건을 정의하고 폰을 흔들어 맞춤 번호를 추출합니다.",
        wf_s2_pill: "가속도계 시뮬레이터",
        wf_s3_title: "03. 백테스팅 & 로컬 저장",
        wf_s3_desc: "생성된 번호를 기기 내부 SQLite에 안전하게 저장하고, 역대 과거 회차에 대입하여 가상 적중 빈도를 검증합니다.",
        wf_s3_pill: "100% 온디바이스 저장",
        disc_badge: "공식 공지",
        disc_title: "독립 도구 안내 및 공식 면책 공지",
        disc_note: "수학적 시뮬레이션 및 통계 빈도 추적은 순수하게 교육적·분석적 목적입니다. 과거 추첨 분포는 미래 당첨 결과를 보장하거나 예측할 수 없으며, 각 추첨은 상호 독립적인 무작위 확률 시행입니다.",
        feat_tag: "핵심 기능",
        feat_title: "수학적 정밀성을 위한 설계",
        feat_desc: "시그마볼은 과장된 당첨 보장 없이 데이터 분석과 조합 시뮬레이션을 위한 전문 도구를 제공합니다.",
        f1_title: "역대 통계 분석",
        f1_desc: "수십 년간의 파워볼 공식 추첨 빈도 분포, 핫/콜드 번호, 미출현 볼 주기 및 표준 편차 분석 차트를 제공합니다.",
        f1_item1: "화이트볼(1–69) 및 파워볼(1–26) 출현 히트맵",
        f1_item2: "번호 총합계 분포도 및 중위값 분석",
        f1_item3: "홀수/짝수 및 고번호/저번호 비율 추적",
        f2_title: "통계 필터 & 프리셋",
        f2_desc: "수학적으로 희박한 조합을 사전에 배제합니다. 연속 번호 제한, 구간 합계, 제외 번호 등 나만의 규칙을 설정하세요.",
        f2_item1: "연속 번호 제한 필터 (최대 2연번 등)",
        f2_item2: "목표 총합계 구간 설정 (예: 130–175)",
        f2_item3: "사용자 맞춤형 통계 프리셋 저장 및 불러오기",
        f3_title: "퀵 쉐이크 & 즉시 추출",
        f3_desc: "기기의 물리 가속도 센서를 활용합니다. 스마트폰을 가볍게 흔들면 설정된 필터를 만족하는 무작위 몬테카를로 조합이 추출됩니다.",
        f3_item1: "하드웨어 가속도계 센서 흔들기 트리거",
        f3_item2: "활성 필터 규칙과의 실시간 일치도 검증",
        f3_item3: "조합 완성 시 햅틱 진동 피드백 제공",
        f4_title: "저장 세트 & 백테스팅",
        f4_desc: "추출한 조합을 기기에 저장하고, 과거 수년간의 실제 파워볼 당첨 결과와 대조하여 가상 매칭률을 시뮬레이션합니다.",
        f4_item1: "수개년 역대 당첨 데이터 백테스팅 시뮬레이터",
        f4_item2: "등수별 매칭 지표 (1등 잭팟, 2등 5개 일치 등)",
        f4_item3: "100% 기기 내부 SQLite 안전 저장",
        f5_title: "다국어 완벽 지원",
        f5_desc: "글로벌 사용자를 위해 영어(EN), 스페인어(ES), 한국어(KO)의 완벽한 UI 및 통계 용어 로컬라이제이션을 지원합니다.",
        f5_item1: "영어 (EN) 글로벌 기본 에디션",
        f5_item2: "스페인어 (ES) 완벽한 지역화 번역",
        f5_item3: "한국어 (KO) 맞춤형 용어 및 UI 지원",
        f6_title: "철저한 프라이버시 보호",
        f6_desc: "의무 회원가입이나 개인정보 수집이 전혀 없습니다. 생성된 조합과 커스텀 설정은 오직 사용자의 안드로이드 기기에만 저장됩니다.",
        f6_item1: "클라우드 계정 가입 및 로그인 불필요",
        f6_item2: "구글 AdMob 개인정보보호 규정 준수",
        f6_item3: "앱 데이터 삭제 또는 삭제 시 즉시 파기",
        faq_tag: "자주 묻는 질문",
        faq_title: "정책 심사 및 일반 문의",
        faq_desc: "데이터 출처, 수학적 모델, 개인정보 처리에 대한 명확한 답변입니다.",
        faq_q1: "이 앱은 파워볼이나 정부 기관의 공식 앱인가요?",
        faq_a1: "아닙니다. SigmaBall for Powerball은 독립적인 제3자 통계 분석 및 조합 시뮬레이션 유틸리티입니다. 파워볼(Powerball), 미국 다주복권협회(MUSL) 및 정부·복권국과 어떠한 제휴나 보증 관계도 없습니다. 실물 복권을 판매하거나 도박 기능을 일체 제공하지 않습니다.",
        faq_q2: "역대 당첨 번호 데이터는 어디서 수집되나요?",
        faq_a2: "뉴욕주 복권위원회가 공개한 data.ny.gov ('Lottery Powerball Winning Numbers: Beginning 2010') 등 미국 정부의 공개 공공 데이터셋에서 수집되며, 순수 분석 및 교육적 목적으로 제공됩니다.",
        faq_q3: "이 앱이 당첨 번호를 보장하거나 확률을 높여주나요?",
        faq_a3: "아닙니다. 모든 독립 복권 추첨에서 각 조합의 당첨 확률(잭팟 약 2억 9,220만 분의 1)은 동일합니다. 통계 필터는 분포를 탐색하기 위한 유틸리티일 뿐, 미래 결과를 예측하거나 확률을 변경할 수 없습니다. 과장 광고를 엄격히 금지합니다.",
        faq_q4: "개인정보와 Google AdMob 광고는 어떻게 처리되나요?",
        faq_a4_p1: "시그마볼은 100% 기기 로컬 저장 방식을 사용합니다. 사용자의 번호 세트와 프리셋은 개발사 서버로 전송되지 않고 기기 내부 SQLite에만 보관됩니다.",
        faq_a4_p2: "무료 서비스 제공을 위해 Google AdMob SDK를 탑재하고 있으며, 광고 ID(AD_ID) 및 IP 기반 대략적 위치 데이터가 Google 정책에 따라 처리됩니다. 자세한 내용은 영문 개인정보처리방침을 참고하세요.",
        spec_tag: "시스템 사양",
        spec_title: "기술 아키텍처 및 상세 사양",
        spec_desc: "구글 플레이 콘솔 가이드라인 및 투명한 앱 정보 제공.",
        spec_app_name_lbl: "애플리케이션 명칭",
        spec_app_name_sub: "통계 분석 유틸리티",
        spec_pkg_lbl: "패키지 식별자 (Package ID)",
        spec_data_lbl: "공공 데이터 출처",
        spec_data_sub: "뉴욕주 열린데이터 (data.ny.gov)",
        spec_ads_lbl: "수익화 및 광고 SDK",
        spec_retention_lbl: "데이터 보존 방식",
        spec_retention_sub: "기기 로컬 Room/SQLite 암호화 저장",
        spec_lang_lbl: "지원 언어",
        spec_lang_sub: "영어, 스페인어, 한국어",
        footer_desc: "안드로이드를 위한 독립적인 수학 시뮬레이션 및 통계 유틸리티. 투명한 역사적 데이터 분석과 조합 모델링을 제공합니다.",
        footer_nav_title: "바로가기",
        footer_contact_title: "운영사 및 문의",
        operator_lbl: "운영사:",
        email_lbl: "문의 메일:",
        footer_privacy_link: "개인정보처리방침 페이지 →",
        footer_musl_note: "SigmaBall for Powerball은 MUSL 및 파워볼과 어떠한 제휴·보증 관계도 없습니다."
      }}
    }};

    // Language Switcher Controller
    let currentLang = localStorage.getItem('sigmaball_lang') || 'en';

    function setLanguage(lang) {{
      if (!translations[lang]) lang = 'en';
      currentLang = lang;
      localStorage.setItem('sigmaball_lang', lang);

      // Update button active states
      document.querySelectorAll('.lang-btn').forEach(btn => {{
        if (btn.getAttribute('data-lang') === lang) {{
          btn.classList.add('active');
        }} else {{
          btn.classList.remove('active');
        }}
      }});

      // Update all data-i18n elements
      document.querySelectorAll('[data-i18n]').forEach(el => {{
        const key = el.getAttribute('data-i18n');
        if (translations[lang] && translations[lang][key]) {{
          el.textContent = translations[lang][key];
        }}
      }});

      document.documentElement.lang = lang;
    }}

    // Bind Language Buttons
    document.querySelectorAll('.lang-btn').forEach(btn => {{
      btn.addEventListener('click', () => {{
        setLanguage(btn.getAttribute('data-lang'));
      }});
    }});

    // Initialize with stored or default language
    setLanguage(currentLang);

    // Copy Package ID Handler
    const copyPkgBtn = document.getElementById('copyPkgBtn');
    const copyPkgText = document.getElementById('copyPkgText');
    if (copyPkgBtn) {{
      copyPkgBtn.addEventListener('click', () => {{
        navigator.clipboard.writeText('com.sigmaball.app').then(() => {{
          copyPkgText.textContent = 'Copied! ✓';
          copyPkgText.style.color = '#34D399';
          setTimeout(() => {{
            copyPkgText.textContent = 'Copy';
            copyPkgText.style.color = '';
          }}, 2000);
        }}).catch(() => {{
          const temp = document.createElement('input');
          temp.value = 'com.sigmaball.app';
          document.body.appendChild(temp);
          temp.select();
          document.execCommand('copy');
          document.body.removeChild(temp);
          copyPkgText.textContent = 'Copied! ✓';
          setTimeout(() => copyPkgText.textContent = 'Copy', 2000);
        }});
      }});
    }}

    // Copy Operator Email Handler (Cho Yeon Planning)
    const copyEmailBtn = document.getElementById('copyEmailBtn');
    const copyEmailText = document.getElementById('copyEmailText');
    if (copyEmailBtn) {{
      copyEmailBtn.addEventListener('click', () => {{
        navigator.clipboard.writeText('sammi0760@gmail.com').then(() => {{
          copyEmailText.textContent = 'Copied! ✓';
          copyEmailText.style.color = '#34D399';
          setTimeout(() => {{
            copyEmailText.textContent = 'Copy';
            copyEmailText.style.color = '';
          }}, 2000);
        }}).catch(() => {{
          const temp = document.createElement('input');
          temp.value = 'sammi0760@gmail.com';
          document.body.appendChild(temp);
          temp.select();
          document.execCommand('copy');
          document.body.removeChild(temp);
          copyEmailText.textContent = 'Copied! ✓';
          setTimeout(() => copyEmailText.textContent = 'Copy', 2000);
        }});
      }});
    }}

    // Interactive Shake Picker Simulator
    const shakeBtn = document.getElementById('shakeBtn');
    const b1 = document.getElementById('b1');
    const b2 = document.getElementById('b2');
    const b3 = document.getElementById('b3');
    const b4 = document.getElementById('b4');
    const b5 = document.getElementById('b5');
    const bp = document.getElementById('bp');

    const sampleSets = [
      {{ balls: [8, 19, 33, 47, 62], pb: 9 }},
      {{ balls: [12, 24, 38, 51, 65], pb: 16 }},
      {{ balls: [4, 17, 29, 44, 58], pb: 22 }},
      {{ balls: [15, 23, 36, 49, 63], pb: 7 }},
      {{ balls: [6, 21, 35, 48, 61], pb: 14 }}
    ];
    let currentIndex = 0;

    if (shakeBtn) {{
      shakeBtn.addEventListener('click', () => {{
        shakeBtn.disabled = true;

        let cycles = 0;
        const interval = setInterval(() => {{
          b1.textContent = String(Math.floor(Math.random() * 69) + 1).padStart(2, '0');
          b2.textContent = String(Math.floor(Math.random() * 69) + 1).padStart(2, '0');
          b3.textContent = String(Math.floor(Math.random() * 69) + 1).padStart(2, '0');
          b4.textContent = String(Math.floor(Math.random() * 69) + 1).padStart(2, '0');
          b5.textContent = String(Math.floor(Math.random() * 69) + 1).padStart(2, '0');
          bp.textContent = String(Math.floor(Math.random() * 26) + 1).padStart(2, '0');
          cycles++;
          if (cycles > 10) {{
            clearInterval(interval);
            currentIndex = (currentIndex + 1) % sampleSets.length;
            const target = sampleSets[currentIndex];
            b1.textContent = String(target.balls[0]).padStart(2, '0');
            b2.textContent = String(target.balls[1]).padStart(2, '0');
            b3.textContent = String(target.balls[2]).padStart(2, '0');
            b4.textContent = String(target.balls[3]).padStart(2, '0');
            b5.textContent = String(target.balls[4]).padStart(2, '0');
            bp.textContent = String(target.pb).padStart(2, '0');
            shakeBtn.disabled = false;
          }}
        }}, 60);
      }});
    }}

    // Local file protocol fix: ensure relative links work when opened directly via file://
    if (location.protocol === 'file:') {{
      document.querySelectorAll('[data-local-href]').forEach(el => {{
        el.href = el.getAttribute('data-local-href');
      }});
    }}
  </script>

</body>
</html>"""

with open(os.path.join(BASE_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(HTML_CONTENT)

print("Successfully regenerated index.html and assets/css/style.css with 2-card mockup redesign!")
