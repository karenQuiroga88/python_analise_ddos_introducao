# Roadmap para Uso do GitHub

## Introdução
Este roadmap tem como objetivo ensinar os principais comandos e práticas para usar o GitHub de forma eficiente. 

## O que é o GitHub?
O GitHub é uma plataforma de hospedagem de código-fonte com controle de versão usando o Git. Ele permite que desenvolvedores colaborem em projetos de software de qualquer lugar do mundo. Além de servir como repositório de código, o GitHub oferece ferramentas para gerenciamento de projetos, revisão de código, e até mesmo hospedagem de sites estáticos.

## Configurando sua Conta no GitHub
1. Acesse [GitHub](https://github.com) e clique em **Sign up**.
2. Siga os passos para criar sua conta.
3. Verifique seu e-mail para confirmar a criação da conta.
4. Complete seu perfil com informações como foto, bio, e links para redes sociais.

## Instalação e Configuração do Git

### Instalar o Git
Baixe e instale o Git a partir de [git-scm.com](https://git-scm.com/downloads). Siga as instruções para o seu sistema operacional.

### Configurar o Git
Após a instalação, configure seu nome de usuário e email:

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seuemail@exemplo.com"
```

Verifique suas configurações:

```bash
git config --list
```

## Comandos Básicos de Git

### Clonar um Repositório
Para clonar um repositório existente:

```bash
git clone https://github.com/usuario/repo.git
```

### Verificar o Status dos Arquivos
Para verificar o status dos arquivos no seu repositório local:

```bash
git status
```

### Adicionar Arquivos ao Staging
Para adicionar arquivos modificados ao staging:

```bash
git add nome_do_arquivo
# Ou para adicionar todos os arquivos modificados
git add .
```

### Comitar as Mudanças
Para salvar as mudanças com uma mensagem de commit:

```bash
git commit -m "Mensagem do commit"
```

### Enviar Mudanças para o Repositório Remoto
Para enviar suas mudanças para o repositório remoto:

```bash
git push origin branch
```

### Puxar Mudanças do Repositório Remoto
Para atualizar seu repositório local com mudanças do repositório remoto:

```bash
git pull origin branch
```

### Verificar Logs de Commits
Para visualizar o histórico de commits:

```bash
git log
```

### Remover um Arquivo do Staging
Para remover um arquivo do staging:

```bash
git reset nome_do_arquivo
```

### Desfazer Modificações em um Arquivo
Para desfazer modificações em um arquivo que não foi adicionado ao staging:

```bash
git checkout -- nome_do_arquivo
```

## Trabalhando com Repositórios

### Criar um Novo Repositório no Site do GitHub
1. Acesse o GitHub e faça login.
2. No canto superior direito, clique no ícone de **+** e selecione **New repository**.
3. Preencha o nome do repositório e outras informações necessárias.
4. Clique em **Create repository**.

### Fork de um Repositório no Site do GitHub
Para fazer um fork de um repositório:
1. Vá até a página do repositório no GitHub.
2. Clique no botão **Fork** no canto superior direito.

### Clonar um Repositório
Para clonar o repositório forkado para seu computador:

```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
```

## Trabalhando com Branches

### Criar uma Nova Branch
Para criar uma nova branch:

```bash
git checkout -b nome-da-branch
```

### Trocar de Branch
Para trocar para uma branch existente:

```bash
git checkout nome-da-branch
```

### Listar Branches
Para listar todas as branches:

```bash
git branch
```

### Excluir uma Branch
Para excluir uma branch:

```bash
git branch -d nome-da-branch
```

### Mesclar Branches
Para mesclar uma branch na branch atual:

```bash
git merge nome-da-branch
```

## Comandos Avançados de Git

### Rebasing
Para rebasear sua branch atual com outra branch:

```bash
git rebase nome-da-branch
```

### Stash
Para salvar mudanças não comitadas em um stash temporário:

```bash
git stash
```

Para aplicar mudanças do stash:

```bash
git stash apply
```

### Cherry-pick
Para aplicar um commit específico de outra branch:

```bash
git cherry-pick commit_hash
```

### Reflog
Para visualizar o histórico de referências (inclusive referências excluídas):

```bash
git reflog
```

## Configuração de SSH

### Gerar Chave SSH
Para gerar uma nova chave SSH:

```bash
ssh-keygen -t rsa -b 4096 -C "seuemail@exemplo.com"
```

### Adicionar Chave SSH ao SSH-Agent
Para adicionar sua chave SSH ao ssh-agent:

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa
```

### Adicionar Chave SSH ao GitHub
1. Copie o conteúdo da sua chave pública SSH:

```bash
cat ~/.ssh/id_rsa.pub
```

2. No GitHub, vá até **Settings > SSH and GPG keys** e clique em **New SSH key**.
3. Cole a chave pública e clique em **Add SSH key**.

## Git Hooks

### O que são Git Hooks?
Git hooks são scripts que são executados automaticamente em pontos específicos do ciclo de vida do Git, como antes de um commit ou antes de um push.

### Exemplos de Git Hooks
Crie um arquivo `pre-commit` no diretório `.git/hooks`:

```bash
#!/bin/sh
# Verifica a formatação do código antes de cada commit
eslint .
```

Torne o script executável:

```bash
chmod +x .git/hooks/pre-commit
```

## Colaborando em Projetos com Pull Requests

### Criar um Pull Request no Site do GitHub
1. Faça um fork do repositório.
2. Clone o fork para seu computador.
3. Crie uma nova branch para suas mudanças.
4. Faça os commits e push para seu fork.
5. Vá até a página do repositório original e clique em **New pull request**.

### Revisar e Mesclar Pull Requests no Site do GitHub
1. Acesse a aba **Pull requests** no repositório.
2. Clique no pull request que deseja revisar.
3. Deixe comentários ou aprove as mudanças.
4. Clique em **Merge pull request** para mesclar as mudanças.

## Usando Issues para Gerenciar Tarefas

### Criar uma Issue no Site do GitHub
1. Acesse a aba **Issues** no repositório.
2. Clique em **New issue**.
3. Preencha o título e a descrição da issue.
4. Clique em **Submit new issue**.

### Gerenciar Issues no Site do GitHub
1. Acesse a aba **Issues**.
2. Clique na issue que deseja gerenciar.
3. Adicione comentários, assigne pessoas, e use labels para organização.

## Usando GitHub Pages para Sites Estáticos

### Configurar GitHub Pages no Site do GitHub
1. Acesse as configurações do repositório.
2. Role até a seção **GitHub Pages**.
3. Escolha a branch que deseja usar para GitHub Pages.
4. Clique em **Save**.

### Acessar seu Site
Após configurar, seu site estará disponível em `https://seu-usuario.github.io/nome-do-repositorio/`.

## Boas Práticas no GitHub

### Mensagens de Commit Claras
Sempre escreva mensagens de commit claras e descritivas.

### Branches para Cada Funcionalidade
Crie branches diferentes para cada funcionalidade ou correção que você estiver trabalhando.

### Revisar Código
Sempre revise o código antes de fazer um merge para garantir a qualidade e evitar conflitos.

### Documentação
Mantenha uma boa documentação para facilitar a colaboração e entendimento do projeto.

### Usar Issues para Gerenciamento
Utilize issues para gerenciar tarefas e bugs, mantendo o acompanhamento do progresso do projeto.

## Exemplos de Fluxos de Trabalho (Workflows)

### Fluxo de Trabalho com Feature Branches
1. Crie uma nova branch para cada nova funcionalidade.
2. Faça commits pequenos e frequentes.
3. Abra um pull request para revisão de código.
4. Mescle a branch após a aprovação.

### Fluxo de Trabalho com Git Flow
1. Use branches dedicadas para desenvolvimento (`develop`) e produção (`main`).
2. Crie branches de feature a partir de `develop`.
3. Crie branches de release a partir de `develop`.
4. Crie branches de hotfix a partir de `main`.

## Recursos Adicionais

- [Documentação do Git](https://git-scm.com/doc)
- [Documentação do GitHub](https://docs.github.com/)
- [Pro Git Book](https://git-scm.com/book/en/v2)
- [Curso de Introdução ao Git e GitHub](https://www.coursera.org/learn/intro-to-git-and-github)
- [Tutoriais em Vídeo no YouTube](https://www.youtube.com/results?search_query=git+and+github+tutorial)
