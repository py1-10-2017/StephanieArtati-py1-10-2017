/* Question 1 */
select sum(amount) from billing 
where month(charged_datetime) = 3 and year(charged_datetime) = 2012;

/* Question 2 */
select sum(amount) from billing
join clients on clients.client_id = billing.client_id
where clients.client_id = 2;

/* Question 3 */
select sites.domain_name from sites
join clients on clients.client_id = sites.client_id
where sites.client_id = 10;

/* Question 4 */
select clients.client_id, count(sites.domain_name) as number_sites, month(sites.created_datetime) as creation_month, year(sites.created_datetime) as creation_year from sites
join clients on clients.client_id = sites.client_id
where clients.client_id = 1
group by creation_month, creation_year;

select clients.client_id, count(sites.domain_name) as number_sites, month(sites.created_datetime) as creation_month, year(sites.created_datetime) as creation_year from sites
join clients on clients.client_id = sites.client_id
where clients.client_id = 20
group by creation_month, creation_year;

/* Question 5 */
select count(*), sites.domain_name from sites
join leads on leads.site_id = sites.site_id
where leads.registered_datetime between '2011-01-01' and '2011-02-15'
group by sites.domain_name;

/* Question 6 */
select concat_ws(' ',clients.first_name, clients.last_name) as client_name, count(leads.leads_id) from clients
join sites on sites.client_id = clients.client_id
join leads on leads.site_id = sites.site_id
where leads.registered_datetime between '2011-01-01' and '2011-12-31'
group by client_name; 

/* Question 7 */
select concat_ws(' ',clients.first_name, clients.last_name) as client_name, monthname(leads.registered_datetime) as month_in_2011, count(leads.leads_id) from clients
join sites on sites.client_id = clients.client_id
join leads on leads.site_id = sites.site_id
where leads.registered_datetime between '2011-01-01' and '2011-06-30'
group by client_name, month_in_2011
order by month(leads.registered_datetime); 

/* Question 8 */
select concat_ws(' ',clients.first_name, clients.last_name) as client_name, count(leads.leads_id) from clients
join sites on sites.client_id = clients.client_id
join leads on leads.site_id = sites.site_id
where leads.registered_datetime between '2011-01-01' and '2011-12-31'
group by client_name
order by clients.client_id;

select concat_ws(' ',clients.first_name, clients.last_name) as client_name, sites.domain_name, count(leads.leads_id) from clients
left join sites on sites.client_id = clients.client_id
left join leads on leads.site_id = sites.site_id
group by client_name, sites.domain_name
order by clients.client_id;

/* Question 9 */
select concat_ws(' ',clients.first_name, clients.last_name) as client_name, monthname(billing.charged_datetime) as bill_month, year(billing.charged_datetime) as bill_year, billing.amount from billing
join clients on billing.client_id = clients.client_id
group by client_name, bill_month, bill_year
order by clients.client_id;

/* Question 10 */
select concat_ws(' ',clients.first_name, clients.last_name) as client_name, group_concat(sites.domain_name) as sites from clients
left join sites on clients.client_id = sites.client_id
group by client_name
order by clients.client_id;