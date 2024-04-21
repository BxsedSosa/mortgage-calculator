# Mortgage Calc Thouhgts

We determining from given information from user what their monthly payment will be with assumed interest that is compounding monthly

3 user inputs that will be needed:
- Loan Amount
- APR
- Loan Duration in years

We will need to convert some data;
- monthly interest rate
- loan duration in months

Formula given:
```
m = p * (j / (1 - (1 + j) ** (-n)))
```

#### Legend:
- m = monthly payment
- p = loan amount
- j = monthly interest rate
- n = loan duration in months

Print monthly payments will 2 decimals: 
- $123.45


