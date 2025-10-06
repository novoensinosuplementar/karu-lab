# Problema: Medicações e Suplementação

**Sprint:** 01  
**Tipo:** Pesquisa + Proposta de Feature  
**Duração:** 2 semanas  


## 🎯 Contexto

Bebês prematuros, após a alta da segunda etapa do Método Canguru, frequentemente recebem prescrição de **suplementos vitamínicos e minerais** para compensar deficiências e apoiar o desenvolvimento adequado. Os mais comuns incluem:
- Vitaminas (A, D, complexo B)
- Ferro
- Ácido fólico
- Outros suplementos específicos

O acompanhamento da **administração correta** desses medicamentos é fundamental, mas atualmente depende da memória e disciplina dos pais. **O desafio:** criar um sistema na plataforma Karu que ajude os pais a administrarem corretamente e permita que a equipe de saúde monitore a aderência ao tratamento.


## 📋 Objetivos

### 1. Pesquisa Clínica (Semana 1)

**a) Identificação de Medicações**
- [ ] Listar os suplementos mais comumente prescritos para prematuros na 3ª etapa
- [ ] Para cada um, descobrir:
  - Dosagem típica (varia com peso/idade?)
  - Frequência de administração (1x/dia, 2x/dia, etc.)
  - Via de administração (oral, gotas, comprimidos)
  - Duração típica do tratamento
  - Quando geralmente é prescrito (logo após alta, após algumas semanas, etc.)

**b) Efeitos e Interações**
- [ ] Efeitos colaterais comuns de cada suplemento
- [ ] Sinais de superdosagem
- [ ] Interações medicamentosas relevantes
- [ ] Cuidados especiais (ex: ferro mancha os dentes, tomar com ou sem alimento)

### 2. Mapeamento do Processo Atual (Semana 1)

**a) Prescrição**
- Como os médicos prescrevem atualmente? (receita física? digital?)
- Informações incluídas na receita
- Quem recebe a receita? (pais, farmácia, ambos?)

**b) Administração**
- Como os pais registram que deram o medicamento? (papel? não registram?)
- Principais dificuldades relatadas (esquecimento, confusão de horários, bebê recusa)
- Como lidam com doses perdidas?

**c) Acompanhamento**
- Como a equipe de saúde monitora se o tratamento está sendo seguido?
- Quando descobrem problemas de aderência?

### 3. Proposta de Sistema de Controle (Semana 2)

**a) Cadastro de Medicações**
- Como seria cadastrada uma prescrição na plataforma?
- Quem cadastra? (médico? pais? ambos?)
- Informações necessárias (nome, dosagem, horários, duração)
- Integração com receitas digitais?

**b) Lembretes e Notificações**
- Quando notificar os pais? (horário exato? janela de tempo?)
- Qual o melhor canal? (push notification, SMS, WhatsApp?)
- Como evitar ser invasivo/irritante?
- Notificações repetidas se não confirmarem?

**c) Registro de Administração**
- Como registrar: "esqueci" ou "bebê recusou"?
- Permitir adicionar observações? (ex: "vomitou após tomar")

**d) Gestão de Estoque**
- Vale a pena rastrear quantidade restante?
- Alertar quando estiver acabando?

### 4. Análise e Relatórios (Semana 2)

**a) Para Equipe de Saúde**
- Dashboard com visão geral de aderência de cada paciente
- Visualização de tendências (está melhorando? piorando?)
- Quais informações são mais relevantes?

**b) Sistema de Alertas**
- Quando gerar alerta? (X doses esquecidas seguidas?)
- Níveis de prioridade
- Alerta para possíveis efeitos colaterais baseado em observações dos pais?

**c) Relatórios para Consultas**
- Relatório resumido para levar na consulta
- Histórico completo de administração
- Correlação com desenvolvimento do bebê (peso, altura)?

**d) Análise Avançada (Opcional)**
- Machine Learning pode prever não-aderência? Como?
- Identificar padrões (ex: "pais tendem a esquecer medicação noturna")
- Personalizar lembretes baseado no comportamento?


