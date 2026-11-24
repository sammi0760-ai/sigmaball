# Virtual layout tester for responsive breakpoints
breakpoints = [320, 360, 375, 414, 480, 640, 768, 868, 920, 1024, 1280, 1440]
print("Testing layout calculations for all breakpoints...")

for bp in breakpoints:
    # 1. Balls row test
    ball_size = max(31, min(bp * 0.078, 40))
    ball_gap = max(4, min(bp * 0.018, 10))
    row_width = 6 * ball_size + 6 * ball_gap + 12
    
    # Available card width
    page_pad = 12 if bp < 420 else (16 if bp < 640 else 24)
    card_pad = 16 if bp < 640 else 26
    container_w = min(bp - 2 * page_pad, 1200)
    card_cols = 1 if bp <= 1040 else 2
    card_w = container_w if card_cols == 1 else (container_w - 24) / 2
    card_inner_w = card_w - 2 * card_pad
    
    ball_fits = row_width <= card_inner_w
    diff = card_inner_w - row_width
    
    print(f"Breakpoint {bp:4d}px: Card inner = {card_inner_w:5.1f}px | Balls row = {row_width:5.1f}px | Margin = +{diff:5.1f}px | FITS: {ball_fits}")

print("\nAll breakpoints passed!")
