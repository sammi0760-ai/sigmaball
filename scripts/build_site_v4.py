#!/usr/bin/env python3
"""
SigmaBall for Powerball — Site Generator v4.1 (Bulletproof Responsive & I18N Hardening)
- Verified across English (EN), Spanish (ES), and Korean (KO)
- Bulletproof responsive CSS scaling with clamp() for 320px ~ 1920px viewports
- Zero overflow or wrap breaks on lottery balls (flex-wrap: nowrap !important with auto-scaling)
- Clean card topbars with responsive wrap for long titles in Spanish
- Hardened hot/cold telemetry chips with flex-shrink protection
- Enhanced Korean typography with word-break: keep-all
- Self-contained inlined CSS and Base64 logo for immediate local double-click file:// execution
"""

import os
import base64

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
LOGO_PATH = os.path.join(BASE_DIR, "assets", "images", "sigmaball-logo.png")

with open(LOGO_PATH, "rb") as f:
    LOGO_B64 = base64.b64encode(f.read()).decode("utf-8")
LOGO_DATA_URI = f"data:image/png;base64,{LOGO_B64}"

CSS_CONTENT = """/* ==========================================================================
   SigmaBall for Powerball — Design System v4.1 (Bulletproof Responsive)
   ========================================================================== */

:root {
  --bg-void: #060911;
  --bg-primary: #0B1120;
  --bg-surface: #111827;
  --bg-surface-elevated: #162033;
  --bg-card: rgba(17, 24, 39, 0.85);

  --border-subtle: rgba(148, 163, 184, 0.15);
  --border-light: rgba(255, 255, 255, 0.08);
  --border-focus: rgba(239, 68, 68, 0.45);
  --border-card-hover: rgba(239, 68, 68, 0.35);

  --text-white: #FFFFFF;
  --text-primary: #F8FAFC;
  --text-secondary: #94A3B8;
  --text-muted: #64748B;

  --accent-red: #EF4444;
  --accent-red-hover: #F87171;
  --accent-red-dark: #DC2626;
  --accent-red-glow: rgba(239, 68, 68, 0.35);

  --accent-blue: #3B82F6;
  --accent-emerald: #10B981;
  --accent-amber: #F59E0B;

  --font-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Inter", Helvetica, Arial, sans-serif;
  --font-mono: ui-monospace, "SF Mono", "JetBrains Mono", Menlo, Consolas, monospace;

  --radius-sm: 6px;
  --radius-md: 10px;
  --radius-lg: 16px;
  --radius-xl: 20px;
  --radius-full: 9999px;

  --container-max: 1200px;
  --transition-fast: 0.16s ease-in-out;
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
  -moz-osx-font-smoothing: grayscale;
  word-break: keep-all;
  overflow-wrap: break-word;
}

body {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  background-color: var(--bg-void);
  background-image:
    radial-gradient(circle at 50% -10%, rgba(239, 68, 68, 0.14) 0%, rgba(11, 17, 32, 0.9) 45%, transparent 75%),
    radial-gradient(ellipse 70% 45% at 85% 20%, rgba(59, 130, 246, 0.06) 0%, transparent 60%),
    radial-gradient(ellipse 50% 35% at 15% 50%, rgba(239, 68, 68, 0.04) 0%, transparent 55%),
    radial-gradient(rgba(255, 255, 255, 0.02) 1px, transparent 1px);
  background-size: 100% 100%, 100% 100%, 100% 100%, 36px 36px;
  background-attachment: fixed;
  overflow-x: hidden;
}

a {
  color: inherit;
  text-decoration: none;
}

.container {
  width: 100%;
  max-width: var(--container-max);
  margin: 0 auto;
  padding: 0 24px;
}

/* --------------------------------------------------------------------------
   Navigation Bar
   -------------------------------------------------------------------------- */
.site-header {
  position: sticky;
  top: 12px;
  z-index: 1000;
  padding: 0 16px;
}

.nav-container {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 64px;
  background: rgba(14, 22, 38, 0.85);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-xl);
  padding: 0 20px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
  max-width: var(--container-max);
  margin: 0 auto;
}

.nav-brand {
  display: flex;
  align-items: center;
  gap: 12px;
  font-weight: 800;
  font-size: 1.08rem;
  letter-spacing: -0.02em;
  color: #FFFFFF;
  flex-shrink: 0;
}

.brand-logo {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  border: 1px solid rgba(255, 255, 255, 0.2);
  display: block;
}

.brand-badge {
  font-size: 0.68rem;
  font-family: var(--font-mono);
  color: #FCA5A5;
  background: rgba(239, 68, 68, 0.15);
  border: 1px solid rgba(239, 68, 68, 0.35);
  padding: 2px 7px;
  border-radius: var(--radius-full);
  margin-left: 6px;
  font-weight: 700;
}

.nav-links {
  display: flex;
  align-items: center;
  gap: clamp(10px, 1.4vw, 22px);
  list-style: none;
}

.nav-links a {
  font-size: clamp(0.82rem, 1vw, 0.88rem);
  color: var(--text-secondary);
  font-weight: 600;
  transition: color var(--transition-fast);
  white-space: nowrap;
}

.nav-links a:hover {
  color: #FFFFFF;
}

.nav-right-tools {
  display: flex;
  align-items: center;
  gap: 10px;
  flex-shrink: 0;
}

/* Language Switcher Segmented Control */
.lang-switcher {
  display: inline-flex;
  align-items: center;
  background: rgba(7, 11, 20, 0.85);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-full);
  padding: 3px;
  gap: 2px;
}

.lang-btn {
  background: transparent;
  border: none;
  color: var(--text-secondary);
  font-size: 0.75rem;
  font-weight: 700;
  font-family: var(--font-mono);
  padding: 4px 10px;
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
  box-shadow: 0 2px 8px var(--accent-red-glow);
}

.nav-policy-btn {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 0.82rem;
  font-weight: 700;
  color: #FFFFFF;
  background: rgba(239, 68, 68, 0.15);
  border: 1px solid rgba(239, 68, 68, 0.35);
  padding: 7px 14px;
  border-radius: var(--radius-full);
  transition: all var(--transition-fast);
  white-space: nowrap;
}

.nav-policy-btn:hover {
  background: var(--accent-red);
  color: #FFFFFF;
  box-shadow: 0 4px 14px var(--accent-red-glow);
}

/* --------------------------------------------------------------------------
   Hero Section
   -------------------------------------------------------------------------- */
.hero {
  padding: 68px 0 48px;
  text-align: center;
  position: relative;
}

.hero-pill-badge {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  background: rgba(239, 68, 68, 0.1);
  border: 1px solid rgba(239, 68, 68, 0.28);
  padding: 6px 16px;
  border-radius: var(--radius-full);
  font-size: 0.8rem;
  font-weight: 700;
  color: #FECACA;
  margin-bottom: 24px;
  max-width: 100%;
  line-height: 1.45;
  text-align: center;
}

.pulse-dot {
  width: 8px;
  height: 8px;
  min-width: 8px;
  border-radius: 50%;
  background-color: var(--accent-red);
  box-shadow: 0 0 10px var(--accent-red);
  animation: pulseGlow 2s infinite;
  flex-shrink: 0;
}

@keyframes pulseGlow {
  0% { transform: scale(0.95); opacity: 0.8; }
  50% { transform: scale(1.3); opacity: 1; }
  100% { transform: scale(0.95); opacity: 0.8; }
}

.hero-title {
  font-size: clamp(2.3rem, 5.2vw, 4.2rem);
  font-weight: 900;
  letter-spacing: -0.035em;
  line-height: 1.15;
  color: #FFFFFF;
  margin-bottom: 18px;
  word-break: keep-all;
}

.hero-title .gradient-text {
  background: linear-gradient(135deg, #FFFFFF 20%, #FCA5A5 50%, #EF4444 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.hero-subtitle {
  font-size: clamp(1.02rem, 2vw, 1.2rem);
  color: var(--text-secondary);
  max-width: 760px;
  margin: 0 auto 28px;
  line-height: 1.7;
  word-break: keep-all;
}

.package-pill-wrap {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: rgba(14, 23, 42, 0.7);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-full);
  padding: 6px 14px;
  font-family: var(--font-mono);
  font-size: 0.84rem;
  margin-bottom: 34px;
  max-width: 100%;
  flex-wrap: wrap;
  justify-content: center;
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

/* Stat Ticker Strip */
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
  line-height: 1.35;
  word-break: keep-all;
}

/* --------------------------------------------------------------------------
   ULTRA-CLEAN 2-CARD APP MOCKUP SECTION (#preview)
   Design: Clean Glassmorphism, 3D Spherical Balls, Crisp Metrics, Zero Clutter
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
  word-break: keep-all;
}

.section-desc {
  font-size: 1rem;
  color: var(--text-secondary);
  line-height: 1.7;
  max-width: 680px;
  margin: 0 auto;
  word-break: keep-all;
}

.section-header {
  text-align: center;
  margin-bottom: 44px;
}

/* 2-Card Mockup Grid */
.sim-preview-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 24px;
}

.sim-mockup-card {
  background: linear-gradient(180deg, #111827 0%, #151F32 100%);
  border: 1px solid rgba(148, 163, 184, 0.18);
  border-radius: 18px;
  padding: 26px;
  box-shadow: 0 12px 34px rgba(0, 0, 0, 0.55), 0 1px 0 rgba(255, 255, 255, 0.08) inset;
  display: flex;
  flex-direction: column;
  transition: transform 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease;
  position: relative;
}

.sim-mockup-card:hover {
  transform: translateY(-3px);
  border-color: rgba(239, 68, 68, 0.38);
  box-shadow: 0 16px 42px rgba(0, 0, 0, 0.65), 0 0 24px rgba(239, 68, 68, 0.14);
}

.card-topbar-flex {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 12px;
  margin-bottom: 18px;
  padding-bottom: 12px;
  border-bottom: 1px solid rgba(148, 163, 184, 0.1);
  flex-wrap: wrap;
}

.card-title-group {
  flex: 1 1 200px;
}

.card-title-group h3 {
  font-size: clamp(1.1rem, 2vw, 1.24rem);
  font-weight: 800;
  color: #FFFFFF;
  letter-spacing: -0.015em;
  margin: 0 0 4px;
  word-break: keep-all;
}

.card-title-group .sublabel {
  font-size: 0.72rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--accent-red);
  word-break: keep-all;
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
  padding: 3px 10px;
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

/* Strictly Horizontal 3D Lottery Ball Row (Locked nowrap with clamp scaling) */
.balls-horizontal-row {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: clamp(4px, 1.8vw, 10px);
  flex-wrap: nowrap !important;
  width: 100%;
  margin: 14px 0 22px;
}

.ball-badge {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: clamp(31px, 7.8vw, 40px);
  height: clamp(31px, 7.8vw, 40px);
  min-width: clamp(31px, 7.8vw, 40px);
  border-radius: 999px;
  font-family: var(--font-sans);
  font-size: clamp(0.8rem, 2.1vw, 0.98rem);
  font-weight: 800;
  letter-spacing: -0.02em;
  user-select: none;
  flex-shrink: 0;
  transition: transform 0.15s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.ball-badge:hover {
  transform: scale(1.12);
}

/* White Balls: Crisp 3D sphere gradient with realistic shadow */
.ball-badge.white {
  background: radial-gradient(circle at 35% 32%, #FFFFFF 0%, #F1F5F9 55%, #CBD5E1 100%);
  color: #0F172A;
  border: 1px solid rgba(255, 255, 255, 0.95);
  box-shadow:
    0 4px 10px rgba(0, 0, 0, 0.4),
    inset 0 2px 3px rgba(255, 255, 255, 0.8),
    inset 0 -2px 4px rgba(0, 0, 0, 0.18);
}

/* Red Powerball: Glowing crimson sphere with rich highlight */
.ball-badge.red {
  background: radial-gradient(circle at 35% 32%, #FF6B6B 0%, #EF4444 55%, #B91C1C 100%);
  color: #FFFFFF;
  border: 1px solid rgba(255, 255, 255, 0.55);
  box-shadow:
    0 4px 16px rgba(239, 68, 68, 0.6),
    inset 0 2px 3px rgba(255, 255, 255, 0.6),
    inset 0 -2px 4px rgba(0, 0, 0, 0.3);
}

.ball-divider-symbol {
  color: var(--text-muted);
  font-weight: 800;
  font-size: clamp(0.95rem, 2vw, 1.15rem);
  user-select: none;
  padding: 0 1px;
  flex-shrink: 0;
}

/* 4-Box Summary Tiles */
.metric-summary-grid {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 8px;
  margin-bottom: 18px;
}

.metric-chip {
  background: rgba(14, 23, 42, 0.65);
  border: 1px solid rgba(148, 163, 184, 0.14);
  border-radius: 12px;
  padding: 10px 8px;
  text-align: center;
}

.metric-chip .chip-label {
  display: block;
  font-size: 0.6875rem;
  color: #94A3B8;
  text-transform: uppercase;
  font-weight: 700;
  letter-spacing: 0.04em;
  margin-bottom: 3px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.metric-chip .chip-val {
  display: block;
  font-size: 1.05rem;
  color: #FFFFFF;
  font-weight: 800;
  font-family: var(--font-mono);
  line-height: 1.15;
}

/* Hot / Cold Information Bars */
.hot-cold-container {
  display: flex;
  flex-direction: column;
  gap: 8px;
  padding-top: 14px;
  border-top: 1px solid rgba(148, 163, 184, 0.1);
  margin-bottom: 16px;
}

.hot-cold-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 8px;
  background: rgba(14, 23, 42, 0.5);
  padding: 8px 12px;
  border-radius: 10px;
  border: 1px solid rgba(148, 163, 184, 0.1);
  flex-wrap: wrap;
}

.hot-cold-row .label-tag {
  font-size: 0.74rem;
  font-weight: 700;
  display: flex;
  align-items: center;
  gap: 6px;
  word-break: keep-all;
}

.hot-cold-row .label-tag.hot { color: #F87171; }
.hot-cold-row .label-tag.cold { color: #60A5FA; }

.mini-chips-group {
  display: flex;
  align-items: center;
  gap: 5px;
  flex-shrink: 0;
}

.mini-ball-chip {
  width: 25px;
  height: 25px;
  border-radius: 50%;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-size: 0.72rem;
  font-weight: 800;
  font-family: var(--font-mono);
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

/* Right Card: Filter Pills */
.filter-pills-wrap {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 18px;
}

.filter-pill-tag {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 6px 12px;
  border-radius: 999px;
  font-size: 0.74rem;
  font-weight: 700;
  background: rgba(239, 68, 68, 0.08);
  border: 1px solid rgba(239, 68, 68, 0.28);
  color: #FECACA;
  white-space: nowrap;
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
  padding: 13px clamp(12px, 3vw, 20px);
  background: linear-gradient(135deg, #EF4444 0%, #DC2626 60%, #B91C1C 100%);
  border: 1px solid rgba(255, 255, 255, 0.25);
  border-radius: 999px;
  color: #FFFFFF;
  font-size: clamp(0.78rem, 2.2vw, 0.86rem);
  font-weight: 800;
  letter-spacing: 0.03em;
  text-transform: uppercase;
  cursor: pointer;
  box-shadow: 0 4px 18px rgba(220, 38, 38, 0.45);
  transition: all 0.18s ease;
  margin-bottom: 14px;
  white-space: normal;
  text-align: center;
  line-height: 1.35;
}

.shake-action-btn:hover {
  background: linear-gradient(135deg, #F87171 0%, #EF4444 60%, #DC2626 100%);
  box-shadow: 0 6px 24px rgba(239, 68, 68, 0.65);
  transform: translateY(-2px);
}

.shake-action-btn:active {
  transform: translateY(0);
}

/* Calm Disclaimer Caption at Card Bottom */
.card-disclaimer-caption {
  font-size: 0.74rem;
  color: #94A3B8;
  text-align: center;
  line-height: 1.45;
  margin-top: auto;
  padding-top: 12px;
  border-top: 1px solid rgba(148, 163, 184, 0.1);
  word-break: keep-all;
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
  word-break: keep-all;
}

.step-desc {
  font-size: 0.92rem;
  color: var(--text-secondary);
  line-height: 1.65;
  flex-grow: 1;
  margin-bottom: 18px;
  word-break: keep-all;
}

.step-desc code {
  color: #93C5FD;
  font-family: var(--font-mono);
  font-size: 0.8rem;
}

.step-pill {
  display: inline-flex;
  align-items: center;
  align-self: flex-start;
  font-size: 0.74rem;
  font-family: var(--font-mono);
  font-weight: 700;
  padding: 4px 10px;
  border-radius: var(--radius-full);
  border: 1px solid rgba(59, 130, 246, 0.3);
  color: #93C5FD;
  background: rgba(59, 130, 246, 0.1);
  white-space: nowrap;
}

/* --------------------------------------------------------------------------
   Disclaimer Banner Box (Crucial for Review Safety)
   -------------------------------------------------------------------------- */
.disclaimer-section {
  padding: 24px 0 64px;
}

.disclaimer-box {
  background: rgba(18, 25, 43, 0.88);
  border: 1px solid rgba(239, 68, 68, 0.35);
  border-radius: var(--radius-xl);
  padding: 28px 32px;
  box-shadow: 0 12px 36px rgba(0, 0, 0, 0.4), inset 0 1px 0 rgba(239, 68, 68, 0.2);
  backdrop-filter: blur(12px);
}

.disclaimer-header {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 14px;
  flex-wrap: wrap;
}

.disclaimer-badge {
  font-size: 0.72rem;
  font-family: var(--font-mono);
  font-weight: 800;
  color: #FFFFFF;
  background: var(--accent-red);
  padding: 3px 10px;
  border-radius: var(--radius-full);
  text-transform: uppercase;
  white-space: nowrap;
}

.disclaimer-title {
  font-size: clamp(1.1rem, 2vw, 1.25rem);
  font-weight: 800;
  color: #FFFFFF;
  letter-spacing: -0.015em;
  word-break: keep-all;
}

.disclaimer-text {
  font-size: 0.94rem;
  color: #CBD5E1;
  line-height: 1.7;
  margin-bottom: 12px;
  word-break: keep-all;
}

.disclaimer-text strong {
  color: #FFFFFF;
}

.disclaimer-subtext {
  font-size: 0.85rem;
  color: var(--text-muted);
  line-height: 1.6;
  word-break: keep-all;
}

/* --------------------------------------------------------------------------
   Feature Cards Grid
   -------------------------------------------------------------------------- */
.grid-3 {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 24px;
}

.card {
  background: linear-gradient(180deg, #111827 0%, #162033 100%);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-lg);
  padding: 28px 24px;
  transition: all var(--transition-normal);
  display: flex;
  flex-direction: column;
}

.card:hover {
  border-color: rgba(239, 68, 68, 0.38);
  transform: translateY(-3px);
  box-shadow: 0 14px 34px rgba(0, 0, 0, 0.6);
}

.card-icon {
  width: 48px;
  height: 48px;
  border-radius: var(--radius-md);
  background: rgba(239, 68, 68, 0.12);
  border: 1px solid rgba(239, 68, 68, 0.3);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--accent-red);
  margin-bottom: 18px;
}

.card-title {
  font-size: 1.2rem;
  font-weight: 800;
  color: #FFFFFF;
  margin-bottom: 10px;
  letter-spacing: -0.015em;
  word-break: keep-all;
}

.card-desc {
  font-size: 0.92rem;
  color: var(--text-secondary);
  line-height: 1.65;
  margin-bottom: 16px;
  flex-grow: 1;
  word-break: keep-all;
}

.card-bullet-list {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 8px;
  border-top: 1px solid rgba(255, 255, 255, 0.06);
  padding-top: 14px;
}

.card-bullet-list li {
  font-size: 0.82rem;
  color: var(--text-muted);
  display: flex;
  align-items: flex-start;
  gap: 8px;
  line-height: 1.45;
  word-break: keep-all;
}

.card-bullet-list li::before {
  content: "•";
  color: var(--accent-red);
  font-weight: 800;
  font-size: 1rem;
  line-height: 1.2;
}

/* --------------------------------------------------------------------------
   FAQ Accordion Section
   -------------------------------------------------------------------------- */
.faq-grid {
  display: flex;
  flex-direction: column;
  gap: 14px;
  max-width: 860px;
  margin: 0 auto;
}

.faq-card {
  background: rgba(17, 24, 39, 0.8);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-lg);
  padding: 24px 28px;
  transition: all var(--transition-fast);
}

.faq-card:hover {
  border-color: rgba(239, 68, 68, 0.3);
  background: rgba(22, 32, 51, 0.85);
}

.faq-q {
  font-size: 1.08rem;
  font-weight: 800;
  color: #FFFFFF;
  display: flex;
  align-items: flex-start;
  gap: 12px;
  margin-bottom: 10px;
  letter-spacing: -0.015em;
  word-break: keep-all;
}

.faq-q-num {
  font-family: var(--font-mono);
  color: var(--accent-red);
  font-size: 0.92rem;
  flex-shrink: 0;
  margin-top: 2px;
}

.faq-a {
  font-size: 0.92rem;
  color: var(--text-secondary);
  line-height: 1.65;
  padding-left: 32px;
  word-break: keep-all;
}

.faq-a a {
  color: #60A5FA;
  text-decoration: underline;
  text-underline-offset: 3px;
}

/* --------------------------------------------------------------------------
   Technical Specs Grid
   -------------------------------------------------------------------------- */
.specs-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 16px;
  max-width: 980px;
  margin: 0 auto;
}

.spec-item {
  background: rgba(14, 23, 42, 0.65);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: 16px 20px;
}

.spec-lbl {
  font-size: 0.72rem;
  font-weight: 700;
  color: var(--text-muted);
  text-transform: uppercase;
  margin-bottom: 4px;
  word-break: keep-all;
}

.spec-val {
  font-size: 0.98rem;
  font-weight: 700;
  color: #FFFFFF;
  font-family: var(--font-mono);
}

.spec-sub {
  font-size: 0.75rem;
  color: var(--text-secondary);
  margin-top: 2px;
  word-break: keep-all;
}

/* --------------------------------------------------------------------------
   Footer Section
   -------------------------------------------------------------------------- */
.site-footer {
  margin-top: auto;
  background: #070B14;
  border-top: 1px solid var(--border-subtle);
  padding: 56px 0 36px;
}

.footer-top {
  display: grid;
  grid-template-columns: 2fr 1fr 1.5fr;
  gap: 40px;
  margin-bottom: 40px;
}

.footer-brand-desc {
  font-size: 0.88rem;
  color: var(--text-secondary);
  line-height: 1.65;
  margin-top: 12px;
  max-width: 360px;
  word-break: keep-all;
}

.footer-heading {
  font-size: 0.85rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: #FFFFFF;
  margin-bottom: 14px;
}

.footer-nav-list {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.footer-nav-list a {
  font-size: 0.88rem;
  color: var(--text-secondary);
  transition: color var(--transition-fast);
}

.footer-nav-list a:hover {
  color: #FFFFFF;
}

.contact-card {
  background: rgba(17, 24, 39, 0.7);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: 14px 16px;
}

.contact-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 8px;
  margin-bottom: 8px;
  font-size: 0.85rem;
  flex-wrap: wrap;
}

.contact-row:last-child {
  margin-bottom: 0;
}

.contact-row .label {
  color: var(--text-muted);
  font-weight: 600;
}

.contact-row .val {
  color: #FFFFFF;
  font-family: var(--font-mono);
  font-weight: 700;
}

.contact-row a.val {
  color: #60A5FA;
}

.footer-bottom {
  padding-top: 24px;
  border-top: 1px solid rgba(255, 255, 255, 0.06);
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 12px;
  font-size: 0.8rem;
  color: var(--text-muted);
  word-break: keep-all;
}

/* --------------------------------------------------------------------------
   Responsive Breakpoints
   -------------------------------------------------------------------------- */
@media (max-width: 1040px) {
  .sim-preview-grid { grid-template-columns: 1fr; }
  .workflow-grid { grid-template-columns: 1fr; }
  .grid-3 { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .specs-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .stat-ticker-strip { grid-template-columns: repeat(2, 1fr); }
  .footer-top { grid-template-columns: 1fr 1fr; }
}

@media (max-width: 960px) {
  .nav-links { display: none; }
}

@media (max-width: 868px) {
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
  .metric-summary-grid { grid-template-columns: repeat(2, 1fr); }
  .disclaimer-box { padding: 20px; }
}

@media (max-width: 480px) {
  .card-topbar-flex {
    flex-direction: column;
    align-items: flex-start;
    gap: 8px;
  }
}

@media (max-width: 420px) {
  .container { padding-left: 12px; padding-right: 12px; }
  .site-header { padding: 0 6px; top: 6px; }
  .nav-container { height: 56px; padding: 0 12px; }
  .brand-logo { width: 30px; height: 30px; }
  .brand-title { font-size: 0.92rem; }
  .lang-btn { padding: 4px 7px; font-size: 0.7rem; }
  .nav-policy-btn { display: none; }
  .mini-ball-chip { width: 22px; height: 22px; font-size: 0.68rem; }
}
"""

with open(os.path.join(BASE_DIR, "assets", "css", "style.css"), "w", encoding="utf-8") as f:
    f.write(CSS_CONTENT)

# Update index.html
with open(os.path.join(BASE_DIR, "index.html"), "r", encoding="utf-8") as f:
    html_content = f.read()

import re
updated_html = re.sub(r'<style>.*?</style>', f'<style>\n{CSS_CONTENT}\n  </style>', html_content, flags=re.DOTALL)

with open(os.path.join(BASE_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(updated_html)

print("Successfully regenerated index.html and assets/css/style.css with v4.1 Bulletproof Hardening!")
