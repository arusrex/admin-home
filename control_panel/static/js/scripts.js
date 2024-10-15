/*!
    * Start Bootstrap - SB Admin v7.0.7 (https://startbootstrap.com/template/sb-admin)
    * Copyright 2013-2023 Start Bootstrap
    * Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-sb-admin/blob/master/LICENSE)
    */
    // 
// Scripts
// 

window.addEventListener('DOMContentLoaded', event => {

    // Toggle the side navigation
    const sidebarToggle = document.body.querySelector('#sidebarToggle');
    if (sidebarToggle) {
        // Uncomment Below to persist sidebar toggle between refreshes
        // if (localStorage.getItem('sb|sidebar-toggle') === 'true') {
        //     document.body.classList.toggle('sb-sidenav-toggled');
        // }
        sidebarToggle.addEventListener('click', event => {
            event.preventDefault();
            document.body.classList.toggle('sb-sidenav-toggled');
            localStorage.setItem('sb|sidebar-toggle', document.body.classList.contains('sb-sidenav-toggled'));
        });
    }

});


// DARK MODE
document.addEventListener('DOMContentLoaded', () => {
    const toggleButton = document.getElementById('toggle-dark-mode');
    const tableDark = document.querySelector('#dataTable');
    const cardDivs = document.querySelectorAll('.card-div-dark');
    const formsDarks = document.querySelectorAll('.form-control');
    const mainDark = document.querySelector('main');
    const footerDark = document.querySelector('footer');

    if (localStorage.getItem('dark-mode') === 'enabled') {
        document.body.classList.add('bg-dark', 'text-secondary');
        mainDark.classList.add('border','border-light', 'rounded');
        footerDark.classList.add('bg-dark', 'text-light');
        if (tableDark){tableDark.classList.add('table-dark');};
        cardDivs.forEach(cardDiv => cardDiv.classList.add('card-dark',));
        formsDarks.forEach(formsDark => formsDark.classList.add('card-dark'));
    };

    if (toggleButton) {
        toggleButton.addEventListener('click', () => {
            document.body.classList.toggle('bg-dark');
            document.body.classList.toggle('text-secondary');

            mainDark.classList.toggle('border');
            mainDark.classList.toggle('border-light');
            mainDark.classList.toggle('rounded');

            footerDark.classList.toggle('bg-dark');
            footerDark.classList.toggle('text-light');

            if (tableDark) {
                tableDark.classList.toggle('table-dark');
            };
    
            cardDivs.forEach(cardDiv => {
                cardDiv.classList.remove('card-dark');
            });
    
            formsDarks.forEach(formsDark => {
                formsDark.classList.remove('card-dark');
            });
    
            if (document.body.classList.contains('bg-dark')) {
                localStorage.setItem('dark-mode', 'enabled');
            } else {
                localStorage.setItem('dark-mode', 'disabled');
            };

            location.reload()
        });
    };    
});

