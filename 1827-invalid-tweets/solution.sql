# Write your MySQL query statement below
select tweet_id
From Tweets
where char_length(content) > 15
