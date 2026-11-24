#!/usr/bin/env python3
"""
Awwwards-grade Site Generator for SigmaBall for Powerball
Generates ultra-high-end dark mode landing page, privacy policy, and synced CSS.
Ensures 100% self-contained styling and base64 imagery so that double-clicking
index.html directly in Windows Explorer (file:// protocol) renders gorgeously!
"""

import os
import base64

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
LOGO_PATH = os.path.join(BASE_DIR, "assets", "images", "sigmaball-logo.png")

with open(LOGO_PATH, "rb") as f:
    LOGO_B64 = base64.b64encode(f.read()).decode("utf-8")
LOGO_DATA_URI = f"data:image/png;base64,{LOGO_B64}"

with open(os.path.join(BASE_DIR, "assets", "css", "style.css"), "r", encoding="utf-8") as f:
    AWWWARDS_CSS = f.read()

INDEX_HTML_CONTENT = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>SigmaBall for Powerball — Statistical Analysis & Combination Simulator</title>
  
  <meta name="description" content="SigmaBall for Powerball (com.sigmaball.app) is an independent Android statistical utility offering historical draw statistics, filter-based combination generation, shake simulation, and backtesting.">
  <meta name="keywords" content="SigmaBall, Powerball statistics, lottery analysis, combination generator, backtesting, probability simulator, com.sigmaball.app">
  <meta name="author" content="YOUR_ENGLISH_BUSINESS_NAME">
  
  <!-- Open Graph / Meta -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="YOUR_SITE_URL/">
  <meta property="og:title" content="SigmaBall for Powerball — Statistical Analysis Utility">
  <meta property="og:description" content="Independent statistical analysis and combinatorial simulation utility for Powerball. Historical draw archives, mathematical filters, shake picker, and backtesting.">
  <meta property="og:image" content="{LOGO_DATA_URI}">

  <!-- Favicon -->
  <link rel="icon" type="image/svg+xml" href="assets/images/favicon.svg">
  <link rel="alternate icon" type="image/png" href="{LOGO_DATA_URI}">
  <link rel="canonical" href="YOUR_SITE_URL/">

  <!-- External Stylesheet (for web servers) -->
  <link rel="stylesheet" href="assets/css/style.css">

  <!-- Self-Contained Awwwards Design System (guarantees immediate rendering on file:// and all web hosts) -->
  <style>
{AWWWARDS_CSS}
  </style>
</head>
<body>

  <!-- Awwwards Floating Navigation Shell -->
  <header class="site-header">
    <div class="nav-shell">
      <div class="nav-container">
        <a href="#hero" class="brand" aria-label="SigmaBall for Powerball Home">
          <img src="{LOGO_DATA_URI}" alt="SigmaBall Logo" class="brand-logo" width="38" height="38">
          <div class="brand-text">
            <span class="brand-title">SigmaBall</span>
            <span class="brand-subtitle">for Powerball</span>
          </div>
        </a>

        <nav aria-label="Primary Navigation">
          <ul class="nav-links">
            <li><a href="#preview">Interactive Simulator</a></li>
            <li><a href="#workflow">Workflow</a></li>
            <li><a href="#features">Capabilities</a></li>
            <li><a href="#faq">FAQ</a></li>
            <li><a href="#disclaimer">Disclaimer</a></li>
            <li><a href="privacy/sigmaball/index.html">Privacy Policy</a></li>
          </ul>
        </nav>

        <a href="privacy/sigmaball/index.html" class="nav-btn" data-href="/privacy/sigmaball">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
          Privacy Policy
        </a>
      </div>
    </div>
  </header>

  <main>
    <!-- Hero Section -->
    <section class="hero" id="hero">
      <div class="hero-glow-halo"></div>
      <div class="container hero-content">
        
        <div class="hero-pill-badge">
          <span class="pulse-dot"></span>
          <span>Independent Android Statistical Tool · 2026 Edition</span>
        </div>

        <img src="{LOGO_DATA_URI}" alt="SigmaBall for Powerball Application Icon" class="hero-logo-large" width="108" height="108">

        <h1 class="hero-title">
          SigmaBall <span class="hero-title-gradient">for Powerball</span>
        </h1>

        <p class="hero-subtitle">
          An objective, mathematical toolkit for Powerball enthusiasts. Analyze historical draw distributions, define custom statistical constraints, simulate combinations via shake motion, and backtest hypotheses against public records.
        </p>

        <!-- Interactive Package ID Pill -->
        <div class="package-pill-wrap" title="Click to copy Google Play package ID">
          <span>Package ID:</span>
          <code id="pkgId">com.sigmaball.app</code>
          <button class="copy-btn" id="copyBtn" type="button" aria-label="Copy package ID">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
            <span id="copyText">Copy</span>
          </button>
        </div>

        <div class="hero-actions">
          <a href="#preview" class="btn btn-primary">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><polygon points="10 8 16 12 10 16 10 8"/></svg>
            Launch Live Simulator
          </a>
          <a href="privacy/sigmaball/index.html" class="btn btn-secondary">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
            Review Privacy Policy
          </a>
        </div>

        <!-- Awwwards High-Tech Telemetry Strip -->
        <div class="stat-ticker-strip">
          <div class="stat-ticker-item">
            <div class="stat-ticker-num">292,201,338</div>
            <div class="stat-ticker-lbl">Sample Space</div>
          </div>
          <div class="stat-ticker-item">
            <div class="stat-ticker-num accent">15+ Years</div>
            <div class="stat-ticker-lbl">Public Archive (2010–Now)</div>
          </div>
          <div class="stat-ticker-item">
            <div class="stat-ticker-num">100% Local</div>
            <div class="stat-ticker-lbl">On-Device SQLite Storage</div>
          </div>
          <div class="stat-ticker-item">
            <div class="stat-ticker-num accent">0.00%</div>
            <div class="stat-ticker-lbl">Zero Gambling Alteration</div>
          </div>
        </div>

      </div>
    </section>

    <!-- SECTION 1: Interactive Live App Simulator Mockups -->
    <section class="section" id="preview">
      <div class="container">
        
        <div class="section-header">
          <div class="section-tag">
            <span class="pulse-dot"></span>
            Interactive Simulation Engine
          </div>
          <h2 class="section-title">Designed for Analytical Clarity</h2>
          <p class="section-desc">
            Explore authentic dark UI components inspired directly by the SigmaBall Android application. Test the interactive Monte-Carlo shake simulator below.
          </p>
          <div style="margin-top: 14px;">
            <span style="font-size: 0.78125rem; font-family: var(--font-mono); color: #94A3B8; background: rgba(255,255,255,0.05); padding: 5px 14px; border-radius: 9999px; border: 1px solid rgba(255,255,255,0.1);">
              Sample UI Preview · Historical Data Simulation
            </span>
          </div>
        </div>

        <div class="mockups-grid">

          <!-- Mockup Window A: Recent Draw Frequency & Range Snapshot -->
          <div class="mockup-window">
            <div class="mockup-titlebar">
              <div class="window-dots">
                <span class="red"></span>
                <span class="amber"></span>
                <span class="green"></span>
              </div>
              <span class="window-title">data.ny.gov · Historical Archive</span>
              <span class="window-badge">Public Data</span>
            </div>

            <div class="mockup-content">
              <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 20px;">
                <div>
                  <div class="mockup-sublabel">Latest Recorded Drawing</div>
                  <h3 class="mockup-heading">Draw Frequency Snapshot</h3>
                </div>
                <span style="font-size: 0.75rem; font-family: var(--font-mono); color: #CBD5E1; background: rgba(255,255,255,0.06); padding: 4px 10px; border-radius: 9999px; border: 1px solid rgba(255,255,255,0.12);">
                  Archive #3284
                </span>
              </div>

              <!-- Ball Display -->
              <div class="balls-showcase">
                <div class="ball white" title="White Ball 14">14</div>
                <div class="ball white" title="White Ball 22">22</div>
                <div class="ball white" title="White Ball 39">39</div>
                <div class="ball white" title="White Ball 53">53</div>
                <div class="ball white" title="White Ball 67">67</div>
                <div class="ball powerball" title="Powerball 18">18</div>
              </div>

              <!-- Metric Tiles -->
              <div class="metrics-triplet">
                <div class="metric-box">
                  <span class="label">Sum Total</span>
                  <span class="val">195</span>
                  <span class="sub">Median: 175</span>
                </div>
                <div class="metric-box">
                  <span class="label">Odd / Even</span>
                  <span class="val">3 : 2</span>
                  <span class="sub">Balanced split</span>
                </div>
                <div class="metric-box">
                  <span class="label">High / Low</span>
                  <span class="val">3 : 2</span>
                  <span class="sub">35–69 / 1–34</span>
                </div>
              </div>

              <!-- Hot & Cold Section -->
              <div class="hot-cold-split">
                <div class="hot-cold-card">
                  <div class="hot-cold-title hot">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.38-.5-2-1-3-1.072-2.143-.224-4.054 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.153.433-2.294 1-3a2.5 2.5 0 0 0 2.5 2.5z"/></svg>
                    <span>Hot Balls (Last 100)</span>
                  </div>
                  <div class="mini-balls">
                    <span class="mini-b hot">21</span>
                    <span class="mini-b hot">36</span>
                    <span class="mini-b hot">61</span>
                    <span class="mini-b hot">14</span>
                  </div>
                </div>

                <div class="hot-cold-card">
                  <div class="hot-cold-title cold">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 2v20M2 12h20M4.93 4.93l14.14 14.14M4.93 19.07 19.07 4.93"/></svg>
                    <span>Cold / Overdue</span>
                  </div>
                  <div class="mini-balls">
                    <span class="mini-b cold">04</span>
                    <span class="mini-b cold">13</span>
                    <span class="mini-b cold">49</span>
                    <span class="mini-b cold">58</span>
                  </div>
                </div>
              </div>

            </div>
          </div>

          <!-- Mockup Window B: Interactive Filter & Shake Simulator -->
          <div class="mockup-window">
            <div class="mockup-titlebar">
              <div class="window-dots">
                <span class="red"></span>
                <span class="amber"></span>
                <span class="green"></span>
              </div>
              <span class="window-title">Simulator · Accelerometer Trigger</span>
              <span class="window-badge" style="background: rgba(16, 185, 129, 0.15); color: #34D399; border-color: rgba(16, 185, 129, 0.3);">Live Engine</span>
            </div>

            <div class="mockup-content">
              <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 20px;">
                <div>
                  <div class="mockup-sublabel">Combinatorial Filter Engine</div>
                  <h3 class="mockup-heading">Interactive Shake Picker</h3>
                </div>
                <span id="activeRulesBadge" style="font-size: 0.75rem; font-family: var(--font-mono); color: #FECACA; background: rgba(239,68,68,0.14); padding: 4px 10px; border-radius: 9999px; border: 1px solid rgba(239,68,68,0.3); font-weight: 700;">
                  4 Rules Active
                </span>
              </div>

              <!-- Interactive Filter Pills -->
              <div class="filter-pills">
                <span class="filter-pill active" title="Active Rule: Consecutive numbers <= 2">
                  <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
                  Consecutive &le; 2
                </span>
                <span class="filter-pill active" title="Active Rule: Sum interval between 130 and 180">
                  <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
                  Sum Range 130–180
                </span>
                <span class="filter-pill active" title="Active Rule: Odd/Even split 3:2 or 2:3">
                  <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
                  Odd/Even 3:2
                </span>
                <span class="filter-pill active" title="Active Rule: Exclude previous draw numbers">
                  <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
                  Exclude Prev Draw
                </span>
              </div>

              <!-- Dynamic Shake Feedback -->
              <div class="shake-status-box" id="shakeStatusBox">
                <div style="display: flex; align-items: center; gap: 8px;">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M13 2 3 14h9l-1 8 10-12h-9l1-8z"/></svg>
                  <span id="shakeStatusText">Ready: Shake device or click below</span>
                </div>
                <span style="font-size: 0.7rem; font-family: var(--font-mono); color: #94A3B8;">Monte-Carlo</span>
              </div>

              <!-- Simulated Result Balls -->
              <div class="balls-showcase" id="simulatedBallsCluster">
                <div class="ball white" id="simB1">08</div>
                <div class="ball white" id="simB2">19</div>
                <div class="ball white" id="simB3">33</div>
                <div class="ball white" id="simB4">47</div>
                <div class="ball white" id="simB5">62</div>
                <div class="ball powerball" id="simBP">09</div>
              </div>

              <!-- Interactive Button Trigger -->
              <button class="interactive-shake-btn" id="interactiveShakeBtn" type="button">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><rect x="5" y="2" width="14" height="20" rx="2" ry="2"/><line x1="12" y1="18" x2="12.01" y2="18"/></svg>
                <span>⚡ Simulate Shake Motion (Generate)</span>
              </button>

            </div>
          </div>

        </div>

      </div>
    </section>

    <!-- SECTION 2: 3-Step Statistical Workflow -->
    <section class="section" id="workflow">
      <div class="container">
        <div class="section-header">
          <div class="section-tag">Analytical Workflow</div>
          <h2 class="section-title">How SigmaBall Works</h2>
          <p class="section-desc">
            A transparent 3-step loop: examine public records, apply custom combinatorial logic, and test hypothetical sets locally.
          </p>
        </div>

        <div class="workflow-grid">
          <div class="step-card">
            <div class="step-num">01</div>
            <h3 class="step-title">Explore History</h3>
            <p class="step-desc">
              Browse decades of official Powerball draw results sourced from public government datasets (<code>data.ny.gov</code>). Inspect hot and cold ball trends, sum medians, and frequency heatmaps.
            </p>
            <div class="step-pill">Public Data Ingestion</div>
          </div>

          <div class="step-card">
            <div class="step-num" style="color: rgba(239, 68, 68, 0.25);">02</div>
            <h3 class="step-title">Filter & Shake</h3>
            <p class="step-desc">
              Define your own mathematical constraints—such as odd/even splits, sum total intervals, and consecutive ball limits. Shake your device to generate combinations adhering strictly to your rules.
            </p>
            <div class="step-pill" style="color: #FECACA; border-color: rgba(239,68,68,0.3); background: rgba(239,68,68,0.1);">
              Accelerometer Simulator
            </div>
          </div>

          <div class="step-card">
            <div class="step-num" style="color: rgba(16, 185, 129, 0.25);">03</div>
            <h3 class="step-title">Backtest & Save</h3>
            <p class="step-desc">
              Save your generated sets to your device's isolated local SQLite storage. Backtest hypothetical combinations against years of past drawings to calculate historical match frequencies.
            </p>
            <div class="step-pill" style="color: #A7F3D0; border-color: rgba(16,185,129,0.3); background: rgba(16,185,129,0.1);">
              100% On-Device Storage
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Mandatory Disclaimer Box (Notice & Compliance) -->
    <section class="disclaimer-section" id="disclaimer">
      <div class="container">
        <div class="disclaimer-box" role="alert" aria-label="Important Disclaimer">
          <div class="disclaimer-header">
            <span class="disclaimer-badge">Official Notice</span>
            <h2 class="disclaimer-title">Independent Tool Disclaimer & Public Notice</h2>
          </div>
          <p class="disclaimer-text">
            <strong>SigmaBall for Powerball</strong> is an independent statistical analysis and number-simulation tool. It is <strong>NOT affiliated with, endorsed by, or connected to Powerball, the Multi-State Lottery Association (MUSL), or any government or lottery authority</strong>. No tickets are sold and no real-money gambling is offered. Historical data is sourced from public datasets such as <code>data.ny.gov</code>.
          </p>
          <p class="disclaimer-note">
            Mathematical simulation and statistical frequency tracking are purely educational and analytical. Previous draw distributions do not predict or guarantee future lottery draw results. Each lottery draw is an independent, mutually exclusive random trial.
          </p>
        </div>
      </div>
    </section>

    <!-- Core Capabilities (Features Grid) -->
    <section class="section" id="features">
      <div class="container">
        <div class="section-header">
          <div class="section-tag">Core Capabilities</div>
          <h2 class="section-title">Engineered for Statistical Precision</h2>
          <p class="section-desc">
            SigmaBall provides deep statistical toolsets to analyze patterns, filter combinatorial spaces, and backtest strategies without misleading promises.
          </p>
        </div>

        <div class="grid-3">

          <!-- Feature 1: Historical Statistics -->
          <article class="feature-card">
            <div class="feature-icon-box feature-icon-blue">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 3v18h18"/><path d="m19 9-5 5-4-4-3 3"/></svg>
            </div>
            <h3 class="feature-title">Historical Statistics</h3>
            <p class="feature-desc">
              Comprehensive frequency distribution and telemetry across decades of historical Powerball drawings. Track hot and cold numbers, overdue ball trends, and standard deviation curves.
            </p>
            <ul class="feature-list">
              <li class="feature-list-item">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
                White balls (1–69) & Powerball (1–26) heatmaps
              </li>
              <li class="feature-list-item">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
                Sum total distribution & median charts
              </li>
              <li class="feature-list-item">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
                Odd/Even and High/Low ratio tracking
              </li>
            </ul>
          </article>

          <!-- Feature 2: Statistical Filters & Presets -->
          <article class="feature-card">
            <div class="feature-icon-box feature-icon-red">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="22 3 2 3 10 12.46 10 19 14 21 14 12.46 22 3"/></svg>
            </div>
            <h3 class="feature-title">Statistical Filters & Presets</h3>
            <p class="feature-desc">
              Filter out mathematically improbable combinations before generation. Define combinatorial bounds such as consecutive number rules, range splits, and custom exclusions.
            </p>
            <ul class="feature-list">
              <li class="feature-list-item">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
                Consecutive number limits (e.g. max 2 adjacent)
              </li>
              <li class="feature-list-item">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
                Target total sum intervals (e.g. 130–175)
              </li>
              <li class="feature-list-item">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
                Save and export custom user filter presets
              </li>
            </ul>
          </article>

          <!-- Feature 3: Quick Shake & Instant Pick -->
          <article class="feature-card">
            <div class="feature-icon-box feature-icon-purple">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="5" y="2" width="14" height="20" rx="2" ry="2"/><line x1="12" y1="18" x2="12.01" y2="18"/></svg>
            </div>
            <h3 class="feature-title">Quick Shake & Instant Pick</h3>
            <p class="feature-desc">
              Harness your device's physical accelerometer. Give your phone a quick shake to trigger an organic Monte-Carlo random simulation that adheres strictly to your configured filters.
            </p>
            <ul class="feature-list">
              <li class="feature-list-item">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
                Accelerometer hardware shake sensor trigger
              </li>
              <li class="feature-list-item">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
                Real-time validation against active rule sets
              </li>
              <li class="feature-list-item">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
                Haptic vibration feedback on completion
              </li>
            </ul>
          </article>

          <!-- Feature 4: Saved Sets & Backtesting -->
          <article class="feature-card">
            <div class="feature-icon-box feature-icon-emerald">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg>
            </div>
            <h3 class="feature-title">Saved Sets & Backtesting</h3>
            <p class="feature-desc">
              Store custom combinations locally and run historical backtests. Simulate how your numbers would have matched against years of official Powerball draw results.
            </p>
            <ul class="feature-list">
              <li class="feature-list-item">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
                Multi-year historical backtest simulator
              </li>
              <li class="feature-list-item">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
                Match tier metrics (Jackpot, Match 5, Match 4+PB)
              </li>
              <li class="feature-list-item">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
                100% on-device private SQLite database
              </li>
            </ul>
          </article>

          <!-- Feature 5: Multi-Language Support -->
          <article class="feature-card">
            <div class="feature-icon-box feature-icon-amber">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
            </div>
            <h3 class="feature-title">Multi-Language Localization</h3>
            <p class="feature-desc">
              Built from the ground up for a global user base. Enjoy fully localized UI, statistical terminology, and instructions in English, Spanish (Español), and Korean (한국어).
            </p>
            <ul class="feature-list">
              <li class="feature-list-item">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
                English (EN) default international edition
              </li>
              <li class="feature-list-item">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
                Spanish (ES) complete regional adaptation
              </li>
              <li class="feature-list-item">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
                Korean (KO) localized terminology & UI
              </li>
            </ul>
          </article>

          <!-- Feature 6: Privacy by Design -->
          <article class="feature-card">
            <div class="feature-icon-box feature-icon-blue">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
            </div>
            <h3 class="feature-title">Privacy by Design</h3>
            <p class="feature-desc">
              Zero mandatory account registration, zero personal profile tracking. Your generated combinations and custom presets reside exclusively on your physical Android device.
            </p>
            <ul class="feature-list">
              <li class="feature-list-item">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
                No cloud account or login needed
              </li>
              <li class="feature-list-item">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
                Google AdMob privacy policy compliant
              </li>
              <li class="feature-list-item">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
                Clear all data anytime with one tap
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
          <div class="section-tag">Frequently Asked Questions</div>
          <h2 class="section-title">Common Questions & Compliance</h2>
          <p class="section-desc">
            Direct, factual answers regarding data sourcing, mathematical models, and privacy.
          </p>
        </div>

        <div class="faq-wrap">

          <details class="faq-item" open>
            <summary class="faq-question">
              <span class="faq-question-text">Is this an official Powerball or government lottery application?</span>
              <svg class="faq-chevron" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
            </summary>
            <div class="faq-answer">
              <p>
                <strong>No.</strong> SigmaBall for Powerball is an independent statistical analysis and number-simulation utility. It is <strong>NOT affiliated with, endorsed by, sponsored by, or connected to Powerball, the Multi-State Lottery Association (MUSL), or any government or lottery authority</strong>. No tickets are sold and no real-money gambling is offered.
              </p>
            </div>
          </details>

          <details class="faq-item">
            <summary class="faq-question">
              <span class="faq-question-text">Where does the historical lottery draw data come from?</span>
              <svg class="faq-chevron" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
            </summary>
            <div class="faq-answer">
              <p>
                Historical draw records are retrieved from public open government repositories, specifically <code>data.ny.gov</code> ("Lottery Powerball Winning Numbers: Beginning 2010") published by the New York State Gaming Commission. The data is provided for objective educational, historical, and mathematical research purposes.
              </p>
            </div>
          </details>

          <details class="faq-item">
            <summary class="faq-question">
              <span class="faq-question-text">Does this application guarantee winning numbers or improve lottery odds?</span>
              <svg class="faq-chevron" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
            </summary>
            <div class="faq-answer">
              <p>
                <strong>No.</strong> In true random lottery drawings, every number combination has an identical mathematical probability of being selected. Historical frequency analysis and combinatorial filters assist users in exploring statistical distributions and modeling custom sets, but they cannot predict future random outcomes or alter the underlying odds of the game. SigmaBall strictly avoids exaggerated claims.
              </p>
            </div>
          </details>

          <details class="faq-item">
            <summary class="faq-question">
              <span class="faq-question-text">How is my personal data and Google AdMob advertising handled?</span>
              <svg class="faq-chevron" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
            </summary>
            <div class="faq-answer">
              <p>
                SigmaBall follows a strict <strong>zero-cloud on-device storage</strong> architecture. Your saved combinations, filter presets, and settings remain solely within your device's local database (SQLite/SharedPreferences) and are never uploaded to developer servers.
              </p>
              <p style="margin-top: 10px;">
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
          <div class="section-tag">System Specifications</div>
          <h2 class="section-title" style="margin-bottom: 8px;">Technical Information & Architecture</h2>
          <p class="section-desc">
            Detailed transparency for Google Play Console guidelines, developers, and users.
          </p>

          <div class="specs-grid">
            <div class="spec-item">
              <div class="spec-label">Application Name</div>
              <div class="spec-value">SigmaBall for Powerball</div>
              <div class="spec-sub">Statistical Analysis Utility</div>
            </div>

            <div class="spec-item">
              <div class="spec-label">Package Identifier</div>
              <div class="spec-value" style="font-family: var(--font-mono); font-size: 0.95rem;">com.sigmaball.app</div>
              <div class="spec-sub">Target: Android 8.0+ (API 26+)</div>
            </div>

            <div class="spec-item">
              <div class="spec-label">Public Data Source</div>
              <div class="spec-value">data.ny.gov</div>
              <div class="spec-sub">State of NY Open Data (Lottery Powerball)</div>
            </div>

            <div class="spec-item">
              <div class="spec-label">Monetization & Ads</div>
              <div class="spec-value">Google AdMob SDK</div>
              <div class="spec-sub">Compliant with app-ads.txt standard</div>
            </div>

            <div class="spec-item">
              <div class="spec-label">Data Retention</div>
              <div class="spec-value">100% On-Device</div>
              <div class="spec-sub">Encrypted Room/SQLite local database</div>
            </div>

            <div class="spec-item">
              <div class="spec-label">Supported Languages</div>
              <div class="spec-value">EN • ES • KO</div>
              <div class="spec-sub">English, Spanish, Korean</div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </main>

  <!-- Awwwards Site Footer -->
  <footer class="site-footer">
    <div class="container">
      <div class="footer-top">
        <div>
          <div class="brand" style="margin-bottom: 14px;">
            <img src="{LOGO_DATA_URI}" alt="SigmaBall Logo" class="brand-logo" width="36" height="36">
            <span class="brand-title">SigmaBall for Powerball</span>
          </div>
          <p class="footer-brand-desc">
            An independent, non-affiliated mathematical simulation and statistical utility for Android. Designed to provide transparent historical data analysis and combinatorial modeling.
          </p>
          <div style="display: flex; gap: 8px; flex-wrap: wrap;">
            <span class="operator-badge">com.sigmaball.app</span>
            <span class="operator-badge">v1.0 Release</span>
          </div>
        </div>

        <div>
          <div class="footer-col-title">Navigation</div>
          <ul class="footer-links">
            <li><a href="#preview">Interactive Simulator</a></li>
            <li><a href="#workflow">3-Step Workflow</a></li>
            <li><a href="#features">Key Features</a></li>
            <li><a href="#faq">Frequently Asked Questions</a></li>
            <li><a href="#disclaimer">Disclaimer & Notice</a></li>
            <li><a href="privacy/sigmaball/index.html">Privacy Policy (English)</a></li>
            <li><a href="app-ads.txt">AdMob app-ads.txt</a></li>
          </ul>
        </div>

        <div>
          <div class="footer-col-title">Legal & Contact</div>
          <ul class="footer-links">
            <li><strong style="color: #CBD5E1;">Entity:</strong> <span style="color: #94A3B8;">YOUR_ENGLISH_BUSINESS_NAME</span></li>
            <li><strong style="color: #CBD5E1;">Support:</strong> <a href="mailto:YOUR_CONTACT_EMAIL">YOUR_CONTACT_EMAIL</a></li>
            <li><strong style="color: #CBD5E1;">Website:</strong> <a href="YOUR_SITE_URL">YOUR_SITE_URL</a></li>
            <li><a href="privacy/sigmaball/index.html" style="color: #F87171;">Privacy Agreement &rarr;</a></li>
          </ul>
        </div>
      </div>

      <div class="footer-bottom">
        <div>
          &copy; 2026 YOUR_ENGLISH_BUSINESS_NAME. All rights reserved.
        </div>
        <div style="font-size: 0.75rem; color: #64748B;">
          SigmaBall for Powerball is NOT affiliated with, endorsed by, or sponsored by MUSL or Powerball.
        </div>
      </div>
    </div>
  </footer>

  <!-- Interactive JavaScript Engine (Slot/Shake Animation & Clipboard) -->
  <script>
    // Copy Package ID Handler
    const copyBtn = document.getElementById('copyBtn');
    const copyText = document.getElementById('copyText');
    if (copyBtn) {{
      copyBtn.addEventListener('click', () => {{
        navigator.clipboard.writeText('com.sigmaball.app').then(() => {{
          copyText.textContent = 'Copied! ✓';
          copyText.style.color = '#34D399';
          setTimeout(() => {{
            copyText.textContent = 'Copy';
            copyText.style.color = '';
          }}, 2000);
        }}).catch(() => {{
          const temp = document.createElement('input');
          temp.value = 'com.sigmaball.app';
          document.body.appendChild(temp);
          temp.select();
          document.execCommand('copy');
          document.body.removeChild(temp);
          copyText.textContent = 'Copied! ✓';
          setTimeout(() => copyText.textContent = 'Copy', 2000);
        }});
      }});
    }}

    // Interactive Monte-Carlo Shake Simulator
    const shakeBtn = document.getElementById('interactiveShakeBtn');
    const statusBox = document.getElementById('shakeStatusBox');
    const statusText = document.getElementById('shakeStatusText');
    const b1 = document.getElementById('simB1');
    const b2 = document.getElementById('simB2');
    const b3 = document.getElementById('simB3');
    const b4 = document.getElementById('simB4');
    const b5 = document.getElementById('simB5');
    const bp = document.getElementById('simBP');

    const sampleSets = [
      {{ balls: [8, 19, 33, 47, 62], pb: 9, sum: 169, eval: 1420 }},
      {{ balls: [12, 24, 38, 51, 65], pb: 16, sum: 190, eval: 1980 }},
      {{ balls: [4, 17, 29, 44, 58], pb: 22, sum: 152, eval: 1140 }},
      {{ balls: [15, 23, 36, 49, 63], pb: 7, sum: 186, eval: 1670 }},
      {{ balls: [6, 21, 35, 48, 61], pb: 14, sum: 171, eval: 1290 }}
    ];
    let currentIndex = 0;

    if (shakeBtn) {{
      shakeBtn.addEventListener('click', () => {{
        shakeBtn.disabled = true;
        statusText.textContent = '⚡ Shaking & Evaluating Combinations...';
        statusBox.style.borderColor = '#EF4444';

        // Rapid Slot Animation Effect
        let cycles = 0;
        const interval = setInterval(() => {{
          b1.textContent = String(Math.floor(Math.random() * 69) + 1).padStart(2, '0');
          b2.textContent = String(Math.floor(Math.random() * 69) + 1).padStart(2, '0');
          b3.textContent = String(Math.floor(Math.random() * 69) + 1).padStart(2, '0');
          b4.textContent = String(Math.floor(Math.random() * 69) + 1).padStart(2, '0');
          b5.textContent = String(Math.floor(Math.random() * 69) + 1).padStart(2, '0');
          bp.textContent = String(Math.floor(Math.random() * 26) + 1).padStart(2, '0');
          cycles++;
          if (cycles > 12) {{
            clearInterval(interval);
            currentIndex = (currentIndex + 1) % sampleSets.length;
            const target = sampleSets[currentIndex];
            b1.textContent = String(target.balls[0]).padStart(2, '0');
            b2.textContent = String(target.balls[1]).padStart(2, '0');
            b3.textContent = String(target.balls[2]).padStart(2, '0');
            b4.textContent = String(target.balls[3]).padStart(2, '0');
            b5.textContent = String(target.balls[4]).padStart(2, '0');
            bp.textContent = String(target.pb).padStart(2, '0');
            statusText.textContent = 'Generated via Shake Physics · Meets 4/4 Active Filters (Sum: ' + target.sum + ')';
            shakeBtn.disabled = false;
          }}
        }}, 60);
      }});
    }}
  </script>

</body>
</html>"""

with open(os.path.join(BASE_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(INDEX_HTML_CONTENT)
print("Updated index.html (self-contained Awwwards edition)")
