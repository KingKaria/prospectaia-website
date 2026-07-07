"""
Generates pages/metodologia-*.html fragments — one per step of the
ProspectaIA methodology. Run this, then `python build.py` to regenerate
the final root pages.

Copy is persuasive but only about the process itself (what we commit to
do), never about fabricated past client outcomes or numbers.
"""
from pathlib import Path

ROOT = Path(__file__).parent

STEPS = [
    {
        "slug": "diagnostico",
        "step": "1",
        "name": "Diagnóstico Gratuito",
        "icon": "🔍",
        "subtitle": "Descubra exatamente onde está a perder clientes — antes de gastar um único euro",
        "image": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800&q=80",
        "intro": "Antes de sugerir seja o que for, analisamos a fundo a presença digital atual do seu negócio: perfil no Google, reviews, plataformas de reserva e redes sociais. Sem diagnóstico, qualquer estratégia é apenas uma suposição.",
        "benefits": [
            ("Clareza Total Sobre a Sua Presença Digital Atual", "Sabe exatamente como o seu negócio aparece aos olhos de quem pesquisa por si online, sem zonas cinzentas."),
            ("Identificação dos Erros que Estão a Custar Reservas Agora", "Apontamos, com precisão, os pontos concretos que hoje afastam clientes antes do primeiro contacto."),
            ("Sem Custos, Sem Compromisso, Sem Letras Pequenas", "A análise é gratuita e não obriga a contratar seja o que for — o objetivo é dar-lhe clareza, primeiro."),
            ("Um Retrato Que Pode Usar Mesmo Sem Avançar Connosco", "O diagnóstico tem valor por si só: fica a saber onde agir, quer decida trabalhar connosco quer não."),
        ],
    },
    {
        "slug": "estrategia",
        "step": "2",
        "name": "Estratégia Personalizada",
        "icon": "🎯",
        "subtitle": "Nenhuma fórmula genérica — um plano desenhado à medida do seu negócio e do seu setor",
        "image": "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=800&q=80",
        "intro": "Com o diagnóstico em mãos, definimos prioridades reais: o que resolver primeiro, o que pode esperar, e onde investir esforço para ter maior impacto no seu negócio específico.",
        "benefits": [
            ("Prioridades Claras Sobre o Que Fazer Primeiro", "Em vez de tentar tudo ao mesmo tempo, sabe exatamente qual é o próximo passo com maior impacto."),
            ("Adaptada ao Seu Orçamento, Não a um Pacote Fixo", "A estratégia é construída à volta do que faz sentido para o seu negócio, não o contrário."),
            ("Baseada no Diagnóstico Real, Não em Suposições", "Cada decisão parte de dados concretos sobre o seu perfil e o seu setor, não de um modelo genérico."),
            ("Objetivos Mensuráveis Definidos Desde o Início", "Sabe, desde o primeiro dia, o que vamos medir e como vai perceber se está a resultar."),
        ],
    },
    {
        "slug": "execucao",
        "step": "3",
        "name": "Execução Contínua",
        "icon": "⚙️",
        "subtitle": "Enquanto cuida do seu negócio, nós cuidamos da sua presença digital",
        "image": "https://images.unsplash.com/photo-1552664730-d307ca884978?w=800&q=80",
        "intro": "Estratégia sem execução consistente não vale nada. Implementamos otimizações de perfil, gestão de reviews e conteúdo de forma contínua, sem depender da sua disponibilidade para acontecer.",
        "benefits": [
            ("Otimizações Feitas por Quem Entende do Assunto", "Sem tentativa e erro — cada ajuste é feito com conhecimento de causa sobre o que funciona em cada plataforma."),
            ("A Consistência Que É Difícil Manter Sozinho", "A maioria dos negócios começa bem e perde o ritmo ao fim de semanas — nós garantimos que isso não acontece."),
            ("Ajustes Constantes Conforme os Dados", "A execução não é estática: adaptamos o que fazemos à medida que percebemos o que está a gerar resultado."),
            ("Zero Preocupações Técnicas do Seu Lado", "Não precisa de perceber de algoritmos ou plataformas — isso é connosco, para o seu negócio continuar a funcionar."),
        ],
    },
    {
        "slug": "relatorio",
        "step": "4",
        "name": "Relatório e Ajuste Mensal",
        "icon": "📊",
        "subtitle": "Nunca mais fique sem saber se o que está a ser feito realmente vale a pena",
        "image": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800&q=80",
        "intro": "Todos os meses, partilhamos o que foi feito, o que mudou e o que vamos ajustar a seguir. Sem jargão técnico sem explicação, sem números soltos sem contexto.",
        "benefits": [
            ("Transparência Total Sobre o Que Foi Feito e Porquê", "Cada ação tomada no mês é explicada de forma clara, sem esconder nada atrás de relatórios complicados."),
            ("Decisões Futuras Baseadas em Dados, Não em Suposições", "O relatório de um mês informa diretamente a estratégia do mês seguinte."),
            ("Oportunidade de Corrigir o Rumo Antes de Ser Tarde", "Problemas são identificados cedo, com tempo para ajustar antes de se tornarem um padrão."),
            ("Prestação de Contas Mensal, Sem Surpresas", "Sabe sempre em que ponto está o trabalho, sem ter de perguntar ou adivinhar."),
        ],
    },
]

