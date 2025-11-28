# 🧪 Karu Lab — Sistema de Gestão de Medicações e Lembretes

## 📘 Sobre o Projeto

O **Karu Lab** é um sistema web desenvolvido para auxiliar usuários no gerenciamento de medicações, controle de estoques, definição de lembretes e registro de dosagens.
O projeto foi criado no âmbito do curso de Tecnologia da **Universidade Federal de Alagoas - Novo Ensino Suplementar**, como parte das atividades práticas de desenvolvimento em *frameworks* modernos.

A aplicação busca otimizar o controle de tratamentos médicos, reduzindo erros humanos e promovendo uma rotina mais segura e organizada.

---

## 🎯 Objetivos

* Permitir o **registro e controle** de medicações.
* Implementar **lembretes automáticos** para o horário de uso.
* Gerenciar o **estoque** de medicamentos de forma integrada.
* Fornecer uma **interface simples e funcional** ao usuário.

---

## 🛠️ Tecnologias Utilizadas

* **Python** (versão 3.10 ou superior)
* **Django** (framework principal)
* **HTML5 / CSS3** (interface do usuário)
* **SQLite** (banco de dados padrão)
* **Git e GitHub** (controle de versão)

---

## ⚙️ Instalação e Execução

### 1. Clonar o repositório

```bash
git clone https://github.com/Equipe-Alpha/Karu-Lab.git
cd Karu-Lab
```

### 2. Criar e ativar o ambiente virtual

```bash
python -m venv venv
venv\Scripts\activate  # (Windows)
source venv/bin/activate  # (Linux/Mac)
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Executar as migrações e iniciar o servidor

```bash
python manage.py migrate
python manage.py runserver
```

### 5. Acessar no navegador

```
http://127.0.0.1:8000/
```

---

## 🧪 Testes

Os testes foram conduzidos por **Eduardo Arakaki**, com foco na validação das funcionalidades principais, integração entre módulos e desempenho da aplicação.
Os resultados indicaram bom funcionamento geral, com sugestões de otimização no carregamento inicial e melhoria na validação de campos obrigatórios.

---

## 💡 Contribuições Futuras

* Implementação de notificações via e-mail ou SMS.
* Otimização da interface com design responsivo aprimorado.

---

## 👨‍💻 Equipe de Desenvolvimento — Equipe Alpha

| Integrante          | Função Principal                                                                  |
| ------------------- | --------------------------------------------------------------------------------- |
| **Eduardo Justo**   | Modelagem de dados, backend Django, registros de medicações, lembretes e estoques |
| **Gustavo**         | Aprimoramento do sistema de lembretes e estoques, lógicas de registro             |
| **Arthur**          | Templates HTML e implementação funcional do sistema de dosagem                    |
| **Eduardo Arakaki** | Testes e validação de desempenho                                                  |
| **Almir**           | Slides, relatório e documentação técnica                                          |

---

## 📍 Instituição

**Universidade Federal de Alagoas - Novo Ensino Suplementar**
Maceió - AL, 2025
