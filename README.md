# 🛍️ **Marketplace App**

Este é um aplicativo web desenvolvido em Flask, que funciona como um marketplace onde os usuários podem registrar-se, vender, comprar, e interagir com produtos. Ele suporta funcionalidades como registro/login de usuários, listagem e busca de produtos, notificações em tempo real, e muito mais.

---

## 🔧 **Funcionalidades**

### **Funcionalidades Principais**
1. **Registro e Login:**
   - Registro com validação de dados (nome, email, telefone, senha).
   - Login seguro com Flask-Login e autenticação de senha.

2. **Home Page:**
   - Visualização de produtos organizados por categorias.
   - Design intuitivo e dinâmico.

3. **Venda de Produtos:**
   - Formulário para cadastrar produtos com upload de imagem.
   - Dados como preço, categoria, e descrição são salvos no banco de dados.

4. **Visualização de Produtos:**
   - Página de detalhes de produtos individuais.
   - Integração com base64 para exibir imagens armazenadas no banco de dados.

5. **Notificações:**
   - Sistema de notificações em tempo real com Flask-SocketIO.

6. **Página do Perfil:**
   - Visualização dos detalhes do usuário e seus produtos à venda.

7. **Meus Produtos e Produtos Gostados:**
   - Visualização personalizada de produtos cadastrados pelo usuário.
   - Página de produtos marcados como favoritos.

### **Funcionalidades Avançadas**
- **Filtragem por Categoria:** Produtos podem ser filtrados diretamente na loja.
- **Sistema de Notificações em Tempo Real:** Notificações automáticas enviadas quando um produto é marcado como interessante.
- **Rota Dinâmica:** Acesso fácil a páginas específicas como perfil e produtos via ID.

---

## ⚙️ **Requisitos**

### **Linguagens e Frameworks:**
- Python 3.9+
- Flask
- Flask-Login
- Flask-SocketIO
- Flask-WTF

### **Dependências Adicionais:**
- `email-validator` para validação de email.
- `Werkzeug` para upload seguro de arquivos.
- `base64` para conversão de imagens para exibição.

### **Banco de Dados:**
- SQLAlchemy como ORM para interação com banco de dados.
