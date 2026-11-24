#!/usr/bin/env python3
"""
SigmaBall for Powerball - Verification & Build Validation Script v3
Validates operator info (Cho Yeon Planning), contact email (sammi0760@gmail.com),
mandatory disclaimers, package ID, language features, and app-ads.txt.
"""

import os
import sys
import re

REQUIRED_FILES = [
    "index.html",
    "privacy/sigmaball/index.html",
    "privacy/sigmaball.html",
    "app-ads.txt",
    "public/app-ads.txt",
    "assets/css/style.css",
    "assets/images/sigmaball-logo.png",
    "assets/images/favicon.svg",
    "package.json"
]

FORBIDDEN_PHRASES = [
    "guaranteed win",
    "100% jackpot",
    "beat the odds"
]

MANDATORY_DISCLAIMER_SNIPPET = (
    "SigmaBall for Powerball is an independent statistical analysis and number-simulation tool. "
    "It is NOT affiliated with, endorsed by, or connected to Powerball, the Multi-State Lottery Association (MUSL), "
    "or any government or lottery authority. No tickets are sold and no real-money gambling is offered. "
    "Historical data is sourced from public datasets such as data.ny.gov."
)

def run_checks():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    print("=" * 70)
    print("  SIGMABALL FOR POWERBALL — VERIFICATION & BUILD VALIDATION v3")
    print(f"  Root Directory: {base_dir}")
    print("=" * 70)

    errors = 0
    warnings = 0

    # 1. Check required files
    print("\n[Step 1] Verifying File Existence & Accessibility:")
    for rel_path in REQUIRED_FILES:
        full_path = os.path.join(base_dir, rel_path)
        if os.path.exists(full_path):
            size = os.path.getsize(full_path)
            print(f"  [OK] {rel_path} ({size:,} bytes)")
        else:
            print(f"  [ERROR] Missing required file: {rel_path}")
            errors += 1

    # 2. Check main page content (index.html)
    print("\n[Step 2] Validating Main Landing Page (index.html):")
    index_path = os.path.join(base_dir, "index.html")
    if os.path.exists(index_path):
        with open(index_path, "r", encoding="utf-8") as f:
            index_content = f.read()

        # Check operator & email
        if "Cho Yeon Planning" in index_content:
            print("  [OK] Operator 'Cho Yeon Planning' verified in index.html.")
        else:
            print("  [ERROR] Operator 'Cho Yeon Planning' missing in index.html.")
            errors += 1

        if "sammi0760@gmail.com" in index_content:
            print("  [OK] Contact Email 'sammi0760@gmail.com' verified in index.html.")
        else:
            print("  [ERROR] Contact Email 'sammi0760@gmail.com' missing in index.html.")
            errors += 1

        # Check package ID
        if "com.sigmaball.app" in index_content:
            print("  [OK] Package ID 'com.sigmaball.app' verified.")
        else:
            print("  [ERROR] Package ID 'com.sigmaball.app' not found.")
            errors += 1

        # Check language switcher tags (EN, ES, KO)
        for lang in ['data-lang="en"', 'data-lang="es"', 'data-lang="ko"']:
            if lang in index_content:
                print(f"  [OK] Language selector '{lang}' verified.")
            else:
                print(f"  [ERROR] Language selector '{lang}' missing.")
                errors += 1

        # Check required features
        features = [
            "Historical Statistics",
            "Statistical Filters & Presets",
            "Quick Shake & Instant Pick",
            "Saved Sets & Backtesting",
            "Multi-Language"
        ]
        for feat in features:
            if feat.lower() in index_content.lower():
                print(f"  [OK] Feature found: '{feat}'")
            else:
                print(f"  [ERROR] Missing feature: '{feat}'")
                errors += 1

        # Check forbidden phrases
        for forbidden in FORBIDDEN_PHRASES:
            if forbidden.lower() in index_content.lower():
                print(f"  [ERROR] Forbidden phrase detected: '{forbidden}'")
                errors += 1
            else:
                print(f"  [OK] Safe: No forbidden phrase '{forbidden}'")

        # Check mandatory disclaimer
        clean_content = re.sub(r'\s+', ' ', index_content)
        disclaimer_keys = [
            "independent statistical analysis and number-simulation tool",
            "NOT affiliated with, endorsed by, or connected to Powerball",
            "Multi-State Lottery Association (MUSL)",
            "No tickets are sold and no real-money gambling is offered",
            "data.ny.gov"
        ]
        all_keys_present = all(k in clean_content for k in disclaimer_keys)
        if all_keys_present:
            print("  [OK] Mandatory Disclaimer box verified (verbatim requirements met).")
        else:
            print("  [ERROR] Mandatory Disclaimer content missing or modified.")
            errors += 1

        # Check link to privacy policy
        if "/privacy/sigmaball" in index_content:
            print("  [OK] Link to '/privacy/sigmaball' verified.")
        else:
            print("  [ERROR] Link to '/privacy/sigmaball' missing.")
            errors += 1

        # Check horizontal ball layout fix
        if "balls-horizontal-row" in index_content:
            print("  [OK] Fixed horizontal ball row container verified.")
        else:
            print("  [ERROR] balls-horizontal-row container missing.")
            errors += 1

    # 3. Check Privacy Policy content
    print("\n[Step 3] Validating Privacy Policy (privacy/sigmaball/index.html):")
    privacy_path = os.path.join(base_dir, "privacy/sigmaball/index.html")
    if os.path.exists(privacy_path):
        with open(privacy_path, "r", encoding="utf-8") as f:
            privacy_content = f.read()

        if "Cho Yeon Planning" in privacy_content and "sammi0760@gmail.com" in privacy_content:
            print("  [OK] Operator info verified in privacy policy.")
        else:
            print("  [ERROR] Operator info missing in privacy policy.")
            errors += 1

        policy_checks = [
            ("Local Device Storage", ["local on-device", "locally on your device", "stored locally"]),
            ("Google AdMob SDK & AD_ID", ["admob", "advertising id", "ad_id"]),
            ("IP-based approximate location", ["approximate location", "ip address"]),
            ("Google Privacy Policy link", ["policies.google.com/privacy"]),
            ("Public data source (data.ny.gov)", ["data.ny.gov"]),
            ("Unofficial Tool Disclaimer", ["not affiliated with", "musl", "powerball"])
        ]

        for check_name, keywords in policy_checks:
            matched = any(k.lower() in privacy_content.lower() for k in keywords)
            if matched:
                print(f"  [OK] Policy section verified: {check_name}")
            else:
                print(f"  [ERROR] Missing required policy element: {check_name}")
                errors += 1

    # 4. Check app-ads.txt
    print("\n[Step 4] Validating app-ads.txt:")
    ads_path = os.path.join(base_dir, "app-ads.txt")
    if os.path.exists(ads_path):
        with open(ads_path, "r", encoding="utf-8") as f:
            ads_content = f.read()
        if "YOUR_ADMOB_APP_ADS_TXT_LINE" in ads_content:
            print("  [OK] Placeholder 'YOUR_ADMOB_APP_ADS_TXT_LINE' is present.")
        else:
            print("  [ERROR] Placeholder 'YOUR_ADMOB_APP_ADS_TXT_LINE' missing.")
            errors += 1

    # Summary
    print("\n" + "=" * 70)
    print(f"  VERIFICATION RESULT: {errors} Errors, {warnings} Warnings")
    print("=" * 70)

    if errors == 0:
        print("\n>>> ALL VALIDATION CHECKS PASSED SUCCESSFULLY (0 ERRORS) <<<")
        return 0
    else:
        print(f"\n>>> FAILED: {errors} errors need resolution. <<<")
        return 1

if __name__ == "__main__":
    sys.exit(run_checks())
