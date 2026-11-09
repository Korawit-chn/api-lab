# api-lab
W11-API_Lab_Exercise

## Input domain model: POST /api/ratings

| Characteristic | Blocks | Values in the tests | Step A2 Coverage |
|---|---|---|---|
| C1 Value of stars | below 1, 1 to 5 (base), above 5 | 0, 3, 6 | 
| C2 Type of stars | whole number (base), decimal, text, missing | 3, 3.5, "3", no field | test_stars_decimal_is_refused, test_stars_text_is_refused, test_stars_missing_is_refused |
| C3 Pizza | exists (base), does not exist | a new pizza, 999999999 | test_unknown_pizza_is_refused |
| C4 Token | the user's own (base), none, wrong length | from auth, no header, token short | test_no_token_is_refused, test_short_token_is_refused |
