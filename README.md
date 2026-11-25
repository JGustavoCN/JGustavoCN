<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=00bfbf&height=120&section=header"/>

<div align="center">
  <img width="100%" src="./assets/bento/hero-blueprint.svg" alt="José Gustavo — Engenharia de Software" />

  <br/>

  <a href="https://git.io/typing-svg">
    <img src="https://readme-typing-svg.herokuapp.com/?color=00bfbf&size=28&center=true&vCenter=true&width=1000&lines=Ol%C3%A1,+meu+nome+%C3%A9+Jos%C3%A9+Gustavo;Formado+em+Sistemas+de+Informa%C3%A7%C3%A3o+no+Instituto+Federal;Full+Stack:+Java+|+DotNet+|+Go+|+TypeScript+|+React;Mobile+Dev+com+Flutter;Foco+em+Engenharia+de+Software+e+Performance;Seja+Bem-vindo!" alt="Typing SVG" />
  </a>
  <p><i>Combinando a robustez do <b>Java/C#</b> com a performance do <b>Go</b> e a agilidade do <b>TypeScript/React/Flutter</b>.</i></p>
  <p>
    <a href="https://www.linkedin.com/in/jgustavocn" target="_blank" rel="noopener noreferrer">
      <img src="./assets/bento/badge-linkedin.svg" alt="LinkedIn — /in/jgustavocn" />
    </a>
  </p>
</div>

---

## Projetos em Destaque

<sub>Clique em qualquer card para abrir o projeto, ou expanda abaixo de cada um para ver o motivo e os ganhos:</sub>

