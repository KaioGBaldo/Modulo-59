# 🏬 Django Relational Models - Gestão de Estoque e Produtos

Este projeto explora a camada de **Models** do Django para criar um sistema de banco de dados relacional. O foco principal é a implementação de relacionamentos "Um para Muitos" (One-to-Many) e a automação da interface administrativa para gestão de inventário.

---

# 📝 Resumo (Resume)
Neste projeto, desenvolvi uma estrutura de dados onde a entidade **Estoque** é vinculada à entidade **Produto** através de uma **ForeignKey**. Essa arquitetura permite que cada produto possua múltiplos registros de estoque em diferentes locais, garantindo a normalização do banco de dados. Utilizei campos especializados como `DecimalField` para valores monetários e `DateTimeField` com `auto_now_add` para auditoria temporal automática. Além disso, configurei o `admin.py` para permitir que esses dados sejam gerenciados de forma visual e intuitiva através do painel administrativo nativo do Django.



## 🚀 Tecnologias e Ferramentas (Tech Stack)

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)

## 📋 Funcionalidades em Destaque
* **Relacionamento ForeignKey:** Implementação de chaves estrangeiras com a regra `on_delete=models.CASCADE`, garantindo que o estoque seja removido automaticamente caso o produto seja excluído.
* **Auditoria Automática:** Uso de `DateTimeField(auto_now_add=True)` para capturar instantaneamente a data e hora de criação de cada registro.
* **Interface Administrativa (CRUD Visual):** Registro de modelos no Django Admin, permitindo a criação, leitura, atualização e exclusão de dados sem escrever uma linha de SQL.
* **Representação de Objetos (__str__):** Sobrescrita do método string para fornecer nomes amigáveis aos registros dentro do painel administrativo e logs do sistema.
* **Tipagem de Dados Precisa:** Uso de `DecimalField` para evitar erros de arredondamento em cálculos financeiros e `IntegerField` para controle exato de unidades.
* **Roteamento de Views:** Configuração de `urlpatterns` para vincular URLs lógicas a funções de visualização, preparando o terreno para a entrega de dados via Web.



---

# 👨‍💻 Sobre mim (About Me)
Olá, meu nome é **Kaio**, tenho 22 anos. Como meu foco principal é o **Back-End com Python**, dominar relacionamentos relacionais é fundamental. No Front-End com **React**, eu manipulava objetos isolados; agora, no Back-End, aprendi a construir a inteligência por trás desses dados, conectando diferentes tabelas para refletir regras de negócio reais. Esta habilidade de estruturar bancos de dados relacionais é o que me permite criar sistemas complexos, escaláveis e seguros para o mundo real.

### Entre em contato (Contact me)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-000?style=for-the-badge&logo=linkedin&logoColor=092E20)](https://linkedin.com/in/kaio-grativol-baldo-071a74150/)
[![Instagram](https://img.shields.io/badge/Instagram-000?style=for-the-badge&logo=instagram&logoColor=092E20)](https://www.instagram.com/kaiull__/)
[![GitHub](
