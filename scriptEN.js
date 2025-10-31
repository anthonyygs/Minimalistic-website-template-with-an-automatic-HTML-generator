
const textoRepetidoMobile = `
    <div class="espacoHorizontal"></div>
    <hr class="linhasInicioFim">
   
    <div class="espacoHorizontal fica"></div>
    <div class="circulo" id="mudarCorUm"><img class="pessoa" src="../imagens/pessoa.png"></div>
    <p class="tituloBarra">about me:</p>
    <p class="textoBarra">Lorem ipsum dolor sit amet consectetur adipiscing elit. Quisque faucibus ex sapien vitae pellentesque sem placerat. Pulvinar vivamus fringilla lacus nec metus bibendum egestas.</p>
    <p class="tituloBarra">contact::</p>
    <p class="textoBarra">youremailhere@tuta.io</p>
    <div class="espacoHorizontal"></div>
    <p class="emProlDosAnimais mudarCorTres">"Plantas alimentam, animais sentem!"</p>
`;


const textoRepetido = `
    <div class="espacoHorizontal"></div>
    <div class="circulo" id="mudarCorDois"><img class="pessoa" src="../imagens/pessoa.png"></div>
    <p class="tituloBarra">about me:</p>
    <p class="textoBarra">Lorem ipsum dolor sit amet consectetur adipiscing elit. Quisque faucibus ex sapien vitae pellentesque sem placerat. Pulvinar vivamus fringilla lacus nec metus bibendum egestas.</p>
    <p class="tituloBarra">contact:</p>
    <p class="textoBarra">youremailhere@tuta.io</p>
    <div class="espacoHorizontal"></div>
    <hr class="hrLateral">
    <p class="emProlDosAnimais mudarCorTres frase"></p>
    <p class="textoBarra autor"></p>
`;


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

// Add new sentences of your choice below: 

const frases = [
    {
    "frase": "Every effort should be made to stop the cruel and unnecessary slaughter of animals, which must be destructive to our morals.",
    "autor": "Nikola Tesla"
    },
    {
    "frase": "It is certainly preferable to raise vegetables, and I think, therefore, that vegetarianism is a commendable departure from the established barbarious habit.",
    "autor": "Nikola Tesla"
    },
    {
    "frase": "That we can subsist on plant food and perform our work even to advantage is not a theory, but a well-demonstrated fact.",
    "autor": "Nikola Tesla"
    },
    {
    "frase": "To free ourselves from animal instincts and appetites, which keep us down, we should begin at the very root from which we spring: we should effect a radical reform in the character of the food.",
    "autor": "Nikola Tesla"
    },
    {
    "frase": "I think whether we’re talking about gender inequality or racism or queer rights or indigenous rights or animal rights, we’re talking about the fight against injustice. ",
    "autor": "Joaquin Phoenix"
    },
    {
    "frase": "We are all animals of this planet. We are all creatures. And non-human animals experience pain sensations just like we do. we do. They too are strong, intelligent, industrious, mobile, and evolutional.",
    "autor": "Joaquin Phoenix"
    },
    {
    "frase": "Every bit of meat, chicken, or fish you eat, every bit of leather or fur you wear, has come from an animal that has been tortured, pulled away from their families and brutally killed.",
    "autor": "Lewis Hamilton"
    },
    {
    "frase": "I am a firm believer in eating a full plant-based, whole food diet that can expand your life length and make you an all-around happier person.",
    "autor": "Ariana Grande"
    },
    {
    "frase": "Besides agreeing with the aims of vegetarianism for aesthetic and moral reasons, it is my view that a vegetarian manner of living by its purely physical effect on the human temperament would most beneficially influence the lot of mankind.",
    "autor": "Albert Einstein"
    },
    {
    "frase": "So I am living without fats, without meat, without fish, but am feeling quite well this way. It always seems to me that man was not born to be a carnivore.",
    "autor": "Albert Einstein"
    },
    {
    "frase": "It was a hot dog company … and I eat these amazing plant‑based hot dogs. … So I said to the company, ‘If you guys come out with plant‑based hot dogs, I will definitely do a commercial for you.’",
    "autor": "Jennifer Coolidge"
    },
    {
    "frase": "I’m a vegan and an animal rights activist because I care about climate change and famine and human health and my health and ocean health and rainforest deforestation and water use.",
    "autor": "Moby"
    },
    {
    "frase": "Most people do not realize the unspeakable cruelty suffered by animals on our factory farms. ", "autor": "Jane Goodall " 
    }, 
    {
    "frase": "I stopped eating meat some 50 years ago when I looked at the pork chop on my plate and thought: this represents fear, pain, death. That did it, and I went plant-based instantly", "autor": "Jane Goodall " 
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

    const elementoUm = document.getElementById("mudarCorUm");
    const elementoDois = document.getElementById("mudarCorDois");
    const elementosTres = document.querySelectorAll(".mudarCorTres");
    
    console.log("Elemento Um:", elementoUm);
    console.log("Elemento Dois:", elementoDois);
    console.log("Elementos Tres:", elementosTres.length);
    
    if (elementoUm) {
        elementoUm.style.backgroundColor = corAleatoriaA();
        console.log("Cor aplicada no elementoUm");
    }
    if (elementoDois) {
        elementoDois.style.backgroundColor = corAleatoriaA();
        console.log("Cor aplicada no elementoDois");
    }
    
    elementosTres.forEach((el, index) => {
        el.style.color = corAleatoriaB();
        console.log(`Cor aplicada no mudarCorTres ${index}`);
    });
    
 
    mostrarFraseAleatoria();
    
}


window.addEventListener("load", inicializarTudo);
document.addEventListener("DOMContentLoaded", inicializarTudo);

