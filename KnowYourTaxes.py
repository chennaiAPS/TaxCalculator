"""
============================================================
  INDIAN INCOME TAX CALCULATOR (FY 2025-2026 / AY 2026-2027 / TA 2026-2027)
  Supports: New Tax Regime & Old Tax Regime
  Recommendation: Since I will calculate tax for both regimes, I will recommend the one with lower tax liability.
============================================================

Author      : Anantha Padmanabhan Sethurman (APS)
Date        : 02/April/2026
Revision    : 1.0
About me    :This program is designed to help Indian taxpayers understand their income tax liability under both the Old and New Tax Regimes for the financial year 2025-26 (assessment year 2026-27).
Help File   : Refer Readme.md for detailed instructions on how to use this program and explanations of the tax rules & slabs.
"""

# ─────────────────────────────────────────────────────────
# HELPER FUNCTIONS
# ─────────────────────────────────────────────────────────

def format_inr(amount):
    """
    Format a number as Indian Rupees with commas (e.g. 1,50,000).
    Indian numbering uses commas after every 2 digits beyond the first 3.
    """
    amount = round(amount)
    is_negative = amount < 0
    amount = abs(amount)
    s = str(amount)

    # Insert commas in Indian format
    if len(s) > 3:
        last3 = s[-3:]
        rest = s[:-3]
        rest_with_commas = ""
        for i, ch in enumerate(reversed(rest)):
            if i > 0 and i % 2 == 0:
                rest_with_commas = "," + rest_with_commas
            rest_with_commas = ch + rest_with_commas
        s = rest_with_commas + "," + last3

    return ("- " if is_negative else "") + "₹ " + s


def get_positive_float(prompt, default=0.0, max_val=None):
    """
    Prompt the user for a non-negative number.
    Press Enter to accept the default value shown.
    Keeps asking until a valid number is entered.
    """
    while True:
        raw = input(f"{prompt} [default: {format_inr(default)}]: ").strip()
        if raw == "":
            return default
        try:
            val = float(raw)
            if val < 0:
                print("  ⚠ Please enter a value of 0 or more.")
                continue
            if max_val is not None and val > max_val:
                print(f"  ⚠ Maximum allowed is {format_inr(max_val)}. Capping to that.")
                return float(max_val)
            return val
        except ValueError:
            print("  ⚠ Invalid input. Please enter a number (e.g. 500000).")


def get_yes_no(prompt, default="y"):
    """
    Ask a Yes/No question.
    Returns True for Yes, False for No.
    """
    hint = "[Y/n]" if default == "y" else "[y/N]"
    while True:
        raw = input(f"{prompt} {hint}: ").strip().lower()
        if raw == "":
            return default == "y"
        if raw in ("y", "yes"):
            return True
        if raw in ("n", "no"):
            return False
        print("  ⚠ Please type Y or N.")


def get_choice(prompt, choices):
    """
    Let the user pick one option from a numbered list.
    Returns the chosen item from the list.
    """
    for i, ch in enumerate(choices, 1):
        print(f"  {i}. {ch}")
    while True:
        raw = input(f"{prompt} (enter number): ").strip()
        try:
            idx = int(raw) - 1
            if 0 <= idx < len(choices):
                return choices[idx]
            print(f"  ⚠ Please enter a number between 1 and {len(choices)}.")
        except ValueError:
            print("  ⚠ Please enter a number.")


def print_section(title):
    """Print a styled section header."""
    print()
    print("─" * 60)
    print(f"  {title}")
    print("─" * 60)


def print_table_row(label, value, indent=2, width=45):
    """Print a formatted two-column row."""
    label_str = " " * indent + label
    print(f"{label_str:<{width}} {value}")


def print_line(char="─", length=60):
    print(char * length)


# ─────────────────────────────────────────────────────────
# STEP 1: COLLECT PERSONAL DETAILS
# ─────────────────────────────────────────────────────────

