import time
import requests

BASE_URL = "http://127.0.0.1:8000"


def test_jwt_flow():
    print("🔍 Testing JWT Bug #1: Login works, protected route returns 401")

    login_data = {
        "username": "testuser",
        "password": "testpassword",
    }

    response = requests.post(
        f"{BASE_URL}/login",
        data=login_data,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )

    print(f"Login status: {response.status_code}")
    print(f"Login response: {response.text}")

    if response.status_code != 200:
        print("❌ Login failed — fix this first before JWT verification.")
        return

    token = response.json().get("access_token")
    if not token:
        print("❌ No access_token returned from /login.")
        return

    time.sleep(1)

    headers = {
        "Authorization": f"Bearer {token}",
    }
    protected_resp = requests.get(f"{BASE_URL}/me", headers=headers)


    print(f"Protected status: {protected_resp.status_code}")
    print(f"Protected response: {protected_resp.text}")

    if protected_resp.status_code == 200:
        print("✅ JWT is working correctly! (Bug fixed)")
    else:
        print("❌ JWT bug still present: login works but protected route fails.")


if __name__ == "__main__":
    test_jwt_flow()
