"""
AI Insights Module - Supply Chain Analytics

Prepares structured supply-chain metrics and prompts
for an LLM-based business insights assistant.
"""

def build_prompt(metrics):
    return f"""
You are a supply chain analytics assistant.

Analyze these metrics:

Total Sales: {metrics['total_sales']}
Total Orders: {metrics['total_orders']}
Average Order Value: {metrics['average_order_value']}
Return Rate: {metrics['return_rate']}%

Provide:
1. Key business insights
2. Possible reasons for the trends
3. Two actionable recommendations

Keep the response concise and data-driven.
"""


def prepare_metrics(total_sales, total_orders,
                    average_order_value, return_rate):

    return {
        "total_sales": total_sales,
        "total_orders": total_orders,
        "average_order_value": average_order_value,
        "return_rate": return_rate
    }


if __name__ == "__main__":

    metrics = prepare_metrics(
        total_sales=1245000,
        total_orders=4520,
        average_order_value=275.22,
        return_rate=8.2
    )

    print("=== AI INSIGHTS PROMPT ===")
    print(build_prompt(metrics))
