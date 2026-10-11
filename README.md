# Site legal do Rokumio

Site estático responsivo em português com três páginas:

- `index.html`: página inicial.
- `privacidade/index.html`: Política de Privacidade.
- `termos/index.html`: Termos e Condições.

## IMPORTANTE: personalização antes de publicar

Os textos são **modelos**, não uma avaliação jurídica nem uma descrição verificada do app. Faça busca nos arquivos `.html` por `[` e `]`, revise **todos** os campos destacados (incluindo titular, endereço de e-mail de contato, práticas reais de dados, terceiros, retenção, perfil etário, situação dos direitos dos conteúdos, assinaturas/monetização e funcionalidades).

Remova os avisos de "modelo" das páginas **somente depois** de verificar e preencher os fatos. Na página de privacidade, descreva com precisão as práticas dos serviços integrados ao canal, incluindo possíveis anúncios, analytics, SDKs e identificadores do dispositivo. Atualize as datas quando publicar a versão final. Se houver uso de conta, login, pagamentos ou coleta de dados de crianças, complemente as seções correspondentes. Considere uma revisão jurídica antes da publicação.

## Publicar na Vercel sem pagar hospedagem

1. Crie um repositório no GitHub e envie **os arquivos e pastas de dentro desta pasta** (sem colocar todos os arquivos dentro de uma pasta extra no repositório).
2. Acesse https://vercel.com, entre com o GitHub e escolha **Add New > Project**.
3. Importe o repositório. Para um site HTML simples, selecione **Other** se necessário, deixe Build Command vazio e use o diretório raiz como Output Directory.
4. Clique em **Deploy**. A plataforma fornecerá uma URL pública com HTTPS, como `seu-projeto.vercel.app`.
5. Teste os seguintes endereços públicos:
   - `https://SEU-PROJETO.vercel.app/privacidade/`
   - `https://SEU-PROJETO.vercel.app/termos/`
6. Cole cada URL em seu campo correspondente no cadastro do canal Roku.

Também é possível hospedar o site no Cloudflare Pages ou no GitHub Pages, com eventuais ajustes de configuração. Planos gratuitos estão sujeitos às condições dos provedores; o Hobby da Vercel pode ter restrições de uso comercial.

## Teste local

Na pasta do projeto, rode:

```bash
python -m http.server 8000
```

Abra `http://localhost:8000/`.

## Tecnologia

HTML + CSS puros. Sem backend, conta, banco de dados, bibliotecas externas, rastreadores ou cookies adicionados pelo código do site. O serviço de hospedagem pode coletar logs técnicos.
