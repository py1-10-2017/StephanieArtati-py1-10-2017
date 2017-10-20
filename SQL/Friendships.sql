select users.first_name, users.last_name, friends.first_name, friends.last_name from users
join friendships on users.id = friendships.user_id
join users as friends on friends.id = friendships.friend_id
order by users.last_name