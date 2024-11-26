window.addEventListener('load', function() {
    // Defina o tempo de carregamento em milissegundos (por exemplo, 3000 ms = 3 segundos)
    const loadingTime = 10000;

    setTimeout(function() {
        window.location.href = '/index'; // Redireciona para a página de conteúdo
    }, loadingTime);
});
