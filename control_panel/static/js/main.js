function pageLoader () {
    const divLoader = document.createElement('div');
    const spinner = document.createElement('span');

    divLoader.innerHTML = 'AGUARDE';
    divLoader.classList.add('div-loader');
    spinner.classList.add('spinner-border');


    divLoader.appendChild(spinner);
    document.body.appendChild(divLoader);
    document.body.classList.add('back-drop');
}

document.addEventListener('DOMContentLoaded', () => {
    setTimeout(() => {
        const divLoader = document.querySelector('.div-loader');
        document.body.classList.remove('back-drop');

        if (divLoader) {
            divLoader.remove();
        };
    }, 1000);
});

document.addEventListener('submit', () => {
    setTimeout(pageLoader, 1000);
});

pageLoader();