def collect_personal_details():
    """
    Collect the taxpayer's personal details.
    Age determines the basic exemption limit in the Old Regime.
    """
    print_section("PERSONAL DETAILS")
    print("""
  Age determines your basic exemption limit in the Old Regime:
    Below 60 (General)      → Exempt up to ₹2,50,000
    60–79  (Senior Citizen) → Exempt up to ₹3,00,000
    80+    (Super Senior)   → Exempt up to ₹5,00,000
    """)

    print("  Select your age category:")
    age_category = get_choice("Your age group", [
        "Below 60 (General)",
        "60-79 (Senior Citizen)",
        "80+ (Super Senior Citizen)"
    ])

    name = input("\n  Your name (optional, for the report): ").strip() or "Taxpayer"
    return name, age_category


# ─────────────────────────────────────────────────────────
# STEP 2: COLLECT INCOME DETAILS
# ─────────────────────────────────────────────────────────

def collect_income_details():
    """
    Collect all income sources.

    In India, income is taxed under five heads:
    1. Salaries
    2. Income from House Property
    3. Profits/Gains from Business or Profession
    4. Capital Gains
    5. Income from Other Sources
    """
    print_section("INCOME DETAILS (Annual amounts in ₹)")
    print("""
  Enter your annual (yearly) income from all sources.
  Leave blank and press Enter to use the default or skip (0).
    """)

    print("  ── Salary Income ──")
    basic       = get_positive_float("  Basic Salary + Dearness Allowance (DA)")
    hra_recv    = get_positive_float("  HRA Received from employer")
    other_allow = get_positive_float("  Other Allowances (LTA, Special Allowance, etc.)")
    bonus       = get_positive_float("  Bonus / Incentive / Performance Pay")

    print("\n  ── Property Income ──")
    rental_income = get_positive_float("  Rental Income from let-out property (gross rent)")

    print("\n  ── Income from Other Sources ──")
    interest_income = get_positive_float("  Interest Income (Savings, FD, RD, bonds)")
    other_income    = get_positive_float("  Any other income (freelance, gifts, etc.)")

    return {
        "basic":          basic,
        "hra_recv":       hra_recv,
        "other_allow":    other_allow,
        "bonus":          bonus,
        "rental_income":  rental_income,
        "interest_income":interest_income,
        "other_income":   other_income,
    }


# ─────────────────────────────────────────────────────────
# STEP 3: COLLECT OLD REGIME DEDUCTIONS
# ─────────────────────────────────────────────────────────