<table>
  <tr>
    <td colspan="6" align="center" valign="top">
      <a href="https://github.com/JGustavoCN/dataprofiler" target="_blank" rel="noopener noreferrer">
        <img src="./assets/bento/bento-dataprofiler.svg" alt="DataProfiler Enterprise — Pipeline Streaming O(1)" width="100%" />
      </a>
      <details>
        <summary><sub><b>Ver motivo, arquitetura e ganhos</b></sub></summary>
        <p align="left"><sub>
          <b>Por que foi feito:</b> Analisadores comuns (como Pandas) carregam arquivos inteiros em RAM, causando <i>Out-Of-Memory</i> em servidores de baixo custo.<br/>
          <b>Solução &amp; Engenharia:</b> Pipeline <i>Producer-Consumer</i> em Go com <code>sync.Pool</code> (zero-allocation), sniffer automático de encoding/separador, progresso via SSE e frontend React embutido via <code>//go:embed</code>.<br/>
          <b>Ganhos Reais:</b> Processa <b>10 GB (~120M linhas)</b> em container limitado a <b>512 MB de RAM</b> mantendo pico de apenas <b>~12 MB de Heap</b> (O(1)) e detecção nativa de padrões BR (CNPJ, CPF, NFe, Placas, CEP).<br/>
          <b>Acessos extras:</b> <a href="https://dataprofiler-jgustavocn.onrender.com" target="_blank" rel="noopener noreferrer">Live Demo</a> • <a href="https://jgustavocn.github.io/dataprofiler/" target="_blank" rel="noopener noreferrer">Documentação</a>
        </sub></p>
      </details>
    </td>
  </tr>
  <tr>
    <td colspan="6" align="center" valign="top">
      <a href="https://base-apoio-partiuif.vercel.app" target="_blank" rel="noopener noreferrer">
        <img src="./assets/bento/bento-partiuif.svg" alt="Base de Apoio Partiu IF — MCP OAuth 2.1 e RLS" width="100%" />
      </a>
      <details>
        <summary><sub><b>Ver motivo, arquitetura e ganhos</b></sub></summary>
        <p align="left"><sub>
          <b>Por que foi feito:</b> Padronizar a elaboração de simulados/provas diagramadas em A4 e a prestação de contas de monitoria do programa federal Partiu IF (MEC/Secadi/IFS).<br/>
          <b>Solução &amp; Engenharia:</b> Plataforma Next.js 16 + Supabase com fluxo editorial travado por máquina de estados, editor KaTeX/MathLive e servidor MCP v2 integrado (<code>mcp-use</code> + OAuth 2.1 PKCE + PostgreSQL RLS).<br/>
          <b>Ganhos Reais:</b> Busca semântica em <b>12.800 habilidades BNCC</b>, preview interativo de folha A4 dentro do Claude/ChatGPT (SEP-1865), controle RBAC com 5 perfis e <b>340+ testes automatizados</b> em Vitest. <i>(Repositório institucional privado)</i><br/>
          <b>Acessos extras:</b> <a href="https://base-apoio-partiuif.vercel.app/conectar-ia" target="_blank" rel="noopener noreferrer">Conectar IA (MCP)</a>
        </sub></p>
      </details>
    </td>
  </tr>
  <tr>
    <td colspan="3" width="50%" align="center" valign="top">
      <a href="https://github.com/JGustavoCN/mcp-gdocs-latex" target="_blank" rel="noopener noreferrer">
        <img src="./assets/bento/bento-mcp.svg" alt="MCP DocsLaTeX Bridge" width="100%" />
      </a>
      <details>
        <summary><sub><b>Ver motivo e ganhos</b></sub></summary>
        <p align="left"><sub>
          <b>Por quê:</b> Orientadores revisam no Google Docs enquanto autores escrevem em LaTeX local, gerando retrabalho manual e quebra de normas.<br/>
          <b>Ganhos:</b> <b>20 tools HATEOAS</b> em binário Go único (zero Python/Node), diff em 3 níveis, edição atômica anti-bleeding, paginação real via goroutines e auditoria ABNT (NBR 14724/6023/6024/6027).<br/>
          <b>Extra:</b> <a href="https://github.com/JGustavoCN/mcp-gdocs-latex/releases" target="_blank" rel="noopener noreferrer">Binários (Releases)</a>
        </sub></p>
      </details>
    </td>
    <td colspan="3" width="50%" align="center" valign="top">
      <a href="https://github.com/JGustavoCN/sispubli-api" target="_blank" rel="noopener noreferrer">
        <img src="./assets/bento/bento-sispubli.svg" alt="Sispubli API Security-First Proxy" width="100%" />
      </a>
      <details>
        <summary><sub><b>Ver motivo e ganhos</b></sub></summary>
        <p align="left"><sub>
          <b>Por quê:</b> O sistema legado institucional trafegava em HTTP puro e expunha o CPF do estudante diretamente nas URLs de certificados e logs.<br/>
          <b>Ganhos:</b> Proxy <i>Security-First</i> em FastAPI com <b>URL Ticket Proxy</b> (tickets efêmeros Fernet), PII Redactor em logs, Edge Cache de 24h e <b>91% de cobertura de testes</b> (Pytest/VCR/E2E).<br/>
          <b>Extra:</b> <a href="https://sispubli-api.vercel.app/docs" target="_blank" rel="noopener noreferrer">Swagger API</a>
        </sub></p>
      </details>
    </td>
  </tr>
  <tr>
    <td colspan="2" width="33.3%" align="center" valign="top">
      <a href="https://github.com/JGustavoCN/aeutb-auditor" target="_blank" rel="noopener noreferrer">
        <img src="./assets/bento/bento-aeutb.svg" alt="AEUTB Auditor" width="100%" />
      </a>
      <details>
        <summary><sub><b>Ver motivo e ganhos</b></sub></summary>
        <p align="left"><sub>
          <b>Por quê:</b> Extravio de vagas e furos de fila em listas de transporte universitário no WhatsApp.<br/>
          <b>Ganhos:</b> Parser estatístico lê milhares de linhas <code>.txt</code>, gera prova comparativa lado a lado e relatórios via hash (<code>/report/[hash]</code>). <a href="https://aeutb-auditor.vercel.app" target="_blank" rel="noopener noreferrer">App</a>
        </sub></p>
      </details>
    </td>
    <td colspan="2" width="33.3%" align="center" valign="top">
      <a href="https://github.com/JGustavoCN/PlayIFS" target="_blank" rel="noopener noreferrer">
        <img src="./assets/bento/bento-playifs.svg" alt="PlayIFS" width="100%" />
      </a>
      <details>
        <summary><sub><b>Ver motivo e ganhos</b></sub></summary>
        <p align="left"><sub>
          <b>Por quê:</b> Competições do IFS dependiam de planilhas manuais propensas a erros.<br/>
          <b>Ganhos:</b> Sorteio balanceado, mata-mata automático (W.O. e <i>byes</i>), súmula em lote e <b>16 manuais de engenharia</b> (Java 21 + Spring Boot + Flutter).
        </sub></p>
      </details>
    </td>
    <td colspan="2" width="33.3%" align="center" valign="top">
      <a href="https://github.com/JGustavoCN/pharmastation" target="_blank" rel="noopener noreferrer">
        <img src="./assets/bento/bento-pharmastation.svg" alt="PharmaStation PDV" width="100%" />
      </a>
      <details>
        <summary><sub><b>Ver motivo e ganhos</b></sub></summary>
        <p align="left"><sub>
          <b>Por quê:</b> Aplicar Estruturas de Dados puras em um PDV desktop de alto acabamento visual.<br/>
          <b>Ganhos:</b> <b>Lista, Fila e Pilha do zero</b> (sem <code>java.util.List</code>), UI Dark/Light com FlatLaf, RBAC SHA-256 e PDFs em JasperReports 7.0. <a href="https://github.com/JGustavoCN/pharmastation/releases/latest" target="_blank" rel="noopener noreferrer">Release</a>
        </sub></p>
      </details>
    </td>
  </tr>
