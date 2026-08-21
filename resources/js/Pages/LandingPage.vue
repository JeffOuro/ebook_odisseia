<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import {
  BookOpen,
  CheckCircle2,
  XCircle,
  ChevronDown,
  ArrowRight,
  ShieldCheck,
  Award,
  Sparkles,
  Lock,
  Compass,
  FileText,
  Lightbulb,
  Scale,
  Brain,
  Feather,
  Clock
} from 'lucide-vue-next';

// Eduzz Checkout Link
const checkoutUrl = 'https://chk.eduzz.com/G92KVYPXWE';

const goToCheckout = () => {
  window.open(checkoutUrl, '_blank');
};

const scrollToOffer = () => {
  const element = document.getElementById('oferta');
  if (element) {
    element.scrollIntoView({ behavior: 'smooth' });
  }
};

// Interactive state
const activeFaq = ref(null);
const showFloatingBar = ref(false);

const toggleFaq = (index) => {
  activeFaq.value = activeFaq.value === index ? null : index;
};

const handleScroll = () => {
  showFloatingBar.value = window.scrollY > 500;
};

onMounted(() => {
  window.addEventListener('scroll', handleScroll);
});

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll);
});

const handleAuthorImgError = (e) => {
  if (e.target.src.endsWith('.jpeg')) {
    e.target.src = '/images/author-avatar.jpg';
  } else if (e.target.src.endsWith('.jpg')) {
    e.target.src = '/images/author-avatar.png';
  }
};

const handleCoverImgError = (e) => {
  if (e.target.src.endsWith('.jpeg')) {
    e.target.src = '/images/ebook-cover.jpg';
  } else if (e.target.src.endsWith('.jpg')) {
    e.target.src = '/images/ebook-cover.png';
  }
};

// Data arrays for scannable structured rendering
const mainDifficulties = [
  'Não saber quais autores, temas ou obras escolher.',
  'Tentar estudar assuntos amplos demais.',
  'Acumular livros, vídeos e cursos sem relacioná-los.',
  'Começar por textos incompatíveis com o próprio momento.',
  'Ler várias páginas sem conseguir explicar o argumento.',
  'Grifar quase tudo e depois não saber o que era realmente importante.',
  'Confundir a interpretação do autor com a própria opinião.',
  'Abandonar os estudos por causa de uma rotina impossível de sustentar.',
  'Acreditar que estudar sozinho significa aprender sem orientação.',
  'Sentir que nunca possui conhecimento suficiente para começar.'
];

const whatYouWillLearn = [
  'Compreender o que caracteriza uma investigação filosófica.',
  'Reconhecer diferentes razões para estudar Filosofia.',
  'Criar condições realistas para começar.',
  'Conhecer as principais áreas e perguntas filosóficas.',
  'Organizar estudos por história, temas ou problemas.',
  'Transformar um interesse amplo em uma pergunta inicial.',
  'Escolher um texto adequado ao seu momento.',
  'Diferenciar obras filosóficas, introduções, comentários e materiais de apoio.',
  'Identificar problema, posição, conceitos, razões e objeções.',
  'Compreender uma posição antes de julgá-la.',
  'Fazer anotações que possam ser realmente utilizadas.',
  'Separar as ideias do autor de suas interpretações e avaliações.',
  'Escrever para tornar o próprio raciocínio mais claro.',
  'Construir ciclos de estudo com começo, objetivo e revisão.',
  'Manter uma rotina de estudos compatível com o tempo disponível.',
  'Reconhecer quando é necessário reler, procurar contexto ou pedir orientação.'
];

const chapters = [
  {
    title: 'Antes de começar — Como transformar interesse em estudo',
    desc: 'Entenda a diferença entre ter contato com conteúdos e construir um percurso. Descubra o que significa estudar de maneira organizada e qual será sua participação nesse processo.'
  },
  {
    title: 'Capítulo 1 — O que é Filosofia e por que estudá-la',
    desc: 'Conheça uma definição introdutória de Filosofia, suas perguntas fundamentais e diferentes razões para se dedicar ao estudo filosófico.'
  },
  {
    title: 'Capítulo 2 — Preparando o terreno',
    desc: 'Aprenda a criar condições possíveis para estudar, organizar sua atenção, buscar o contexto necessário e utilizar materiais de apoio sem entregar sua leitura a eles.'
  },
  {
    title: 'Capítulo 3 — O mapa da Filosofia',
    desc: 'Conheça áreas como metafísica, epistemologia, lógica, ética, filosofia política e estética. Aprenda também a organizar percursos históricos, temáticos ou problemáticos.'
  },
  {
    title: 'Capítulo 4 — Como escolher por onde começar',
    desc: 'Transforme uma curiosidade ampla em uma pergunta delimitada. Escolha seus primeiros textos e organize um ciclo de estudo com poucos recursos relacionados.'
  },
  {
    title: 'Capítulo 5 — Como ler um texto filosófico sem se perder',
    desc: 'Aprenda a localizar o problema, identificar posições, esclarecer conceitos, reconstruir argumentos, interpretar passagens e avaliar ideias com responsabilidade.'
  },
  {
    title: 'Capítulo 6 — Como anotar, compreender e escrever',
    desc: 'Descubra como marcar seletivamente, produzir sínteses, registrar dúvidas, elaborar ideias e utilizar a escrita para revelar lacunas na própria compreensão.'
  },
  {
    title: 'Capítulo 7 — Como continuar estudando Filosofia',
    desc: 'Construa uma rotina possível, organize ciclos revisáveis, cuide do seu acervo e reconheça a importância do diálogo e da orientação no aprendizado.'
  },
  {
    title: 'Conclusão — Do estudo à vida examinada',
    desc: 'Reflita sobre como o conhecimento filosófico pode participar da vida sem se transformar em receita, promessa de felicidade ou resposta pronta.'
  },
  {
    title: 'Material complementar — Percursos por área de formação',
    desc: 'Encontre sugestões de entrada na Filosofia relacionadas a diferentes áreas, como Psicologia, Direito, Ciências Humanas, Saúde, Ciências Naturais, Tecnologia e estudos da religião.'
  }
];

