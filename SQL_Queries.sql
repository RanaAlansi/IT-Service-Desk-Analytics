-- Total Tickets by Department

SELECT
    Department,
    COUNT(*) AS Total_Tickets
FROM Tickets
GROUP BY Department
ORDER BY Total_Tickets DESC;


-- Average Resolution Days

SELECT
    Department,
    ROUND(AVG(Resolution_Days),2) AS Avg_Resolution_Days
FROM Tickets
WHERE Resolution_Days IS NOT NULL
GROUP BY Department
ORDER BY Avg_Resolution_Days DESC;


-- Total Tickets by SLA Status

SELECT
    SLA_Status,
    COUNT(*) AS Total_Tickets
FROM Tickets
WHERE SLA_Status IS NOT NULL
GROUP BY SLA_Status;


--Total Tickets by Category

SELECT
    Category,
    COUNT(*) AS Total_Tickets
FROM Tickets
GROUP BY Category
ORDER BY Total_Tickets DESC;


-- Total Ticktes by Priority

SELECT
    Priority,
    COUNT(*) AS Total_Tickets
FROM Tickets
GROUP BY Priority
ORDER BY Total_Tickets DESC;