def collect_old_regime_deductions(income, age_category):
    """
    Collect deductions applicable ONLY under the Old Tax Regime.

    The Old Regime allows many deductions & exemptions that reduce
    your taxable income. The New Regime does NOT allow these
    (except the ₹75,000 standard deduction for salaried employees).
    """
    print_section("OLD REGIME — DEDUCTIONS & EXEMPTIONS")
    print("""
  These deductions ONLY apply to the Old Tax Regime.
  The program will ask you which ones apply to you.
    """)

    deductions = {}
    ded_labels  = {}

    # ── Standard Deduction ────────────────────────────────
    # Every salaried employee automatically gets this. No proof needed.
    std_ded = 50000
    deductions["standard_deduction"] = std_ded
    ded_labels["standard_deduction"] = "Standard Deduction (auto)"
    print(f"  ✓ Standard Deduction of {format_inr(std_ded)} applied automatically for salaried employees.")

    # ── HRA Exemption ─────────────────────────────────────
    # HRA received from employer is NOT fully taxable.
    # Exempt portion = Minimum of:
    #   a) Actual HRA received
    #   b) 50% of Basic+DA (metro) or 40% of Basic+DA (non-metro)
    #   c) Rent paid – 10% of Basic+DA
    print("\n  ── House Rent Allowance (HRA) Exemption [Section 10(13A)] ──")
    print("""
  HRA Exemption is the MINIMUM of three values:
    (a) Actual HRA received
    (b) 50% of Basic+DA (if metro city) or 40% (non-metro)
    (c) Actual rent paid minus 10% of Basic+DA
  Metro cities: Delhi, Mumbai, Kolkata, Chennai
    """)

    if income["hra_recv"] > 0 and get_yes_no("  Do you pay rent and want to claim HRA exemption?"):
        rent_paid = get_positive_float("  Rent paid per year (₹)")
        print("  Is your city a metro (Delhi/Mumbai/Kolkata/Chennai)?")
        is_metro = get_yes_no("  Metro city?")

        basic_da = income["basic"]
        city_pct = 0.50 if is_metro else 0.40
        hra_a = income["hra_recv"]
        hra_b = city_pct * basic_da
        hra_c = max(0, rent_paid - 0.10 * basic_da)
        hra_exempt = min(hra_a, hra_b, hra_c)

        print(f"""
  HRA Exemption Calculation:
    (a) Actual HRA received          = {format_inr(hra_a)}
    (b) {int(city_pct*100)}% of Basic+DA ({"metro" if is_metro else "non-metro"})  = {format_inr(hra_b)}
    (c) Rent paid – 10% of Basic+DA  = {format_inr(hra_c)}
    Minimum (a, b, c) = Exempt HRA   = {format_inr(hra_exempt)}
        """)

        deductions["hra_exemption"] = hra_exempt
        ded_labels["hra_exemption"] = "HRA Exemption [Sec 10(13A)]"
    else:
        deductions["hra_exemption"] = 0

    # ── Section 80C ───────────────────────────────────────
    # Investments in specified instruments reduce taxable income.
    # Limit: ₹1,50,000 per year.
    # Includes: EPF, PPF, ELSS Mutual Funds, NSC, LIC Premium,
    #           Home Loan Principal, Sukanya Samriddhi, Tuition Fees
    print("  ── Section 80C (Investments & Payments) ──")
    print("""
  Eligible investments (combined limit: ₹1,50,000):
    • EPF/VPF/PPF contributions
    • ELSS Mutual Fund investments
    • Life Insurance (LIC) premiums
    • NSC (National Savings Certificate)
    • 5-year bank/post office FD
    • Home loan principal repayment
    • Children's tuition fees (up to 2 children)
    • Sukanya Samriddhi Yojana
    """)

    if get_yes_no("  Do you have 80C investments?", "y"):
        sec80c = get_positive_float("  Total 80C investment amount (₹)", 0, max_val=150000)
        deductions["sec_80c"] = sec80c
        ded_labels["sec_80c"] = "Section 80C"
    else:
        deductions["sec_80c"] = 0

    # ── Section 80D ───────────────────────────────────────
    # Health insurance premium deduction.
    # Limit (self+family): ₹25,000 (₹50,000 if self is senior citizen)
    # Additional for parents: ₹25,000 (₹50,000 if parents are senior)
    is_senior = age_category != "Below 60 (General)"
    max_self = 50000 if is_senior else 25000
    print("  ── Section 80D (Health Insurance Premium) ──")
    print(f"""
  Health insurance premium deduction:
    For self + family    : up to {format_inr(max_self)}
    For parents          : up to ₹25,000 (₹50,000 if parents are senior)
    Preventive health check-up: up to ₹5,000 (included in above limits)
    """)

    if get_yes_no("  Do you pay health insurance premiums?"):
        sec80d = get_positive_float("  Total health insurance premium paid (₹)", 0, max_val=max_self)
        deductions["sec_80d"] = sec80d
        ded_labels["sec_80d"] = "Section 80D (Health Insurance)"
    else:
        deductions["sec_80d"] = 0

    # ── Section 80CCD(1B) — NPS ───────────────────────────
    # Additional NPS contribution over and above the 80C limit.
    # This is an EXTRA ₹50,000 deduction, not part of the ₹1.5L 80C limit.
    print("  ── Section 80CCD(1B) — NPS Additional Contribution ──")
    print("""
  Self-contribution to National Pension System (NPS) Tier 1.
  This is OVER AND ABOVE the ₹1,50,000 limit of Section 80C.
  Additional deduction limit: ₹50,000
    """)

    if get_yes_no("  Do you contribute to NPS (Tier 1)?"):
        nps = get_positive_float("  NPS self-contribution amount (₹)", 0, max_val=50000)
        deductions["nps_80ccd1b"] = nps
        ded_labels["nps_80ccd1b"] = "Section 80CCD(1B) NPS"
    else:
        deductions["nps_80ccd1b"] = 0

    # ── Section 80TTA / 80TTB ─────────────────────────────
    # 80TTA: Savings account interest deduction for non-seniors (limit ₹10,000)
    # 80TTB: For senior citizens, all interest income up to ₹50,000
    print("  ── Section 80TTA / 80TTB — Interest Income Deduction ──")
    if is_senior:
        max_tta = min(income["interest_income"], 50000)
        print(f"""
  80TTB (Senior Citizens): Deduction on ALL interest income
  (savings + FD + RD + post office) up to ₹50,000.
  Your interest income: {format_inr(income['interest_income'])}
  Maximum eligible deduction: {format_inr(max_tta)}
        """)
        if income["interest_income"] > 0 and get_yes_no("  Claim 80TTB?"):
            deductions["int_ded"] = max_tta
            ded_labels["int_ded"] = "Section 80TTB (Senior Int. Deduction)"
        else:
            deductions["int_ded"] = 0
    else:
        max_tta = min(income["interest_income"], 10000)
        print(f"""
  80TTA (General): Deduction on savings account interest only, up to ₹10,000.
  Your interest income: {format_inr(income['interest_income'])}
  Maximum eligible deduction: {format_inr(max_tta)}
        """)
        if income["interest_income"] > 0 and get_yes_no("  Claim 80TTA?"):
            deductions["int_ded"] = max_tta
            ded_labels["int_ded"] = "Section 80TTA (Savings Int. Deduction)"
        else:
            deductions["int_ded"] = 0

    # ── Section 24(b) — Home Loan Interest ───────────────
    # Interest paid on home loan for self-occupied property.
    # Limit: ₹2,00,000 per year.
    # (For let-out property, there's no cap but losses have restrictions.)
    print("  ── Section 24(b) — Home Loan Interest ──")
    print("""
  Interest component of your home loan EMI for a self-occupied house.
  Deduction limit: ₹2,00,000 per year.
  Note: Loan must be for purchase/construction/repair of residential property.
    """)

    if get_yes_no("  Do you pay home loan EMI and want to claim interest deduction?"):
        hl_int = get_positive_float("  Home loan interest paid this year (₹)", 0, max_val=200000)
        deductions["home_loan_int"] = hl_int
        ded_labels["home_loan_int"] = "Section 24(b) Home Loan Interest"
    else:
        deductions["home_loan_int"] = 0

    # ── 30% Standard Deduction on Rental Income ──────────
    # If you have rental income, 30% of it is deducted as a flat
    # standard deduction for repairs/maintenance (no bills needed).
    if income["rental_income"] > 0:
        rental_std_ded = income["rental_income"] * 0.30
        deductions["rental_std_ded"] = rental_std_ded
        ded_labels["rental_std_ded"] = "30% Std Ded on Rental Income [Sec 24(a)]"
        print(f"\n  ✓ 30% standard deduction on rental income auto-applied: {format_inr(rental_std_ded)}")

    # ── Section 80G — Donations ───────────────────────────
    # Donations to approved charitable institutions.
    # 100% or 50% deduction depending on the institution.
    # Enter only the eligible portion (i.e. 100% or 50% of actual donation).
    print("\n  ── Section 80G — Donations to Charitable Institutions ──")
    print("""
  Donations to notified funds/trusts are deductible.
    • 100% deduction: PM Relief Fund, National Defence Fund, etc.
    • 50%  deduction: Other approved charities
  Enter only the eligible portion:
    e.g. if you donated ₹10,000 to a 50% eligible charity, enter ₹5,000.
    """)

    if get_yes_no("  Do you have eligible donations under 80G?"):
        donation = get_positive_float("  Eligible donation deduction amount (₹)")
        deductions["donations_80g"] = donation
        ded_labels["donations_80g"] = "Section 80G Donations"
    else:
        deductions["donations_80g"] = 0

    # ── Section 80E — Education Loan Interest ─────────────
    # Interest on education loan for self/spouse/children.
    # No upper limit! Deductible for 8 years from start of repayment.
    print("  ── Section 80E — Education Loan Interest ──")
    print("""
  Interest paid on loans taken for higher education (self, spouse, children).
  No upper limit — the entire interest amount is deductible.
  Applicable for a maximum of 8 consecutive years.
    """)

    if get_yes_no("  Do you pay education loan interest?"):
        edu_int = get_positive_float("  Education loan interest paid this year (₹)")
        deductions["edu_loan_80e"] = edu_int
        ded_labels["edu_loan_80e"] = "Section 80E Education Loan Interest"
    else:
        deductions["edu_loan_80e"] = 0

    return deductions, ded_labels