## 📦 Entregáveis

### Obrigatórios
1. **Documento de Medicações** (`medicacoes-prematuros.md`)
   - Lista completa com características de cada suplemento
   - Tabela ou formato estruturado

2. **Mapeamento do Processo Atual** (`processo-atual.md`)
   - Como funciona hoje (prescrição → administração → acompanhamento)
   - Pontos de dor identificados

3. **Proposta de Sistema** (`proposta-sistema.md`)
   - Como seria o fluxo completo na plataforma
   - Desde prescrição até relatórios
   - Considerar diferentes cenários (esquecimento, recusa, etc.)

4. **Sistema de Alertas** (`sistema-alertas.md`)
   - Regras para geração de alertas
   - Níveis de urgência
   - Quem é notificado e como

### Opcionais (se houver tempo)
5. **Mockup/Wireframe**
   - Interface de registro de medicação
   - Tela de lembretes
   - Dashboard para equipe de saúde

6. **Análise ML** (`analise-ml.ipynb`)
   - Viabilidade de predição de não-aderência
   - Dados necessários
   - Benefícios esperados

### Apresentação Final
7. **Slides ou documento resumido** para apresentar descobertas e propostas


## 📚 Recursos

### Documentos
- `recursos/suplementacao-prematuros.pdf` - Guias clínicos
- `recursos/metodo-canguru-medicacoes.pdf` - Seção específica do manual
- `recursos/referencias-adicionais.md` - Artigos científicos

### Ferramentas Sugeridas
- **Pesquisa:** Planilha para organizar medicações
- **Mockups:** Figma, draw.io, ou papel e caneta
- **Documentação:** Markdown files
- **Fluxogramas:** draw.io, Miro, ou Excalidraw


## ✅ Critérios de Avaliação

- **Completude** - Cobriu os principais suplementos?
- **Precisão** - Informações clínicas estão corretas?
- **Viabilidade** - Sistema proposto é implementável?
- **Usabilidade** - Considerou a experiência dos pais cansados?
- **Utilidade** - Sistema realmente ajudaria equipe de saúde?
- **Documentação** - Material claro e bem estruturado?


## 🗓️ Cronograma Sugerido

### Semana 1
- **Dias 1-2:** Pesquisa de medicações e suplementos
- **Dias 3-4:** Mapeamento do processo atual
- **Dia 5:** Organização dos dados + checkpoint

### Semana 2
- **Dias 1-3:** Desenvolvimento das propostas de sistema
- **Dias 4-5:** Documentação final e preparação da apresentação
- **Final:** Apresentação e revisão

## 💡 Dicas

- **Foco nos mais comuns** - Não tentem cobrir todas as medicações possíveis
- **Pais cansados** - Quanto mais simples, melhor
- **Mobile-first** - Provavelmente vão usar no celular, com uma mão só
- **Horários flexíveis** - Nem sempre é possível dar medicação no horário exato
- **Não julgar** - Sistema deve ser compreensivo, não punitivo



## 🚨 Atenção

Este trabalho lida com medicações reais:
- **Dosagens importam** - Erro pode ser perigoso
- **Interações medicamentosas** - Importante alertar
- **Não substitui orientação médica** - Sistema é apoio, não substitui consulta
- **Linguagem acessível** - Nem todos os pais têm formação em saúde
- **Privacidade** - Dados de saúde são sensíveis

**Sempre validem informações clínicas** - Quando em dúvida, perguntem ou marquem para revisão.



## 🤔 Perguntas para Reflexão

- Como o sistema poderia adaptar lembretes à rotina de cada família?
- O que fazer se os pais consistentemente esquecem uma medicação específica?
- Como balancear entre lembretes úteis e notificações irritantes?
- Vale a pena gamificar? (streaks, badges por consistência?)
- Como lidar com múltiplos cuidadores? (avó às vezes dá a medicação)
