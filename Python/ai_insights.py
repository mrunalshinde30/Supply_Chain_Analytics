"""
AI Insights Module - Supply Chain Analytics

Uses Gemini to convert supply-chain metrics into
natural-language business insights and recommendations.
"""

import os
from google import genai


def prepare_metrics(total_sales, total_orders, average_order_value, return_rate):
    return {
        "total_sales": total_sales,
        "total_orders": total_orders,
        "average_order_value": average_order_value,
        "return_rate": return_rate
    }


def build_prompt(metrics):
    return f"""
You are a supply chain analytics assistant.

Analyze the following business metrics:

Total Sales: {metrics['total_sales']}
Total Orders: {metrics['total_orders']}
Average Order Value: {metrics['average_order_value']}
Return Rate: {metrics['return_rate']}%

Provide:
1. Three key business insights
2. Possible reasons behind the observed trends
3. Two actionable recommendations

Keep the response concise, practical and data-driven.
"""


def generate_ai_insights(metrics):
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError(
            "GEMINI_API_KEY environment variable is not set."
        )

    client = genai.Client(api_key=api_key)

    prompt = build_prompt(metrics)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text


if __name__ == "__main__":

    metrics = prepare_metrics(
        total_sales=100000,
        total_orders=2500,
        average_order_value=40,
        return_rate=5.2
    )

    print("\n--- AI Supply Chain Insights ---\n")
    print(generate_ai_insights(metrics))
