-- public.users definition

-- Drop table

-- DROP TABLE public.users;

CREATE TABLE public.users (
	id int8 NOT NULL,
	"name" varchar NULL,
	CONSTRAINT users_pkey PRIMARY KEY (id)
);