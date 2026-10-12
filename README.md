# Rokumio

Site oficial de documentação do Rokumio, aplicativo para Roku.

> **Escopo deste repositório:** contém o site público (HTML/CSS), as páginas legais e a central de suporte. **Não contém o código-fonte do canal Roku (BrightScript/SceneGraph).** Alterações na reprodução, catálogo, login e interface da TV precisam ser feitas no repositório do aplicativo.

## Páginas

- [Início](https://wesleyfreii.github.io/RokumioTv/)
- [Privacidade](https://wesleyfreii.github.io/RokumioTv/privacidade/)
- [Termos de uso](https://wesleyfreii.github.io/RokumioTv/termos/)
- [Suporte e soluções rápidas](https://wesleyfreii.github.io/RokumioTv/suporte/)

## Desenvolvimento

Site estático em HTML e CSS, sem dependências JavaScript, compatível com GitHub Pages e hospedagem estática como Vercel.

Para visualizar localmente, execute na raiz do repositório:

```bash
python3 -m http.server 8000
```

Abra `http://localhost:8000`. Para verificar os links internos e a estrutura básica de acessibilidade:

```bash
python3 scripts/check_site.py
```

O GitHub Actions executa essa verificação em alterações enviadas e pull requests.

## Relatar problemas

Use os [formulários de issues](https://github.com/wesleyfreii/RokumioTv/issues/new/choose). Informe modelo do dispositivo, versão e passos para reproduzir. **Não compartilhe senhas, tokens, links privados ou dados pessoais em issues públicas.**

Antes de publicar ou atualizar o canal na loja Roku, revise os textos legais e os dados de contato privado com o responsável pelo projeto.