const readingOperations = [
  {
    name: 'Compreender',
    desc: 'Explicar o problema, os conceitos e os elementos fundamentais de uma posição.',
    icon: Brain
  },
  {
    name: 'Interpretar',
    desc: 'Investigar o sentido de uma passagem e sua função no conjunto do texto.',
    icon: Feather
  },
  {
    name: 'Avaliar',
    desc: 'Examinar a qualidade das razões, os pressupostos e as possíveis objeções.',
    icon: Scale
  },
  {
    name: 'Aplicar',
    desc: 'Utilizar uma ideia para iluminar outro problema sem distorcer seu significado original.',
    icon: Lightbulb
  }
];

const differentials = [
  {
    title: 'Orientação sem prescrição universal',
    desc: 'Você recebe critérios e alternativas, não uma lista rígida que desconsidera seus interesses e suas condições.'
  },
  {
    title: 'Profundidade sem pedantismo',
    desc: 'Os conceitos são apresentados com clareza, sem empobrecer o conteúdo nem utilizar linguagem difícil apenas para parecer intelectual.'
  },
  {
    title: 'Prática sem autoajuda',
    desc: 'O livro aproxima o estudo da experiência, mas não transforma teorias filosóficas em receitas para felicidade, sucesso ou transformação pessoal.'
  },
  {
    title: 'Autonomia sem abandono',
    desc: 'Estudar por conta própria não significa aprender sem professores, comentadores, grupos, introduções ou outras formas de orientação.'
  },
  {
    title: 'Método sem mecanização',
    desc: 'Os procedimentos servem para orientar a atenção. Eles não substituem o pensamento nem precisam ser aplicados igualmente a todo texto.'
  },
  {
    title: 'Rigor sem paralisia',
    desc: 'Você aprende a reconhecer dúvidas e limites sem esperar conhecer toda a história da Filosofia para começar.'
  },
  {
    title: 'Rotina sem idealização',
    desc: 'O percurso considera as condições reais do estudante e não exige uma quantidade universal de horas ou páginas diárias.'
  },
  {
    title: 'Autonomia intelectual',
    desc: 'O objetivo não é ensinar o que você deve pensar, mas ajudá-lo a compreender posições, examinar razões e revisar seus próprios julgamentos.'
  }
];

const targetAudience = [
  'Deseja começar a estudar Filosofia, mas não sabe por onde.',
  'Já consome conteúdos filosóficos, mas sente que eles permanecem dispersos.',
  'Começa livros e costuma abandoná-los por dificuldade ou falta de orientação.',
  'Quer aprender a ler textos filosóficos com mais atenção.',
  'Procura um método de estudo flexível e responsável.',
  'Deseja construir uma vida intelectual sem depender de formação acadêmica prévia.',
  'Quer desenvolver maior clareza conceitual e autonomia intelectual.',
  'Precisa organizar uma rotina possível de leitura, anotação e escrita.',
  'Estuda outra área e deseja descobrir caminhos de aproximação com a Filosofia.'
];

const notTargetAudience = [
  'Uma lista definitiva dos únicos livros que merecem ser lidos.',
  'Uma explicação completa de toda a história da Filosofia.',
  'Resumos que substituam a leitura das obras.',
  'Frases motivacionais ou fórmulas de transformação.',
  'Um método infalível e adequado a todas as pessoas.',
  'Respostas prontas para problemas filosóficos complexos.',
  'Um caminho que elimine completamente o esforço, a dúvida e a releitura.'
];

const contrastWithout = [
  'Recomendações acumuladas.',
  'Livros iniciados e abandonados.',
  'Conceitos memorizados sem compreensão.',
  'Anotações que nunca são retomadas.',
  'Planos de estudo impossíveis de sustentar.',
  'Dependência constante da opinião de outras pessoas.'
];

const contrastWith = [
  'Uma pergunta delimitada.',
  'Materiais escolhidos com critérios.',
  'Leitura conduzida por operações claras.',
  'Dúvidas registrada com precisão.',
  'Ciclos de estudo que podem ser revisados.',
  'Desenvolvimento gradual de autonomia.'
];

const faqs = [
  {
    q: 'Preciso ter formação em Filosofia?',
    a: 'Não. O e-book foi desenvolvido principalmente para iniciantes e explica os conceitos necessários ao percurso.'
  },
  {
    q: 'Nunca li uma obra filosófica. Conseguirei acompanhar?',
    a: 'Sim. O guia parte das dificuldades de quem está começando e apresenta gradualmente critérios para escolher e enfrentar as primeiras leituras.'
  },
  {
    q: 'O e-book indica por qual filósofo devo começar?',
    a: 'Ele apresenta critérios, rotas e possibilidades. Não determina um único autor adequado para todas as pessoas, porque o ponto de partida depende dos seus interesses, conhecimentos e objetivos.'
  },
  {
    q: 'Receberei uma lista de livros obrigatórios?',
    a: 'Não uma lista universal. O e-book ensina a selecionar materiais e oferece possibilidades de leitura de acordo com temas, perguntas e diferentes percursos.'
  },
  {
    q: 'O livro ensina História da Filosofia?',
    a: 'Ele oferece um mapa introdutório e contextualizações necessárias, mas não pretende resumir toda a História da Filosofia. Seu foco principal é ensinar você a começar e organizar os estudos.'
  },
  {
    q: 'O conteúdo é apenas teórico?',
    a: 'Não. O e-book apresenta perguntas, procedimentos, quadros e orientações que podem ser utilizados na escolha de materiais, leitura, anotação, escrita e organização da rotina.'
  },
  {
    q: 'O método serve para qualquer texto filosófico?',
    a: 'Os procedimentos são flexíveis e precisam respeitar o gênero, a estrutura e a dificuldade de cada obra. O e-book não apresenta um formulário mecânico ou universal.'
  },
  {
    q: 'O e-book substitui um curso ou professor?',
    a: 'Não. Ele pode ajudar você a começar e organizar o estudo, mas reconhece que alguns textos e problemas exigem orientação, diálogo e contextualização especializada.'
  },
  {
    q: 'Em qual formato receberei o material?',
    a: 'O e-book será entregue em formato PDF.'
  },
  {
    q: 'Posso ler no celular?',
    a: 'Sim. O PDF poderá ser acessado em celulares, tablets e computadores. Para maior conforto, recomenda-se utilizar um dispositivo com tela adequada à leitura prolongada.'
  },
  {
    q: 'O acesso é imediato?',
    a: 'Sim. As instruções de acesso serão enviadas após a confirmação do pagamento.'
  },
  {
    q: 'Qual é o preço?',
    a: 'O preço promocional inicial será de R$ 39,90, por tempo limitado. O valor poderá ser alterado após o período de lançamento.'
  },
  {
    q: 'O e-book promete transformar minha vida?',
    a: 'Não. A Filosofia pode ampliar perguntas, conceitos e formas de examinar a experiência, mas nenhum livro garante sabedoria, felicidade ou transformação moral. A proposta é oferecer um começo organizado e intelectualmente responsável.'
  }
];
</script>

