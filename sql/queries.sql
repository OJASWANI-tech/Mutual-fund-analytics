-- Top 5 funds by AUM
SELECT *
FROM fact_aum
ORDER BY aum_crore DESC
LIMIT 5;

-- Average NAV per month
SELECT
strftime('%Y-%m',date) as month,
AVG(nav)
FROM fact_nav
GROUP BY month;

-- Funds with expense ratio < 1%
SELECT scheme_name
FROM dim_fund
WHERE expense_ratio_pct < 1;

-- Transactions by state
SELECT state,
COUNT(*)
FROM fact_transactions
GROUP BY state;

-- Total schemes per fund house
SELECT fund_house,
COUNT(*)
FROM dim_fund
GROUP BY fund_house;

-- Highest Sharpe Ratio
SELECT scheme_name, sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 10;

-- Highest Alpha
SELECT scheme_name, alpha
FROM fact_performance
ORDER BY alpha DESC
LIMIT 10;

-- Average Transaction Amount
SELECT AVG(amount_inr)
FROM fact_transactions;

-- Transactions by City Tier
SELECT city_tier,
COUNT(*)
FROM fact_transactions
GROUP BY city_tier;

-- Top States by Investors
SELECT state,
COUNT(DISTINCT investor_id)
FROM fact_transactions
GROUP BY state
ORDER BY COUNT(*) DESC;