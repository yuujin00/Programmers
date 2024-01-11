-- 코드를 입력하세요
SELECT substr(SALES_DATE,1,10) AS SALES_DATE, PRODUCT_ID, USER_ID, SALES_AMOUNT
FROM ONLINE_SALE
WHERE substr(SALES_DATE,1,7)='2022-03'
UNION ALL
SELECT SALES_DATE, PRODUCT_ID, NULL AS USER_ID, SALES_AMOUNT
FROM OFFLINE_SALE
WHERE substr(SALES_DATE,1,7)='2022-03'
ORDER BY SALES_DATE, PRODUCT_ID, USER_ID