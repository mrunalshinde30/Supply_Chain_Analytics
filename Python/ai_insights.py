"""
AI Insights Assistant for Supply Chain Analytics

Generates natural-language business insights from
calculated supply-chain metrics using an LLM.
"""

def build_prompt(metrics):
    prompt = f"""
You are a supply chain analytics assistant.

Analyze the following business metrics:

Total Sales: {metrics['total_sales']}
Total Orders: {metrics['total_orders']}
Average Order Value: {metrics['average_order_value']}
Return Rate: {metrics['return_rate']}

Provide:
1. Key business insights
2. Possible reasons for the observed trends
3. Two actionable recommendations

Keep the response concise and data-driven.
"""
    return prompt


if __name__ == "__main__":

    # Example metrics produced from the project's analysis
    metrics = {
        "total_sales": 1245000,
        "total_orders": 4520,
        "average_order_value": 275.22,
        "return_rate": 8.2
    }

    prompt = build_prompt(metrics)

    print("=== SUPPLY CHAIN AI INSIGHTS ===")
    print(prompt)
