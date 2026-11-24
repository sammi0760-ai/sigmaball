import os
import base64

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
LOGO_PATH = os.path.join(BASE_DIR, 'assets', 'images', 'sigmaball-logo.png')

with open(LOGO_PATH, 'rb') as f:
    LOGO_B64 = base64.b64encode(f.read()).decode('utf-8')
LOGO_DATA_URI = f'data:image/png;base64,{LOGO_B64}'

with open(os.path.join(BASE_DIR, 'assets', 'css', 'style.css'), 'r', encoding='utf-8') as f:
    AWWWARDS_CSS = f.read()

PRIVACY_HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Privacy Policy — SigmaBall for Powerball</title>
  
  <meta name="description" content="Privacy Policy for SigmaBall for Powerball (com.sigmaball.app). Learn how device local data, Google AdMob SDK, and public lottery datasets are handled.">
  <meta name="robots" content="index, follow">
  <meta name="author" content="YOUR_ENGLISH_BUSINESS_NAME">

  <!-- Open Graph -->
  <meta property="og:type" content="article">
  <meta property="og:url" content="YOUR_SITE_URL/privacy/sigmaball">
  <meta property="og:title" content="Privacy Policy — SigmaBall for Powerball">
  <meta property="og:description" content="Official Privacy Policy for SigmaBall for Powerball (com.sigmaball.app). 100% on-device data storage, Google AdMob disclosures, and public data source notices.">
  <meta property="og:image" content="{LOGO_DATA_URI}">

  <!-- Favicon -->
  <link rel="icon" type="image/svg+xml" href="../../assets/images/favicon.svg">
  <link rel="alternate icon" type="image/png" href="{LOGO_DATA_URI}">
  <link rel="canonical" href="YOUR_SITE_URL/privacy/sigmaball">

  <!-- Stylesheet -->
  <link rel="stylesheet" href="../../assets/css/style.css">

  <style>
{AWWWARDS_CSS}
  </style>
