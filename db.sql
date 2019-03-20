DROP DATABASE IF EXISTS vha;
CREATE DATABASE vha;
USE vha;

CREATE TABLE tbOrgao(
	id int(5) primary key auto_increment not null comment 'Identifica o registro de órgão',
    cnpj varchar(14) not null comment 'Registra o Cadastro Nacional de Pessoa Jurídica do órgão',
    nome varchar(200) not null comment 'Registra a razão social do órgão'
) comment = 'Tabela para registrar os órgãos';

CREATE TABLE tbPessoa(
	id int(5) primary key auto_increment not null comment 'Identifica o registro de pessoa',
    nome varchar(150) not null comment 'Registra o nome da pessoa',
    cpf varchar(11) not null comment 'Registra o cpf da pessoa',
    senha varchar(11) not null comment 'Senha de acesso'
) comment = 'Tabela para registrar as pessoas';

CREATE TABLE tbBairro(
	id int(5) primary key auto_increment not null comment 'Identifica o registro de bairro',
    nome varchar(30) not null comment 'Nome do bairro'
) comment = 'Registra os nomes de bairros';

CREATE TABLE tbTipoLotacao(
	id int(5) primary key auto_increment not null comment 'Identifica o registro de tipo de lotação',
    descricao varchar(50) not null comment 'Registra o tipo de lotação'
)comment = 'Registra os tipos de lotação';

CREATE TABLE tbTipoTelefone(
	id int(5) primary key auto_increment not null comment 'Identifica o registro de tipo de telefone',
    descricao varchar(20) not null comment 'Descrição do tipo de telefone'
) comment = 'Registra os tipos de telefones';

CREATE TABLE tbStatus(
	id int(5) primary key auto_increment not null comment 'Identifica o registro de status',
    descricao varchar(50) not null comment 'Descrição do registro'
) comment = 'Tabela para registrar os tipos de status';

CREATE TABLE tbEventos(
	id int(5) primary key auto_increment not null comment 'Identifica o registro de eventos',
    idOrgao int(5) not null comment 'Referencia um órgão',
    descricao varchar(50) not null comment 'Descrição do evento',
    CONSTRAINT fkEventosOrgao FOREIGN KEY (idOrgao)
		REFERENCES tbOrgao (id)
) comment = 'Tabela para registrar os tipos de eventos';

CREATE TABLE tbEndereco(
	id int(5) primary key auto_increment not null comment 'Identifica o registro de endereço',
    idPessoa int(5) not null comment 'Referencia uma pessoa',
    rua varchar(100) not null comment 'Registra a rua',
    numero varchar(5) not null comment 'Registra o número',
    complemento varchar(50) comment 'Registra o complemento',
    idBairro int(5) not null comment 'Referencia um bairro',
    CONSTRAINT fkEnderecoPessoa FOREIGN KEY (idPessoa)
		REFERENCES tbPessoa (id),
	CONSTRAINT fkEnderecoBairro FOREIGN KEY (idBairro)
		REFERENCES tbBairro (id)
) comment = 'Registra os enderecos';

CREATE TABLE tbTelefone(
	id int(5) primary key auto_increment not null comment 'Identifica o registro de telefone',
    idPessoa int(5) not null comment 'Referencia uma pessoa',
    idTipo int(5) not null comment 'Referencia tipo de telefone',
    numero varchar(11) not null comment 'Número do telefone',
    CONSTRAINT fkTelefonePessoa FOREIGN KEY (idPessoa)
		REFERENCES tbPessoa (id),
	CONSTRAINT fkTelefoneTipo FOREIGN KEY (idTipo)
		REFERENCES tbTipoTelefone (id)
) comment = 'Registra os números de telefones';

CREATE TABLE tbLotacao(
	id int(5) primary key auto_increment not null comment 'Identifica o registro de lotação dos funcionários dos órgãos',
    idTipoLotacao int(5) not null comment 'Referencia um tipo de lotação',
    idOrgao int(5) not null comment 'Referencia um órgão',
    idPessoa int(5) not null comment 'Referencia uma pessoa',
    CONSTRAINT fkLotacaoTipoLotacao FOREIGN KEY (idTipoLotacao)
		REFERENCES tbTipoLotacao (id),
    CONSTRAINT fkLotacaoOrgao FOREIGN KEY (idOrgao)
		REFERENCES tbOrgao (id),
	CONSTRAINT fkLotacaoPessoa FOREIGN KEY (idPessoa)
		REFERENCES tbPessoa (id)
) comment = 'Registra a lotação dos funcionários dos órgãos';

