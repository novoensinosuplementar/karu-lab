BEGIN TRANSACTION;

--------------------------------------------------------
-- CATEGORIAS
--------------------------------------------------------

INSERT INTO questionarios_questioncategory (name, frequency) VALUES
("Saúde mental materna", "Semanal"),
("Adaptação familiar / rede de apoio", "Mensal"),
("Nutrição / aleitamento materno", "Semanal"),
("Adaptação", "Semanal"),
("Desenvolvimento sensorial e motor", "Mensal"),
("Saúde", "Mensal"),
("Adesão ao tratamento", "Semanal");

--------------------------------------------------------
-- PERGUNTAS
--------------------------------------------------------

-- Categoria 1: Saúde mental materna
INSERT INTO questionarios_question (text, category_id) VALUES
("Como você está se sentindo? Você tem sentido ansiedade, tristeza ou alguma outra coisa?", 20),
("Você se sente confiante para cuidar do bebê em casa?", 20),
("Você tem conseguido descansar e dormir o suficiente?", 20),
("Você tem alguém com quem conversar sobre suas preocupações e sentimentos?", 20);

-- Categoria 2: Adaptação familiar / rede de apoio
INSERT INTO questionarios_question (text, category_id) VALUES
("Quem está te ajudando em casa com o bebê e as atividades gerais?", 21),
("Há apoio familiar ou emocional suficiente para lidar com os cuidados diários?", 21),
("Você tem feito contato pele a pele com o bebê (posição canguru)?", 21),
("Você conversa, canta ou brinca com o bebê durante o dia?", 21);

-- Categoria 3: Nutrição / aleitamento materno
INSERT INTO questionarios_question (text, category_id) VALUES
("O bebê tem se alimentado bem? Quantas vezes por dia mais ou menos?", 22),
("Há dificuldade para sugar, respirar ao se alimentar? O bebê costuma se engasgar?", 22);

-- Categoria 4: Adaptação
INSERT INTO questionarios_question (text, category_id) VALUES
("O bebê costuma acordar para se alimentar?", 23),
("O bebê chora mais que o habitual ou parece muito sonolento?", 23),
("O sono do bebê está regulado?", 23);

-- Categoria 5: Desenvolvimento sensorial e motor
INSERT INTO questionarios_question (text, category_id) VALUES
("O bebê responde a sons? ex: vira a cabeça, pisca, se assusta", 24),
("Você percebe que o bebê fixa o olhar ou segue objetos com os olhos?", 24),
("O bebê movimenta braços e pernas igualmente?", 24),
("O bebê apresenta ganho de peso? Está de acordo com o esperado?", 24),
("O bebê reage a sons (vira a cabeça, pisca, se assusta)?", 24),
("O bebê fixa o olhar ou acompanha objetos com os olhos?", 24),
("O bebê movimenta braços e pernas igualmente?", 24);

-- Categoria 6: Saúde
INSERT INTO questionarios_question (text, category_id) VALUES
("O bebê apresenta alguma dificuldade respiratória (chiado, respiração rápida)?", 25),
("Teve febre ou alguma intercorrência (ex: tosse, diarreia, vômitos)?", 25),
("Como está o sono do bebê (horas dormidas e despertares noturnos)?", 25),
("O bebê tem apresentado refluxo, regurgitação frequente ou dificuldade para manter o alimento?", 25),
("A pele do bebê está com boa coloração (sem palidez, manchas ou icterícia)?", 25);

-- Categoria 7: Adesão ao tratamento
INSERT INTO questionarios_question (text, category_id) VALUES
("O bebê tem contato pele a pele com os pais (posição canguru)?", 26),
("Você tem conseguido administrar os medicamentos do bebê conforme a orientação médica?", 26),
("Você tem conseguido comparecer às consultas e retornos agendados do bebê?", 26);

commit;
