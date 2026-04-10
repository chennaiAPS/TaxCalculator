## INDIAN INCOME TAX CALCULATOR (FY 2025-2026 / AY 2026-2027 / TY 2026-2027)

My first beginner friendly, fully interactive Python program that calculates your income tax under both New Tax Regime & Old Tax Regime, then gives you a recommendation which one saves you more money and by exactly how much. I have tried to calculate the Tax percentage as well that you are expected to pay after all calculations. I have tried my best to include all standard/hidden taxation criteria/deductions in this program. If you are a Chartered Accountant and you feel anything is missed, do let me know on aps04@outlook.com for corrections/inclusions. I am happy to make the corrections.



## APS DISCLAIMERS

1. This calculator is for educational and planning purposes only.
2. It is not a substitute for professional tax advice . Always consult a Chartered Accountant (CA) for your actual ITR filing.
3. Surcharge marginal relief  is not implemented. For incomes near surcharge thresholds, actual tax may differ slightly.
4. Capital gains  (STCG/LTCG) have special tax rates not covered here — enter them under "Other Income" for a rough estimate only.
5. Business/professional income  has different rules (presumptive taxation, audit requirements) not covered in this program.
6. Tax laws change every year. This program reflects  Finance Act 2025 provisions for FY 2025-26.
7. The New Regime is the  default  from FY 2023-24. To use the Old Regime, you must  explicitly opt in  while filing your return.
8. Salaried employees can  switch regimes every year . Business owners can switch only  once  (from Old to New).



## TABLE OF CONTENTS

