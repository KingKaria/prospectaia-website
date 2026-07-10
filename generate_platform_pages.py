"""
Generates pages/plataforma-*.html fragments (one per platform ProspectaIA
manages) from the PLATFORMS data below. Run this, then `python build.py`
to regenerate the final root pages.
"""
from pathlib import Path

ROOT = Path(__file__).parent

PLATFORMS = [
    {
        "slug": "google-maps",
        "name": "Google Maps & Google My Business",
        "icon": "📍",
        "subtitle": "O primeiro lugar onde o seu negócio é encontrado — ou perdido para a concorrência",
        "image": "https://images.unsplash.com/photo-1524661135-423995f22d0b?w=800&q=80",
        "intro": "Antes de visitar o seu site ou ligar, o cliente vê o seu perfil no Google Maps. É aí que decide, em segundos, se o seu negócio parece confiável e ativo — ou se passa para o próximo resultado da lista.",
        "benefits": [
            ("Apareça Primeiro na Pesquisa Local", "Otimizamos categoria, palavras-chave e atributos do perfil para que o seu negócio apareça nas pesquisas \"perto de mim\" antes da concorrência direta."),
            ("Perfil Verificado Transmite Confiança Imediata", "Um perfil completo, com informação consistente e selo de verificação, reduz a hesitação de quem está a decidir entre várias opções."),
            ("Fotos e Posts que Convertem Visualização em Visita", "Gerimos fotos profissionais e publicações regulares que mantêm o perfil ativo aos olhos do Google e dos clientes."),
            ("Nunca Mais Perca um Cliente por Informação Errada", "Monitorizamos horários, morada e contactos constantemente, eliminando o atrito que faz o cliente desistir antes de chegar."),
        ],
    },
    {
        "slug": "google-reviews",
        "name": "Google Reviews",
        "icon": "🔍",
        "subtitle": "9 em cada 10 clientes leem reviews antes de decidir — garantimos que as suas contam a história certa",
        "image": "https://images.unsplash.com/photo-1553877522-43269d4ea984?w=800&q=80",
        "intro": "As reviews são hoje o fator de decisão mais consultado antes de qualquer reserva, marcação ou compra. Geri-las bem não é opcional — é o que separa um negócio que cresce de um que estagna.",
        "benefits": [
            ("Prova Social que Fecha Decisões Antes do Primeiro Contacto", "Uma reputação forte e visível reduz a necessidade de convencer — o cliente já chega predisposto a confiar."),
            ("Resposta Profissional a Cada Review, Boa ou Má", "Respondemos com tom consistente e estratégico, protegendo a imagem do negócio em cada interação pública."),
            ("Mais Estrelas, Mais Cliques, Mais Reservas", "Aumentar a média de avaliação tem impacto direto e mensurável na taxa de cliques nos resultados de pesquisa."),
            ("Reviews Negativas Transformadas em Oportunidade", "Uma resposta bem gerida a uma crítica pode reverter a perceção de quem lê, mostrando cuidado real com o cliente."),
        ],
    },
    {
        "slug": "tripadvisor",
        "name": "TripAdvisor",
        "icon": "🦉",
        "subtitle": "O primeiro nome que turistas e viajantes consultam antes de decidir onde ir",
        "image": "https://images.unsplash.com/photo-1488646953014-85cb44e25828?w=800&q=80",
        "intro": "Para negócios que dependem de turismo — restaurantes, hotéis, experiências — o TripAdvisor é muitas vezes o critério de desempate final. Uma posição alta no ranking local vale mais do que qualquer anúncio.",
        "benefits": [
            ("Subida no Ranking Local Entre Concorrentes Diretos", "Otimizamos os fatores que o algoritmo do TripAdvisor mais valoriza: qualidade, quantidade e recência das reviews."),
            ("Certificado de Excelência ao Seu Alcance", "Trabalhamos para que o negócio reúna os critérios que tornam este selo — e a confiança que ele transmite — uma realidade."),
            ("Gestão de Reviews para Público Internacional", "Respondemos com qualidade em múltiplos idiomas, cobrindo o perfil de visitantes que mais influenciam a reputação global."),
            ("Fotos e Descrição Pensadas para Decisão Rápida", "Um viajante compara várias opções em minutos — garantimos que o seu perfil é o que convence primeiro."),
        ],
    },
    {
        "slug": "booking",
        "name": "Booking.com",
        "icon": "🛎️",
        "subtitle": "Milhões de pesquisas diárias — garantimos que o seu alojamento não passa despercebido",
        "image": "https://images.unsplash.com/photo-1445019980597-93fa8acb246c?w=800&q=80",
        "intro": "O Booking.com continua a ser o motor de reservas mais usado para alojamento em Portugal e na Europa. Estar bem posicionado ali é, para muitos hotéis, a diferença entre uma época cheia e uma época incerta.",
        "benefits": [
            ("Otimização de Perfil para Subir no Ranking de Relevância", "Ajustamos descrição, fotos e categorias para melhorar a posição do seu alojamento nos resultados de pesquisa."),
            ("Gestão de Reviews que Protege a Pontuação", "Uma pontuação elevada tem impacto direto na visibilidade — cuidamos de cada avaliação com esse objetivo em mente."),
            ("Mais Reservas Diretas, Sem Perder o Tráfego da Plataforma", "Desenhamos uma estratégia que usa o Booking como canal de descoberta, sem depender exclusivamente dele."),
            ("Resposta Rápida que Mantém o Estatuto de Parceiro Preferencial", "Ajudamos a cumprir os critérios que garantem maior destaque e melhores condições na plataforma."),
        ],
    },
    {
        "slug": "thefork",
        "name": "TheFork",
        "icon": "🍴",
        "subtitle": "Transformamos os horários mais vazios da semana em reservas garantidas",
        "image": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=800&q=80",
        "intro": "TheFork é a plataforma de referência para reservas de restaurante em Portugal. O segredo não é só estar lá — é estar otimizado para os momentos em que o restaurante mais precisa de encher mesas.",
        "benefits": [
            ("Visibilidade Prioritária Quando Mais Precisa", "Ajustamos promoções e disponibilidade para captar clientes exatamente nos horários de menor procura."),
            ("Promoções que Enchem a Agenda Sem Sacrificar Margem", "Definimos descontos estratégicos que atraem reservas sem desvalorizar a experiência ou o preço médio."),
            ("Perfil com Fotos e Menu que Convertem", "Um perfil visualmente cuidado é frequentemente o fator decisivo entre dois restaurantes parecidos."),
            ("Reviews Geridas para Reforçar Reputação", "Respostas consistentes constroem confiança junto de quem ainda não conhece o restaurante."),
        ],
    },
    {
        "slug": "airbnb",
        "name": "Airbnb",
        "icon": "🏠",
        "subtitle": "O estatuto de Superhost não é sorte — é estratégia",
        "image": "https://images.unsplash.com/photo-1502672260266-1c1ef2d93688?w=800&q=80",
        "intro": "No Airbnb, a diferença entre um anúncio esquecido e um anúncio com lista de espera está nos detalhes que o algoritmo — e os hóspedes — mais valorizam.",
        "benefits": [
            ("Caminho Estruturado Até ao Estatuto de Superhost", "Trabalhamos os critérios de resposta, avaliação e cancelamento que sustentam este selo de confiança."),
            ("Otimização de Anúncio para Subir na Pesquisa", "Título, fotos e descrição são ajustados para melhorar a posição do anúncio nos resultados relevantes."),
            ("Gestão de Reviews que Protege a Classificação", "Cada avaliação é acompanhada de perto, respondendo com cuidado sempre que necessário."),
            ("Resposta Rápida que Maximiza a Conversão", "Tempo de resposta é um fator de ranking — garantimos que nenhum pedido fica por responder."),
        ],
    },
    {
        "slug": "vrbo",
        "name": "Vrbo",
        "icon": "🏡",
        "subtitle": "Presença forte onde famílias e grupos procuram a próxima estadia",
        "image": "https://images.unsplash.com/photo-1568605114967-8130f3a36994?w=800&q=80",
        "intro": "O Vrbo atrai um público específico — famílias e grupos à procura de estadias mais longas. Um anúncio bem otimizado para este perfil de hóspede faz toda a diferença na taxa de ocupação.",
        "benefits": [
            ("Perfil Otimizado para o Público Específico do Vrbo", "Ajustamos a comunicação e as fotos para falar diretamente com quem procura estadias em família ou grupo."),
            ("Reviews Geridas para Reforçar Confiança em Estadias Longas", "Estadias mais longas exigem mais confiança — cuidamos da reputação com esse objetivo em mente."),
            ("Estratégia de Preço Alinhada com Época Alta", "Ajudamos a ajustar disponibilidade e preço aos períodos de maior procura deste público específico."),
            ("Comunicação Ágil que Reduz Cancelamentos", "Respostas rápidas e claras diminuem a incerteza que leva a cancelamentos de última hora."),
        ],
    },
    {
        "slug": "yelp",
        "name": "Yelp",
        "icon": "⭐",
        "subtitle": "Confiança local construída review a review",
        "image": "https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?w=800&q=80",
        "intro": "Ainda muito usado por quem procura recomendações locais de confiança, o Yelp recompensa negócios com perfis completos e reputação bem gerida.",
        "benefits": [
            ("Perfil Completo que Reduz Abandono", "Um perfil com informação incompleta é um dos maiores motivos de perda de clientes antes do primeiro contacto."),
            ("Gestão de Reviews com Resposta Consistente", "Cada avaliação recebe uma resposta profissional, alinhada com o tom da marca."),
            ("Selo de Negócio Verificado Reforça Credibilidade", "Ajudamos a cumprir os critérios que dão acesso a este sinal de confiança adicional."),
            ("Monitorização Contínua da Reputação", "Acompanhamos novas reviews em tempo útil, sem deixar nada por responder."),
        ],
    },
    {
        "slug": "facebook",
        "name": "Facebook",
        "icon": "📘",
        "subtitle": "Onde a comunidade decide em quem confiar",
        "image": "https://images.unsplash.com/photo-1611162617213-7d7a39e9b1d7?w=800&q=80",
        "intro": "O Facebook continua a ser um canal decisivo para negócios locais — recomendações de amigos, reviews e mensagens diretas influenciam decisões todos os dias.",
        "benefits": [
            ("Página Otimizada com Reviews em Destaque", "Organizamos a página para que recomendações e avaliações estejam sempre visíveis a quem visita."),
            ("Gestão de Mensagens Sem Perder Nenhum Contacto", "Cada pedido de informação é respondido a tempo, evitando perder clientes por falta de resposta."),
            ("Conteúdo Regular que Mantém o Negócio Relevante", "Publicações consistentes mantêm o negócio presente no feed de quem já o segue."),
            ("Integração de Reservas e Marcações na Própria Página", "Facilitamos o caminho entre ver a página e agir, sem obrigar o cliente a sair da plataforma."),
        ],
    },
    {
        "slug": "instagram",
        "name": "Instagram",
        "icon": "📷",
        "subtitle": "A primeira impressão visual que decide se alguém quer conhecer o seu negócio",
        "image": "https://images.unsplash.com/photo-1611162616305-c69b3fa7fbe0?w=800&q=80",
        "intro": "No Instagram, a decisão acontece em segundos — uma bio confusa ou fotos fracas afastam tão depressa quanto um perfil cuidado atrai.",
        "benefits": [
            ("Perfil que Transmite Qualidade em Segundos", "Bio, destaque e grelha são organizados para comunicar profissionalismo à primeira vista."),
            ("Conteúdo que Gera Desejo, Não Só Curtidas", "Focamos em conteúdo que aproxima o cliente da decisão de visitar, reservar ou marcar."),
            ("Destaques Estruturados que Convertem Visitantes", "Organizamos informação essencial — serviços, localização, contactos — de forma acessível e visual."),
            ("Gestão de Comentários e Mensagens Diretas", "Nenhuma pergunta ou pedido de reserva fica sem resposta atempada."),
        ],
    },
    {
        "slug": "linkedin",
        "name": "LinkedIn",
        "icon": "💼",
        "subtitle": "Autoridade profissional para quem decide com base em credibilidade, não em impulso",
        "image": "https://images.unsplash.com/photo-1611944212129-29977ae1398c?w=800&q=80",
        "intro": "Para agências, consultórios e negócios B2B, o LinkedIn é onde a reputação profissional se constrói — e onde parcerias e novos clientes muitas vezes começam.",
        "benefits": [
            ("Perfil de Empresa que Reforça Autoridade no Setor", "Organizamos a página para comunicar experiência e credibilidade a quem pesquisa antes de decidir."),
            ("Conteúdo Estratégico que Posiciona Como Referência", "Publicações regulares e relevantes constroem reconhecimento junto do público certo, ao longo do tempo."),
            ("Networking Direcionado para Oportunidades B2B", "Ajudamos a identificar e alcançar contactos com maior potencial de parceria ou negócio."),
            ("Presença Consistente com a Imagem da Marca", "Garantimos que a comunicação no LinkedIn reflete o mesmo profissionalismo do resto do negócio."),
        ],
    },
    {
        "slug": "fresha",
        "name": "Fresha",
        "icon": "💇",
        "subtitle": "A maior marketplace de marcações de beleza — esteja visível onde milhões de clientes já procuram salão",
        "image": "https://images.unsplash.com/photo-1560066984-138dadb4c035?w=800&q=80",
        "intro": "O Fresha tornou-se a plataforma de referência para marcações em salões de cabeleireiro, barbearias e centros de estética. Um perfil bem otimizado aqui significa aparecer primeiro quando alguém procura marcação para hoje ou amanhã — e não perder essa marcação para o concorrente ao lado.",
        "benefits": [
            ("Perfil Otimizado para Aparecer Primeiro na Marketplace", "Ajustamos categoria, serviços e palavras-chave para que o seu salão apareça nas primeiras posições quando alguém procura marcação na sua zona."),
            ("Agenda Sempre Atualizada, Zero Marcações Perdidas", "Garantimos que disponibilidade, preços e serviços estão sempre corretos, eliminando o atrito que faz o cliente desistir e marcar noutro lado."),
            ("Gestão de Reviews que Constrói Confiança Imediata", "Respondemos a cada avaliação com um tom profissional e consistente, reforçando a reputação que decide entre marcar consigo ou com a concorrência."),
            ("Fotos e Portefólio que Convertem Visualização em Marcação", "Cuidamos da apresentação visual do seu perfil — o fator que mais pesa na decisão de quem está a comparar vários salões ao mesmo tempo."),
        ],
    },
    {
        "slug": "treatwell",
        "name": "Treatwell",
        "icon": "💆",
        "subtitle": "A plataforma líder na Europa para descobrir e reservar salões e spas — presença aqui é visibilidade garantida",
        "image": "https://images.unsplash.com/photo-1540555700478-4be289fbecef?w=800&q=80",
        "intro": "Para spas, salões e centros de bem-estar, o Treatwell é muitas vezes a primeira paragem de quem procura um tratamento novo numa zona desconhecida. Estar bem posicionado aqui abre a porta a um fluxo constante de clientes que, de outra forma, nunca chegariam a conhecer o seu espaço.",
        "benefits": [
            ("Maior Visibilidade Junto de Quem Procura Marcar Já", "Otimizamos o perfil para captar o público que está pronto a reservar um tratamento nos próximos dias, não só a pesquisar."),
            ("Reputação Gerida para Reforçar Cada Decisão de Reserva", "Cuidamos das respostas a avaliações, mantendo a pontuação que mais pesa na hora de escolher entre spas parecidos."),
            ("Promoções Estratégicas para Preencher os Horários Mais Fracos", "Ajudamos a desenhar ofertas que enchem a agenda nos períodos de menor procura, sem desvalorizar o serviço."),
            ("Perfil Visual Cuidado que Transmite Qualidade e Higiene", "Fotos e descrição são organizadas para comunicar profissionalismo — essencial num setor onde a confiança decide tudo."),
        ],
    },
]

