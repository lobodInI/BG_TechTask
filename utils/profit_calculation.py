from typing import Any

from models import TradingStrategy

def profit_calculation(
        strategy: TradingStrategy,
        historical_data: dict[str, Any]
) -> dict[str, Any]:
    buy_threshold = strategy.buy_condition["threshold"]
    sell_threshold = strategy.sell_condition["threshold"]
    trades = 0
    trade_by_sell = 0
    profit = 0
    max_drawdown = 0

    for day in range(len(historical_data)):
        select_data = historical_data[day]

        max_drawdown = min(max_drawdown, select_data["low"] - select_data["high"])

        # buy if the opening index is greater than the smallest or closing index
        if (
                select_data["open"] - select_data["close"] >= buy_threshold or
                select_data["open"] - select_data["low"] >= buy_threshold
        ):
            profit -= select_data["volume"] * min(select_data["close"], select_data["low"])
            trades += 1

        # sell if the opening index is less than the highest or closing index
        if (
                select_data["open"] - select_data["close"] <= sell_threshold or
                select_data["open"] - select_data["high"] <= sell_threshold
        ):
            profit += select_data["volume"] * max(select_data["close"], select_data["high"])
            trade_by_sell += 1
            trades += 1

    win_rate = (trade_by_sell / trades) * 100 if trades > 0 else 0

    return {
        "stategy_id": strategy.id,
        "trades": trades,
        "profit": profit,
        "win_rate": round(win_rate, 2),
        "max_drawdown": round(max_drawdown, 1)
    }
