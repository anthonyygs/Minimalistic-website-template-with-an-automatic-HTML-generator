const textoRepetidoMobile = `
    <div class="espacoHorizontal"></div>
    <hr class="linhasInicioFim">
    
    <div class="espacoHorizontal fica"></div>
    <div class="circulo" id="mudarCorUm"><img class="pessoa" src="../imagens/pessoa.png"></div>
    <p class="tituloBarra">sobre mim:</p>
    <p class="textoBarra">Lorem ipsum dolor sit amet consectetur adipiscing elit. Quisque faucibus ex sapien vitae pellentesque sem placerat. Pulvinar vivamus fringilla lacus nec metus bibendum egestas.</p>
    <p class="tituloBarra">contato:</p>
    <p class="textoBarra">seuemailaqui@tuta.io</p>
    <div class="espacoHorizontal"></div>
    <p class="emProlDosAnimais mudarCorTres">"Plantas alimentam, animais sentem!"</p>
`;


const textoRepetido = `
    <div class="espacoHorizontal"></div>
    <div class="circulo" id="mudarCorDois"><img class="pessoa" src="../imagens/pessoa.png"></div>
    <p class="tituloBarra">sobre mim:</p>
    <p class="textoBarra">Lorem ipsum dolor sit amet consectetur adipiscing elit. Quisque faucibus ex sapien vitae pellentesque sem placerat. Pulvinar vivamus fringilla lacus nec metus bibendum egestas.</p>
    <p class="tituloBarra">contato:</p>
    <p class="textoBarra">seuemailaqui@tuta.io</p>
    <div class="espacoHorizontal"></div>
    <hr class="hrLateral">
    <p class="emProlDosAnimais mudarCorTres frase"></p>
    <p class="textoBarra autor"></p>
`;

// Color system, choose the colors below:

const cores = [
  "#7ead7d", "#92679c", "#628697", "#629783", "#c45f9d", "#628697",
  "#5f66c4", "#5fc4bc", "#b05fc4", "#628697", "#dcff5b", "#628697",
  "#74ff80", "#628697", "#74efff", "#ff7c9d", "#ebff7c", "#628697",
  "#ac62b3", "#a5e472",
]; 

const coresB = [ 
  "#7ead7d", "#629783", "#5f66c4", "#ac62b3", "#628697", "#628697", 
  "#5f66c4", "#92679c", "#b05fc4", "#629783",
]; 

function corAleatoriaA() {
  const indice = Math.floor(Math.random() * cores.length);
  return cores[indice];
}

function corAleatoriaB() {
  const indice = Math.floor(Math.random() * coresB.length);
  return coresB[indice];
}

// Adicione novas frases de sua preferência abaixo:

