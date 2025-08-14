#!/usr/bin/env python3
"""
Test script for the Render FastAPI application.
Run this to verify the application works locally before deploying.
"""

import requests
import json
import time
from datetime import datetime

def test_endpoint(base_url, endpoint, expected_status=200, method="GET", data=None):
    """Test a single endpoint"""
    print(f"🔍 Testing {method} {endpoint}...")
    
    try:
        if method == "GET":
            response = requests.get(f"{base_url}{endpoint}", timeout=10)
        elif method == "POST":
            response = requests.post(f"{base_url}{endpoint}", json=data, timeout=10)
        
        if response.status_code == expected_status:
            print(f"✅ {method} {endpoint} - Status: {response.status_code}")
            
            # Try to parse JSON response
            try:
                json_data = response.json()
                print(f"   📄 Response: {json.dumps(json_data, indent=2)[:200]}...")
            except:
                print(f"   📄 Response: {response.text[:200]}...")
            
            return True
        else:
            print(f"❌ {method} {endpoint} - Expected {expected_status}, got {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ {method} {endpoint} - Error: {e}")
        return False

def main():
    """Main test function"""
    print("🚀 Render FastAPI Test - Local Testing")
    print("=" * 50)
    
    # Test configuration
    base_url = "http://localhost:8000"
    
    print(f"📍 Testing against: {base_url}")
    print(f"⏰ Test started at: {datetime.now()}")
    print()
    
    # Test endpoints
    tests = [
        ("/", "GET", 200),
        ("/health", "GET", 200),
        ("/info", "GET", 200),
        ("/echo", "GET", 200),
        ("/test", "GET", 200),
        ("/api/echo/hello", "GET", 200),
        ("/api/echo", "POST", 200, {"message": "Hello, Render!"}),
    ]
    
    results = []
    for test in tests:
        if len(test) == 3:
            endpoint, method, expected_status = test
            data = None
        else:
            endpoint, method, expected_status, data = test
        
        result = test_endpoint(base_url, endpoint, expected_status, method, data)
        results.append((endpoint, result))
        print()
    
    # Summary
    print("📊 Test Summary")
    print("=" * 50)
    passed = 0
    total = len(results)
    
    for endpoint, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} {endpoint}")
        if result:
            passed += 1
    
    print()
    print(f"🎯 Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Your application is ready for deployment.")
        print("\n📋 Next steps:")
        print("1. Commit your code to GitHub")
        print("2. Create a new Web Service on Render")
        print("3. Connect your GitHub repository")
        print("4. Set build command: pip install -r requirements.txt")
        print("5. Set start command: uvicorn main:app --host 0.0.0.0 --port $PORT")
        print("6. Deploy!")
        return 0
    else:
        print("⚠️ Some tests failed. Check your application before deploying.")
        return 1

if __name__ == "__main__":
    exit(main())
