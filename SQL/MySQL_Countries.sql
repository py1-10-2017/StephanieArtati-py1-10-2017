select countries.name, languages.language, languages.percentage from countries 
join languages on countries.id = languages.country_id 
where languages.language='Slovene'
order by languages.percentage desc;

select countries.name, count(*) as num_cities from countries
join cities on countries.id = cities.country_id
group by countries.name
order by num_cities desc;

select cities.name, cities.population from cities
join countries on countries.id = cities.country_id
where countries.name = 'Mexico' and cities.population > 500000
order by cities.population desc;

select countries.name, languages.language, languages.percentage from countries
join languages on countries.id = languages.country_id
where languages.percentage > 89
order by languages.percentage desc;

select name from countries
where surface_area < 501 and population > 100000;

select name, government_form, capital, life_expectancy from countries
where government_form = 'Constitutional Monarchy' and capital > 200 and life_expectancy > 75;

select cities.name from cities 
join countries on countries.id = cities.country_id
where countries.name = 'Argentina' and cities.district = 'Buenos Aires' and cities.population > 500000;	

select countries.region, count(*) as num_countries from countries 
group by countries.region
order by num_countries desc;

