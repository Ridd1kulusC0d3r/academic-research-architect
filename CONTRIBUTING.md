# Contribuindo com Academic Research Architect

## Proposta
Aceitamos correções de metodologia, normalização editorial, traduções, melhorias de acessibilidade, testes e exemplos documentados.

## Antes de um PR
1. Abra uma issue descrevendo o problema ou proposta.
2. Anexe fonte oficial para mudanças de normas e políticas de periódicos.
3. Preserve a divisão estrutura científica / layout editorial / sistema bibliográfico.
4. Nunca inclua fontes bibliográficas, DOI ou números de estudos não verificados.
5. Execute `python scripts/validate_skill.py` e `python -m unittest discover -s tests`.
6. Atualize documentação e CHANGELOG quando alterar comportamento.

## Convenções
- Portuguese (pt-BR) como idioma principal; termos internacionais são aceitos.
- Skill em pasta instalável com SKILL.md e referências modulares.
- Exemplos com marcadores de lacunas e sem resultados empíricos inventados.
- Não usar marcas de terceiros como selo de certificação.

## Licença
Contribuições são disponibilizadas sob MIT, de acordo com LICENSE.

