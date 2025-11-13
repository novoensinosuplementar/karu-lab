# 🟢 Karu Gamma - Documentação & Manuais de Uso


---

## 🎯 Objetivo

Criar **manuais completos de utilização da plataforma Karu** e implementar um **sistema de FAQ em Django** para centralizar dúvidas frequentes.

---

## 📦 Entregas Obrigatórias

### 1. Exploração da Plataforma Karu

Antes de documentar, vocês precisam **usar o sistema**:

- Cadastrar usuários (gestores, profissionais de saúde, pais)
- Cadastrar pacientes (bebês)
- Criar prontuários recorrentes
- Editar informações
- Explorar todas as funcionalidades
- Anotar dúvidas que usuários teriam

---

### 2. Manual Textual (Markdown)

Criar documentação completa em **Markdown**:

**Estrutura mínima:**
```
manual-karu/
├── 00-introducao.md
├── 01-primeiros-passos.md
├── 02-gestao-usuarios.md
├── 03-gestao-pacientes.md
├── 04-prontuarios.md
├── 05-funcionalidades-avancadas.md
├── 06-solucao-problemas.md
├── 07-glossario.md
└── prints/
```

**O que cada arquivo deve ter:**

- **00-introducao.md**: O que é o Karu, para quem serve, tipos de usuários
- **01-primeiros-passos.md**: Como acessar, primeiro login, recuperação de senha
- **02-gestao-usuarios.md**: Como cadastrar gestor, profissional de saúde, pais, como editar/remover
- **03-gestao-pacientes.md**: Como criar paciente, editar, vincular pais, arquivar
- **04-prontuarios.md**: O que é prontuário recorrente, como criar, editar, visualizar histórico
- **05-funcionalidades-avancadas.md**: Outras funcionalidades que descobrirem
- **06-solucao-problemas.md**: Problemas comuns, mensagens de erro
- **07-glossario.md**: Termos técnicos explicados

**Requisitos:**
- Linguagem clara e acessível
- Cada passo numerado
- **Tem que ter prints de tela** (um por ação importante)
- Avisos e dicas destacados

---

### 3. Manual Visual

Criar material visual complementar (escolham uma ou mais opções):

**Opção A: PDF Ilustrado**
- Screenshots grandes e claras
- Setas e destaques nas imagens
- Layout limpo e profissional
- Guia rápido visual

**Opção B: Apresentação/Slides**
- Um slide = um passo
- Muito visual, pouco texto
- Pode usar Google Slides, PowerPoint, Canva

**Opção C: Infográficos**
- Fluxos principais simplificados
- Visual e colorido
- Ferramentas: Canva, Figma

**Requisito:** Mínimo **10-20 páginas/slides**

---

### 4. Vídeos Tutoriais

Gravar **5 vídeos curtos** mostrando os processos:

**Vídeos obrigatórios:**
1. **Cadastro de usuário** (gestor ou profissional) - 2-3 min
2. **Cadastro de paciente** completo - 3-4 min
3. **Criação de prontuário recorrente** - 3-4 min
4. **Edição de informações** - 2-3 min
5. **Visão geral da plataforma** - 3-5 min

**Requisitos:**
- Gravação de tela (OBS Studio, Loom, ShareX)
- **Narração em português** explicando cada passo
- Qualidade: 720p (HD) no mínimo
- Áudio claro, sem ruídos
- Edição básica (cortar erros)

**Dicas:**
- Façam roteiro antes de gravar
- Testem o fluxo antes
- Destaquem o cursor
- Ritmo adequado (nem rápido, nem lento)

---

### 5. Sistema de FAQ em Django

Implementar aplicação Django para gerenciar perguntas frequentes.

**Models necessários:**
- **Categoria**: nome, descrição, ordem
- **PerguntaFrequente**: categoria, pergunta, resposta, ordem, visualizações, votos útil/não útil, datas

**Funcionalidades obrigatórias:**

✅ **Django Admin:**
- Cadastrar categorias
- Cadastrar perguntas e respostas
- Organizar ordem de exibição

✅ **Interface Pública:**
- Página inicial listando categorias
- Listagem de perguntas por categoria
- Página individual de pergunta/resposta
- Sistema de busca por palavra-chave
- Feedback "Esta resposta foi útil?" (Sim/Não)
- Contador de visualizações
- Ranking de perguntas mais vistas

✅ **Templates:**
- Design simples e funcional
- Responsivo (mobile)
- Navegação clara
- Breadcrumbs

**Conteúdo do FAQ (mínimo 25 perguntas):**

