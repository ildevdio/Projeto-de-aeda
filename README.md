📌 Guia Básico para Trabalhar em Grupo no GitHub
1. Clonar o Repositório (Baixar o Projeto)
Se alguém já criou o projeto no GitHub, você precisa baixar (clonar) para seu computador:

bash
git clone https://github.com/nome-do-grupo/nome-do-projeto.git
cd nome-do-projeto  # Entra na pasta do projeto
2. Criar uma Branch (Área de Trabalho Separada)
Nunca trabalhe direto na main ou master! Crie sua própria branch (como um "rascunho" separado):

bash
git checkout -b minha-branch  # Cria e entra na sua branch
3. Fazer Alterações no Código
Agora você pode:

Criar/editar/deletar arquivos

Salvar normalmente (Ctrl+S)

4. Salvar as Alterações Localmente (Commit)
Quando terminar uma parte do trabalho, "salve" suas mudanças no Git:

bash
git add .  # Marca TODAS as alterações para commit
git commit -m "Adicionei o botão de login"  # Salva com uma mensagem
5. Enviar para o GitHub (Push)
Agora, envie suas alterações para o repositório do grupo:

bash
git push origin minha-branch  # Envia sua branch para o GitHub
6. Criar um Pull Request (Pedido para Adicionar seu Código ao Projeto Principal)
Vá no repositório no GitHub

Clique em "Pull Requests" → "New Pull Request"

Selecione:

Base: main (ou master)

Compare: minha-branch

Escreva uma descrição clara do que você fez

Clique em "Create Pull Request"

✅ Pronto! Agora um colega do grupo pode revisar e aprovar seu código.

🔄 Como Atualizar Seu Código Quando o Projeto Avançar?
Se alguém do grupo fez alterações no main, você precisa atualizar sua branch:

Volte para a main e pegue as atualizações:

bash
git checkout main           # Volta para a main
git pull origin main        # Pega as últimas alterações
Agora, volte para SUA branch e atualize:

bash
git checkout minha-branch   # Volta para sua branch
git merge main              # Atualiza com as mudanças da main
Se der conflito, edite os arquivos marcados, salve e depois:

bash
git add .  
git commit -m "Resolvi conflitos"  
git push origin minha-branch  
📌 Resumo do Fluxo Básico
git clone (baixa o projeto)

git checkout -b minha-branch (cria sua área de trabalho)

Edita os arquivos

git add . + git commit -m "mensagem" (salva localmente)

git push origin minha-branch (envia para o GitHub)

Cria um Pull Request no GitHub

Dica Extra
Se você só quer praticar, crie um repositório teste no seu GitHub e tente:

Clonar

Criar uma branch

Fazer commits

Enviar e fazer um PR
