document.addEventListener("DOMContentLoaded", function() {
    const alerts = document.querySelectorAll('.alert');
    
    alerts.forEach(alert => {
        alert.classList.add('alert-show');
        
        // Fechar a notificação após 5 segundos
        setTimeout(() => {
            alert.classList.remove('alert-show');
            alert.classList.add('slideOut');
            setTimeout(() => {
                alert.remove();
            }, 300);
        }, 5000);
    });
});
