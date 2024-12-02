# Inventário de Materiais

## Tema:
Sistema para reutilização de materiais entre projetos de instalação de estruturas submarinas no setor de óleo e gás.

## Funcionalidades:
- **Usuários** pertencem a **grupos (projetos)** e podem **criar itens** no inventário.
- Cada **item** possui campos como data de disponibilidade, localização e custo.
- **Usuários** podem **alterar a localização** de itens e **fazer reservas** nas datas disponíveis.
- **Consulta de reservas** feitas para os itens do projeto.
- **KPIs** por projeto (quantidade de itens, vendas e compras entre projetos).

## Páginas:
- **Login**: Permite autenticação de usuários.
- **Página Inicial**: Visão geral do sistema.
- **Itens**: Tabela com itens, possibilidade de filtro e alteração de localização em massa.
- **Item**: Detalhes do item e reservas.
- **Reserva**: Escolha da data para reserva.
- **Projeto**: Exibe KPIs (quantidade de itens, vendas, compras, etc.).

## Funcionalidades Implementadas:
- Login e página inicial.
- Cadastro, deleção e alteração de localização de itens.
- Reserva de itens e consulta de reservas.
- Página de projeto com informações de itens e KPIs.

## Funcionalidades Pendentes:
- Filtragem avançada de itens.
- Exibição completa de KPIs do projeto.
- Transações financeiras para transferências de itens entre projetos.

## Componentes do Grupo:
- **Lucas [Seu Nome]**: Backend (Django).
- **[Nome do colega]**: Frontend.
- **[Nome do colega]**: Banco de dados e autenticação.