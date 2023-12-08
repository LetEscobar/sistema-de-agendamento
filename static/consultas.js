window.onload = () => {
    const btn = document.querySelector('#btn-nova-consulta');

    btn.addEventListener('click', () => {
        document.querySelector('#id').value = ''
        document.querySelector('#paciente').value = ''
        document.querySelector('#data_consulta').value = ''
        document.querySelector('#hora_consulta').value = ''
        document.querySelector('#informacoes_adicionais').value = ''
        document.querySelector('#modal-nova-consulta form').action = 'cadastro';
        
        const modal = document.querySelector('#modal-nova-consulta');
        modal.style.display = 'block';
    });
};

const closeModal = () => {
    const modal = document.querySelector('#modal-nova-consulta');
    modal.style.display = 'none';
}

const edit = (id, paciente, data_consulta, hora_consulta, informacoes_adicionais) => {
    document.querySelector('#id').value = id
    document.querySelector('#paciente').value = paciente
    document.querySelector('#data_consulta').value = data_consulta
    document.querySelector('#hora_consulta').value = hora_consulta
    document.querySelector('#informacoes_adicionais').value = informacoes_adicionais
    document.querySelector('#modal-nova-consulta form').action = 'editar';
    const modal = document.querySelector('#modal-nova-consulta');
    modal.style.display = 'block';
}