CREATE TABLE tbChamado(
	id int(5) primary key auto_increment not null comment 'Identifica o registro de chamado',
    idPessoa int(5) not null comment 'Referencia a pessoa que abriu o chamado',
    idEvento int(5) not null comment 'Referencia o evento do chamado',
    idEndereco int(5) not null comment 'Referencia o endereço para execução do serviço',
    idStatus int(5) not null comment 'Referencia um status',
    dataAbertura date not null comment 'Registra a data de abertura do chamado',
    dataFechamento date comment 'Registra a data de fechamento do chamado',
    observacao text comment 'Registra alguma observação',
    CONSTRAINT fkChamadoPessoa FOREIGN KEY (idPessoa)
		REFERENCES tbPessoa (id),
	CONSTRAINT fkChamadoEvento FOREIGN KEY (idEvento)
		REFERENCES tbEventos (id),
	CONSTRAINT fkChamadoEndereco FOREIGN KEY (idEndereco)
		REFERENCES tbEndereco (id),
	CONSTRAINT fkChamadoStatus FOREIGN KEY (idStatus)
		REFERENCES tbStatus (id)
) comment = 'Registra os chamados abertos';

INSERT INTO tbOrgao (cnpj,nome) VALUES ('00000000000000','SECRETARIA MUNICIPAL DE OBRAS PÚBLICAS');
INSERT INTO tbOrgao (cnpj,nome) VALUES ('11111111111111','SECRETARIA MUNICIPAL DE SAÚDE');
INSERT INTO tbOrgao (cnpj,nome) VALUES ('22222222222222','SECRETARIA MUNICIPAL DE EDUCAÇÃO');

INSERT INTO tbPessoa (nome,cpf,senha) VALUES ('Pantera Negra', '11111111111', '11111111111');
INSERT INTO tbPessoa (nome,cpf,senha) VALUES ('Capitão América', '22222222222', '22222222222');
INSERT INTO tbPessoa (nome,cpf,senha) VALUES ('Viúva Negra', '33333333333', '33333333333');
INSERT INTO tbPessoa (nome,cpf,senha) VALUES ('Thor Odinson', '44444444444', '44444444444');
INSERT INTO tbPessoa (nome,cpf,senha) VALUES ('Homem de Ferro', '55555555555', '55555555555');
INSERT INTO tbPessoa (nome,cpf,senha) VALUES ('Bruce Banner', '66666666666', '66666666666');

INSERT INTO tbBairro (nome) VALUES ('Centro');
INSERT INTO tbBairro (nome) VALUES ('5º BEC');
INSERT INTO tbBairro (nome) VALUES ('Jardim das Oliveiras');
INSERT INTO tbBairro (nome) VALUES ('Cidade Verde I');
INSERT INTO tbBairro (nome) VALUES ('Cidade Verde II');
INSERT INTO tbBairro (nome) VALUES ('Cidade Verde III');

INSERT INTO tbTipoLotacao (descricao) VALUES ('Chefe');
INSERT INTO tbTipoLotacao (descricao) VALUES ('Subordinado');

INSERT INTO tbTipoTelefone (descricao) VALUES ('Fixo Pessoal');
INSERT INTO tbTipoTelefone (descricao) VALUES ('Fixo Comercial');
INSERT INTO tbTipoTelefone (descricao) VALUES ('Celular Pessoal');
INSERT INTO tbTipoTelefone (descricao) VALUES ('Fixo Recado');
INSERT INTO tbTipoTelefone (descricao) VALUES ('Celular Recado');

INSERT INTO tbStatus (descricao) VALUES ('Aberto');
INSERT INTO tbStatus (descricao) VALUES ('Em andamento');
INSERT INTO tbStatus (descricao) VALUES ('Finalizado');

INSERT INTO tbEventos (idOrgao,descricao) VALUES (1,'Poda de árvore');
INSERT INTO tbEventos (idOrgao,descricao) VALUES (1,'Troca de lâmpada');
INSERT INTO tbEventos (idOrgao,descricao) VALUES (1,'Limpeza de praça ou terreno baldio');
INSERT INTO tbEventos (idOrgao,descricao) VALUES (2,'Disponibilização de remédio');
INSERT INTO tbEventos (idOrgao,descricao) VALUES (3,'Disponibilização de vaga escolar');
INSERT INTO tbEventos (idOrgao,descricao) VALUES (3,'Transporte Escolar');