</table>

<details>
<summary><strong>Explorar mais projetos próprios (Mobile, Automação LaTeX e .NET Clean Architecture)</strong></summary>

<br/>

<table>
  <tr>
    <td width="33.3%" align="center" valign="top">
      <a href="https://github.com/JGustavoCN/ifdex" target="_blank" rel="noopener noreferrer">
        <img src="./assets/bento/bento-ifdex.svg" alt="IFdex — Cofre Acadêmico Gamificado" width="100%" />
      </a>
      <details>
        <summary><sub><b>Ver motivo e ganhos</b></sub></summary>
        <p align="left"><sub>
          <b>Por quê:</b> Estudantes perdem certificados espalhados entre sistemas e pastas.<br/>
          <b>Ganhos:</b> App híbrido Flutter (Android/PWA) integrado ao Sispubli com sistema de XP, FVM e Lefthook. <a href="https://ifdex-app.firebaseapp.com/" target="_blank" rel="noopener noreferrer">PWA</a>
        </sub></p>
      </details>
    </td>
    <td width="33.3%" align="center" valign="top">
      <a href="https://github.com/JGustavoCN/template-tcc-ifs-latex" target="_blank" rel="noopener noreferrer">
        <img src="./assets/bento/bento-tcc.svg" alt="Template TCC IFS LaTeX" width="100%" />
      </a>
      <details>
        <summary><sub><b>Ver motivo e ganhos</b></sub></summary>
        <p align="left"><sub>
          <b>Por quê:</b> Eliminar barreiras de configuração de ambiente LaTeX ABNT.<br/>
          <b>Ganhos:</b> Compilação na nuvem (GitHub Pages/Releases a cada push), Dev Containers e <code>.agents/skills/</code> compatível com o <code>mcp-gdocs-latex</code>. <a href="https://jgustavocn.github.io/template-tcc-ifs-latex/" target="_blank" rel="noopener noreferrer">PDF</a>
        </sub></p>
      </details>
    </td>
    <td width="33.3%" align="center" valign="top">
      <a href="https://github.com/JGustavoCN/miles-manager" target="_blank" rel="noopener noreferrer">
        <img src="./assets/bento/bento-miles.svg" alt="Miles Manager — C# .NET 8" width="100%" />
      </a>
      <details>
        <summary><sub><b>Ver motivo e ganhos</b></sub></summary>
        <p align="left"><sub>
          <b>Por quê:</b> Centralizar cálculo de pontos dispersos entre cartões e programas de fidelidade.<br/>
          <b>Ganhos:</b> Clean Architecture (Core, Infrastructure e WebApp) em .NET 8, Blazor Server, MudBlazor, EF Core + SQL Server. <a href="https://miles-manager-app-jgustavocn-acbhhhavcgchgsgk.eastus-01.azurewebsites.net/" target="_blank" rel="noopener noreferrer">Azure</a>
        </sub></p>
      </details>
    </td>
  </tr>
</table>

</details>

---

## Arsenal Técnico

<div align="center">
  <img src="https://skills.syvixor.com/api/icons?perline=12&i=go,java,cs,python,typescript,react,nextjs,flutter,spring,dotnet,docker,postgresql" alt="Core Stack" />
</div>

<br>

<details>
<summary><strong>Ver stack complementar, testes e infraestrutura</strong></summary>

<br/>

