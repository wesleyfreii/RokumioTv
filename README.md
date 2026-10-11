# Rokumio — Site de documentação

Site oficial de documentação do projeto Rokumio. Estático, responsivo, em português (Brasil), sem frameworks e sem etapas de compilação.

## Páginas
- Início: `index.html`
- Política de Privacidade: `privacidade/index.html`
- Termos e Condições: `termos/index.html`
- Suporte: `suporte/index.html`

O CSS está em `assets/style.css`. **Todos os links e recursos são relativos à localização do HTML**, permitindo abrir `index.html` localmente, publicar na raiz de uma hospedagem como a Vercel ou hospedar em um subdiretório no GitHub Pages.

## Responsável público e suporte
- Projeto/canal: Rokumio
- Perfil público do mantenedor: https://github.com/wesleyfreii
- Canal de suporte: https://github.com/wesleyfreii/RokumioTv/issues

### Antes de usar as páginas na submissão final da loja Roku
O mantenedor **não forneceu ainda** o nome civil/empresarial e um e-mail ou outro meio privado adequado para pedidos de privacidade; ambos são relevantes para finalizar a identificação legal e o contato. **Não invente essas informações.** Atualize os documentos com os dados reais.

As informações sobre funcionalidades foram baseadas no pacote do aplicativo Roku fornecido localmente: o código inclui conexões de bibliotecas Jellyfin e complementos compatíveis com o formato Stremio. Confirme se a versão efetivamente enviada à loja corresponde a essas funcionalidades, quais dados e tokens são transmitidos, se há SDK de anúncios/análise, política para menores, práticas de retenção, fontes de conteúdo e eventuais assinaturas. O conteúdo deve ser revisto antes de informar as URLs à Roku. Esta documentação não é parecer jurídico e não garante aprovação na loja.

## Publicação

### GitHub Pages (grátis)
Em Settings > Pages, escolha Deploy from a branch, branch `main` e pasta `/ (root)`. Os caminhos terão o formato:
- `https://wesleyfreii.github.io/RokumioTv/`
- `https://wesleyfreii.github.io/RokumioTv/privacidade/`
- `https://wesleyfreii.github.io/RokumioTv/termos/`

### Vercel
Importe `wesleyfreii/RokumioTv` e use preset "Other" (site HTML estático), diretório raiz, sem build command. Na raiz do site implantado, utilize os caminhos `/privacidade/` e `/termos/`.

## Teste local
Execute `python3 -m http.server 8000` na pasta raiz e visite http://localhost:8000/.

O site, por si só, não adiciona cookies, rastreadores, publicidade, login ou formulários. O host pode produzir logs técnicos de acesso.
