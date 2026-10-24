# Publicar e distribuir a skill

## Objetivo
Tornar código, documentação e skill instalável publicamente acessíveis sem confundir **publicação no GitHub** com **publicação no catálogo interno do Claude**.

## 1. Distribuir publicamente no GitHub
O repositório https://github.com/Ridd1kulusC0d3r/academic-research-architect é público. Qualquer pessoa pode baixar o código, revisar as instruções e gerar seu próprio pacote ZIP.

A licença MIT permite redistribuição sob suas condições. Leia também SECURITY.md antes de instalar scripts de terceiros.

## 2. Gerar o ZIP da skill
Execute da raiz do repositório:

~~~bash
python3 scripts/validate_skill.py
python3 scripts/package_skill.py
~~~

O pacote instalável é `dist/academic-research-architect.zip`, contendo exatamente a pasta `academic-research-architect/` e seus conteúdos. O ZIP completo do repositório **não** deve ser enviado para o Claude.

## 3. Publicar um arquivo distribuível
É possível anexar o ZIP produzido a uma **Release** do GitHub. O workflow de validação incluído testa a estrutura no push/PR, mas **não cria uma Release automaticamente**. Para lançamentos, gerar o ZIP, criar a release e anexar o pacote após revisão humana.

## 4. Habilitar site público (GitHub Pages)
1. Acesse o repositório → **Settings** → **Pages**.
2. Em **Build and deployment**, selecione **Deploy from a branch**.
3. Escolha branch **main** e pasta **/docs**, depois salve.
4. Aguarde o GitHub Pages publicar e verifique a URL fornecida na página de configuração.
5. O arquivo de entrada é `docs/index.html`; o configurador funciona inteiramente no navegador, sem backend.

O GitHub Pages não é ativado pelo simples commit de `docs/index.html`. Esta configuração deve ser realizada por alguém com permissão.

## 5. Compartilhamento pelo Claude
No Claude.ai, o caminho descrito oficialmente é **Personalizar → Skills** para upload e gerenciamento. Em planos Team/Enterprise, as opções de compartilhar/publicar podem distribuir skills **dentro da organização**, com políticas específicas. Isso não garante que uma skill esteja disponível para todas as contas Claude públicas.

## 6. Atualizações
Versionar SKILL.md e CHANGELOG. Antes de promover uma release, validar compatibilidade, exemplos e documentação. Usuários do ZIP deverão reinstalar ou atualizar conforme o mecanismo suportado pelo Claude; não presumir atualizações automáticas do pacote baixado do GitHub.

## 7. Branding e posicionamento
- Nome público: Academic Research Architect
- Slug: academic-research-architect
- Slogan: “Planeje com método. Escreva com evidências. Publique com rigor.”
- Distinção: motor de pesquisa baseado em evidências, não gerador irrestrito de páginas.
- Identidade independente: não usar selos que insinuem certificação da Anthropic/IEEE.

## Fontes
- https://support.claude.com/pt/articles/12512180-usar-skills-no-claude
- https://support.claude.com/pt/articles/12512198-como-criar-habilidades-personalizadas
- https://claude.com/resources/guides/the-complete-guide-to-building-skills-for-claude/distribution-and-sharing
- https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site

