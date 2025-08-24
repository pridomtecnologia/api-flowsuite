-- BASE DE DADOS DO SISTEMA FLOWSUITE
-- Criado por: Juliano Rezende
-- CREATE DATABASE flowsuite_db

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

insert into roles (role) values ('Administrador');
insert into roles (role) values ('Usuário');

create table permissions (
	id_permission INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY key,
	permission varchar(255) not null,
	created_at TIMESTAMP DEFAULT NOW(),
	updated_at TIMESTAMP DEFAULT NOW()
);

insert into permissions (permission) values ('Dashboard');
insert into permissions (permission) values ('Cadastros');
insert into permissions (permission) values ('Projetos');
insert into permissions (permission) values ('Produtos');
insert into permissions (permission) values ('Pedidos de Compra');
insert into permissions (permission) values ('Pedidos de Venda');
insert into permissions (permission) values ('Estoque');

create table user_permissions (
	user_id INTEGER not null,
	permission_id INTEGER not null,
	created_at TIMESTAMP DEFAULT NOW(),
	updated_at TIMESTAMP DEFAULT NOW(),
	PRIMARY KEY (user_id, permission_id),
    FOREIGN KEY (user_id) REFERENCES users(id_user) ON DELETE CASCADE,
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

create table tags(
	id_tag INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY key,
	tag varchar(255) not null,
	created_at TIMESTAMP DEFAULT NOW(),
	updated_at TIMESTAMP DEFAULT NOW()
);

insert into tags (tag) values ('Cliente');
insert into tags (tag) values ('Fornecedor');
insert into tags (tag) values ('Funcionário');
insert into tags (tag) values ('Artista');
insert into tags (tag) values ('Vendedor');


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
	razao_social varchar(255) not null,
	nome_fantasia varchar(255) not null,
	documento varchar(20) not null UNIQUE,
	email varchar(150) not null UNIQUE,
	telefone varchar(20) not null,
	responsavel_contato varchar(255) not null,
	observacao text,
	banco varchar(250) DEFAULT NULL,
	agencia varchar(10) DEFAULT NULL,
	conta_corrente varchar(20) DEFAULT NULL,
	inscricao_estadual varchar(100) DEFAULT NULL,
	inscricao_municipal varchar(100) DEFAULT NULL,
	web_site varchar(200) DEFAULT NULL,
	created_at TIMESTAMP DEFAULT NOW(),
	updated_at TIMESTAMP DEFAULT NOW()
);

