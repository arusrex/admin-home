window.addEventListener('DOMContentLoaded', event => {
    const datatablesSimple = document.getElementById('dataTable');
    if (datatablesSimple) {
        new DataTable(datatablesSimple,{
            responsive: true,
            language: {
                search: 'Buscar:',
                info: 'Mostrando de _START_ a _END_ de _TOTAL_ items no total',
                lengthMenu: 'Mostrar _MENU_ registros por página',  // Tradução da seleção de número de registros
                infoEmpty: 'Nenhum registro disponível',
                infoFiltered: '(filtrado de _MAX_ registros no total)',
                paginate: {
                    first: 'Primeiro',
                    last: 'Último',
                    next: 'Próximo',
                    previous: 'Anterior'
                },
                zeroRecords: 'Nenhum registro encontrado',
                emptyTable: 'Nenhum dado disponível na tabela',
                loadingRecords: 'Carregando...',
                processing: 'Processando...',
            },
            layout: {
                topStart: 'buttons',
            },
            buttons: [{
                extend:'copy', text:'Copiar dados',
            },{
                extend:'excel', text:'Relatório excel simples',
            },{
                extend:'pdf', text:'Relatório pdf simples',
            }],
        });
    };
});