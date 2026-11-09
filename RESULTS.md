# API lab results

## Part 0
- Step 0.1, the number of pizza names: 18
- Step 0.3, status code of the request without a token: 401 Unauthorized
- Step 0.4, the name of your pizza: The Mammoth Calzone
- Step 0.12, results of the three runs without a session (optional): All fail with 401
- Step 0.16, blocks of "how many of the three tools are excluded": | 0 tool: {[]} | 1 tool: {["Knife"]} | 2 tools: {["Knife", "Scissor"]} | 3 tools: {["Knife", "Pizza cutter", "Scissors"]} | The test only cover 1 tool block

## Defect report
- Title: All three tools excluded return 500 instead of 400
- Request: POST https://quickpizza.grafana.com/api/pizza with header `Authorization: token abcdef0123456789` and body `{"excludedTools":["Knife", "Pizza cutter", "Scissors"]}`
- Expected result: 400
- Actual result: 500
- Severity: Medium

## Part A
- Step A4, status codes when the other user reads, changes and deletes: reads=404, change=400, delete=400

## Part B
1. the load balancer losing a user and a crash with a 500, unit test with stubs are fast
2. So the test's data cannot be changed; Will apply for create new cart or booking for each test
3. The AWSALB cookie keeps every request on the same server; in Step 0.12 all three runs failed with 401.
4. All three tools excluded; a 500 with an empty body gives the app no message, and xfail keeps the defect visible.
5. Base choice needs 1 + 2 + 3 + 1 + 2 = 9 tests, and all combinations needs 3 × 4 × 2 × 3 = 72.
6. In part A
7. A list of rating data return which is a defect since stranger can read other data
8. API tests check status codes and server rules better; only web page tests check what the user sees.