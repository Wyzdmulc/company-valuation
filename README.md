# Company Valuation - Income-Based Approach

This tool calculates the intrinsic value of a company using an income-based valuation method, specifically the Dividend Discount Model (DDM) and Free Cash Flow approaches.

## Overview

The program uses the present value of future dividends (or free cash flows) to determine a company's intrinsic value. It supports multiple valuation scenarios based on different growth assumptions.

## Features

- **Two Valuation Modes:**
  - **No Growth Model**: Used when dividends are expected to remain constant
  - **Constant Growth Model**: Applied when dividends grow at a steady rate indefinitely
  - **Two-Step Growth Model**: Handles scenarios where dividend growth changes after a specified period

- **Flexible Input Parameters:**
  - Current dividend amount (or free cash flow)
  - Growth rates (primary and secondary)
  - Cost of equity / Interest rates / WACC

- **Detailed Output:**
  - Year-by-year discount factors (DCF)
  - Estimated future dividends
  - Present value calculations
  - Cumulative net present value
  - Final intrinsic value

## How to Use

Run the program:
```bash
python "intrinsic value income based.py"
```

Follow the interactive prompts:

1. **Enter the current dividend** - The most recent dividend paid or expected free cash flow
2. **Choose if dividend grows** - Select yes or no
3. **If yes, choose growth type:**
   - **Constant Growth**: Dividends grow at a fixed percentage annually
   - **Two-Step Growth**: Dividends grow at one rate, then change to another rate

4. **Enter financial parameters:**
   - Growth rate (as decimal, e.g., 0.05 for 5%)
   - Cost of equity/capital (as decimal)
   - For two-step model: number of years for first growth phase

## Formulas

### No Growth Model
```
Intrinsic Value = Dividend / Cost of Capital
```

### Constant Growth Model (Gordon Growth Model)
```
Intrinsic Value = (Dividend × (1 + Growth)) / (Cost of Capital - Growth)
```

### Two-Step Growth Model
```
Intrinsic Value = Sum of PV(Dividends, Years 1-N) + PV(Terminal Value)
```

Where:
- PV = Present Value
- DCF = Discount Factor = 1 / (1 + Interest Rate)^n

## Example

For a company with:
- Current dividend: $2.00
- Constant growth rate: 5%
- Cost of equity: 10%

The intrinsic value would be calculated as:
```
(2.00 × 1.05) / (0.10 - 0.05) = $42.00
```

## Notes

- The cost of equity can be derived from CAPM, WACC, or other methods
- The model assumes perpetual dividend payments or free cash flows
- Growth rates should realistically be lower than the cost of capital for the calculation to be valid