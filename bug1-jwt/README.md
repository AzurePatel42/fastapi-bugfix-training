# Bug X – <Short Bug Title>

## 1. Bug Summary
A short description of what is broken.
Example:
“Database connection fails due to wrong DSN string.”

---

## 2. Steps to Reproduce
1. Start the FastAPI server
2. Hit the endpoint: <endpoint>
3. Observe the failure
4. Check logs / console output

---

## 3. Expected Behavior
Describe what SHOULD happen.

---

## 4. Actual Behavior
Describe what DOES happen.
Include error messages if possible.

---

## 5. Root Cause Analysis (RCA)
Explain WHY the bug happens.
Example:
- Wrong connection string
- Missing await
- Wrong CORS origin
- Wrong JWT algorithm

---

## 6. Fix Implemented
Explain HOW you fixed it.
Example:
- Updated DSN string
- Added await
- Added correct CORS origins
- Matched JWT algorithms

---

## 7. Verification
Explain how you confirmed the fix.

Example:
- Ran test script: `test_db_bug2.py`
- Endpoint returned 200 OK
- Logs show successful connection

---

## 8. Before/After Code

### Before (broken code)
```python
# broken code snippet
