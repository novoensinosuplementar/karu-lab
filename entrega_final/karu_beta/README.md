# 🔵 Karu beta
 - Acompanhamento Psicológico


---

## 🎯 Objetivo

Implementar em **Django** o sistema de questionários psicológicos para acompanhamento das famílias no pós-alta do Método Canguru.

---

## 📦 Entregas Obrigatórias

### 1. Implementação Django

#### Models (banco de dados)
Criar os modelos necessários:
- **Questionario**: representa um conjunto de perguntas (ex: "Avaliação Semanal - Vínculo Afetivo")
- **Pergunta**: perguntas individuais com tipo (múltipla escolha, escala, texto livre)
- **Resposta**: respostas dadas pelos pais, vinculadas a um usuário identificador
- **Alerta**: alertas gerados automaticamente baseado nas respostas

**Importante:** 
- Não implementar cadastro de usuários (já existe no Karu)
- Usar identificador simbólico para os pais (ex: `usuario_id = "PAI_001"`)

#### Views e URLs
- Listagem de questionários disponíveis
- Tela para responder questionário
- Visualização de respostas anteriores de um usuário
- Dashboard para equipe de saúde ver respostas de todos os usuários
- Sistema de alertas (respostas que indicam risco)

#### Templates
- Interface simples e limpa para responder questionários
- Dashboard com tabelas/gráficos das respostas
- Lista de alertas gerados

### 2. Funcionalidades Essenciais

✅ **Cadastrar questionários**
- Criar perguntas com diferentes tipos (escala 1-5, sim/não, texto livre)
- Categorizar perguntas (vínculo afetivo, saúde mental, adaptação)
- Definir frequência recomendada

✅ **Responder questionários**
- Pais conseguem acessar e responder
- Salvar data/hora da resposta
- Permitir observações/comentários adicionais

✅ **Visualizar respostas**
- Ver histórico de respostas de um usuário específico
- Comparar respostas ao longo do tempo (evolução)
- Filtros por período, categoria, usuário

✅ **Sistema de alertas**
- Gerar alerta automático para respostas preocupantes
  - Ex: "Me sinto muito triste todos os dias" = alerta ALTO
  - Ex: "Tenho dificuldade de sentir carinho pelo bebê" = alerta CRÍTICO
- Níveis: BAIXO, MÉDIO, ALTO, CRÍTICO
- Dashboard de alertas para equipe de saúde

### 3. Testes

Criar testes automatizados para:
- Models (validações, métodos)
- Views (criação de respostas, geração de alertas)
- Sistema de alertas (verificar se regras funcionam)

**Mínimo esperado:** 10 testes cobrindo funcionalidades principais

### 4. Documentação

Criar arquivo `COMO_USAR.md` explicando:
- Como rodar o projeto
- Como criar um questionário
- Como simular um pai respondendo
- Como ver o dashboard
- Como funcionam os alertas

---

## 🎁 Entrega Extra (Opcional - Aumenta nota)

### Modelo de IA/ML para Análise de Risco

Implementar um modelo simples que analisa as respostas de algumas semanas e:
- **Identifica padrões de desapego** (dificuldade no vínculo mãe-bebê)
- **Detecta sinais de depressão pós-parto**
- **Prevê não-aderência ao acompanhamento**

**Sugestões de abordagem:**
- Modelo de classificação (Baixo Risco / Médio Risco / Alto Risco)
- Usar scikit-learn (Logistic Regression, Random Forest, ou SVM)
- Treinar com dados sintéticos inicialmente
- Integrar no Django para rodar predições automaticamente

**Entregáveis do ML:**
- Notebook Jupyter (`analise_ml.ipynb`) com experimentação
- Script Python (`modelo.py`) integrado ao Django
- Documentação de como o modelo funciona

---

## 📁 Estrutura de Arquivos Esperada

karu-beta
/
├── README.md (este arquivo)
├── COMO_USAR.md
├── manage.py
├── acompanhamento/
│   ├── models.py (Questionario, Pergunta, Resposta, Alerta)
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   ├── templates/
│   │   ├── questionario_lista.html
│   │   ├── questionario_responder.html
│   │   ├── dashboard.html
│   │   └── alertas.html
│   ├── tests.py
│   └── migrations/
├── requirements.txt
└── [opcional] ml/
    ├── analise_ml.ipynb
    └── modelo.py



---

## 🗓️ Cronograma Sugerido

**Semana 1:**
- Dias 1-2: Definir models 
- Dias 3-4: Implementar models, migrations, criar dados de teste
- Dia 5: Checkpoint 1 - Mostrar models funcionando

**Semana 2:**
- Dias 1-2: Implementar views, templates, sistema de alertas
- Dias 3-4: Escrever testes, [opcional] começar modelo ML
- Dia 5: Revisão final, apresentação


---

## 💡 Dicas

- **Comece simples**: Primeiro faça funcionar, depois melhore
- **Dados de teste**: Criem fixtures ou comando Django para popular com dados
- **Foco no core**: Questionários funcionando > design bonito
- **ML é extra**: Só faça se o básico estiver 100% pronto
- **Perguntem**: Usem as reuniões para tirar dúvidas

---

## 🚨 Critérios de Reprovação

❌ Não entregar código funcionando  
❌ Sistema não consegue criar/responder questionários  
❌ Menos de 5 testes ou testes não passando  
❌ Sem documentação de como usar  
❌ Não participar das reuniões/checkpoints