create table cadastro_tag (
	id_cadastro_tag INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY key,
	cadastro_id INTEGER not null,
	tag_id INTEGER not null,
	created_at TIMESTAMP DEFAULT NOW(),
	updated_at TIMESTAMP DEFAULT NOW(),
	FOREIGN KEY (cadastro_id) REFERENCES cadastros(id_cadastro) ON DELETE cascade,
    FOREIGN KEY (tag_id) REFERENCES tags(id_tag) ON DELETE CASCADE
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

create table centro_custos(
	id_centro_custo INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY key,
	centro_custo varchar(200) not null,
	created_at TIMESTAMP DEFAULT NOW(),
	updated_at TIMESTAMP DEFAULT NOW()
);

insert into centro_custos (centro_custo) values ('PUBLICIDADE');

create table coprodutores(
	id_coprodutor INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY key,
	nome_fantasia varchar(200) not null,
	nome varchar(200) not null,
	cnpj varchar(20) not null,
	cpf varchar(15) not null,
	identificador_lancamento varchar(200) not null,
	nome_artistico varchar(200) not null,
	created_at TIMESTAMP DEFAULT NOW(),
	updated_at TIMESTAMP DEFAULT NOW()
);

-- insert into coprodutores (nome_fantasia, nome, cnpj, cpf, identificador_lancamento, nome_artistico) values ('mc juliano', 'juliano maciel', '46.333.555-0001/30', '465.104.168-08', '1111111', 'juju batidao');

create table diretores(
	id_diretor INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY key,
	nome_interno varchar(200) not null,
	nome varchar(200) not null,
	identificador_lancamento varchar(200) not null,
	created_at TIMESTAMP DEFAULT NOW(),
	updated_at TIMESTAMP DEFAULT NOW()
);

-- insert into diretores (nome_interno, nome, identificador_lancamento) values ('ju diretor', 'juliano', 'xxxxxxxxxxx55');

create table orcamentos(
	id_orcamento INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY key,
	numero_orcamento varchar(150) default 0,
	empresa_id INTEGER not null,
	centro_custo_id INTEGER not null,
	agencia_id INTEGER not null,
	cliente_id INTEGER not null,
	titulo varchar(200) not null,
	coprodutor_id INTEGER default 0,
	diretor_id INTEGER default 0,
	tipo_job_id INTEGER default 0,
	agrupamento varchar(200) not null,
	data_fechamento_job DATE default null,
	validade_orcamento DATE default null,
	imposto varchar(150) default null,
	taxa_impulsionamento varchar(150) default null,
	comissao_comercial varchar(150) default null,
	total_geral varchar(200) default null,
	created_at TIMESTAMP DEFAULT NOW(),
	updated_at TIMESTAMP DEFAULT NOW(),
	FOREIGN KEY (empresa_id) REFERENCES cadastros(id_cadastro) ON DELETE cascade,
	FOREIGN KEY (centro_custo_id) REFERENCES centro_custos(id_centro_custo) ON DELETE cascade,
	FOREIGN KEY (agencia_id) REFERENCES cadastros(id_cadastro) ON DELETE cascade,
	FOREIGN KEY (cliente_id) REFERENCES cadastros(id_cadastro) ON DELETE cascade,
	FOREIGN KEY (coprodutor_id) REFERENCES coprodutores(id_coprodutor) ON DELETE cascade,
	FOREIGN KEY (diretor_id) REFERENCES diretores(id_diretor) ON DELETE cascade,
	FOREIGN KEY (tipo_job_id) REFERENCES centro_custos(id_centro_custo) ON DELETE cascade
);

-- nome do custo
create table status_planilha_custo(
	id_status_planilha_custo INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY key,
	status_planilha_custo varchar(200) not null,
	created_at TIMESTAMP DEFAULT NOW(),
	updated_at TIMESTAMP DEFAULT NOW()
);

insert into status_planilha_custo (status_planilha_custo) values ('Em andamento');
insert into status_planilha_custo (status_planilha_custo) values ('Finalizado');

create table planilha_custos_orcamentos(
	id_planilha_custo_orcamento INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY key,
	status_planilha_custo_id integer not null,
	orcamento_id integer not null,
	nome_custo_orcamento varchar(255) not null,
	descricao varchar(255) not null,
	quantidade integer not null,
	valor_unitario varchar(200) not null,
	dias integer default 0,
	unidade varchar(255) default null,
	total varchar(200) default null,
	observacao text default null,
	versao integer,
	total_planilha varchar(200) default null,
	created_at TIMESTAMP DEFAULT NOW(),
	updated_at TIMESTAMP DEFAULT NOW(),
	FOREIGN KEY (orcamento_id) REFERENCES orcamentos(id_orcamento) ON DELETE cascade,
	FOREIGN KEY (status_planilha_custo_id) REFERENCES status_planilha_custo(id_status_planilha_custo) ON DELETE cascade
);

-- validar processo do job -a andamento validado e finalizado
create table status_job(
	id_status_job INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY key,
	status_job varchar(200) not null,
	created_at TIMESTAMP DEFAULT NOW(),
	updated_at TIMESTAMP DEFAULT NOW()
);

insert into status_job (status_job) values ('aprovado');

create table orcamento_jobs (
	id_orcamento_job INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY key,
	orcamento_id INTEGER not null,
	job INTEGER not null,
	status_job_id integer not null,
	created_at TIMESTAMP DEFAULT NOW(),
	updated_at TIMESTAMP DEFAULT NOW(),
    FOREIGN KEY (orcamento_id) REFERENCES orcamentos(id_orcamento) ON DELETE cascade,
    FOREIGN KEY (status_job_id) REFERENCES status_job(id_status_job) ON DELETE cascade
);

create table tipo_controle(
	id_tipo_controle INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY key,
	tipo_controle varchar(100) not null,
	created_at TIMESTAMP DEFAULT NOW(),
	updated_at TIMESTAMP DEFAULT NOW()
);

insert into tipo_controle (tipo_controle) values ('Unidade');
insert into tipo_controle (tipo_controle) values ('Rolo / Bobina');
insert into tipo_controle (tipo_controle) values ('Número de Série');

create table produtos(
	id_produto INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY key,
	codigo_sku varchar(100) not null,
	descricao varchar(255) not null,
	categoria varchar(100) not null,
	marca varchar(100) not null,
	modelo varchar(100) not null,
	codigo_fabrica varchar(100),
	tipo_material varchar(100) not null,
	unidade_medida varchar(100) not null,
	ncm varchar(100) not null,
	caracteristicas_tecnicas text,
	tipo_controle_id integer not null,
	estoque_minimo integer not null,
	estoque_maximo integer not null,
	preco_custo NUMERIC(10, 2) not null,
	preco_venda NUMERIC(10, 2) not null,
	garantia integer not null,
	created_at TIMESTAMP DEFAULT NOW(),
	updated_at TIMESTAMP DEFAULT NOW(),
	FOREIGN KEY (tipo_controle_id) REFERENCES tipo_controle(id_tipo_controle) ON DELETE cascade
);