# ─────────────────────────────────────────────────────────
# STEP 4: COMPUTE TAX SLABS
# ─────────────────────────────────────────────────────────

def compute_tax_slabs(taxable_income, regime, age_category):
    """
    Compute tax using the applicable slab rates.

    NEW REGIME (FY 2025-26) — same slabs for all ages:
      ₹0       – ₹4,00,000   →  0%
      ₹4,00,001 – ₹8,00,000  →  5%
      ₹8,00,001 – ₹12,00,000 → 10%
      ₹12,00,001 – ₹16,00,000→ 15%
      ₹16,00,001 – ₹20,00,000→ 20%
      ₹20,00,001 – ₹24,00,000→ 25%
      Above ₹24,00,000        → 30%

    OLD REGIME — slabs depend on age:
      General (below 60):
        ₹0        – ₹2,50,000  →  0%
        ₹2,50,001 – ₹5,00,000  →  5%
        ₹5,00,001 – ₹10,00,000 → 20%
        Above ₹10,00,000        → 30%
      Senior (60-79):
        ₹0        – ₹3,00,000  →  0%
        ₹3,00,001 – ₹5,00,000  →  5%
        ₹5,00,001 – ₹10,00,000 → 20%
        Above ₹10,00,000        → 30%
      Super Senior (80+):
        ₹0        – ₹5,00,000  →  0%
        ₹5,00,001 – ₹10,00,000 → 20%
        Above ₹10,00,000        → 30%
    """
    if regime == "new":
        slabs = [
            (0,         400000,   0.00),
            (400000,    800000,   0.05),
            (800000,   1200000,   0.10),
            (1200000,  1600000,   0.15),
            (1600000,  2000000,   0.20),
            (2000000,  2400000,   0.25),
            (2400000,  float("inf"), 0.30),
        ]
    else:  # old
        if age_category == "80+ (Super Senior Citizen)":
            slabs = [
                (0,        500000,  0.00),
                (500000,  1000000,  0.20),
                (1000000, float("inf"), 0.30),
            ]
        elif age_category == "60-79 (Senior Citizen)":
            slabs = [
                (0,        300000,  0.00),
                (300000,   500000,  0.05),
                (500000,  1000000,  0.20),
                (1000000, float("inf"), 0.30),
            ]
        else:  # general
            slabs = [
                (0,        250000,  0.00),
                (250000,   500000,  0.05),
                (500000,  1000000,  0.20),
                (1000000, float("inf"), 0.30),
            ]

    total_tax = 0
    slab_details = []

    for (lower, upper, rate) in slabs:
        if taxable_income <= lower:
            break
        slab_upper = min(taxable_income, upper)
        slab_income = slab_upper - lower
        slab_tax = slab_income * rate
        total_tax += slab_tax
        slab_details.append({
            "range": f"{format_inr(lower)} – {'Above' if upper == float('inf') else format_inr(upper)}",
            "rate":  f"{int(rate*100)}%",
            "income_in_slab": slab_income,
            "tax_in_slab":    slab_tax
        })

    return total_tax, slab_details