const frases = [
    {
        "frase": "Todo esforço deve ser feito para parar o cruel e desnecessário abate de animais, que deve ser destrutivo para nossa moral.",
        "autor": "Nikola Tesla"
    },
    {
        "frase": "Certamente é preferível cultivar vegetais, e eu penso, portanto, que o vegetarianismo é um afastamento louvável do hábito bárbaro estabelecido.",
        "autor": "Nikola Tesla"
    },
    {
        "frase": "Que podemos subsistir com alimentos vegetais e realizar nosso trabalho até com vantagem não é uma teoria, mas um fato bem demonstrado.",
        "autor": "Nikola Tesla"
    },
    {
        "frase": "Para nos libertarmos dos instintos e apetites animais, que nos mantêm para baixo, devemos começar pela raiz da qual emergimos: devemos efetuar uma reforma radical no caráter da alimentação.",
        "autor": "Nikola Tesla"
    },
    {
        "frase": "Acredito que, seja falando sobre desigualdade de gênero, racismo, direitos queer, direitos indígenas ou direitos dos animais, estamos falando sobre a luta contra a injustiça.",
        "autor": "Joaquin Phoenix"
    },
    {
        "frase": "Todos nós somos animais deste planeta. Todos nós somos criaturas. E os animais não-humanos sentem dor assim como nós sentimos. Eles também são fortes, inteligentes, industriosos, móveis e evolutivos.",
        "autor": "Joaquin Phoenix"
    },
    {
        "frase": "Cada pedaço de carne, frango ou peixe que você come, cada pedaço de couro ou pele que você usa, veio de um animal que foi torturado, separado de suas famílias e brutalmente morto.",
        "autor": "Lewis Hamilton"
    },
    {
        "frase": "Sou um firme defensor de uma dieta totalmente baseada em plantas e alimentos integrais, que pode expandir a longevidade e tornar você uma pessoa mais feliz de forma geral.",
        "autor": "Ariana Grande"
    },
    {
        "frase": "Além de concordar com os objetivos do vegetarianismo por razões estéticas e morais, é minha opinião que um modo de vida vegetariano, por seu efeito puramente físico no temperamento humano, influenciaria de forma muito benéfica a sorte da humanidade.",
        "autor": "Albert Einstein"
    },
    {
        "frase": "Então estou vivendo sem gorduras, sem carne, sem peixe, mas me sinto muito bem assim. Sempre me pareceu que o homem não nasceu para ser carnívoro.",
        "autor": "Albert Einstein"
    },
    {
        "frase": "Era uma empresa de hot dogs … e eu como esses incríveis hot dogs à base de plantas. … Então eu disse à empresa: 'Se vocês lançarem hot dogs à base de plantas, eu definitivamente farei um comercial para vocês.'",
        "autor": "Jennifer Coolidge"
    },
    {
        "frase": "Sou vegano e ativista pelos direitos dos animais porque me importo com mudanças climáticas, fome, saúde humana, minha saúde, saúde dos oceanos, desmatamento da floresta tropical e uso da água.",
        "autor": "Moby"
    },
    {
        "frase": "A maioria das pessoas não percebe a crueldade indescritível sofrida pelos animais em nossas fazendas industriais.",
        "autor": "Jane Goodall"
    },
    {
        "frase": "Parei de comer carne há cerca de 50 anos, quando olhei para a costeleta de porco no meu prato e pensei: isso representa medo, dor, morte. Foi o suficiente, e imediatamente adotei uma alimentação à base de plantas.",
        "autor": "Jane Goodall"
    }


];

function sortearFrase() {
    const indiceAleatorio = Math.floor(Math.random() * frases.length);
    return frases[indiceAleatorio];
}

function mostrarFraseAleatoria() {
    const fraseSorteada = sortearFrase();
    
    const elementosFrase = document.getElementsByClassName('frase');
    const elementosAutor = document.getElementsByClassName('autor');
    
    if (elementosFrase.length > 0) {
        elementosFrase[0].textContent = `"${fraseSorteada.frase}"`;
    }
    if (elementosAutor.length > 0) {
        elementosAutor[0].textContent = `-- ${fraseSorteada.autor} --`;
    }
}

function inicializarTudo() {
    const containersMobile = document.querySelectorAll('.barraLateralMobile');
    const containers = document.querySelectorAll('.barraLateral');
    if (containersMobile.length > 0) {
        containersMobile.forEach(container => {
            container.innerHTML = textoRepetidoMobile;
        });
        console.log("Conteúdo mobile inserido");
    }
    
    if (containers.length > 0) {
        containers.forEach(container => {
            container.innerHTML = textoRepetido;
        });
        console.log("Conteúdo desktop inserido");
    }
    
    // 2. Depois aplica as cores
    const elementoUm = document.getElementById("mudarCorUm");
    const elementoDois = document.getElementById("mudarCorDois");
    const elementosTres = document.querySelectorAll(".mudarCorTres");

    
    if (elementoUm) {
        elementoUm.style.backgroundColor = corAleatoriaA();
       
    }
    if (elementoDois) {
        elementoDois.style.backgroundColor = corAleatoriaA();
     
    }
    
    elementosTres.forEach((el, index) => {
        el.style.color = corAleatoriaB();
    
    });
    mostrarFraseAleatoria();
   
}

window.addEventListener("load", inicializarTudo);
document.addEventListener("DOMContentLoaded", inicializarTudo);
