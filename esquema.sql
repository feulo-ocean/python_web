drop table if exists entradas;
create table entradas (
  id integer primary key autoincrement,
  titulo string not null,
  texto string not null
);