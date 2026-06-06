create table users(
	id serial primary key,
	name varchar(255),
	surname varchar(255),
	age int
);

create table category(
	name varchar(255) primary key);

create table products(
	id serial primary key,
	name varchar(255),
	category varchar(255) references category(name),
	price int,
	
	unique(name, category),
	dimensions int
	
);
drop table products

create table orders(
	id serial primary key,
	user_id int references users(id),
	created_at timestamptz default now(),
	served_at timestamptz default now());

create table orders_product(
	order_id int references orders(id),
	product_id int references products(id),
	created_at timestamptz default now());

create table discount(
	user_id int references users(id),
	discount int not null,
	sum_orders int);

create table users_address(
	user_id int references users(id),
	city varchar(255) not null,
	street varchar(255) not null,
	bild varchar(255) not null,
	appart varchar(255) not null);


create table delivery(
	delivert_id serial primary key,
	order_id int references orders(id),
	user_id int references users(id),
    place int references products(dimensions)
    delivery_city varchar(255) references users_address(city),
	delivery_street varchar(255) references users_address(street),
	delivery_bild varchar(255) references users_address(bild),
	delivery_appart varchar(255) references users_address(appart))
    ;
	
insert into category(name)
values
('Food'),
('Electronics'),
('Books'),
('Tools'),
('Clothes');

insert into users(name, surname, age)
select
    'Name_' || gs,
    'Surname_' || gs,
    (18 + random() * 50)::int
from generate_series(1,100000) gs;

insert into users_address(user_id, city, street, bild, appart)
select
    id,
    'City_' || (id % 100),
    'Street_' || (id % 500),
    (id % 200 + 1)::text,
    (id % 300 + 1)::text
from users;

insert into products(name, category, price, dimensions)
select
    'Product_' || gs,
    (array['Food','Electronics','Books','Tools','Clothes'])
        [((random()*4)::int)+1],
    (random()*5000 + 100)::int,
    (random()*100 + 1)::int
from generate_series(1,100000) gs;

insert into orders(user_id)
select
    (random()*99999 + 1)::int
from generate_series(1,100000);

insert into orders_product(order_id, product_id)
select
    (random()*99999 + 1)::int,
    (random()*99999 + 1)::int
from generate_series(1,100000);

insert into discount(user_id, discount, sum_orders)
select
    id,
    (random()*30)::int,
    (random()*50000)::int
from users;

insert into delivery(order_id, user_id)
select
    id,
    user_id
from orders;


select
    users.name,
    users.surname,
    users_address.city,
    users_address.street,
    users_address.bild,
    users_address.appart
from users
join users_address
    on users.id = users_address.user_id;


select
    orders.id,
    orders.user_id,
    users_address.city,
    users_address.street,
    users_address.bild,
    users_address.appart
from orders
join users_address
    on orders.id = users_address.user_id;