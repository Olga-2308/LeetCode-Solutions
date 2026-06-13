-- 1. First, we group users who have definitely paid for a subscription (if there is a payment in the group, then it is not 0)
-- 2. Then, in each group, we find the average value among those with a free period or payment, respectively.

SELECT user_id, 

    ROUND(AVG(CASE 
        WHEN activity_type = 'free_trial' THEN activity_duration END), 2) 
    AS trial_avg_duration,

    ROUND(AVG(CASE 
        WHEN activity_type = 'paid' THEN activity_duration END), 2) 
    AS paid_avg_duration
    
FROM UserActivity
GROUP BY user_id
HAVING SUM(activity_type = 'paid') > 0
ORDER BY user_id ASC;