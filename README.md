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

## 🏗️ Arquitetura

- **Backend (Python + SQLAlchemy + MySQL)**
  - Classe `Cliente`
  - Classe `Endereco` (relacionada 1:N com Cliente)
  - Classe `Telefone` (relacionada 1:N com Cliente)
  - Classe `Produto`
  - Classe `Venda`
  - Classe `ItemVenda` (para permitir múltiplos produtos em uma venda)

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