INSERT INTO tbEndereco (idPessoa,rua,numero,complemento,idBairro) VALUES (1,'Rua Mil Trezentos', '1020', 'Wakanda', 1);
INSERT INTO tbEndereco (idPessoa,rua,numero,complemento,idBairro) VALUES (2,'Rua A', '36-B', '1º Andar', 2);
INSERT INTO tbEndereco (idPessoa,rua,numero,complemento,idBairro) VALUES (3,'Rua dos Heróis', '8815', 'MCU', 3);
INSERT INTO tbEndereco (idPessoa,rua,numero,complemento,idBairro) VALUES (4,'Rua dos Vilões', '666', 'Hades', 4);

INSERT INTO tbTelefone (idPessoa,idTipo,numero) VALUES (1,1,'69021010700');
INSERT INTO tbTelefone (idPessoa,idTipo,numero) VALUES (1,2,'69021010701');
INSERT INTO tbTelefone (idPessoa,idTipo,numero) VALUES (1,3,'69999523266');
INSERT INTO tbTelefone (idPessoa,idTipo,numero) VALUES (2,1,'69033221100');
INSERT INTO tbTelefone (idPessoa,idTipo,numero) VALUES (2,3,'69955887496');

INSERT INTO tbLotacao (idTipoLotacao,idOrgao,idPessoa) VALUES (1,1,3);
INSERT INTO tbLotacao (idTipoLotacao,idOrgao,idPessoa) VALUES (2,1,4);
INSERT INTO tbLotacao (idTipoLotacao,idOrgao,idPessoa) VALUES (2,2,5);
INSERT INTO tbLotacao (idTipoLotacao,idOrgao,idPessoa) VALUES (2,3,6);

INSERT INTO tbChamado (idPessoa,idEvento,idEndereco,idStatus,dataAbertura,dataFechamento,observacao) VALUES (1,1,3,1,'2018-03-18',null,null);
INSERT INTO tbChamado (idPessoa,idEvento,idEndereco,idStatus,dataAbertura,dataFechamento,observacao) VALUES (2,2,4,1,'2018-03-18',null,null);




USE `vha`;
CREATE  OR REPLACE VIEW `vwLotacao` AS 
SELECT 
	vha.tbPessoa.id as ID_SERVIDOR,
    vha.tbPessoa.nome as NOME_SERVIDOR,
    vha.tbPessoa.cpf as CPF_SERVIDOR,
    vha.tbOrgao.id as ID_ORGAO, 
    vha.tbOrgao.nome as ORGAO,
    vha.tbTipoLotacao.id as ID_LOTACAO,
    vha.tbTipoLotacao.descricao as TIPO_LOTACAO
from 
	vha.tbPessoa
JOIN 
	vha.tbLotacao on 
		vha.tbLotacao.idPessoa = vha.tbPessoa.id
JOIN
	vha.tbTipoLotacao on
		vha.tbTipoLotacao.id = vha.tbLotacao.idTipoLotacao
JOIN 
	vha.tbOrgao on 
		vha.tbOrgao.id = vha.tbLotacao.idOrgao;

USE vha;
CREATE OR REPLACE VIEW vwChamado AS
SELECT
	vha.tbChamado.id AS ID_CHAMADO,
    vha.tbChamado.dataAbertura AS ABERTURA_CHAMADO,
    vha.tbChamado.dataFechamento AS FECHAMENTO_CHAMADO,
    vha.tbChamado.observacao AS OBS_CHAMADO,
    vha.tbChamado.idEvento AS ID_EVENTO,
    vha.tbChamado.idPessoa AS ID_PESSOA,
    vha.tbPessoa.nome AS NOME_PESSOA,
    vha.tbChamado.idstatus AS ID_STATUS,
    vha.tbStatus.descricao AS DESCRICAO_STATUS,
    vha.tbChamado.idEndereco AS ID_ENDERECO,
    vha.tbEndereco.rua AS RUA,
    vha.tbEndereco.numero AS NUMERO,
    vha.tbEndereco.complemento AS COMPLEMENTO,
    vha.tbEndereco.idBairro AS ID_BAIRRO,
    vha.tbBairro.nome AS NOME_BAIRRO
FROM
	vha.tbChamado
JOIN
	vha.tbPessoa on
		vha.tbPessoa.id = vha.tbChamado.idPessoa
JOIN
	vha.tbEndereco on
		vha.tbEndereco.id = vha.tbChamado.idEndereco
JOIN
	vha.tbBairro on
		vha.tbBairro.id = vha.tbEndereco.idBairro
JOIN
	vha.tbStatus on
		vha.tbStatus.id = vha.tbChamado.idStatus;