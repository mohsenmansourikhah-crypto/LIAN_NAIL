document.addEventListener("DOMContentLoaded", function () {

    const dateInput = document.querySelector(".jalali-datepicker");
    const timeButtons = document.querySelectorAll(".time-buttons button");
    const hiddenTimeInput = document.querySelector('input[name="time"]');

    if (!dateInput || !timeButtons.length || !hiddenTimeInput) return;

    // انتخاب ساعت
    timeButtons.forEach(btn => {
        btn.addEventListener("click", () => {
            if (btn.classList.contains("disabled")) return;

            timeButtons.forEach(b => b.classList.remove("active"));
            btn.classList.add("active");
            hiddenTimeInput.value = btn.dataset.time;
        });
    });

    // تغییر تاریخ
    dateInput.addEventListener("change", function () {
        const date = this.value;
        hiddenTimeInput.value = "";

        timeButtons.forEach(btn => {
            btn.classList.remove("active", "disabled");
            btn.disabled = false;
        });

        fetch(`/api/reserved-times/?date=${date}`)
            .then(res => res.json())
            .then(reservedTimes => {
                console.log("Reserved:", reservedTimes); // 👈 حتما ببین

                timeButtons.forEach(btn => {
                    if (reservedTimes.includes(btn.dataset.time)) {
                        btn.classList.add("disabled");
                        btn.disabled = true;
                    }
                });
            });
    });

});
