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
- Step A4, status codes when the other user reads, changes and deletes:

## Part B
1.
2.
3.
4.
5.
6.
7.
8.