Categorias sugeridas:
- **Primeiros Passos** (5 perguntas): login, senha, navegação
- **Cadastros** (8 perguntas): como cadastrar cada tipo de usuário, editar, remover
- **Prontuários** (7 perguntas): criar, editar, visualizar
- **Problemas Comuns** (5 perguntas): erros, botões que não aparecem

---

### 6. Testes do FAQ Django

Criar testes automatizados:

**Mínimo 8 testes** cobrindo:
- Criação de categoria
- Criação de pergunta
- Busca de perguntas
- Contador de visualizações
- Sistema de feedback
- Listagem por categoria

---

## 📁 Estrutura de Arquivos
```
karu-gamma/
├── README.md
├── manual-karu/
│   ├── 00-introducao.md
│   ├── 01-primeiros-passos.md
│   ├── 02-gestao-usuarios.md
│   ├── 03-gestao-pacientes.md
│   ├── 04-prontuarios.md
│   ├── 05-funcionalidades-avancadas.md
│   ├── 06-solucao-problemas.md
│   ├── 07-glossario.md
│   └── prints/
├── manual-visual/
│   └── guia-visual-karu.pdf (ou slides)
├── videos/
│   ├── 01-cadastro-usuario.mp4
│   ├── 02-cadastro-paciente.mp4
│   ├── 03-prontuario.mp4
│   ├── 04-edicao.mp4
│   └── 05-visao-geral.mp4
├── faq-django/
│   ├── manage.py
│   ├── faq/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── admin.py
│   │   ├── templates/
│   │   ├── static/
│   │   └── tests.py
│   └── requirements.txt
└── COMO_USAR.md
```

---

## ✅ Checklist de Entrega

**Manuais:**
- [ ] Manual textual completo (20+ páginas)
- [ ] Mínimo 30 prints de tela
- [ ] Manual visual (15-20 páginas)
- [ ] Todos os fluxos principais cobertos

**Vídeos:**
- [ ] 5 vídeos gravados e editados
- [ ] Narração clara em português
- [ ] Qualidade 720p+

**FAQ Django:**
- [ ] Sistema funcionando
- [ ] 25+ perguntas cadastradas
- [ ] Busca implementada
- [ ] Feedback "útil" funcionando
- [ ] 8+ testes passando
- [ ] Documentação de como usar

**Geral:**
- [ ] Arquivos organizados
- [ ] Commits de todos os membros
- [ ] `COMO_USAR.md` completo

---

## 🗓️ Cronograma Sugerido

**Semana 1:**
- Dias 1-2: Explorar plataforma Karu, criar usuários/pacientes de teste
- Dias 3-4: Começar manual textual, capturar prints
- Dia 5: Checkpoint 1

**Semana 2:**
- Dias 1-2: Finalizar manual, criar visual, gravar vídeos
- Dias 3-4: Implementar FAQ Django, cadastrar perguntas
- Dia 5: Revisão final, apresentação

---

## 💡 Dicas

**Manuais:**
- Escreva como se fosse para alguém que nunca usou computador
- Um print para cada ação importante
- Destaque botões com setas/círculos

**Vídeos:**
- Escreva roteiro antes de gravar
- Grave em lugar silencioso
- Teste o fluxo antes
- Edite para remover erros

**FAQ Django:**
- Comece simples, depois melhore
- Use Bootstrap para UI rápida
- Baseie perguntas nas dúvidas reais que tiverem

**Divisão de trabalho:**
- Pessoa 1: Seções 1-3 do manual + 2 vídeos
- Pessoa 2: Seções 4-5 do manual + 2 vídeos
- Pessoa 3: Seções 6-7 + visual + 1 vídeo
- Todos: FAQ Django (dividir funcionalidades)

---

## 🎯 Apresentação (10-15 min)

1. Mostrar estrutura e qualidade dos manuais
2. Reproduzir trechos de 1-2 vídeos
3. Demo do FAQ Django funcionando
4. Mostrar busca e feedback
5. Estatísticas (quantas páginas, vídeos, perguntas)

---

## 🚨 Critérios de Reprovação

❌ Manual com menos de 5 páginas ou menos de 10 prints  
❌ Menos de 3 vídeos ou vídeos sem narração  
❌ FAQ Django não funciona  
❌ Menos de 10 perguntas no FAQ  
❌ Menos de 3 testes ou testes não passando  
❌ Não participar das reuniões/checkpoints

---

## 📚 Ferramentas Úteis

**Gravação de vídeos:**
- OBS Studio (gratuito)
- Loom (gratuito até 5min)
- ShareX (Windows)

**Edição de vídeo:**
- DaVinci Resolve (gratuito)
- OpenShot (simples)

**Material visual:**
- Canva (templates)
- Google Slides
- Figma

**Django:**
- daisyui para UI
- Django Admin (economiza tempo)