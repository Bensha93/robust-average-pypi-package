#!/usr/bin/env python3
"""
Simple test script for robust_average function.
"""

from robust_average import robust_average

def test_robust_average():
    """Test the robust_average function with various scenarios."""
    
    print("Testing robust_average function...\n")
    
    # Test 1: Clean data (should use mean)
    print("Test 1: Clean data")
    prices = [97.87, 109.99, 129.99, 89.99, 119.99]
    result = robust_average(prices)
    print(f"Prices: {prices}")
    print(f"Result: {result['value']} (method: {result['method']})")
    print(f"Expected: mean\n")
    
    # Test 2: Data with outliers (should use median)
    print("Test 2: Data with outliers")
    prices_with_outlier = [97.87, 109.99, 129.99, 89.99, 119.99, 500.00]
    result = robust_average(prices_with_outlier)
    print(f"Prices: {prices_with_outlier}")
    print(f"Result: {result['value']} (method: {result['method']})")
    print(f"Outliers detected: {result['outliers']}")
    print(f"Expected: median\n")
    
    # Test 3: Skewed data (should use median)
    print("Test 3: Skewed data")
    skewed_prices = [10, 12, 15, 18, 20, 25, 30, 35, 40, 100]
    result = robust_average(skewed_prices)
    print(f"Prices: {skewed_prices}")
    print(f"Result: {result['value']} (method: {result['method']})")
    print(f"Skewness: {result['skew']:.3f}")
    print(f"Expected: median\n")
    
    # Test 4: Mode scenario (dominant value)
    print("Test 4: Mode scenario")
    mode_prices = [100, 100, 100, 100, 100, 150, 200]
    result = robust_average(mode_prices)
    print(f"Prices: {mode_prices}")
    print(f"Result: {result['value']} (method: {result['method']})")
    print(f"Expected: mode\n")
    
    print("All tests completed!")

if __name__ == "__main__":
    test_robust_average() 