<table>
  <tr>
    <th align="left">Domínio</th>
    <th align="left">Tecnologias &amp; Ferramentas</th>
  </tr>
  <tr>
    <td><b>Linguagens &amp; UI</b></td>
    <td><code>TypeScript</code> <code>JavaScript</code> <code>PowerShell</code> <code>Blazor</code> <code>MudBlazor</code> <code>Material UI</code> <code>Tailwind v4</code> <code>Vite</code> <code>SWC</code></td>
  </tr>
  <tr>
    <td><b>Backend &amp; IA</b></td>
    <td><code>FastAPI</code> <code>Spring Security</code> <code>Hibernate</code> <code>EF Core</code> <code>Node.js</code> <code>MCP (mcp-use)</code> <code>OAuth 2.1</code></td>
  </tr>
  <tr>
    <td><b>Testes &amp; Qualidade</b></td>
    <td><code>Pytest (VCR/E2E)</code> <code>Vitest</code> <code>JUnit 5</code> <code>Ruff</code> <code>Apache JMeter</code> <code>Lefthook</code></td>
  </tr>
  <tr>
    <td><b>Dados &amp; Cloud</b></td>
    <td><code>Supabase (RLS)</code> <code>SQL Server</code> <code>MySQL</code> <code>Oracle</code> <code>MongoDB</code> <code>GitHub Actions</code> <code>Vercel</code> <code>Render</code> <code>Azure</code></td>
  </tr>
</table>

</details>

---

## Atividade &amp; Releases Recentes

<div align="center">
  <a href="https://github.com/JGustavoCN?tab=repositories" target="_blank" rel="noopener noreferrer">
    <img src="./assets/bento/activity-panel.svg" alt="Atividade e Releases Recentes" width="100%" />
  </a>
</div>

<details>
<summary><sub><b>Abrir links diretos dos repositórios e releases recentes</b></sub></summary>

<br/>

<table>
  <tr>
    <td width="50%" valign="top">
      <strong>Últimos Repositórios Atualizados</strong><br/><br/>
      <!-- recent_updates starts -->
• <a href="https://github.com/JGustavoCN/template-tcc-ifs-latex"><b>template-tcc-ifs-latex</b></a> <sub>(JavaScript • 2026-11-25)</sub><br>• <a href="https://github.com/JGustavoCN/mcp-gdocs-latex"><b>mcp-gdocs-latex</b></a> <sub>(Go • 2026-11-23)</sub><br>• <a href="https://github.com/JGustavoCN/PlayIFS"><b>PlayIFS</b></a> <sub>(Dart • 2026-09-10)</sub><br>• <a href="https://github.com/JGustavoCN/pharmastation"><b>pharmastation</b></a> <sub>(Java • 2026-09-08)</sub>
<!-- recent_updates ends -->
    </td>
    <td width="50%" valign="top">
      <strong>Últimos Releases Publicados</strong><br/><br/>
      <!-- recent_releases starts -->
• <a href="https://github.com/JGustavoCN/template-tcc-ifs-latex/releases/tag/build-17"><b>template-tcc-ifs-latex</b> <code>build-17</code></a> <sub>(2026-11-25)</sub><br>• <a href="https://github.com/JGustavoCN/pharmastation/releases/tag/v1.1.0"><b>pharmastation</b> <code>v1.1.0</code></a> <sub>(2026-09-08)</sub><br>• <a href="https://github.com/JGustavoCN/latex-filhos-de-obaluaie/releases/tag/build-1"><b>latex-filhos-de-obaluaie</b> <code>build-1</code></a> <sub>(2026-07-14)</sub>
<!-- recent_releases ends -->
    </td>
  </tr>
</table>

</details>

---

## GitHub Stats

<div align="center">
  <img width="48%" src="https://github-readme-stats.vercel.app/api?username=JGustavoCN&show_icons=true&count_private=true&hide_border=true&title_color=00bfbf&icon_color=00bfbf&text_color=c9d1d9&bg_color=0d1117" alt="José Gustavo github stats" /> 
  <img width="40%" src="https://github-readme-stats.vercel.app/api/top-langs/?username=JGustavoCN&layout=compact&hide_border=true&title_color=00bfbf&text_color=c9d1d9&bg_color=0d1117" alt="Top Languages" />
</div>

<br>

<div align="center">
  <img width="90%" src="https://github-readme-streak-stats.herokuapp.com/?user=JGustavoCN&theme=react&border=c9d1d9&hide_border=true&ring=00bfbf&fire=00bfbf&currStreakNum=00bfbf&sideNums=00bfbf&currStreakLabel=00bfbf" alt="José Gustavo streak stats" />
</div>

<br>

---

<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/JGustavoCN/JGustavoCN/output/github-contribution-grid-snake-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/JGustavoCN/JGustavoCN/output/github-contribution-grid-snake.svg" />
    <img alt="github contribution grid snake animation" src="https://raw.githubusercontent.com/JGustavoCN/JGustavoCN/output/github-contribution-grid-snake.svg" />
  </picture>
</div>

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=00bfbf&height=120&section=footer"/>
