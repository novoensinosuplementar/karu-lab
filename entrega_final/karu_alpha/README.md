# 🟡 Karu alpha
 - Medicações e Suplementação


---

## 🎯 Objetivo

Implementar em **Django** o sistema de controle de medicações e suplementos para bebês prematuros no acompanhamento domiciliar.

---

## 📦 Entregas Obrigatórias

### 1. Implementação Django

#### Models (banco de dados)
Criar os modelos necessários:
- **Medicamento**: cadastro de medicamentos/suplementos (nome, tipo, cuidados especiais)
- **Prescricao**: prescrição para um usuário específico (medicamento, dosagem, frequência, duração)
- **Administracao**: registro de quando foi administrado (data/hora, observações)
- **Alerta**: alertas automáticos (doses esquecidas, possível superdosagem, fim do estoque)

**Importante:**
- Não implementar cadastro de usuários (já existe no Karu)
- Usar identificador simbólico para os pacientes (ex: `paciente_id = "BEBE_001"`)

#### Views e URLs
- Cadastro de medicamentos no sistema
- Criar prescrição para um paciente
- Registrar administração de medicamento
- Histórico de administrações de um paciente
- Dashboard para visualizar aderência ao tratamento
- Sistema de alertas

#### Templates
- Formulário para registrar administração (mobile-friendly!)
- Histórico com calendário/timeline
- Dashboard com gráficos de aderência
- Lista de alertas

### 2. Funcionalidades Essenciais

✅ **Cadastrar medicamentos**
- Nome, tipo (vitamina, ferro, etc.)
- Dosagem padrão
- Frequência típica
- Cuidados especiais (ex: "tomar com alimento", "pode manchar dentes")
- Efeitos colaterais comuns

✅ **Criar prescrições**
- Vincular medicamento a um paciente
- Definir dosagem específica
- Horários de administração
- Data de início e fim do tratamento
- Quantidade total prescrita (para controle de estoque)

✅ **Registrar administração**
- Marcar como "Administrado", "Esquecido" ou "Recusado"
- Adicionar observações (ex: "bebê vomitou após", "dormiu antes do horário")
- Timestamp automático
- Permitir registro retroativo (esqueceu de marcar)

✅ **Visualizar histórico**
- Ver todas as administrações de um paciente
- Filtrar por medicamento, período
- Calcular taxa de aderência (% de doses tomadas vs. prescritas)
- Gráfico de evolução (melhorou? piorou?)

✅ **Sistema de alertas**
Gerar alertas automáticos para:
- **Doses esquecidas**: 2+ doses seguidas não registradas = alerta MÉDIO
- **Padrão de esquecimento**: esquece sempre no mesmo horário = alerta BAIXO
- **Possível superdosagem**: doses muito próximas = alerta ALTO
- **Estoque acabando**: menos de 7 dias de medicamento = alerta BAIXO
- **Recusas frequentes**: bebê recusou 3+ vezes = alerta MÉDIO

### 3. Testes

Criar testes automatizados para:
- Models (cálculo de aderência, validações)
- Views (criar prescrição, registrar administração)
- Sistema de alertas (verificar se regras funcionam corretamente)
- Lógica de detecção de padrões

**Mínimo esperado:** 10 testes cobrindo funcionalidades principais

### 4. Documentação

Criar arquivo `COMO_USAR.md` explicando:
- Como rodar o projeto
- Como cadastrar um medicamento
- Como criar uma prescrição
- Como registrar administração
- Como funciona o sistema de alertas
- Como popular com dados de teste

---

## 🎁 Entrega Extra (Opcional - Aumenta nota)

### Modelo de IA/ML para Predição e Alertas Inteligentes

Implementar modelo que analisa padrões de administração e:
- **Prediz não-aderência**: identifica famílias com risco de abandonar tratamento
- **Detecta excesso/falta de medicação**: padrões anormais de administração
- **Alerta inteligente**: prevê quando um paciente vai esquecer (baseado no histórico)
- **Recomenda melhor horário**: sugere horários com maior taxa de sucesso

**Sugestões de abordagem:**
- Classificação binária: vai aderir ou não?
- Séries temporais: predição de próxima administração
- Usar scikit-learn ou até LSTM (se tiver tempo)
- Treinar com dados sintéticos de padrões diversos

**Entregáveis do ML:**
- Notebook Jupyter (`analise_ml.ipynb`) com experimentação
- Script Python (`modelo.py`) integrado ao Django
- Documentação explicando o modelo

---

## 📁 Estrutura de Arquivos Esperada
```
karu-alpha
/
├── README.md (este arquivo)
├── COMO_USAR.md
├── manage.py
├── medicacoes/
│   ├── models.py (Medicamento, Prescricao, Administracao, Alerta)
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   ├── templates/
│   │   ├── medicamento_lista.html
│   │   ├── prescricao_criar.html
│   │   ├── administracao_registrar.html
│   │   ├── historico.html
│   │   ├── dashboard.html
│   │   └── alertas.html
│   ├── tests.py
│   └── migrations/
├── requirements.txt
└── [opcional] ml/
    ├── analise_ml.ipynb
    └── modelo.py
```

---

## ✅ Checklist de Entrega

- [ ] Projeto Django roda sem erros
- [ ] Models criados e migrados
- [ ] Sistema de medicações funciona (cadastrar, prescrever, administrar)
- [ ] Cálculo de aderência implementado
- [ ] Sistema de alertas automáticos funcionando
- [ ] Dashboard com visualizações
- [ ] Pelo menos 10 testes escritos
- [ ] Testes passando (`python manage.py test`)
- [ ] `COMO_USAR.md` com instruções claras
- [ ] `requirements.txt` atualizado
- [ ] **[Opcional]** Modelo ML implementado e documentado

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

- **Mobile-first**: Pais vão registrar no celular, com uma mão, bebê na outra
- **Simplicidade**: 3 botões grandes > formulário complexo
- **Dados realistas**: Criem fixtures com Ferro, Vitamina D, etc.
- **Horários flexíveis**: Nem sempre conseguem dar no horário exato
- **ML é extra**: Só faça se o básico estiver perfeito
- **Perguntem**: Usem as reuniões para tirar dúvidas

---

## 📊 Exemplo de Taxa de Aderência
```python
# Exemplo de cálculo
doses_prescritas = 30  # 1x/dia por 30 dias
doses_administradas = 25  # registrou 25 vezes
doses_esquecidas = 3
doses_recusadas = 2

aderencia = (doses_administradas / doses_prescritas) * 100
# aderencia = 83.3%
```

---

## 🚨 Critérios de Reprovação

❌ Não entregar código funcionando  
❌ Sistema não consegue registrar/visualizar administrações  
❌ Menos de 5 testes ou testes não passando  
❌ Sem documentação de como usar  
❌ Não participar das reuniões/checkpoints