# ─────────────────────────────────────────────────────────
# STEP 5: APPLY REBATE (Section 87A)
# ─────────────────────────────────────────────────────────

def apply_rebate_87a(tax, taxable_income, regime):
    """
    Section 87A provides a full tax rebate if income is within limits.

    New Regime (FY 2025-26): Rebate of 100% of tax if taxable income ≤ ₹12,00,000.
      (Effectively zero tax up to ₹12 lakh for most taxpayers)

    Old Regime: Rebate of 100% of tax if taxable income ≤ ₹5,00,000.
      (Maximum rebate = ₹12,500)
    """
    rebate = 0.0
    note   = ""

    if regime == "new":
        if taxable_income <= 1200000:
            rebate = tax  # full rebate → zero tax
            note = "Full tax rebate under Section 87A (income ≤ ₹12,00,000)"
    else:  # old
        if taxable_income <= 500000:
            rebate = min(tax, 12500)
            note = "Tax rebate under Section 87A (income ≤ ₹5,00,000)"

    return rebate, note


# ─────────────────────────────────────────────────────────
# STEP 6: COMPUTE SURCHARGE
# ─────────────────────────────────────────────────────────

def compute_surcharge(tax_after_rebate, taxable_income):
    """
    Surcharge is an additional tax on high-income earners.
    It is calculated on the base tax (after 87A rebate).

    Income > ₹50 lakh but ≤ ₹1 crore    → 10% surcharge
    Income > ₹1 crore  but ≤ ₹2 crore   → 15% surcharge
    Income > ₹2 crore  but ≤ ₹5 crore   → 25% surcharge
    Income > ₹5 crore                   → 37% surcharge

    Note: Marginal relief applies (not implemented here for simplicity).
    """
    if   taxable_income > 50000000:  # > 5 crore
        rate = 0.37
    elif taxable_income > 20000000:  # > 2 crore
        rate = 0.25
    elif taxable_income > 10000000:  # > 1 crore
        rate = 0.15
    elif taxable_income > 5000000:   # > 50 lakh
        rate = 0.10
    else:
        rate = 0.0

    return tax_after_rebate * rate


