select customer.first_name, customer.last_name, customer.email, address.address from customer
join address on customer.address_id = address.address_id
join city on address.city_id = city.city_id
where city.city_id = 312;

select film.title, film.description, film.release_year, film.rating, film.special_features, category.name from film
join film_category on film_category.film_id = film.film_id
join category on film_category.category_id = category.category_id
where category.name = 'Comedy';

select actor.actor_id, actor.first_name, actor.last_name, film.title, film.description, film.release_year from film
join film_actor on film_actor.film_id = film.film_id
join actor on actor.actor_id = film_actor.actor_id
where actor.actor_id = 5;

select store.store_id, city.city_id, customer.first_name, customer.last_name, customer.email, address.address from customer
join store on store.store_id = customer.store_id
join address on customer.address_id = address.address_id
join city on address.city_id = city.city_id
where customer.store_id = 1 and city.city_id in (1, 42, 312, 459);

select film.title, film.description, film.release_year, film.rating, film.special_features from film
join film_actor on film_actor.film_id = film.film_id
where film_actor.actor_id = 15 and film.rating = 'G' and film.special_features LIKE '%behind the scenes%';

select film_actor.actor_id, concat_ws(' ', actor.first_name, actor.last_name) as actor_name, film.film_id, film.title from film
join film_actor on film_actor.film_id = film.film_id
join actor on actor.actor_id = film_actor.actor_id
where film.film_id = 369;

select film.title, film.description, film.release_year, film.rating, film.special_features, category.name, film.rental_rate from film
join film_category on film.film_id = film_category.film_id
join category on category.category_id = film_category.category_id
where category.name = 'Drama' and film.rental_rate = 2.99;

select film.title, film.description, film.release_year, film.rating, film.special_features, category.name, actor.first_name, actor.last_name from film
join film_category on film_category.film_id = film.film_id
join category on category.category_id = film_category.category_id
join film_actor on film_actor.film_id = film.film_id
join actor on actor.actor_id = film_actor.actor_id
where category.name = 'Action' and actor.first_name = 'Sandra' and actor.last_name = 'Kilmer';