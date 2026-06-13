SELECT * FROM fact_aum ORDER BY aum_crore DESC LIMIT 5;

SELECT strftime('%Y-%m', date), AVG(nav)
FROM fact_nav
GROUP BY 1;

SELECT transaction_type, COUNT(*)
FROM fact_transactions
GROUP BY 1;

SELECT state, SUM(amount_inr)
FROM fact_transactions
GROUP BY state;

SELECT * FROM fact_performance
WHERE expense_ratio_pct < 1;

SELECT category, AVG(return_3yr_pct)
FROM fact_performance
GROUP BY category;

SELECT risk_grade, AVG(sharpe_ratio)
FROM fact_performance
GROUP BY risk_grade;

SELECT fund_house, SUM(aum_crore)
FROM fact_aum
GROUP BY fund_house;

SELECT city_tier, SUM(amount_inr)
FROM fact_transactions
GROUP BY city_tier;

SELECT amfi_code, MAX(nav)
FROM fact_nav
GROUP BY amfi_code;