# ─────────────────────────────────────────────────────────
# STEP 7: MAIN CALCULATION ENGINE
# ─────────────────────────────────────────────────────────

def calculate_tax(income, deductions, ded_labels, age_category):
    """
    Master function that calculates tax for BOTH regimes.
    Returns a dictionary with all computed values.
    """
    # ── Gross Total Income ──────────────────────────────
    gross_income = (
        income["basic"]
        + income["hra_recv"]
        + income["other_allow"]
        + income["bonus"]
        + income["rental_income"]
        + income["interest_income"]
        + income["other_income"]
    )

    # ════════════════════════════════════════════════════
    # NEW REGIME CALCULATION
    # ════════════════════════════════════════════════════
    # Only one deduction allowed: Standard Deduction of ₹75,000
    new_std_ded     = 75000
    new_taxable     = max(0, gross_income - new_std_ded)

    new_base_tax, new_slab_details = compute_tax_slabs(new_taxable, "new", age_category)
    new_rebate, new_rebate_note    = apply_rebate_87a(new_base_tax, new_taxable, "new")
    new_tax_after_rebate           = max(0, new_base_tax - new_rebate)
    new_surcharge                  = compute_surcharge(new_tax_after_rebate, new_taxable)

    # Health & Education Cess: 4% on (tax + surcharge)
    new_cess   = (new_tax_after_rebate + new_surcharge) * 0.04
    new_total  = new_tax_after_rebate + new_surcharge + new_cess
    new_eff_rate = (new_total / gross_income * 100) if gross_income > 0 else 0

    # ════════════════════════════════════════════════════
    # OLD REGIME CALCULATION
    # ════════════════════════════════════════════════════
    old_total_ded = sum(deductions.values())
    old_taxable   = max(0, gross_income - old_total_ded)

    old_base_tax, old_slab_details = compute_tax_slabs(old_taxable, "old", age_category)
    old_rebate, old_rebate_note    = apply_rebate_87a(old_base_tax, old_taxable, "old")
    old_tax_after_rebate           = max(0, old_base_tax - old_rebate)
    old_surcharge                  = compute_surcharge(old_tax_after_rebate, old_taxable)
    old_cess   = (old_tax_after_rebate + old_surcharge) * 0.04
    old_total  = old_tax_after_rebate + old_surcharge + old_cess
    old_eff_rate = (old_total / gross_income * 100) if gross_income > 0 else 0

    return {
        "gross_income":         gross_income,
        # New Regime
        "new_std_ded":          new_std_ded,
        "new_taxable":          new_taxable,
        "new_base_tax":         new_base_tax,
        "new_slab_details":     new_slab_details,
        "new_rebate":           new_rebate,
        "new_rebate_note":      new_rebate_note,
        "new_surcharge":        new_surcharge,
        "new_cess":             new_cess,
        "new_total":            new_total,
        "new_eff_rate":         new_eff_rate,
        # Old Regime
        "deductions":           deductions,
        "ded_labels":           ded_labels,
        "old_total_ded":        old_total_ded,
        "old_taxable":          old_taxable,
        "old_base_tax":         old_base_tax,
        "old_slab_details":     old_slab_details,
        "old_rebate":           old_rebate,
        "old_rebate_note":      old_rebate_note,
        "old_surcharge":        old_surcharge,
        "old_cess":             old_cess,
        "old_total":            old_total,
        "old_eff_rate":         old_eff_rate,
    }


