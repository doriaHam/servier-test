
--------------------1----------------------------------------

SELECT date, IFNULL(sum(prod_price * prod_qty),0) AS ventes
FROM TRANSACTIONS
WHERE EXTRACT(YEAR FROM date) > 2019
GROUP BY date
ORDER BY date

--------------------2----------------------------------------

SELECT client_id, 
    CASE WHEN product_type='DECO' THEN IFNULL(sum(prod_price * prod_qty),0) AS ventes_deco,
    CASE WHEN product_type='MEUBLE' THEN IFNULL(sum(prod_price * prod_qty),0) AS ventes_meuble
FROM TRANSACTIONS
    LEFT JOIN PRODUCT_NOMENCLATURE
    USING(product_id)
WHERE EXTRACT(YEAR FROM date) > 2019
GROUP BY client_id
ORDER BY date

