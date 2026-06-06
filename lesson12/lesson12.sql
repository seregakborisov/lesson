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
	appart varchar(255) not null,

	unique(user_id, city),
	unique(user_id, street),
	unique(user_id, bild),
	unique(user_id, appart));

create table delivery(
	delivert_id serial primary key,
	order_id int references orders(id),
	user_id int references users(id),
	delivery_city varchar(255) references users_address(city),
	delivery_street varchar(255) references users_address(street),
	delivery_bild varchar(255) references users_address(bild),
	delivery_appart varchar(255) references users_address(appart));
	
drop table 