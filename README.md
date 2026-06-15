
# ApexMarket

O **ApexMarket** é um projeto **fictício e de estudo** criado para praticar **programação orientada a objetos (POO)** com **Python** e **MySQL**.  
O objetivo é aplicar conceitos fundamentais de POO, persistência de dados e arquitetura modular em um sistema de vendas.

---

## 🧠 Objetivo do Projeto

Este projeto foi desenvolvido para fins **educacionais** e não representa um sistema comercial real.  
Serve como base para aprendizado de boas práticas de desenvolvimento backend e futura integração com frontend web.

---

## 🎓 Metas de Aprendizado

- Aplicar **conceitos fundamentais de POO**:
  - Classes e objetos  
  - Encapsulamento  
  - Herança e polimorfismo  
  - Composição e agregação  

- Implementar **persistência de dados** com SQLAlchemy e MySQL.  
- Criar uma **arquitetura modular** com separação clara entre camadas (model, repository, service, controller).  
- Desenvolver **testes unitários** para validar regras de negócio.  
- Preparar o backend para futura integração com um **frontend web**.

---

## 🚀 Funcionalidades

- **Cadastro de Cliente**
  - Nome
  - Dados pessoais
    - e-mail
    - Data Nascimento
    - Estado Civil
  - Endereços
  - Telefones

- **Cadastro de Produto**
  - Nome
  - Código de barras
  - Categoria
  - Valor de venda

- **Registro de Vendas**
  - Cliente
  - Produto(s)
  - Data da venda
  - Valor total

---

## 🏗️ [Arquitetura](./docs/arquitetura.md)

O sistema segue uma arquitetura **modular e orientada a objetos**, dividida em camadas com responsabilidades bem definidas:

| Camada | Responsabilidade |
|--------|------------------|
| **App (`app.py`)** | Ponto de entrada da aplicação. Inicializa o Flask, conecta o banco e registra as rotas. |
| **Controller** | Define as rotas da API e recebe requisições HTTP. Interage com os serviços e retorna respostas JSON. |
| **Service** | Aplica regras de negócio e validações antes de persistir ou buscar dados. |
| **Repository** | Executa operações CRUD no banco via SQLAlchemy. Traduz objetos Python em registros MySQL. |
| **Model** | Define as classes e relacionamentos que representam as tabelas do banco. |
| **Config** | Centraliza parâmetros de conexão e inicialização do banco de dados. |

---

## 📂 Estrutura do Projeto
```plaintext
📦 apexmarket
┣ 📂 src
┃ ┣ 📂 config
┃ ┃ ┗ 📄 database.py
┃ ┣ 📂 models
┃ ┃ ┣ 📄 cliente.py
┃ ┃ ┣ 📄 endereco.py
┃ ┃ ┣ 📄 telefone.py
┃ ┃ ┣ 📄 produto.py
┃ ┃ ┣ 📄 venda.py
┃ ┃ ┗ 📄 item_venda.py
┃ ┣ 📂 repositories
┃ ┃ ┣ 📄 cliente_repository.py
┃ ┃ ┣ 📄 endereco_repository.py
┃ ┃ ┣ 📄 telefone_repository.py
┃ ┃ ┣ 📄 produto_repository.py
┃ ┃ ┗ 📄 venda_repository.py
┃ ┣ 📂 services
┃ ┃ ┣ 📄 cliente_service.py
┃ ┃ ┣ 📄 produto_service.py
┃ ┃ ┗ 📄 venda_service.py
┃ ┗ 📄 app.py
┣ 📂 tests
┃ ┣ 📄 test_cliente.py
┃ ┣ 📄 test_endereco.py
┃ ┣ 📄 test_telefone.py
┃ ┣ 📄 test_produto.py
┃ ┗ 📄 test_venda.py
┣ 📂 docs
┃ ┣ 📄 diagrama_classes.png
┃ ┣ 📄 diagrama_casos_uso.png
┃ ┣ 📄 diagrama_sequencia.png
┃ ┗ 📄 arquitetura.md
┣ 📄 requirements.txt
┗ 📄 README.md
```


---

## 🔧 Tecnologias

- **Python** (POO)  
- **Flask** ou **FastAPI** (API REST)  
- **SQLAlchemy** (ORM)  
- **MySQL** (Banco de dados relacional)  
- **pytest** (Testes automatizados)  

---

## 🔮 Futuro do Projeto

O sistema será expandido com:
- **Frontend web** para interação com o usuário (cadastro, listagem e vendas).  
- **API REST** para comunicação entre frontend e backend.  
- **Autenticação e controle de acesso** (login, perfis de usuário).  
- **Relatórios e dashboards** com estatísticas de vendas.  

---

## 👨‍💻 Autor

Marcelo de Souza Dias [Linkedin](https://www.linkedin.com/in/marcelosouzadias/).  
Anderson [Linkedin](https://www.linkedin.com)