# ─────────────────────────────────────────────────────────
# STEP 8: PRINT THE FINAL REPORT
# ─────────────────────────────────────────────────────────

def print_report(name, age_category, income, result):
    """
    Print a comprehensive, easy-to-read tax report.
    Shows both regimes side by side and makes a recommendation.
    """
    W = 62  # total width of the report box

    def box_line(content="", fill=" "):
        return "│" + content.center(W) + "│"

    def header_line():
        return "┌" + "─" * W + "┐"

    def footer_line():
        return "└" + "─" * W + "┘"

    def separator():
        return "├" + "─" * W + "┤"

    print("\n\n")
    print(header_line())
    print(box_line())
    print(box_line("INDIA INCOME TAX REPORT — FY 2025-26 / AY 2026-27"))
    print(box_line(f"Prepared for: {name}  |  {age_category}"))
    print(box_line())
    print(footer_line())

    # ── Income Summary ───────────────────────────────────
    print_section("INCOME SUMMARY")
    print_table_row("Basic Salary + DA",             format_inr(income["basic"]))
    print_table_row("HRA Received",                  format_inr(income["hra_recv"]))
    print_table_row("Other Allowances",              format_inr(income["other_allow"]))
    print_table_row("Bonus / Incentives",            format_inr(income["bonus"]))
    print_table_row("Rental Income",                 format_inr(income["rental_income"]))
    print_table_row("Interest Income",               format_inr(income["interest_income"]))
    print_table_row("Other Income",                  format_inr(income["other_income"]))
    print_line()
    print_table_row("GROSS TOTAL INCOME",            format_inr(result["gross_income"]), indent=0, width=47)

    # ── Old Regime Deductions ────────────────────────────
    print_section("OLD REGIME — DEDUCTIONS CLAIMED")
    for key, amt in result["deductions"].items():
        if amt > 0:
            label = result["ded_labels"].get(key, key)
            print_table_row(label, format_inr(amt))
    print_line()
    print_table_row("TOTAL DEDUCTIONS",              format_inr(result["old_total_ded"]), indent=0, width=47)
    print_table_row("OLD REGIME TAXABLE INCOME",     format_inr(result["old_taxable"]),   indent=0, width=47)

    # ── New Regime ───────────────────────────────────────
    print_section("NEW REGIME — DEDUCTION APPLIED")
    print_table_row("Standard Deduction (FY 2025-26)",  format_inr(result["new_std_ded"]))
    print_line()
    print_table_row("NEW REGIME TAXABLE INCOME",     format_inr(result["new_taxable"]),   indent=0, width=47)

    # ── Slab-wise Breakdown ──────────────────────────────
    print_section("TAX SLAB CALCULATION — NEW REGIME")
    print(f"  {'Income Range':<35} {'Rate':>6}  {'Tax':>14}")
    print_line()
    for slab in result["new_slab_details"]:
        print(f"  {slab['range']:<35} {slab['rate']:>6}  {format_inr(slab['tax_in_slab']):>14}")
    print_line()
    print_table_row("Base Tax (New Regime)",         format_inr(result["new_base_tax"]))
    if result["new_rebate"] > 0:
        print_table_row(f"  Less: {result['new_rebate_note']}", f"- {format_inr(result['new_rebate'])}")
    if result["new_surcharge"] > 0:
        print_table_row("  Add: Surcharge",          format_inr(result["new_surcharge"]))
    print_table_row("  Add: H&E Cess @ 4%",         format_inr(result["new_cess"]))
    print_line()
    print_table_row("NET TAX PAYABLE (New Regime)",  format_inr(result["new_total"]),     indent=0, width=47)
    print_table_row("Effective Tax Rate",            f"{result['new_eff_rate']:.2f}%")

    print_section("TAX SLAB CALCULATION — OLD REGIME")
    print(f"  {'Income Range':<35} {'Rate':>6}  {'Tax':>14}")
    print_line()
    for slab in result["old_slab_details"]:
        print(f"  {slab['range']:<35} {slab['rate']:>6}  {format_inr(slab['tax_in_slab']):>14}")
    print_line()
    print_table_row("Base Tax (Old Regime)",         format_inr(result["old_base_tax"]))
    if result["old_rebate"] > 0:
        print_table_row(f"  Less: {result['old_rebate_note']}", f"- {format_inr(result['old_rebate'])}")
    if result["old_surcharge"] > 0:
        print_table_row("  Add: Surcharge",          format_inr(result["old_surcharge"]))
    print_table_row("  Add: H&E Cess @ 4%",         format_inr(result["old_cess"]))
    print_line()
    print_table_row("NET TAX PAYABLE (Old Regime)",  format_inr(result["old_total"]),     indent=0, width=47)
    print_table_row("Effective Tax Rate",            f"{result['old_eff_rate']:.2f}%")

    # ── Comparison ────────────────────────────────────────
    print_section("COMPARISON & RECOMMENDATION")
    print_table_row("New Regime Tax",  format_inr(result["new_total"]))
    print_table_row("Old Regime Tax",  format_inr(result["old_total"]))
    print_line()

    diff = abs(result["new_total"] - result["old_total"])

    if result["new_total"] < result["old_total"]:
        better  = "NEW REGIME"
        savings = diff
        print(f"""
  ╔══════════════════════════════════════════════════════╗
  ║  ✅  RECOMMENDATION: Choose the NEW TAX REGIME       ║
  ║                                                      ║
  ║  You save {format_inr(savings):>16} per year with the New Regime  ║
  ╚══════════════════════════════════════════════════════╝
        """)
    elif result["old_total"] < result["new_total"]:
        better  = "OLD REGIME"
        savings = diff
        print(f"""
  ╔══════════════════════════════════════════════════════╗
  ║  ✅  RECOMMENDATION: Choose the OLD TAX REGIME       ║
  ║                                                      ║
  ║  You save {format_inr(savings):>16} per year with the Old Regime  ║
  ╚══════════════════════════════════════════════════════╝
        """)
    else:
        better = "EITHER (same tax)"
        print("""
  ╔══════════════════════════════════════════════════════╗
  ║  ℹ  Both regimes result in exactly the same tax.     ║
  ║     You may choose either one.                       ║
  ╚══════════════════════════════════════════════════════╝
        """)

    # ── Important Notes ──────────────────────────────────
    print_section("IMPORTANT NOTES")
    notes = [
        "This calculator covers FY 2025-26 (Assessment Year 2026-27).",
        "New Regime is the DEFAULT regime from FY 2023-24 onwards.",
        "You must opt INTO the Old Regime before filing your return.",
        "Salaried employees can switch regimes every year.",
        "Business owners/self-employed can switch only ONCE.",
        "Surcharge marginal relief is not applied in this calculator.",
        "This is an estimate. Consult a CA for exact tax planning.",
        "Rebate u/s 87A: New regime up to ₹12L, Old regime up to ₹5L.",
    ]
    for note in notes:
        print(f"  • {note}")

    print()
    print("═" * 62)
    print("  Thank you for using the India Income Tax Calculator!")
    print("═" * 62)
    print()