1. [Overview](#overview)
2. [Features](#features)
3. [Requirements](#requirements)
4. [How to Run](#how-to-run)
5. [Program Flow — Step by Step](#program-flow--step-by-step)
6. [Income Sources Covered](#income-sources-covered)
7. [Deductions & Exemptions Covered (Old Regime)](#deductions--exemptions-covered-old-regime)
8. [Tax Regime Details](#tax-regime-details)
   - [New Tax Regime (FY 2025-26)](#new-tax-regime-fy-2025-26)
   - [Old Tax Regime](#old-tax-regime)
9. [How Tax Is Calculated](#how-tax-is-calculated)
10. [Sample Output](#sample-output)
11. [Project Structure](#project-structure)
12. [Function Reference](#function-reference)
13. [Key Python Concepts Used](#key-python-concepts-used)
14. [Important Disclaimers](#important-disclaimers)
15. [Future Improvements](#future-improvements)



## OVERVIEW 

India's Income Tax system currently offers taxpayers a choice between two regimes every financial year for salaried individuals:

| Details | New Regime | Old Regime |
| Standard Deduction | ₹75,000 | ₹50,000 |
| Other Deductions | Not allowed | Allowed (80C, 80D, HRA, etc.) |
| Default from FY 2023-24 | Yes | Must opt in explicitly |
| Slab rates | Lower rates, more slabs | Higher rates, fewer slabs |

This program takes your income and deduction details as input, computes tax under both regimes in full detail & tells you definitively which one to choose.



## FEATURES

Covers all major income sources — salary, HRA, bonus, rental, FD interest & more
Covers all major deductions — 80C, 80D, HRA exemption, NPS (80CCD1B), home loan interest (Sec 24b), 80TTA/TTB, 80G, 80E
Age-awareness — applies correct exemption limits for General, Senior Citizen (60-79) & Super Senior Citizen (80+) taxpayers
ection 87A rebate applied correctly for both regimes
Surcharge  computed for incomes above ₹50 lakh
Health & Education Cess (4%) applied automatically
lab by slab tax breakdown  printed for both regimes
HRA exemption  auto calculated using the three condition formula
Clear recommendation  with exact annual savings amount
Effective tax rate shown for both regimes
Input validation — reprompts on invalid entries, supports defaults



## HOW TO RUN THE PROGRAM

Save "KnowYourTaxes.py" to any folder on your computer.
Run the file in PowerShell in Windows or Terminal in macOS.
The program will guide you thru each section interactively.
Press ENTER to accept default values or type your own.
To exit at any point, press Ctrl + c.



## PROGRAM FLOW STEP BY STEP

START
	Step 1: Personal Details
	       	Age category (General / Senior / Super Senior)
       		Your name (for the report header)

	Step 2: Income Details
		Basic Salary + DA, HRA, Allowances, Bonus
		Rental Income, Interest Income, Other Income
	Step 3: Old Regime Deductions
		Standard Deduction (auto: ₹50,000)
		HRA Exemption (asks rent paid + city type)
		Section 80C, 80D, 80CCD(1B), 80TTA/TTB
		Section 24(b), 80G, 80E
	Step 4: Tax Calculation
		New Regime: Gross Income − ₹75,000 = Taxable Income → Slabs → Rebate → Cess
		Old Regime: Gross Income − All Deductions = Taxable Income → Slabs → Rebate → Cess
	Step 5: Print Report
		Slab-wise breakdown for both regimes
		Recommendation: which regime saves more, and by how much



## INCOME SOURCES COVERED

| Income Head | Field | Description |
| Salary | Basic Salary + DA | Your fixed pay plus dearness allowance |
| Salary | HRA Received | House Rent Allowance from employer |
| Salary | Other Allowances | LTA, special allowance, city/transport allowances |
| Salary | Bonus / Incentive | Annual bonus, performance pay |
| House Property | Rental Income | Gross annual rent from let-out property |
| Other Sources | Interest Income | Savings bank, FD, RD, bonds, post office interest |
| Other Sources | Other Income | Freelance earnings, gifts, casual income |

Note:  All amounts are entered as  annual figures in INR.



## DEDUCTIONS & EXEMPTIONS COVERED UNDER OLD REGIME

Standard Deduction — Auto Applied
Every salaried employee gets ₹50,000 automatically. No documents required.
HRA Exemption — Section 10(13A)
The exempt portion of HRA is the  minimum  of these three values:

(a) Actual HRA received from employer
(b) 50% of Basic+DA  →  if metro city (Delhi, Mumbai, Kolkata, Chennai)
    40% of Basic+DA  →  if non-metro city
(c) Rent paid − 10% of Basic+DA

You provide: rent paid per year & whether your city is a metro.



SECTION 80C - INVESTMENTS & PAYMENTS
 Limit: ₹1,50,000 per year 

Eligible instruments include:
- Employee Provident Fund (EPF) and Voluntary PF (VPF) contributions
- Public Provident Fund (PPF)
- ELSS Mutual Funds (Equity Linked Savings Scheme)
- Life Insurance premiums (LIC or any insurer)
- National Savings Certificate (NSC)
- 5-year tax-saving Fixed Deposit (bank or post office)
- Home loan principal repayment
- Children's tuition fees (up to 2 children)
- Sukanya Samriddhi Yojana



SECTION 80D - HEALTH INSURANCE PREMIUM
| Category | Limit |
| Self + Family (below 60) | ₹25,000 |
| Self + Family (60+) | ₹50,000 |
| Parents (below 60) | ₹25,000 extra |
| Parents (60+) | ₹50,000 extra |

Preventive health check-up (up to ₹5,000) is included within the above limits.



SECTION 80CCD (1B) - NPS ADDITIONAL CONTRIBUTION
 Limit: ₹50,000 per year (over and above the ₹1,50,000 of 80C)
Self-contribution to National Pension System (NPS) Tier 1 account. This is an exclusive deduction — it is not part of your 80C limit.



SECTION 80TTA/80TTB - SAVINGS INTEREST DEDUCTIONS
| Taxpayer | Section | Eligible Income | Limit |
| Below 60 | 80TTA | Savings bank interest only | ₹10,000 |
| 60 and above | 80TTB | All interest (savings + FD + RD + post office) | ₹50,000 |



SECTION 24(B) - HOME LOAN INTEREST
 Limit: ₹2,00,000 per year  (for self-occupied property)

The interest component of your home loan EMI. The property must be purchased, constructed or repaired using this loan. For letout properties, the deduction is unlimited but losses are restricted to  ₹2 lakh setoff against other income.



30% STANDARD DEDUCTIONS ON RENTAL INCOME - PART OF SECTION 24(A)
If you have rental income,  30% of gross rent  is automatically allowed as a deduction for repairs and maintenance for which no bills required.



SECTION 80G - DONATIONS
Donations to approved institutions are deductible at 100% or 50% depending on the fund. Enter only the eligible deductible portion ( 100% or 50% of the donation actually made).



SECTION 80E - EDUCATION LOAN INTEREST
 No upper limit.  The entire interest paid on an education loan for higher studies (for self, spouse, or children) is deductible. Applicable for a maximum of 8 consecutive years from the year repayment begins.



## TAX REGIME DETAILS

## New Tax Regime (FY 2025-26)

Applicable to all taxpayers regardless of age.

| Income Slab | Tax Rate |
|---|---|
| ₹0 – ₹4,00,000 | 0% |
| ₹4,00,001 – ₹8,00,000 | 5% |
| ₹8,00,001 – ₹12,00,000 | 10% |
| ₹12,00,001 – ₹16,00,000 | 15% |
| ₹16,00,001 – ₹20,00,000 | 20% |
| ₹20,00,001 – ₹24,00,000 | 25% |
| Above ₹24,00,000 | 30% |

 Section 87A Rebate (New Regime):  Full tax rebate if taxable income ≤ ₹12,00,000. Effectively zero tax for most taxpayers earning up to ₹12 lakh.

 Standard Deduction:  ₹75,000 (auto-applied for salaried employees).



## Old Tax Regime (FY 2025-26)

Slab rates vary by age category.

 General (Below 60 years): 

| Income Slab | Tax Rate |
|---|---|
| ₹0 – ₹2,50,000 | 0% |
| ₹2,50,001 – ₹5,00,000 | 5% |
| ₹5,00,001 – ₹10,00,000 | 20% |
| Above ₹10,00,000 | 30% |

 Senior Citizen (60–79 years): 

| Income Slab | Tax Rate |
|---|---|
| ₹0 – ₹3,00,000 | 0% |
| ₹3,00,001 – ₹5,00,000 | 5% |
| ₹5,00,001 – ₹10,00,000 | 20% |
| Above ₹10,00,000 | 30% |

 Super Senior Citizen (80+ years): 

| Income Slab | Tax Rate |
|---|---|
| ₹0 – ₹5,00,000 | 0% |
| ₹5,00,001 – ₹10,00,000 | 20% |
| Above ₹10,00,000 | 30% |

 Section 87A Rebate (Old Regime):  Full rebate (up to ₹12,500) if taxable income ≤ ₹5,00,000.

 Standard Deduction:  ₹50,000 (auto-applied for salaried employees).



## HOW TAX IS CALCULATED

The program follows this exact sequence for both regimes:


1.  Gross Total Income
        = Basic + HRA + Allowances + Bonus + Rental + Interest + Other

2.  Less: Deductions
        New Regime → only Standard Deduction of ₹75,000
        Old Regime → Standard Deduction + all applicable deductions

3.  Taxable Income
        = Gross Income − Total Deductions (minimum: ₹0)

4.  Base Tax
        = Sum of tax across each applicable slab

5.  Less: Section 87A Rebate
        New Regime → full rebate if taxable income ≤ ₹12,00,000
        Old Regime → rebate up to ₹12,500 if taxable income ≤ ₹5,00,000

6.  Add: Surcharge (on tax after rebate)
        > ₹50 lakh  → 10%
        > ₹1 crore  → 15%
        > ₹2 crore  → 25%
        > ₹5 crore  → 37%

7.  Add: Health & Education Cess
        = 4% × (Tax after rebate + Surcharge)

8.  Net Tax Payable = Step 5 result + Surcharge + Cess

9.  Effective Tax Rate = Net Tax Payable ÷ Gross Income × 100




## SAMPLE OUTPUT

Below is a representative excerpt from the program's report:

══════════════════════════════════════════════════════════════
   INDIA INCOME TAX REPORT — FY 2025-26 / AY 2026-27
   Prepared for: Anantha Sethuraman  |  Below 60 (General)
══════════════════════════════════════════════════════════════

────────────────────────────────────────────────────────────
  INCOME SUMMARY
────────────────────────────────────────────────────────────
  Basic Salary + DA                        ₹ 8,00,000
  HRA Received                             ₹ 2,00,000
  Other Allowances                         ₹ 1,00,000
  Bonus / Incentives                       ₹   50,000
  Interest Income                          ₹   10,000
────────────────────────────────────────────────────────────
GROSS TOTAL INCOME                         ₹ 11,60,000

────────────────────────────────────────────────────────────
  TAX SLAB CALCULATION — NEW REGIME
────────────────────────────────────────────────────────────
  Income Range                              Rate           Tax
  ₹ 0 – ₹ 4,00,000                           0%       ₹ 0
  ₹ 4,00,000 – ₹ 8,00,000                    5%   ₹ 20,000
  ₹ 8,00,000 – ₹ 10,85,000                  10%   ₹ 28,500
────────────────────────────────────────────────────────────
  Base Tax (New Regime)                     ₹ 48,500
    Less: 87A Rebate (income ≤ ₹12L)      - ₹ 48,500
    Add:  H&E Cess @ 4%                     ₹      0
────────────────────────────────────────────────────────────
NET TAX PAYABLE (New Regime)               ₹       0
Effective Tax Rate                          0.00%

  ╔══════════════════════════════════════════════════════
  ║  ✅  RECOMMENDATION: Choose the NEW TAX REGIME       
  ║                                                      
  ║  You save        ₹ 52,728 per year with New Regime   
  ╚══════════════════════════════════════════════════════



## PROJECT STRUCTURE
1. Number of Functions that I created to make it easy to read.
2. Number of Data Collections from the User that I created to make it easy to process.
3. Number of Engines that I created to make it easy for calculations.
4. Reporting Structure to make it easy for reading the results.

Helper Functions
	format_inr()          — Format numbers as ₹ with Indian commas
	get_positive_float()  — Validated number input with default support
	get_yes_no()          — Y/N question prompt
	get_choice()          — Numbered menu selection
	print_section()       — Styled section header
	print_table_row()     — Two-column formatted row
	print_line()          — Horizontal divider

Data Collection
	collect_personal_details()        — Age category, name
	collect_income_details()          — All income sources
	collect_old_regime_deductions()   — All applicable deductions

Tax Calculation Engine
	compute_tax_slabs()    — Slab-by-slab tax computation
	apply_rebate_87a()     — Section 87A rebate logic
	compute_surcharge()    — Surcharge for high incomes
	calculate_tax()        — Master function: runs both regimes

Reporting
	print_report()         — Full formatted report with recommendation



## FUNCTIONAL REFERENCES

| Function | Purpose | Parameters | Returns |
| `format_inr(amount)` | Formats a number as ₹ with Indian-style commas | `amount` (int/float) | String, e.g. `"₹ 1,50,000"` |
| `get_positive_float(prompt, default, max_val)` | Validated number input with optional cap | prompt, default=0, max_val=None | float |
| `get_yes_no(prompt, default)` | Y/N question | prompt, default="y" | bool |
| `get_choice(prompt, choices)` | Numbered menu | prompt, list of strings | chosen string |
| `collect_personal_details()` | Gather age & name | — | `(name, age_category)` |
| `collect_income_details()` | Gather all income | — | dict of income values |
| `collect_old_regime_deductions(income, age)` | Gather deductions | income dict, age string | `(deductions dict, labels dict)` |
| `compute_tax_slabs(taxable, regime, age)` | Apply slab rates | taxable income, regime, age | `(total_tax, slab_details list)` |
| `apply_rebate_87a(tax, taxable, regime)` | Apply 87A rebate | base tax, taxable income, regime | `(rebate amount, note string)` |
| `compute_surcharge(tax, taxable)` | Compute surcharge | tax after rebate, taxable income | surcharge amount (float) |
| `calculate_tax(income, deductions, labels, age)` | Master calculator | all collected data | result dict with all computed values |
| `print_report(name, age, income, result)` | Print full report | name, age, income dict, result dict | None (prints to console) |
| `main()` | Entry point | — | None |



## VERSION 2.0 IMPROVEMENTS PLANNED

	Add capital gains (LTCG/STCG) with special rate handling
	Add presumptive taxation for small businesses (Section 44AD/44ADA)
	Export the report to a text file or PDF
	Add a GUI
	Support multiple financial years (FY 2023-24, 2024-25)
	Add marginal relief for surcharge calculations
	Add employer's NPS contribution deduction (Section 80CCD(2))
	Add Section 80EEA (additional home loan interest for first-time buyers)


-----
APS.