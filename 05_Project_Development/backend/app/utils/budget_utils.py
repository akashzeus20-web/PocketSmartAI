from typing import List, Dict, Any

def audit_and_cap_budget(items: List[Dict[str, Any]], budget: float) -> tuple[List[Dict[str, Any]], float, float]:
    """
    Audits an item list to guarantee that the sum of item costs does NOT exceed budget.
    If the sum exceeds budget, prices are proportionally scaled down and rounded.
    Returns: (audited_items, total_estimated_cost, remaining_budget)
    """
    if not items:
        return [], 0.0, round(budget, 2)

    total_sum = sum(float(item.get("estimated_price", 0.0)) * int(item.get("quantity", 1)) for item in items)

    # If items exceed the user's hard budget limit, scale them down
    if total_sum > budget and total_sum > 0:
        ratio = (budget * 0.95) / total_sum  # Leave 5% buffer
        for item in items:
            original_price = float(item.get("estimated_price", 0.0))
            adjusted_price = max(round(original_price * ratio, 2), 5.0)
            item["estimated_price"] = adjusted_price

    # Recalculate true sum
    recalculated_sum = round(sum(float(item.get("estimated_price", 0.0)) * int(item.get("quantity", 1)) for item in items), 2)
    remaining_budget = max(round(budget - recalculated_sum, 2), 0.0)

    return items, recalculated_sum, remaining_budget


def compute_party_budget_split(budget: float, guest_count: int, venue_type: str) -> Dict[str, float]:
    """
    Computes a realistic baseline allocation for an event based on venue and guest count.
    """
    venue_lower = venue_type.lower()
    if "home" in venue_lower or "backyard" in venue_lower:
        # Lower venue cost, more budget goes to food and decor
        venue_ratio = 0.10
        catering_ratio = 0.50
        decor_ratio = 0.22
        entertainment_ratio = 0.18
    elif "hall" in venue_lower or "rented" in venue_lower or "hotel" in venue_lower:
        venue_ratio = 0.30
        catering_ratio = 0.40
        decor_ratio = 0.15
        entertainment_ratio = 0.15
    else:
        venue_ratio = 0.20
        catering_ratio = 0.45
        decor_ratio = 0.20
        entertainment_ratio = 0.15

    return {
        "catering_and_drinks": round(budget * catering_ratio, 2),
        "venue_and_rentals": round(budget * venue_ratio, 2),
        "decorations": round(budget * decor_ratio, 2),
        "entertainment_and_favors": round(budget * entertainment_ratio, 2)
    }


def compute_home_budget_split(budget: float) -> Dict[str, float]:
    """
    Computes baseline allocation for home interior spaces.
    """
    return {
        "key_furniture": round(budget * 0.60, 2),
        "lighting": round(budget * 0.15, 2),
        "decor_and_rugs": round(budget * 0.25, 2)
    }

