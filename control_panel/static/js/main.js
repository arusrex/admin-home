function excluirRegistro (deleteButton) {
    const divExclude = document.createElement('div');
    const divSimple = document.createElement('div');
    const pExclude = document.createElement('p');
    const btnConfirm = document.createElement('button');
    const btnCancel = document.createElement('button');

    document.body.classList.add('back-drop');
    divExclude.classList.add('div-exclude');
    divSimple.classList.add('div-simple');
    btnConfirm.classList.add('btn-confirm-exclude');
    btnConfirm.value = "confirm";
    btnCancel.classList.add('btn-cancel-exclude');
    btnCancel.value = "cancel";

    pExclude.innerText = 'Deseja realmente excluir?'
    btnConfirm.innerText = 'Sim';
    btnCancel.innerText = 'Cancelar';

    divExclude.appendChild(pExclude);
    divExclude.appendChild(divSimple);
    divSimple.appendChild(btnConfirm);
    divSimple.appendChild(btnCancel);

    document.body.appendChild(divExclude);
    
    let deleteUrl = deleteButton.href;

    if (btnConfirm) {
        document.querySelector('.btn-confirm-exclude').addEventListener('click', function (e) {
            e.preventDefault();
            console.log('Confirm pressionado');
            console.log(deleteUrl);
            window.location.href = deleteUrl;
        });
    }

    if (btnCancel) {
        document.querySelector('.btn-cancel-exclude').addEventListener('click', (e) => {
            e.preventDefault();
            console.log('Cancel pressionado');
            divExclude.remove();
            document.body.classList.remove('back-drop');
        });
    }
};

function removeBackdropMessages () {
    console.log('Chegou no remove back-drop');
    document.querySelector('.messages').remove();
    document.body.classList.remove('back-drop');
};

function pageLoader (messages) {
    if (messages) {
        document.body.classList.add('back-drop');
        setTimeout(removeBackdropMessages, 3000);
    } else {
        const divLoader = document.createElement('div');
        const spinner = document.createElement('span');
    
        divLoader.innerHTML = 'AGUARDE';
        divLoader.classList.add('div-loader');
        spinner.classList.add('spinner-border');
    
        divLoader.appendChild(spinner);
        document.body.appendChild(divLoader);
        document.body.classList.add('back-drop');
    };
};

document.addEventListener('DOMContentLoaded', () => {
    const messages = document.querySelector('.messages');

    if (messages) {
        pageLoader(messages);
    } else {
        pageLoader();
        setTimeout(() => {
            const divLoader = document.querySelector('.div-loader');
            document.body.classList.remove('back-drop');
        
            if (divLoader) {
                divLoader.remove();
            };
        }, 1000);
    }

    document.addEventListener('submit', () => {
        if (messages) {
            pageLoader(messages);
        } else {
            pageLoader();
        }
    });

    document.querySelector('#dataTable').addEventListener('click', (e) => {
        let target = e.target.closest('.deleteUser');

        if (target) {
            e.preventDefault();
            
            // Log apenas para depuração
            console.log('Clicou em delete:', target);
            
            excluirRegistro(target);
        }
    });
});

