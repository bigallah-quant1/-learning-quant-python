# Day 1 - Trade Logger
# My journey to Quant Researcher

trades = []

print("=== Trade Logger ===")
asset = input("Asset (e.g BTC): ")
entry = float(input("Entry price: "))
exit_price = float(input("Exit price: "))
pnl = exit_price - entry

print(f"\nAsset: {asset}")
print(f"P/L: {pnl}")

if pnl > 0:
    print("Result: Good trade, meticulous work!")
else:
    print("Result: Loss, let's infer what went wrong")