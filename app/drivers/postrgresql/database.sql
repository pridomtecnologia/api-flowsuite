"""

BASE DE DADOS DO SISTEMA FLOWSUITE

"""
CREATE DATABASE flowsuite_db

-- tabela da base de dados
create table users (
	id_user INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY key,
	name varchar(255) not null,
	email varchar(150) not null unique,
	password text not null,
	created_at TIMESTAMP DEFAULT NOW(),
	updated_at TIMESTAMP DEFAULT NOW()
);

create table roles (
	id_role INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY key,
	role varchar(255) not null,
	created_at TIMESTAMP DEFAULT NOW(),
	updated_at TIMESTAMP DEFAULT NOW()
);

create table permissions (
	id_permission INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY key,
	permission varchar(255) not null,
	created_at TIMESTAMP DEFAULT NOW(),
	updated_at TIMESTAMP DEFAULT NOW()
);

create table role_permissions (
	role_id INTEGER not null,
	permission_id INTEGER not null,
	created_at TIMESTAMP DEFAULT NOW(),
	updated_at TIMESTAMP DEFAULT NOW(),
	PRIMARY KEY (role_id, permission_id),
    FOREIGN KEY (role_id) REFERENCES roles(id_role) ON DELETE CASCADE,
    FOREIGN KEY (permission_id) REFERENCES permissions(id_permission) ON DELETE CASCADE
);

create table user_roles (
	user_id INTEGER not null,
	role_id INTEGER not null,
	PRIMARY KEY (user_id, role_id),
	created_at TIMESTAMP DEFAULT NOW(),
	updated_at TIMESTAMP DEFAULT NOW(),
	FOREIGN KEY (user_id) REFERENCES users(id_user) ON DELETE cascade,
    FOREIGN KEY (role_id) REFERENCES roles(id_role) ON DELETE CASCADE
);

create table logs(
	id_log INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY key,
	user_id INTEGER, 
    action VARCHAR(100) NOT NULL, 
    data JSONB, 
    created_at TIMESTAMP DEFAULT NOW(),
	updated_at TIMESTAMP DEFAULT NOW(),
    CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES users(id_user)
);

create table cadastros(
	id_cadastro INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY key,
	tag_id INTEGER not null,
	razao_social varchar(255) not null,
	nome_fantasia varchar(255) not null,
	documento varchar(20) not null UNIQUE,
	email varchar(150) not null UNIQUE,
	telefone varchar(20) not null,
	responsavel_contato varchar(255) not null,
	observacao text,
	created_at TIMESTAMP DEFAULT NOW(),
	updated_at TIMESTAMP DEFAULT NOW(),
	FOREIGN KEY (tag_id) REFERENCES tags(id_tag) ON DELETE cascade
);

create table addresses(
	id_address INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY key,
	address varchar(255) not null,
	bairro varchar(255) not null,
	numero varchar(10) not null,
	estado varchar(255) not null,	
	cidade varchar(255) not null,
	cep varchar(10) not null,
	complemento TEXT,
    owner_id INTEGER NOT NULL,
	created_at TIMESTAMP DEFAULT NOW(),
	updated_at TIMESTAMP DEFAULT NOW()
);

create table user_cadastros(
	id_user_cadastro INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY key,
	user_id integer not null,
	cadastro_id integer not null,
	created_at TIMESTAMP DEFAULT NOW(),
	updated_at TIMESTAMP DEFAULT NOW(),
	FOREIGN KEY (user_id) REFERENCES users(id_user) ON DELETE cascade,
	FOREIGN KEY (cadastro_id) REFERENCES cadastros(id_cadastro) ON DELETE cascade
);

create table tags(
	id_tag INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY key,
	tag varchar(255) not null,
	created_at TIMESTAMP DEFAULT NOW(),
	updated_at TIMESTAMP DEFAULT NOW()
);