<template>
  <div class="min-h-screen bg-[#F8F7F4] text-[#18232C] font-sans">
    
    <!-- Top Announcement Bar -->
    <div class="bg-[#091A2F] text-[#E9E2D3] py-2.5 px-4 text-center text-xs md:text-sm font-medium border-b border-[#B18A47]/30 tracking-wide flex items-center justify-center gap-2">
      <Sparkles class="w-4 h-4 text-[#B18A47] animate-pulse" />
      <span>Oferta Especial de Lançamento — Por tempo limitado por apenas <strong class="text-[#B18A47]">R$ 39,90</strong></span>
    </div>

    <!-- Floating Sticky Top Bar (Sem Logo, apenas texto e botão) -->
    <transition enter-active-class="transition duration-300 ease-out" enter-from-class="-translate-y-full" enter-to-class="translate-y-0" leave-active-class="transition duration-200 ease-in" leave-from-class="translate-y-0" leave-to-class="-translate-y-full">
      <div v-if="showFloatingBar" class="fixed top-0 left-0 right-0 z-50 bg-[#0E2340]/95 backdrop-blur-md text-[#F8F7F4] border-b border-[#B18A47]/40 shadow-xl py-3 px-4 md:px-8 flex items-center justify-between">
        <div class="flex items-center gap-3">
          <span class="font-serif text-sm md:text-base text-[#F8F7F4] font-semibold">Primeiros Passos no Estudo da Filosofia</span>
        </div>
        <div class="flex items-center gap-4">
          <div class="hidden md:flex flex-col text-right">
            <span class="text-xs text-[#E9E2D3]/70 line-through">De R$ 79,90</span>
            <span class="text-sm font-bold text-[#B18A47]">R$ 39,90</span>
          </div>
          <a :href="checkoutUrl" target="_blank" rel="noopener noreferrer" class="btn-gold-cta font-bold text-xs md:text-sm px-5 py-2.5 rounded-lg flex items-center gap-2 cursor-pointer group">
            <span>Quero começar meu percurso</span>
            <ArrowRight class="w-4 h-4 group-hover:translate-x-1 transition-transform" />
          </a>
        </div>
      </div>
    </transition>

    <!-- Header Navigation com a Logo Principal -->
    <header class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-6 flex items-center justify-between border-b border-[#E9E2D3]">
      <div class="flex items-center gap-3">
        <img src="/images/logo.png" alt="Odisseia Filosófica Logo" class="h-20 sm:h-26 md:h-28 w-auto object-contain mix-blend-multiply transition-all" />
      </div>
      <a :href="checkoutUrl" target="_blank" rel="noopener noreferrer" class="btn-gold-outline text-xs font-bold uppercase tracking-wider px-4 py-2.5 rounded-lg flex items-center gap-2 cursor-pointer">
        <span>Garantir e-book</span>
        <ArrowRight class="w-3.5 h-3.5" />
      </a>
    </header>

    <!-- BLOCO 1 — Seção principal (Hero) -->
    <section class="relative pt-10 pb-20 md:pt-14 md:pb-28 overflow-hidden bg-gradient-to-b from-[#F8F7F4] via-[#F3EEE3] to-[#F8F7F4]">
      <div class="absolute top-0 right-0 w-96 h-96 bg-[#B18A47]/10 rounded-full filter blur-3xl -z-10 pointer-events-none"></div>
      <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 lg:gap-8 items-center">
          
          <!-- Left Text Column -->
          <div class="lg:col-span-7 space-y-6 text-left">
            <!-- Chamada de apoio -->
            <div class="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-white border border-[#B18A47]/40 text-[#6A5542] text-xs md:text-sm font-semibold shadow-xs">
              <Compass class="w-4 h-4 text-[#B18A47]" />
              <span>Um percurso possível para quem deseja começar a estudar Filosofia com seriedade.</span>
            </div>

            <!-- Título do e-book -->
            <h2 class="font-serif text-2xl sm:text-3xl md:text-4xl font-bold text-[#0E2340] leading-tight">
              Primeiros Passos no Estudo da Filosofia
            </h2>

            <!-- Subtítulo -->
            <p class="text-base sm:text-lg text-[#2E4A3D] font-medium italic border-l-3 border-[#B18A47] pl-4 py-1">
              Um guia prático para escolher, ler, compreender e construir seu percurso filosófico.
            </p>

            <!-- Headline -->
            <h1 class="font-serif text-3xl sm:text-4xl lg:text-5xl font-extrabold text-[#091A2F] leading-[1.15] tracking-tight">
              Você não precisa conhecer toda a Filosofia para começar. Precisa saber qual é o próximo passo.
            </h1>

            <!-- Subheadline -->
            <p class="text-base sm:text-lg text-[#18232C]/85 font-normal leading-relaxed">
              Aprenda a transformar seu interesse pela Filosofia em um percurso de estudo organizado — com critérios para escolher temas e textos, enfrentar leituras difíceis, fazer anotações úteis e construir uma rotina possível.
            </p>

            <!-- Preço & CTA Hero Box -->
            <div class="pt-4 space-y-4">
              <div class="p-6 rounded-2xl bg-white border border-[#B18A47]/30 shadow-md max-w-lg space-y-4">
                <div class="flex items-center justify-between border-b border-[#E9E2D3] pb-3">
                  <span class="text-xs font-bold uppercase tracking-wider text-[#657078]">Preço promocional:</span>
                  <div class="flex items-baseline gap-2">
                    <span class="text-sm text-[#657078] line-through">De R$ 79,90</span>
                    <span class="text-2xl sm:text-3xl font-extrabold text-[#0E2340]">por <span class="text-[#B18A47]">R$ 39,90</span></span>
                  </div>
                </div>

                <p class="text-xs text-[#2E4A3D] font-medium flex items-center gap-1.5">
                  <Clock class="w-4 h-4 text-[#B18A47]" />
                  Preço especial de lançamento por tempo limitado.
                </p>

                <!-- Botão Principal de Conversão Hero -->
                <a :href="checkoutUrl" target="_blank" rel="noopener noreferrer" class="w-full btn-gold-cta font-extrabold text-base sm:text-lg py-4 sm:py-4.5 px-6 rounded-xl flex items-center justify-center gap-3 cursor-pointer group">
                  <span class="tracking-wide">Quero começar meu percurso</span>
                  <div class="w-7 h-7 rounded-full bg-[#091A2F]/10 flex items-center justify-center group-hover:translate-x-1 transition-transform">
                    <ArrowRight class="w-4 h-4 text-[#091A2F]" />
                  </div>
                </a>
                
                <div class="flex items-center justify-center gap-4 text-xs text-[#657078] pt-1">
                  <span class="flex items-center gap-1"><FileText class="w-3.5 h-3.5 text-[#B18A47]" /> Formato PDF</span>
                  <span class="flex items-center gap-1"><Lock class="w-3.5 h-3.5 text-[#2E4A3D]" /> Pagamento Seguro</span>
                </div>
              </div>
            </div>

          </div>

          <!-- Right Mockup Column -->
          <div class="lg:col-span-5 flex flex-col items-center justify-center relative">
            <div class="relative w-full max-w-md">
              <div class="absolute -inset-4 bg-gradient-to-tr from-[#B18A47]/30 to-[#0E2340]/20 rounded-3xl filter blur-2xl -z-10"></div>
              <div class="bg-white p-3 rounded-2xl shadow-navy-depth border border-[#E9E2D3]">
                <img 
                  src="/images/ebook-cover.jpeg"
                  @error="handleCoverImgError" 
                  alt="E-book Primeiros Passos no Estudo da Filosofia" 
                  fetchpriority="high"
                  decoding="async"
                  class="w-full h-auto rounded-xl object-cover shadow-inner"
                />
              </div>
              <div class="mt-5 flex items-center justify-center gap-6 text-xs text-[#6A5542] font-semibold">
                <span class="flex items-center gap-1.5"><ShieldCheck class="w-4 h-4 text-[#2E4A3D]" /> Formato PDF</span>
                <span class="flex items-center gap-1.5"><BookOpen class="w-4 h-4 text-[#B18A47]" /> Leitura Adaptada</span>
                <span class="flex items-center gap-1.5"><Lock class="w-4 h-4 text-[#0E2340]" /> Compra Segura</span>
              </div>
            </div>
          </div>

        </div>
      </div>
    </section>

    <!-- BLOCO 2 — Identificação com o problema -->
    <section class="py-16 md:py-24 bg-white border-y border-[#E9E2D3]">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 space-y-8">
        <div class="text-center space-y-3">
          <span class="text-xs font-bold uppercase tracking-widest text-[#B18A47]">Diagnóstico</span>
          <h2 class="font-serif text-3xl sm:text-4xl font-bold text-[#0E2340]">
            Você quer estudar Filosofia, mas não sabe por onde começar?
          </h2>
        </div>

        <div class="prose prose-lg text-[#18232C]/90 space-y-6 leading-relaxed text-base sm:text-lg">
          <p>
            Talvez você já tenha procurado listas de livros, assistido a aulas, acompanhado debates ou salvado dezenas de recomendações.
          </p>
          <p>
            Um vídeo indica Platão. Outro recomenda começar pelos estoicos. Uma lista apresenta cinquenta obras fundamentais. Alguém afirma que você precisa estudar toda a história da Filosofia. Outra pessoa diz que basta escolher um autor e começar.
          </p>
          <p class="font-semibold text-[#0E2340]">
            Quanto mais você procura, mais caminhos aparecem — e mais difícil parece escolher um deles.
          </p>
          <p>
            Você começa um livro, encontra palavras desconhecidas, percebe que não compreendeu o argumento e se pergunta se escolheu a obra errada ou se simplesmente não possui capacidade para estudar Filosofia.
          </p>
          <p class="text-[#2E4A3D] font-bold">
            Mas a dificuldade pode não estar em você.
          </p>
          <p>
            O problema é tentar começar sem um mapa, sem critérios e sem saber o que fazer diante de um texto filosófico.
          </p>
        </div>

        <!-- Frase de destaque -->
        <div class="my-8 p-6 md:p-8 rounded-2xl bg-[#F8F7F4] border-l-4 border-[#B18A47] shadow-xs text-center">
          <p class="font-serif text-xl sm:text-2xl font-bold text-[#0E2340]">
            "Encontrar conteúdos não é o mesmo que construir um percurso de estudo."
          </p>
        </div>
      </div>
    </section>

    <!-- BLOCO 3 — As principais dificuldades -->
    <section class="py-16 md:py-24 bg-[#F8F7F4]">
      <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 space-y-12">
        <div class="text-center max-w-3xl mx-auto space-y-4">
          <h2 class="font-serif text-3xl sm:text-4xl font-bold text-[#091A2F]">
            O interesse existe. O que falta é uma orientação inicial.
          </h2>
          <p class="text-base sm:text-lg text-[#657078]">
            Quem começa a estudar Filosofia por conta própria costuma enfrentar problemas como:
          </p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div 
            v-for="(diff, i) in mainDifficulties" 
            :key="i"
            class="p-4 sm:p-5 rounded-xl bg-white border border-[#E9E2D3] shadow-xs flex items-start gap-3.5 hover:border-[#B18A47]/50 transition-colors"
          >
            <XCircle class="w-5 h-5 text-[#6A5542] shrink-0 mt-0.5" />
            <span class="text-sm sm:text-base text-[#18232C] font-medium">{{ diff }}</span>
          </div>
        </div>

        <!-- Fechamento -->
        <div class="p-6 sm:p-8 rounded-2xl bg-[#E9E2D3]/60 border border-[#B18A47]/40 text-center space-y-4 max-w-3xl mx-auto">
          <p class="text-base sm:text-lg text-[#18232C] leading-relaxed">
            Sem critérios, o estudante pode oscilar entre dois extremos: consumir conteúdos dispersos ou criar um plano tão exigente que nunca consegue colocá-lo em prática.
          </p>
          <p class="font-serif font-bold text-xl text-[#2E4A3D]">
            Este e-book apresenta um caminho diferente.
          </p>
        </div>
      </div>
    </section>

    <!-- BLOCO 4 — Apresentação da solução -->
    <section class="py-16 md:py-24 bg-[#0E2340] text-[#F8F7F4] relative overflow-hidden">
      <div class="absolute -bottom-20 -left-20 w-80 h-80 bg-[#B18A47]/10 rounded-full filter blur-3xl"></div>
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 space-y-8 relative z-10">
        <div class="text-center space-y-4">
          <span class="text-xs font-bold uppercase tracking-widest text-[#B18A47]">A Proposta</span>
          <h2 class="font-serif text-3xl sm:text-4xl md:text-5xl font-bold text-white">
            Um guia para transformar curiosidade em estudo organizado
          </h2>
        </div>

        <div class="space-y-6 text-base sm:text-lg text-[#E9E2D3]/90 leading-relaxed text-center sm:text-left">
          <p class="text-xl font-serif text-[#B18A47] font-semibold text-center italic">
            Primeiros Passos no Estudo da Filosofia foi escrito para ajudar você a sair da dispersão e construir um primeiro percurso filosófico.
          </p>
          <p>
            O livro não oferece uma lista universal de obras obrigatórias nem promete escolher toda a sua formação por você.
          </p>
          <p>
            Ele apresenta mapas, perguntas, critérios e procedimentos para que você participe ativamente das próprias escolhas.
          </p>
          <p>
            Você aprenderá a delimitar uma pergunta, reconhecer a área filosófica relacionada, selecionar materiais adequados, enfrentar um texto com mais clareza, registrar sua compreensão e organizar ciclos de estudo compatíveis com sua realidade.
          </p>
        </div>

        <!-- Frase de destaque -->
        <div class="p-6 md:p-8 rounded-2xl bg-[#091A2F] border border-[#B18A47]/40 text-center shadow-xl">
          <p class="font-serif text-xl sm:text-2xl font-bold text-[#F8F7F4]">
            "O objetivo não é dizer tudo o que você deve estudar. É ajudá-lo a escolher, compreender e revisar o próprio caminho."
          </p>
        </div>
      </div>
    </section>

    <!-- BLOCO 5 — O que o leitor aprenderá -->
    <section class="py-16 md:py-24 bg-white">
      <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 space-y-12">
        <div class="text-center max-w-3xl mx-auto space-y-3">
          <span class="text-xs font-bold uppercase tracking-widest text-[#2E4A3D]">Resultados Práticos</span>
          <h2 class="font-serif text-3xl sm:text-4xl font-bold text-[#0E2340]">
            Ao longo deste guia, você aprenderá a:
          </h2>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div 
            v-for="(item, i) in whatYouWillLearn" 
            :key="i"
            class="p-4 sm:p-5 rounded-xl bg-[#F8F7F4] border border-[#E9E2D3] flex items-start gap-3.5 hover:bg-white hover:border-[#2E4A3D]/50 transition-all shadow-xs"
          >
            <CheckCircle2 class="w-5 h-5 text-[#2E4A3D] shrink-0 mt-0.5" />
            <span class="text-sm sm:text-base text-[#18232C] font-medium leading-snug">{{ item }}</span>
          </div>
        </div>
      </div>
    </section>

    <!-- BLOCO 6 — Conteúdo do e-book -->
    <section class="py-16 md:py-24 bg-[#F8F7F4] border-y border-[#E9E2D3]">
      <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 space-y-12">
        <div class="text-center max-w-3xl mx-auto space-y-3">
          <span class="text-xs font-bold uppercase tracking-widest text-[#B18A47]">Estrutura da Obra</span>
          <h2 class="font-serif text-3xl sm:text-4xl font-bold text-[#091A2F]">
            O que você encontrará no e-book
          </h2>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div 
            v-for="(chap, i) in chapters" 
            :key="i"
            class="bg-white p-6 rounded-2xl border border-[#E9E2D3] shadow-xs hover:shadow-md transition-shadow space-y-3 flex flex-col justify-between"
          >
            <div class="space-y-2">
              <span class="text-xs font-bold uppercase tracking-wider text-[#B18A47] px-2.5 py-1 rounded bg-[#E9E2D3]/50 inline-block">
                Módulo {{ i + 1 }}
              </span>
              <h3 class="font-serif text-lg sm:text-xl font-bold text-[#0E2340]">
                {{ chap.title }}
              </h3>
              <p class="text-sm text-[#657078] leading-relaxed">
                {{ chap.desc }}
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- BLOCO 7 — Método de leitura -->
    <section class="py-16 md:py-24 bg-white">
      <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 space-y-12">
        <div class="text-center max-w-3xl mx-auto space-y-4">
          <span class="text-xs font-bold uppercase tracking-widest text-[#2E4A3D]">Metodologia de Leitura</span>
          <h2 class="font-serif text-3xl sm:text-4xl font-bold text-[#0E2340]">
            Não basta terminar uma página. É preciso saber o que fazer com aquilo que foi lido.
          </h2>
          <p class="text-base sm:text-lg text-[#657078]">
            O e-book ajuda o leitor a distinguir quatro operações fundamentais do estudo filosófico:
          </p>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
          <div 
            v-for="(op, i) in readingOperations" 
            :key="i"
            class="p-6 rounded-2xl bg-[#F8F7F4] border border-[#E9E2D3] text-center space-y-4 hover:border-[#B18A47] transition-all"
          >
            <div class="w-12 h-12 rounded-xl bg-[#0E2340] text-[#B18A47] flex items-center justify-center mx-auto shadow-sm">
              <component :is="op.icon" class="w-6 h-6" />
            </div>
            <h3 class="font-serif text-xl font-bold text-[#0E2340]">{{ op.name }}</h3>
            <p class="text-sm text-[#657078] leading-relaxed">{{ op.desc }}</p>
          </div>
        </div>

        <!-- Fechamento -->
        <div class="p-6 sm:p-8 rounded-2xl bg-[#E9E2D3]/50 border border-[#B18A47]/40 text-center max-w-3xl mx-auto">
          <p class="text-base sm:text-lg text-[#18232C] leading-relaxed font-medium">
            Essas operações ajudam você a evitar dois erros frequentes: concordar com um autor antes de compreendê-lo ou rejeitar uma ideia apenas porque ela causou uma primeira impressão negativa.
          </p>
        </div>
      </div>
    </section>

    <!-- BLOCO 8 — Diferenciais -->
    <section class="py-16 md:py-24 bg-[#091A2F] text-[#F8F7F4]">
      <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 space-y-12">
        <div class="text-center max-w-3xl mx-auto space-y-3">
          <span class="text-xs font-bold uppercase tracking-widest text-[#B18A47]">Diferenciais</span>
          <h2 class="font-serif text-3xl sm:text-4xl font-bold text-white">
            Um guia prático sem transformar a Filosofia em fórmula pronta
          </h2>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          <div 
            v-for="(diff, i) in differentials" 
            :key="i"
            class="p-6 rounded-2xl bg-[#0E2340] border border-[#B18A47]/30 space-y-3 hover:border-[#B18A47] transition-all"
          >
            <h3 class="font-serif text-lg font-bold text-[#B18A47]">
              {{ diff.title }}
            </h3>
            <p class="text-sm text-[#E9E2D3]/80 leading-relaxed">
              {{ diff.desc }}
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- BLOCO 9 & 10 — Para quem é / Para quem não é -->
    <section class="py-16 md:py-24 bg-[#F8F7F4]">
      <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 space-y-12">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 lg:gap-12">
          
          <!-- Para quem é -->
          <div class="bg-white p-8 rounded-3xl border border-[#2E4A3D]/30 shadow-xs space-y-6">
            <div class="flex items-center gap-3">
              <div class="w-10 h-10 rounded-full bg-[#2E4A3D]/10 text-[#2E4A3D] flex items-center justify-center">
                <CheckCircle2 class="w-6 h-6" />
              </div>
              <h2 class="font-serif text-2xl font-bold text-[#0E2340]">
                Este e-book é para você que:
              </h2>
            </div>
            <ul class="space-y-3.5">
              <li 
                v-for="(item, i) in targetAudience" 
                :key="i"
                class="flex items-start gap-3 text-sm sm:text-base text-[#18232C]"
              >
                <CheckCircle2 class="w-5 h-5 text-[#2E4A3D] shrink-0 mt-0.5" />
                <span>{{ item }}</span>
              </li>
            </ul>
          </div>

          <!-- Para quem NÃO é -->
          <div class="bg-white p-8 rounded-3xl border border-[#6A5542]/30 shadow-xs space-y-6 flex flex-col justify-between">
            <div class="space-y-6">
              <div class="flex items-center gap-3">
                <div class="w-10 h-10 rounded-full bg-[#6A5542]/10 text-[#6A5542] flex items-center justify-center">
                  <XCircle class="w-6 h-6" />
                </div>
                <h2 class="font-serif text-2xl font-bold text-[#0E2340]">
                  Este e-book provavelmente não é para quem procura:
                </h2>
              </div>
              <ul class="space-y-3.5">
                <li 
                  v-for="(item, i) in notTargetAudience" 
                  :key="i"
                  class="flex items-start gap-3 text-sm sm:text-base text-[#657078]"
                >
                  <XCircle class="w-5 h-5 text-[#6A5542] shrink-0 mt-0.5" />
                  <span>{{ item }}</span>
                </li>
              </ul>
            </div>

            <!-- Fechamento -->
            <div class="pt-6 border-t border-[#E9E2D3] mt-6">
              <p class="text-sm font-serif font-bold text-[#0E2340] italic text-center">
                A proposta é mais honesta: oferecer condições melhores para que você escolha, leia, compreenda e continue estudando.
              </p>
            </div>
          </div>

        </div>
      </div>
    </section>

    <!-- BLOCO 11 — Sobre o autor -->
    <section class="py-16 md:py-24 bg-white border-y border-[#E9E2D3]">
      <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="bg-[#F8F7F4] rounded-3xl p-8 sm:p-12 border border-[#E9E2D3] shadow-xs grid grid-cols-1 md:grid-cols-12 gap-8 items-center">
          
          <div class="md:col-span-4 flex flex-col items-center text-center">
            <div class="relative w-44 h-44 rounded-full p-2 bg-gradient-to-tr from-[#B18A47] to-[#0E2340] shadow-md">
              <img 
                src="/images/author-avatar.jpeg"
                @error="handleAuthorImgError"
                alt="Jefferson Alves da Silva" 
                loading="lazy"
                decoding="async"
                class="w-full h-full object-cover rounded-full"
              />
            </div>
            <h3 class="font-serif text-xl font-bold text-[#0E2340] mt-4">Jefferson Alves da Silva</h3>
            <p class="text-xs text-[#B18A47] font-semibold uppercase tracking-wider">Autor & Professor</p>
          </div>

          <div class="md:col-span-8 space-y-4">
            <span class="text-xs font-bold uppercase tracking-widest text-[#B18A47]">Sobre o Autor</span>
            <h2 class="font-serif text-3xl font-bold text-[#0E2340]">
              Quem escreveu este guia
            </h2>
            <div class="space-y-4 text-sm sm:text-base text-[#18232C]/90 leading-relaxed">
              <p>
                <strong>Jefferson Alves da Silva</strong> é professor de Filosofia e Ciências da Religião, farmacêutico e escritor. Atualmente, encontra-se em formação em Psicologia e Psicanálise.
              </p>
              <p>
                Sua trajetória reúne experiência docente, estudo interdisciplinar e interesse pelos processos de formação intelectual e autoconhecimento.
              </p>
              <p>
                Neste e-book, essa experiência é colocada a serviço de uma questão concreta: como ajudar uma pessoa interessada em Filosofia a construir um começo organizado, intelectualmente responsável e possível de sustentar?
              </p>
              <p class="font-medium text-[#2E4A3D]">
                O resultado é um guia comprometido com clareza, rigor conceitual, responsabilidade interpretativa e respeito à autonomia do leitor.
              </p>
            </div>
          </div>

        </div>
      </div>
    </section>

    <!-- BLOCO 13 — Contraste -->
    <section class="py-16 md:py-24 bg-[#F8F7F4]">
      <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 space-y-12">
        <div class="text-center max-w-3xl mx-auto space-y-3">
          <span class="text-xs font-bold uppercase tracking-widest text-[#B18A47]">Comparativo</span>
          <h2 class="font-serif text-3xl sm:text-4xl font-bold text-[#0E2340]">
            Você pode continuar procurando o ponto de partida — ou começar a construí-lo
          </h2>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
          
          <!-- Sem percurso -->
          <div class="p-8 rounded-2xl bg-white border border-[#6A5542]/30 space-y-6 shadow-xs">
            <h3 class="font-serif text-xl font-bold text-[#6A5542] flex items-center gap-2">
              <XCircle class="w-6 h-6 text-[#6A5542]" />
              Sem um percurso organizado
            </h3>
            <ul class="space-y-3 text-sm sm:text-base text-[#657078]">
              <li v-for="(item, i) in contrastWithout" :key="i" class="flex items-center gap-2">
                <span class="w-2 h-2 rounded-full bg-[#6A5542]"></span>
                <span>{{ item }}</span>
              </li>
            </ul>
          </div>

          <!-- Com orientação -->
          <div class="p-8 rounded-2xl bg-[#0E2340] text-[#F8F7F4] border border-[#B18A47] space-y-6 shadow-lg">
            <h3 class="font-serif text-xl font-bold text-[#B18A47] flex items-center gap-2">
              <CheckCircle2 class="w-6 h-6 text-[#B18A47]" />
              Com uma orientação inicial
            </h3>
            <ul class="space-y-3 text-sm sm:text-base text-[#E9E2D3]">
              <li v-for="(item, i) in contrastWith" :key="i" class="flex items-center gap-2">
                <span class="w-2 h-2 rounded-full bg-[#B18A47]"></span>
                <span>{{ item }}</span>
              </li>
            </ul>
          </div>

        </div>

        <!-- Frase de destaque -->
        <div class="p-6 md:p-8 rounded-2xl bg-white border-l-4 border-[#2E4A3D] text-center shadow-xs">
          <p class="font-serif text-lg sm:text-xl font-bold text-[#0E2340]">
            "Começar bem não significa escolher imediatamente o percurso perfeito. Significa saber por que você escolheu um caminho e como poderá corrigi-lo."
          </p>
        </div>
      </div>
    </section>

    <!-- BLOCO 12 — Oferta (Principal Checkout Box) -->
    <section id="oferta" class="py-16 md:py-24 bg-gradient-to-b from-[#091A2F] to-[#0E2340] text-white relative">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="bg-[#0E2340] rounded-3xl border-2 border-[#B18A47] p-8 sm:p-12 shadow-2xl space-y-8 relative overflow-hidden">
          <div class="absolute top-0 right-0 bg-[#B18A47] text-[#091A2F] text-xs font-extrabold uppercase px-6 py-2 rounded-bl-xl tracking-wider">
            Lançamento Especial
          </div>

          <div class="text-center space-y-4">
            <h2 class="font-serif text-3xl sm:text-4xl md:text-5xl font-extrabold text-white">
              Comece seu percurso filosófico com mais clareza
            </h2>
            <p class="text-lg text-[#E9E2D3]">
              E-book <strong>Primeiros Passos no Estudo da Filosofia</strong>
            </p>
          </div>

          <!-- Product Details Card -->
          <div class="bg-[#091A2F]/90 p-8 rounded-2xl border border-[#B18A47]/40 max-w-lg mx-auto text-center space-y-6 shadow-xl">
            <div class="inline-block px-3.5 py-1 rounded-full bg-[#B18A47]/20 text-[#B18A47] text-xs font-bold uppercase tracking-wider border border-[#B18A47]/30">
              Formato PDF
            </div>
            
            <div class="space-y-1">
              <span class="text-sm text-[#E9E2D3]/60 line-through block">De R$ 79,90</span>
              <div class="text-4xl sm:text-5xl font-extrabold text-white">
                R$ 39,90
              </div>
              <span class="text-xs text-[#B18A47] font-medium block pt-1">Preço promocional de lançamento — Oferta válida por tempo limitado.</span>
            </div>

            <!-- Botão Principal Oferta -->
            <a :href="checkoutUrl" target="_blank" rel="noopener noreferrer" class="w-full btn-gold-cta font-extrabold text-lg sm:text-xl py-4 sm:py-5 px-8 rounded-xl flex items-center justify-center gap-3 cursor-pointer group">
              <span class="tracking-wide">Quero adquirir o e-book</span>
              <div class="w-8 h-8 rounded-full bg-[#091A2F]/10 flex items-center justify-center group-hover:translate-x-1 transition-transform">
                <ArrowRight class="w-5 h-5 text-[#091A2F]" />
              </div>
            </a>

            <p class="text-xs text-[#E9E2D3]/75 leading-relaxed">
              Pagamento seguro. Após a confirmação, você receberá as instruções para acessar o arquivo digital.
            </p>
          </div>

          <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 pt-4 border-t border-[#B18A47]/30 text-center text-xs text-[#E9E2D3]">
            <div class="flex items-center justify-center gap-2">
              <ShieldCheck class="w-4 h-4 text-[#B18A47]" />
              <span>Compra 100% Segura</span>
            </div>
            <div class="flex items-center justify-center gap-2">
              <FileText class="w-4 h-4 text-[#B18A47]" />
              <span>Acesso Imediato em PDF</span>
            </div>
            <div class="flex items-center justify-center gap-2">
              <Award class="w-4 h-4 text-[#B18A47]" />
              <span>Garantia de Qualidade</span>
            </div>
          </div>

        </div>
      </div>
    </section>

    <!-- BLOCO 14 — Perguntas frequentes (FAQ) -->
    <section class="py-16 md:py-24 bg-white">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 space-y-12">
        <div class="text-center space-y-3">
          <span class="text-xs font-bold uppercase tracking-widest text-[#B18A47]">Dúvidas Frequentes</span>
          <h2 class="font-serif text-3xl sm:text-4xl font-bold text-[#0E2340]">
            Perguntas Frequentes
          </h2>
        </div>

        <div class="space-y-4">
          <div 
            v-for="(faq, i) in faqs" 
            :key="i"
            class="border border-[#E9E2D3] rounded-2xl overflow-hidden transition-all bg-[#F8F7F4]"
          >
            <button 
              @click="toggleFaq(i)"
              class="w-full p-5 text-left font-serif text-base sm:text-lg font-bold text-[#0E2340] flex items-center justify-between gap-4 hover:bg-[#E9E2D3]/40 transition-colors cursor-pointer"
            >
              <span>{{ faq.q }}</span>
              <ChevronDown 
                class="w-5 h-5 text-[#B18A47] shrink-0 transition-transform duration-200" 
                :class="{ 'rotate-180': activeFaq === i }"
              />
            </button>
            <div 
              v-show="activeFaq === i"
              class="p-5 pt-0 text-sm sm:text-base text-[#18232C]/85 border-t border-[#E9E2D3]/60 leading-relaxed bg-white"
            >
              {{ faq.a }}
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- BLOCO 15 — Chamada final -->
    <section class="py-16 md:py-24 bg-[#F8F7F4] border-t border-[#E9E2D3]">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center space-y-8">
        <div class="space-y-4">
          <h2 class="font-serif text-3xl sm:text-4xl md:text-5xl font-extrabold text-[#091A2F] leading-tight">
            O primeiro passo não é ler tudo. É aprender a escolher, compreender e continuar.
          </h2>
        </div>

        <div class="prose prose-lg mx-auto text-[#18232C]/90 space-y-4 leading-relaxed text-base sm:text-lg max-w-2xl">
          <p>
            Você não precisa esperar até possuir mais tempo, conhecer todos os autores ou encontrar a lista perfeita.
          </p>
          <p>
            Pode começar com uma pergunta, um texto adequado e critérios para reconhecer o que compreendeu, o que permanece difícil e qual deverá ser o próximo passo.
          </p>
          <p class="font-serif text-xl font-bold text-[#0E2340]">
            Primeiros Passos no Estudo da Filosofia oferece a estrutura inicial. O percurso será construído por você.
          </p>
        </div>

        <!-- Botão Chamada Final Otimizado -->
        <div class="pt-4 max-w-xl mx-auto space-y-3">
          <a :href="checkoutUrl" target="_blank" rel="noopener noreferrer" class="w-full btn-gold-cta font-extrabold py-4 sm:py-5 px-6 sm:px-8 rounded-2xl flex flex-col sm:flex-row items-center justify-center gap-2 sm:gap-4 cursor-pointer group shadow-lg">
            <span class="text-base sm:text-lg md:text-xl tracking-tight text-center">Quero começar meu percurso</span>
            <div class="flex items-center gap-2">
              <span class="text-sm sm:text-base bg-[#091A2F]/15 text-[#091A2F] px-3.5 py-1 rounded-lg font-extrabold whitespace-nowrap">por R$ 39,90</span>
              <div class="w-7 h-7 sm:w-8 sm:h-8 rounded-full bg-[#091A2F]/10 flex items-center justify-center group-hover:translate-x-1 transition-transform">
                <ArrowRight class="w-4 h-4 sm:w-5 sm:h-5 text-[#091A2F]" />
              </div>
            </div>
          </a>

          <p class="text-xs text-[#657078] font-medium">
            Receba o e-book em formato PDF.
          </p>
        </div>
      </div>
    </section>

    <!-- BLOCO 16 — Rodapé e aviso -->
    <footer class="bg-[#091A2F] text-[#E9E2D3] py-12 border-t border-[#B18A47]/30 text-xs sm:text-sm">
      <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 space-y-8">
        <div class="flex flex-col md:flex-row items-center justify-between gap-6 pb-8 border-b border-[#E9E2D3]/10">
          <div class="flex items-center gap-3 bg-white/95 px-5 py-2.5 rounded-xl border border-[#B18A47]/40 shadow-md">
            <img src="/images/logo.png" alt="Odisseia Filosófica" class="h-16 sm:h-20 w-auto object-contain" />
          </div>
          <div class="text-center md:text-right text-xs text-[#E9E2D3]/60">
            © Odisseia Filosófica. Todos os direitos reservados.
          </div>
        </div>

        <div class="text-center max-w-3xl mx-auto space-y-2 text-xs text-[#E9E2D3]/60 leading-relaxed">
          <p>
            <strong>Aviso:</strong> Este é um produto digital de finalidade educacional. O e-book não substitui formação acadêmica, orientação profissional ou acompanhamento psicológico.
          </p>
        </div>
      </div>
    </footer>

  </div>
</template>
