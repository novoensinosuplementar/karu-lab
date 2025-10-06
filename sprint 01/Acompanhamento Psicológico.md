# Problema: Acompanhamento Psicológico e Perguntas-Chave

**Sprint:** 01  
**Tipo:** Pesquisa + Proposta de Feature  
**Duração:** 2 semanas  


## 🎯 Contexto

O Método Canguru preconiza um acompanhamento psicológico contínuo das famílias durante a terceira etapa (acompanhamento domiciliar). Para isso, existem **perguntas-chave** que devem ser feitas periodicamente aos pais para:
- Avaliar o bem-estar emocional da família
- Identificar situações de risco (depressão pós-parto, dificuldades no vínculo, etc.)
- Acompanhar a adaptação familiar
- Oferecer suporte adequado no momento certo

Atualmente, essas perguntas são feitas presencialmente nas consultas. **O desafio:** como integrar isso na plataforma Karu de forma que os pais respondam voluntariamente e os dados sejam úteis para a equipe de saúde?


## 📋 Objetivos

### 1. Estudo do Manual (Semana 1)
- [ ] Ler o documento "Método Canguru - Seguimento Compartilhado" (seções sobre acompanhamento psicológico)
- [ ] Identificar todas as perguntas-chave mencionadas
- [ ] Entender o contexto e objetivo de cada pergunta

### 2. Mapeamento Estruturado (Semana 1)
Para cada pergunta identificada, documentar:
- **Texto da pergunta**
- **Objetivo** (o que a equipe quer saber?)
- **Categoria** (vínculo afetivo, saúde mental materna, adaptação familiar, etc.)
- **Frequência recomendada** (semanal, quinzenal, mensal?)
- **Público** (mãe, pai, ambos, cuidador)
- **Momento adequado** (primeira semana em casa, após 1 mês, etc.)

### 3. Proposta de Integração (Semana 2)
Pensar e documentar:

**a) Design de Questionários**
- Como apresentar as perguntas? (múltipla escolha, escala 1-5, texto livre?)
- Quantas perguntas por vez? (não sobrecarregar os pais)
- Tom da comunicação (formal? acolhedor? breve?)

**b) Estratégia de Engajamento**
- Quando enviar? (horário do dia, dia da semana)
- Via qual canal? (app, SMS, WhatsApp, notificação push)
- Como lidar com perguntas sensíveis?
- O que fazer se os pais não responderem?

**c) Considerações de UX**
- Pensar em diferentes perfis (mãe alfabetizada digitalmente vs não)
- Acessibilidade (tamanho de fonte, cores, simplicidade)
- Versão mobile é essencial

### 4. Uso dos Dados Coletados (Semana 2)

**a) Relatórios para Equipe de Saúde**
- Que visualizações seriam úteis?
- Como mostrar evolução ao longo do tempo?
- Quais métricas acompanhar?

**b) Sistema de Alertas**
- Que respostas devem gerar alerta imediato? (ex: "me sinto muito triste todos os dias")
- Níveis de urgência (baixo, médio, alto, crítico)
- Quem deve ser notificado?

**c) Análise Avançada (Opcional)**
- É possível usar Machine Learning?
- Que tipo de modelo? (classificação de risco, predição de não-aderência, etc.)
- Quais dados seriam necessários para treinar?
- Questões éticas (privacidade, viés algorítmico)


## 📦 Entregáveis

### Obrigatórios
1. **Documento de Mapeamento** (`mapeamento-perguntas.md`)
   - Tabela ou lista estruturada com todas as perguntas identificadas e suas características

2. **Proposta de Questionários** (`proposta-questionarios.md`)
   - Como seria o fluxo de questionários na plataforma
   - Exemplos de formatos de perguntas
   - Estratégia de frequência e timing

3. **Sistema de Alertas** (`sistema-alertas.md`)
   - Regras para geração de alertas
   - Níveis de prioridade
   - Fluxo de notificação

### Opcionais (se houver tempo)
4. **Mockup/Wireframe** (desenho à mão ou ferramenta digital)
   - Como ficaria a interface de responder questionário no app

5. **Análise ML** (`analise-ml.ipynb`)
   - Viabilidade de uso de machine learning
   - Tipo de problema (classificação, regressão, etc.)
   - Dados necessários

### Apresentação Final
6. **Slides ou documento resumido** para apresentar descobertas e propostas


## 📚 Recursos

### Documentos
- `recursos/metodo-canguru-seguimento.pdf` - Manual principal
- `recursos/referencias-adicionais.md` - Artigos e materiais extras

### Ferramentas Sugeridas
- **Mapeamento:** Planilha (Google Sheets/Excel) ou Markdown
- **Mockups:** Figma (gratuito), draw.io, ou papel e caneta
- **Documentação:** Markdown files

### Apoio
- Issues para dúvidas: use tag `[sprint-01][acompanhamento]`
- Repositório principal (leitura) para entender arquitetura existente


## ✅ Critérios de Avaliação

- **Completude** - Todas as perguntas-chave foram identificadas?
- **Profundidade** - Análise vai além do superficial?
- **Viabilidade** - Propostas são implementáveis?
- **Empatia** - Considerou a experiência dos pais?
- **Impacto** - Propostas realmente ajudariam a equipe de saúde?
- **Documentação** - Material claro e bem organizado?


## 🗓️ Cronograma Sugerido

### Semana 1
- **Dias 1-2:** Leitura do manual
- **Dias 3-4:** Mapeamento de perguntas
- **Dia 5:** Discussão em grupo + checkpoint

### Semana 2
- **Dias 1-3:** Desenvolvimento das propostas
- **Dias 4-5:** Documentação final e preparação da apresentação
- **Final:** Apresentação e revisão


## 💡 Dicas

- **Não tentem mapear tudo de uma vez** - Façam seções do manual por vez
- **Pensem como pais cansados** - Bebês prematuros demandam muito, os pais estão exaustos
- **Perguntas sensíveis** - Como perguntar sobre depressão pós-parto sem assustar?
- **Dados úteis** - A equipe vai ver centenas de respostas. Como tornar isso gerenciável?


## 🚨 Atenção

Este é um trabalho sobre situações reais e delicadas. Lembrem-se que:
- Estamos falando de famílias em situação de vulnerabilidade
- Perguntas mal formuladas podem causar desconforto
- Alertas errados podem gerar pânico ou serem ignorados
- Privacidade dos dados é crítica

**Pensem sempre:** "Se eu fosse o pai/mãe, como eu gostaria que isso fosse feito?"
