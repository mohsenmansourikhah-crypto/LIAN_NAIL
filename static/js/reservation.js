document.addEventListener('DOMContentLoaded', function () {
    const buttons = document.querySelectorAll('.time-buttons button');
    const hiddenInput = document.getElementById('id_time');
    const dateInput = document.getElementById('id_date');

    if (!hiddenInput || !dateInput || buttons.length === 0) {
        return;
    }

    buttons.forEach(btn => {
        btn.addEventListener('click', () => {
            if (btn.classList.contains('disabled')) return;

            buttons.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            hiddenInput.value = btn.dataset.time;
        });
    });

    dateInput.addEventListener('change', () => {
        // ریست کامل ساعت
        hiddenInput.value = '';
        buttons.forEach(b => {
            b.classList.remove('active');
            b.classList.remove('disabled');
        });

        fetch(`/reserve/api/reserved-times/?date=${dateInput.value}`)
            .then(res => res.json())
            .then(times => {
                buttons.forEach(btn => {
                    if (times.includes(btn.dataset.time)) {
                        btn.classList.add('disabled');
                    }
                });
            });
    });
});