</head>
<body>

  <!-- Floating Navigation -->
  <header class="site-header">
    <div class="nav-shell">
      <div class="nav-container">
        <a href="../../index.html" class="brand" aria-label="SigmaBall for Powerball Home">
          <img src="{LOGO_DATA_URI}" alt="SigmaBall Logo" class="brand-logo" width="38" height="38">
          <div class="brand-text">
            <span class="brand-title">SigmaBall</span>
            <span class="brand-subtitle">for Powerball</span>
          </div>
        </a>

        <nav aria-label="Primary Navigation">
          <ul class="nav-links">
            <li><a href="../../index.html">Home</a></li>
            <li><a href="../../index.html#preview">Simulator</a></li>
            <li><a href="../../index.html#features">Capabilities</a></li>
            <li><a href="../../index.html#faq">FAQ</a></li>
            <li><a href="#" class="active">Privacy Policy</a></li>
          </ul>
        </nav>

        <a href="../../index.html" class="nav-btn">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m15 18-6-6 6-6"/></svg>
          Back to App Page
        </a>
      </div>
    </div>
  </header>

  <!-- Privacy Policy Content -->
  <main class="policy-wrap">
    <div class="container" style="max-width: 880px;">
      
      <header class="policy-header">
        <div class="hero-pill-badge" style="margin-bottom: 16px;">
          <span class="pulse-dot"></span>
          <span>Legal & Compliance · Play Store Certified</span>
        </div>
        <h1 class="policy-title">Privacy Policy for SigmaBall for Powerball</h1>
        <div class="policy-meta">
          <span><strong>Application:</strong> SigmaBall for Powerball</span>
          <span>&bull;</span>
          <span><strong>Package ID:</strong> <code>com.sigmaball.app</code></span>
          <span>&bull;</span>
          <span><strong>Effective Date:</strong> November 24, 2026</span>
        </div>
      </header>

      <!-- Section 1: Introduction & Identity -->
      <section class="policy-card">
        <h2 class="policy-section-title">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/></svg>
          1. Introduction & Operator Identity
        </h2>
        <div class="policy-content">
          <p>
            This Privacy Policy describes how <strong>YOUR_ENGLISH_BUSINESS_NAME</strong> ("we", "us", or "our") collects, uses, protects, and discloses information in connection with your use of the Android mobile application <strong>SigmaBall for Powerball</strong> (Package Identifier: <code>com.sigmaball.app</code>).
          </p>
          <p>
            SigmaBall for Powerball is an independent statistical analysis and combinatorial number-simulation utility. We uphold a strict <strong>Privacy-by-Design</strong> principle: we do not maintain central user accounts, do not require personal login credentials, and store all user-generated application data solely on your local device.
          </p>
          <div class="policy-highlight-box">
            <strong>Contact for Privacy Matters:</strong><br>
            Entity: <strong>YOUR_ENGLISH_BUSINESS_NAME</strong><br>
            Privacy & Policy Inquiries: <a href="mailto:YOUR_CONTACT_EMAIL">YOUR_CONTACT_EMAIL</a><br>
            Official Website: <a href="YOUR_SITE_URL">YOUR_SITE_URL</a>
          </div>
        </div>
      </section>

      <!-- Section 2: Local Device Data Storage -->
      <section class="policy-card">
        <h2 class="policy-section-title">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="5" y="2" width="14" height="20" rx="2" ry="2"/><line x1="12" y1="18" x2="12.01" y2="18"/></svg>
          2. Local On-Device Data Storage
        </h2>
        <div class="policy-content">
          <p>
            When you use SigmaBall for Powerball, the application creates and manages data entirely on your physical Android device. This includes:
          </p>
          <ul>
            <li><strong>Saved Number Sets:</strong> Combinations generated or manually saved by you.</li>
            <li><strong>Filter Configurations:</strong> Custom statistical boundaries (e.g. odd/even ratios, sum total limits, consecutive number rules).</li>
            <li><strong>User Preferences:</strong> UI theme preferences, motion shake sensitivity settings, and language selection (English, Spanish, Korean).</li>
            <li><strong>Backtesting Results:</strong> Historical simulation records computed against cached public draw results.</li>
          </ul>
          <p>
            <strong>Zero Cloud Transmission:</strong> None of these saved numbers, filter rules, or personal preferences are ever uploaded to, transmitted across, or stored upon external servers owned or operated by us. The data remains strictly inside your device's isolated application sandbox (via Android Room SQLite and SharedPreferences).
          </p>
          <p>
            <strong>Data Eradication:</strong> You can completely and permanently delete all locally stored data at any time by clearing the application storage via <em>Android Settings &rarr; Apps &rarr; SigmaBall &rarr; Storage & Cache &rarr; Clear Storage</em>, or by uninstalling the application.
          </p>
        </div>
      </section>

      <!-- Section 3: Third-Party Advertising & AdMob -->
      <section class="policy-card">
        <h2 class="policy-section-title">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
          3. Advertising & Analytics (Google AdMob SDK)
        </h2>
        <div class="policy-content">
          <p>
            To support free access and ongoing maintenance, SigmaBall for Powerball integrates the <strong>Google AdMob SDK</strong>, an advertising service provided by Google LLC ("Google"). Google AdMob may automatically collect and process certain device and usage data in accordance with Google's Privacy Policy.
          </p>
          <table class="policy-table">
            <thead>
              <tr>
                <th>Data Type</th>
                <th>Purpose</th>
                <th>Collected By</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Advertising ID (AD_ID / GAID)</strong></td>
                <td>Frequency capping, fraud prevention, ad attribution, and interest-based ad personalization (if enabled by the user).</td>
                <td>Google AdMob SDK</td>
              </tr>
              <tr>
                <td><strong>Approximate Location (IP-derived)</strong></td>
                <td>Serving regionally relevant advertisements and respecting geographical advertising laws. Non-precise (city/country level).</td>
                <td>Google AdMob SDK</td>
              </tr>
              <tr>
                <td><strong>Interaction & Diagnostics</strong></td>
                <td>Measuring ad impressions, clicks, render performance, and technical crash telemetry.</td>
                <td>Google AdMob SDK</td>
              </tr>
              <tr>
                <td><strong>Device Information</strong></td>
                <td>Operating system version, device model, screen resolution, and carrier metadata for proper ad rendering.</td>
                <td>Google AdMob SDK</td>
              </tr>
            </tbody>
          </table>

          <p>
            For detailed information on how Google processes, secures, and retains this data, please consult:
          </p>
          <ul>
            <li><a href="https://policies.google.com/privacy" target="_blank" rel="noopener noreferrer">Google Privacy Policy &rarr;</a></li>
            <li><a href="https://policies.google.com/technologies/ads" target="_blank" rel="noopener noreferrer">Google Advertising Technologies &rarr;</a></li>
            <li><a href="https://policies.google.com/technologies/partner-sites" target="_blank" rel="noopener noreferrer">How Google uses information from sites or apps that use our services &rarr;</a></li>
          </ul>

          <h3 style="color: #F8FAFC; font-size: 1.05rem; margin-top: 20px; margin-bottom: 8px;">User Choice & Opt-Out Controls</h3>
          <p>
            Android provides users with native system controls to manage or opt-out of personalized advertising:
          </p>
          <ul>
            <li><strong>Reset or Delete Advertising ID:</strong> On Android devices (Android 12+), navigate to <em>Settings &rarr; Google &rarr; Ads</em>. You can tap <em>"Reset advertising ID"</em> to erase current profiling or <em>"Delete advertising ID"</em> to prevent apps from accessing your advertising identifier entirely.</li>
            <li><strong>Google Ad Settings:</strong> You can also customize your ad personalization preferences via <a href="https://adssettings.google.com" target="_blank" rel="noopener noreferrer">Google Ad Settings</a>.</li>
          </ul>
        </div>
      </section>

      <!-- Section 4: Public Data Source & Disclaimer -->
      <section class="policy-card">
        <h2 class="policy-section-title">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg>
          4. Public Open Data Source & Lottery Disclaimer
        </h2>
        <div class="policy-content">
          <p>
            Historical Powerball draw results displayed in the application are retrieved from open government datasets, specifically:
          </p>
          <ul>
            <li><strong>Source Dataset:</strong> "Lottery Powerball Winning Numbers: Beginning 2010"</li>
            <li><strong>Portal:</strong> State of New York Open Data (<a href="https://data.ny.gov" target="_blank" rel="noopener noreferrer">data.ny.gov</a>)</li>
            <li><strong>Publisher:</strong> New York State Gaming Commission</li>
          </ul>
          
          <div class="policy-highlight-box warning">
            <strong>Non-Affiliation Notice:</strong><br>
            SigmaBall for Powerball is an independent third-party mathematical application. It is <strong>NOT affiliated with, endorsed by, sponsored by, or associated with Powerball, the Multi-State Lottery Association (MUSL), the New York State Gaming Commission, or any official government or lottery agency</strong>.
          </div>

          <p>
            <strong>No Gambling Activity:</strong> SigmaBall does not sell lottery tickets, does not accept wagers, and does not facilitate real-money gambling in any form. All statistical calculations, frequency distributions, and combination simulations are purely educational and analytical. No statistical tool can alter the independent mathematical odds of random lottery drawings.
          </p>
        </div>
      </section>

      <!-- Section 5: Children's Privacy -->
      <section class="policy-card">
        <h2 class="policy-section-title">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
          5. Children's Privacy Protection (COPPA Compliance)
        </h2>
        <div class="policy-content">
          <p>
            Protecting the privacy of young children is paramount. SigmaBall for Powerball is designed as a general utility tool and is not directed at or intended for children under the age of 13 (or under the applicable age of digital consent in your jurisdiction).
          </p>
          <p>
            We do not knowingly solicit, collect, or store personal information from children under 13 years of age. If you believe that a minor has provided information through our services or advertising channels, please contact us immediately at <a href="mailto:YOUR_CONTACT_EMAIL">YOUR_CONTACT_EMAIL</a> so we can take prompt corrective action.
          </p>
        </div>
      </section>

      <!-- Section 6: Data Security & Retention -->
      <section class="policy-card">
        <h2 class="policy-section-title">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
          6. Data Security & Retention
        </h2>
        <div class="policy-content">
          <p>
            Because we do not operate remote user databases or collect personal credentials, the risk of centralized data breaches is eliminated. Your on-device data is secured by the Android operating system's application sandbox, which isolates application data from other software installed on your device.
          </p>
          <p>
            We do not retain user-generated content on any developer-managed infrastructure. Data retention periods for advertising identifiers and diagnostic telemetry handled by Google AdMob are governed directly by Google's data retention standards.
          </p>
        </div>
      </section>

      <!-- Section 7: Rights Under International Regulations -->
      <section class="policy-card">
        <h2 class="policy-section-title">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
          7. Rights Under GDPR, CCPA/CPRA, and Regional Laws
        </h2>
        <div class="policy-content">
          <p>
            Depending on your geographic location (such as the European Economic Area, United Kingdom, or California, USA), you may possess statutory privacy rights including the right to access, rectify, restrict, or erase personal data, or to opt-out of the "sale" or "sharing" of personal data for cross-context behavioral advertising.
          </p>
          <p>
            Because all application combinations and presets exist solely on your physical device, you can exercise your right of erasure immediately at any time by clearing application data or deleting the application. For rights concerning AdMob advertising identifiers, please exercise your device-level opt-out settings as described in Section 3 or contact us directly.
          </p>
        </div>
      </section>

      <!-- Section 8: Changes to This Policy -->
      <section class="policy-card">
        <h2 class="policy-section-title">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>
          8. Changes to This Privacy Policy
        </h2>
        <div class="policy-content">
          <p>
            We may update our Privacy Policy periodically to reflect enhancements to our features, statutory amendments, or evolving Google Play Developer policies. Any modifications will be posted directly to this URL (<code>YOUR_SITE_URL/privacy/sigmaball</code>) with a revised "Effective Date".
          </p>
          <p>
            You are advised to review this page periodically for any changes. Continued use of SigmaBall for Powerball following the posting of updates constitutes your acceptance of the revised terms.
          </p>
        </div>
      </section>

      <!-- Section 9: Contact Information -->
      <section class="policy-card">
        <h2 class="policy-section-title">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
          9. Contact Us
        </h2>
        <div class="policy-content">
          <p>
            If you have questions, feedback, or data requests regarding this Privacy Policy or our privacy practices, please contact us at:
          </p>
          <ul>
            <li><strong>Developer / Business Name:</strong> YOUR_ENGLISH_BUSINESS_NAME</li>
            <li><strong>Support & Policy Email:</strong> <a href="mailto:YOUR_CONTACT_EMAIL">YOUR_CONTACT_EMAIL</a></li>
            <li><strong>Official Website:</strong> <a href="YOUR_SITE_URL">YOUR_SITE_URL</a></li>
            <li><strong>Application:</strong> SigmaBall for Powerball (<code>com.sigmaball.app</code>)</li>
          </ul>
        </div>
      </section>

    </div>
  </main>

  <!-- Site Footer -->
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
            <li><a href="../../index.html">Home</a></li>
            <li><a href="../../index.html#preview">Simulator</a></li>
            <li><a href="../../index.html#features">Capabilities</a></li>
            <li><a href="../../index.html#disclaimer">Disclaimer</a></li>
            <li><a href="#">Privacy Policy</a></li>
            <li><a href="../../app-ads.txt">app-ads.txt</a></li>
          </ul>
        </div>

        <div>
          <div class="footer-col-title">Legal & Contact</div>
          <ul class="footer-links">
            <li><strong style="color: #CBD5E1;">Entity:</strong> <span style="color: #94A3B8;">YOUR_ENGLISH_BUSINESS_NAME</span></li>
            <li><strong style="color: #CBD5E1;">Support:</strong> <a href="mailto:YOUR_CONTACT_EMAIL">YOUR_CONTACT_EMAIL</a></li>
            <li><strong style="color: #CBD5E1;">Website:</strong> <a href="YOUR_SITE_URL">YOUR_SITE_URL</a></li>
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

</body>
</html>"""

with open(os.path.join(BASE_DIR, 'privacy', 'sigmaball', 'index.html'), 'w', encoding='utf-8') as f:
    f.write(PRIVACY_HTML)

with open(os.path.join(BASE_DIR, 'privacy', 'sigmaball.html'), 'w', encoding='utf-8') as f:
    f.write(PRIVACY_HTML)

print("Updated privacy pages with self-contained Awwwards styling")
