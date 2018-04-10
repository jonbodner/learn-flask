drop table if exists documents;
drop table if exists users;

create table users (
  id serial primary key,
  name text not null,
  email text unique not null,
  password text not null,
  date_created timestamp default current_timestamp,
  date_deleted timestamp
);

create table documents (
  id serial primary key,
  user_id int references users not null,
  key text unique not null,
  name text not null,
  date_created timestamp default current_timestamp,
  date_deleted timestamp
);