# ─────────────────────────────────────────────────────────
# MAIN PROGRAM ENTRY POINT
# ─────────────────────────────────────────────────────────

def main():
    print("═" * 62)
    print("   INDIA INCOME TAX CALCULATOR — FY 2025-26 / AY 2026-27")
    print("   Covers: New Regime & Old Regime with Recommendation")
    print("═" * 62)
    print("""
  This program will:
    1. Ask for your income from all sources
    2. Ask for your eligible deductions (Old Regime)
    3. Calculate tax under BOTH regimes
    4. Show a slab-wise breakdown for each
    5. Recommend which regime saves you more money

  Press Ctrl+C at any time to exit.
  All amounts are in Indian Rupees (₹) per year (annual).
    """)

    try:
        # Step 1: Personal details
        name, age_category = collect_personal_details()

        # Step 2: Income details
        income = collect_income_details()

        # Step 3: Old regime deductions
        deductions, ded_labels = collect_old_regime_deductions(income, age_category)

        # Step 4: Calculate tax for both regimes
        result = calculate_tax(income, deductions, ded_labels, age_category)

        # Step 5: Print the report
        print_report(name, age_category, income, result)

    except KeyboardInterrupt:
        print("\n\n  Exiting. Goodbye!")


# ─────────────────────────────────────────────────────────
# Run the program
# ─────────────────────────────────────────────────────────
if __name__ == "__main__":
    main()