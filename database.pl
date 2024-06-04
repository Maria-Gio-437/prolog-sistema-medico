% Definição de sintomas
sintoma(dor_nas_articulacoes).
sintoma(tosse_com_catarro).
sintoma(tosse_seca).
sintoma(tosse_forte).
sintoma(tosse_leve).
sintoma(calafrios).
sintoma(desidratacao).
sintoma(fadiga).
sintoma(febre).
sintoma(mal_estar).
sintoma(perda_de_apetite).
sintoma(rubor).
sintoma(dor_no_corpo).
sintoma(suor).
sintoma(congestao_nasal).
sintoma(nariz_escorrendo).
sintoma(espirros).
sintoma(dor_de_garganta).
sintoma(irritacao_na_garganta).
sintoma(dor_de_cabeca).
sintoma(falta_de_ar).
sintoma(fraqueza_muscular).
sintoma(inchaco_dos_ganglios).
sintoma(nausea).
sintoma(pressao_no_peito).
sintoma(dor_nos_musculos).
sintoma(dor_nos_ouvidos).
sintoma(dor_nos_seios_paranasais).
sintoma(cansaso_extremo).
sintoma(perda_de_olfato).
sintoma(vermelhidao_no_nariz).
sintoma(gotejamento_pos_nasal).
sintoma(olhos_marejados).
sintoma(privacao_de_sono).
sintoma(dor_atras_dos_olhos).
sintoma(dor_nas_costas).
sintoma(dor_no_abdomen).
sintoma(dor_nos_ossos).
sintoma(dor_forte_nas_articulacoes).
sintoma(tremor).
sintoma(manchas_avermelhadas).
sintoma(dor_no_peito).
sintoma(tontura).
sintoma(zumbido).
sintoma(sangramento_nasal).
sintoma(cansaco).
sintoma(inchacos).
sintoma(perda_de_peso).
sintoma(suor_noturno).
sintoma(perda_de_paladar).
sintoma(vomito).
sintoma(diarreia).
sintoma(olhos_vermelhos).
sintoma(irritacao_na_pele).
sintoma(conjuntivite).
sintoma(dor_nos_dentes).
sintoma(secrecao_nasal_espessa).
sintoma(secrecao_nasal_amarelada).
sintoma(secrecao_nasal_esverdeada).
sintoma(secrecao_nasal_com_sangue).
sintoma(dor_no_rosto).
sintoma(coceira_no_nariz).
sintoma(coriza).
sintoma(olhos_umidos).
sintoma(olhos_com_coceira).
sintoma(visao_embacada).
sintoma(sensibilidade_a_luz).
sintoma(nariz_entupido).
sintoma(rinorreia).
sintoma(secrecao_intensa_anoite).
sintoma(secrecao_nos_olhos_esverdeada).
sintoma(olhos_lacrimejando).
sintoma(coceira_nos_olhos).
sintoma(irritacao_nos_olhos).


% Definição de doenças e seus sintomas associados
doenca(gripe, [dor_nas_articulacoes, tosse_com_catarro, tosse_seca, tosse_forte, tosse_leve, calafrios, desidratacao, fadiga, febre, mal_estar, perda_de_apetite, rubor, dor_no_corpo, suor, congestao_nasal, nariz_escorrendo, espirros, dor_de_garganta, irritacao_na_garganta, dor_de_cabeca, falta_de_ar, fraqueza_muscular, inchaco_dos_ganglios, nausea, pressao_no_peito]).
doenca(resfriado, [dor_nos_musculos, dor_nos_ouvidos, dor_nos_seios_paranasais, tosse_seca, calafrios, cansaso_extremo, fadiga, febre, mal_estar, perda_de_apetite, dor_no_corpo, sentindo_frio, suor, congestao_nasal, nariz_escorrendo, perda_de_oufato, vermelhidao_no_nariz, espirros, gotejamento_pos_nasal, dor_de_garganta, irritacao_na_garganta, garganta_seca, dor_de_cabeca, inchaco_dos_ganglios, olhos_marejados, pressao_no_peito, privacao_de_sono]).
doenca(dengue, [dor_nos_musculos, dor_atras_dos_olhos, dor_nas_costas, dor_no_abdomen, dor_nos_ossos, dor_forte_nas_articulacoes, febre, fadiga, mal_estar, perda_de_apetite, tremor, suor, dor_de_cabeca, manchas_avermelhadas, nausea]).
doenca(pneumonia, [tosse_com_catarro, febre, falta_de_ar, dor_no_peito, mal_estar]).
doenca(hipertensao_arterial, [dor_de_cabeca, tontura, zumbido, sangramento_nasal]).
doenca(insuficiencia_cardiaca, [falta_de_ar, cansaco, inchacos, tosse_com_catarro]).
doenca(tuberculose, [tosse_com_catarro, febre, perda_de_peso, suor_noturno, cansaco]).
doenca(covid, [febre, tosse_seca, cansaco, perda_de_olfato, perda_de_paladar, dor_de_garganta, dor_de_cabeca, dor_no_corpo, falta_de_ar, perda_de_apetite, nausea, vomito, diarreia]).
doenca(zika, [febre, irritacao_na_pele, dor_nas_articulacoes, conjuntivite, olhos_vermelhos, dor_nos_musculos, dor_de_cabeca, dor_atras_dos_olhos, vomito]).
doenca(conjuntivite, [olhos_vermelhos, irritacao_nos_olhos, coceira_nos_olhos, olhos_lacrimejando, secrecao_nos_olhos_esverdeada, secrecao_intensa_anoite, visao_embacada, sensibilidade_a_luz]).
doenca(rinite, [nariz_entupido, congestao_nasal, espirros, rinorreia, gotejamento_pos_nasal, coceira_no_nariz, coriza, dor_de_cabeca, olhos_umidos, olhos_vermelhos, olhos_com_coceira]).
doenca(sinusite, [secrecao_nasal_espessa, secrecao_nasal_amarelada, secrecao_nasal_esverdeada, secrecao_nasal_com_sangue, nariz_entupido, congestao_nasal, dor_no_rosto, dor_de_cabeca, dor_nos_dentes, tosse, perda_de_olfato, perda_de_paladar]).

% Regra para verificar se uma lista de sintomas corresponde a uma doença
diagnostico(Sintomas, Doenca) :-
    doenca(Doenca, SintomasDoenca),
    subset(Sintomas, SintomasDoenca).

% Função auxiliar para verificar se uma lista é subconjunto de outra
subset([], _).
subset([H|T], List) :-
    member(H, List),
    subset(T, List).