PAGE_TEMPLATE = """<!--META-->
<title>{name} | ProspectaIA</title>
<meta name="description" content="Como funciona a etapa de {name_lower} na metodologia da ProspectaIA para o seu negócio.">
<meta name="author" content="ProspectaIA">
<meta property="og:title" content="{name} - ProspectaIA">
<meta property="og:type" content="website">
<meta property="og:locale" content="pt_PT">
<link rel="stylesheet" href="css/style.css">
<!--BODY-->
<section class="hero">
  <div class="container hero-inner">
    <div class="hero-text fade-in">
      <span class="article-meta">Etapa {step} da Metodologia</span>
      <h1>{icon} {name}</h1>
      <p class="subtitle">{subtitle}</p>
      <a href="contacto.html" class="btn btn-primary btn-large">Agendar Análise Grátis</a>
    </div>
    <div class="hero-image fade-in">
      <img src="{image}" alt="{name}" loading="lazy">
    </div>
  </div>
</section>

<section class="services-section">
  <div class="container">
    <h2 class="section-title">O Que Esta Etapa Significa Para Si</h2>
    <p class="section-subtitle">{intro}</p>
    <div class="services-grid">
{benefit_cards}
    </div>
    <p class="section-link-center" style="margin-top:40px;"><a href="metodologia.html" class="link-more">← Ver metodologia completa</a></p>
  </div>
</section>

<section class="cta-final">
  <div class="container">
    <h2>Pronto para começar pelo diagnóstico?</h2>
    <a href="contacto.html" class="btn btn-primary btn-large">Agendar Análise Grátis</a>
    <p class="cta-note">Análise sem compromisso em 5 minutos</p>
  </div>
</section>
"""

BENEFIT_CARD = """      <div class="service-card fade-in">
        <div class="service-icon">✅</div>
        <h3>{title}</h3>
        <p>{desc}</p>
      </div>"""


def build_fragment(s):
    cards = "\n".join(
        BENEFIT_CARD.format(title=t, desc=d) for t, d in s["benefits"]
    )
    return PAGE_TEMPLATE.format(
        name=s["name"],
        name_lower=s["name"][0].lower() + s["name"][1:],
        step=s["step"],
        icon=s["icon"],
        subtitle=s["subtitle"],
        image=s["image"],
        intro=s["intro"],
        benefit_cards=cards,
    )


def main():
    for s in STEPS:
        fragment = build_fragment(s)
        out = ROOT / "pages" / f"metodologia-{s['slug']}.html"
        out.write_text(fragment, encoding="utf-8", newline="\n")
        print(f"Wrote {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
