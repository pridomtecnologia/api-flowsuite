"""

BASE DE DADOS DO SISTEMA FLOWSUITE

"""
CREATE DATABASE flowsuite_db

-- tabela da base de dados
create table users (
	id_user INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY key,
	name varchar(255) not null,
	email varchar(150) not null unique,
	password text not null
)

create table roles (
	id_role INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY key,
	role varchar(255) not null
)

create table permissions (
	id_permission INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY key,
	permission varchar(255) not null
)

create table role_permissions (
	role_id INTEGER not null,
	permission_id INTEGER not null,
	PRIMARY KEY (role_id, permission_id),
    FOREIGN KEY (role_id) REFERENCES roles(id_role) ON DELETE CASCADE,
    FOREIGN KEY (permission_id) REFERENCES permissions(id_permission) ON DELETE CASCADE
)

create table user_roles (
	user_id INTEGER not null,
	role_id INTEGER not null,
	PRIMARY KEY (user_id, role_id),
	FOREIGN KEY (user_id) REFERENCES users(id_user) ON DELETE cascade,
    FOREIGN KEY (role_id) REFERENCES roles(id_role) ON DELETE CASCADE
)

create table logs(
	id_log INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY key,
	user_id INTEGER, 
    action VARCHAR(100) NOT NULL, 
    data JSONB, 
    created_at TIMESTAMP DEFAULT NOW(),
    CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES users(id_user)
)