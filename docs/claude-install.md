# Instalar Academic Research Architect no Claude

> Compatível com o formato aberto Agent Skills. A disponibilidade de interfaces e controles pode variar conforme versão, plano e políticas da organização.

## Caminho A: Claude.ai (chat web)

**Pré-requisito:** habilitar execução de código/criação de arquivos em Configurações → Capacidades. A Anthropic documenta Skills nos planos elegíveis, com gerenciamento em **Personalizar → Skills**.

1. Obtenha o repositório localmente pelo botão **Code → Download ZIP** do GitHub e extraia o arquivo; ou clone via Git.
2. **Não** envie o ZIP do repositório inteiro. Gere um ZIP contendo apenas a pasta interna `academic-research-architect/` como diretório-raiz.
3. Execute no computador com Python 3: `python scripts/package_skill.py`. O arquivo aparecerá em `dist/academic-research-architect.zip`.
4. Abra o Claude → **Personalizar → Skills** → botão **+** → **Criar skill** → **Fazer upload de uma skill**.
5. Envie o arquivo ZIP produzido, ative a skill e use uma das solicitações do guia de casos de uso.

### ZIP correto

~~~text
academic-research-architect.zip
└── academic-research-architect/
    ├── SKILL.md
    ├── references/
    └── assets/
~~~

O arquivo obrigatório se chama **SKILL.md** (maiúsculas). O diretório interno deve permanecer com o nome da skill. Não inclua README de repositório dentro da pasta da skill.

### Teste funcional
Peça: “Use academic-research-architect e proponha três estruturas para uma pesquisa em ciência de dados; não selecione OSINT.” Depois peça: “Agora aplique IEEE SMC 2025 a um artigo, distinguindo as regras de uma dissertação.”

## Caminho B: Claude Code (projeto)

No repositório do seu projeto, copie ou vincule a pasta instalável para:

~~~text
seu-projeto/
└── .claude/
    └── skills/
        └── academic-research-architect/
            ├── SKILL.md
            ├── references/
            └── assets/
~~~

Exemplo no terminal (macOS/Linux), executado **na raiz deste repositório**:

~~~bash
mkdir -p /caminho/do/seu-projeto/.claude/skills
cp -R academic-research-architect /caminho/do/seu-projeto/.claude/skills/
~~~

Abra o projeto no Claude Code e solicite: “Use academic-research-architect para auditar a seção 2.1”. A descoberta também pode ser automática quando o assunto corresponder à descrição.

## Caminho C: Claude Code (uso pessoal)

Coloque a mesma pasta em `~/.claude/skills/academic-research-architect/`. O diretório é por usuário; skills no projeto são por repositório.

## Compartilhamento vs publicação

- **Distribuição pública no GitHub:** qualquer pessoa pode baixar ou clonar e instalar por conta própria. Isso **não instala automaticamente** a skill nas contas Claude de outras pessoas.
- **Team/Enterprise:** autores e administradores podem usar mecanismos nativos de compartilhamento ou publicação **na organização**, sujeitos a permissões e revisão. Isso não equivale a um marketplace público universal.
- **Repositório público:** não implica que Anthropic tenha avaliado, recomendado ou adotado a skill.

## Solução de problemas

| Sintoma | Diagnóstico |
|---|---|
| Upload recusado | Confira estrutura do ZIP e o arquivo SKILL.md no diretório interno |
| Skill não ativa | Confira opção de execução de código, habilitação de Skills e políticas da conta |
| Claude não a invoca | Cite o nome explicitamente e avalie a descrição no frontmatter |
| Referências ausentes | Verifique se references/ e assets/ foram incluídos no ZIP |
| Claude escolheu OSINT sem pedir | Reforce “estrutura livre” e reporte falha no repositório |
| ZIP contém outra pasta superior | Gere com o script oficial, não use o download ZIP integral do GitHub |

## Fontes da Anthropic

- https://support.claude.com/pt/articles/12512198-como-criar-habilidades-personalizadas
- https://support.claude.com/pt/articles/12512180-usar-skills-no-claude
- https://code.claude.com/docs/en/skills
- https://agentskills.io/specification

