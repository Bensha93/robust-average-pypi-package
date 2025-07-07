#!/usr/bin/env python3
"""
Example usage of the robust_average function.
"""

from robust_average import robust_average
import pandas as pd

def main():
    """Demonstrate robust_average usage with real-world examples."""
    
    print("=== Robust Average Example ===\n")
    
    # Example 1: E-commerce price comparison
    print("1. E-commerce Price Analysis")
    print("-" * 30)
    
    # Prices from different online stores for the same product
    amazon_prices = [29.99, 32.50, 31.25, 30.00, 33.75]
    ebay_prices = [25.00, 28.50, 27.99, 26.50, 29.99, 45.00]  # Has outlier
    
    amazon_result = robust_average(amazon_prices)
    ebay_result = robust_average(ebay_prices)
    
    print(f"Amazon prices: {amazon_prices}")
    print(f"Amazon average: ${amazon_result['value']:.2f} ({amazon_result['method']})")
    print(f"eBay prices: {ebay_prices}")
    print(f"eBay average: ${ebay_result['value']:.2f} ({ebay_result['method']})")
    print(f"eBay outliers: {ebay_result['outliers']}")
    print()
    
    # Example 2: Stock price analysis
    print("2. Stock Price Analysis")
    print("-" * 30)
    
    # Daily closing prices for a week
    stock_prices = [150.25, 152.30, 151.80, 153.45, 152.90]
    stock_result = robust_average(stock_prices)
    
    print(f"Stock prices: {stock_prices}")
    print(f"Average price: ${stock_result['value']:.2f} ({stock_result['method']})")
    print(f"Standard deviation: ${stock_result['std']:.2f}")
    print()
    
    # Example 3: Real estate prices
    print("3. Real Estate Price Analysis")
    print("-" * 30)
    
    # House prices in a neighborhood (some outliers)
    house_prices = [250000, 275000, 280000, 265000, 290000, 500000, 260000]
    house_result = robust_average(house_prices)
    
    print(f"House prices: {house_prices}")
    print(f"Typical price: ${house_result['value']:,.0f} ({house_result['method']})")
    print(f"Outliers: {house_result['outliers']}")
    print(f"Skewness: {house_result['skew']:.3f}")
    print()
    
    # Example 4: Using pandas Series
    print("4. Using with Pandas Series")
    print("-" * 30)
    
    # Create a pandas Series
    price_series = pd.Series([10.50, 11.25, 10.75, 11.00, 10.90, 15.00])
    series_result = robust_average(price_series)
    
    print(f"Price series: {price_series.tolist()}")
    print(f"Average: ${series_result['value']:.2f} ({series_result['method']})")
    print(f"Count: {series_result['count']} prices")
    print()
    
    # Example 5: Detailed statistics
    print("5. Detailed Statistics")
    print("-" * 30)
    
    prices = [100, 105, 110, 115, 120, 125, 130, 135, 140, 200]
    detailed_result = robust_average(prices, return_all_stats=True)
    
    print(f"Prices: {prices}")
    print(f"Selected average: {detailed_result['value']} ({detailed_result['method']})")
    print(f"Mean: {detailed_result['mean']:.2f}")
    print(f"Median: {detailed_result['median']:.2f}")
    print(f"Mode: {detailed_result['mode']}")
    print(f"Standard deviation: {detailed_result['std']:.2f}")
    print(f"Skewness: {detailed_result['skew']:.3f}")
    print(f"Outliers: {detailed_result['outliers']}")
    print(f"Total prices: {detailed_result['count']}")

if __name__ == "__main__":
    main() 