PAGE_TEMPLATE = """<!--META-->
<title>{name} | ProspectaIA</title>
<meta name="description" content="Como a ProspectaIA gere e otimiza a sua presença no {name}: {subtitle_lower}">
<meta name="author" content="ProspectaIA">
<meta property="og:title" content="{name} - ProspectaIA">
<meta property="og:type" content="website">
<meta property="og:locale" content="pt_PT">
<link rel="stylesheet" href="css/style.css">
<!--BODY-->
<section class="hero">
  <div class="container hero-inner">
    <div class="hero-text fade-in">
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
    <h2 class="section-title">O Que Fazemos no {name}</h2>
    <p class="section-subtitle">{intro}</p>
    <div class="services-grid">
{benefit_cards}
    </div>
  </div>
</section>

<section class="cta-final">
  <div class="container">
    <h2>Pronto para tirar mais partido do {name}?</h2>
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


def build_fragment(p):
    cards = "\n".join(
        BENEFIT_CARD.format(title=t, desc=d) for t, d in p["benefits"]
    )
    return PAGE_TEMPLATE.format(
        name=p["name"],
        subtitle=p["subtitle"],
        subtitle_lower=p["subtitle"][0].lower() + p["subtitle"][1:],
        icon=p["icon"],
        image=p["image"],
        intro=p["intro"],
        benefit_cards=cards,
    )


def main():
    for p in PLATFORMS:
        fragment = build_fragment(p)
        out = ROOT / "pages" / f"plataforma-{p['slug']}.html"
        out.write_text(fragment, encoding="utf-8", newline="\n")
        print(f"Wrote {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
