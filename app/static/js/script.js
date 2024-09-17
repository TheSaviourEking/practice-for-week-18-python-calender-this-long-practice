document.addEventListener('DOMContentLoaded', () => {
    // USING THE DATE PICKER THROUGH CALENDAR
    const changeDate = document.getElementById('change-date');
    changeDate.addEventListener('change', (e) => {
        const dateInput = e.target.value;

        if (dateInput) {
            const [year, month, day] = dateInput.split('-');
            const url = `/${year}/${month}/${day}`;

            window.location.href = url;
        }
    });

    // ------------------------------------------ USING DROPDOWN MENU --------------------------------------------------------------------------------------
    const changeYearSelect = document.getElementById('change-year');
    const changeMonthSelect = document.getElementById('change-month');
    const changeDaySelect = document.getElementById('change-day');

    // List of months
    const currentDate = new Date()
    const currentMonth = currentDate.getMonth() + 1;
    const currentYear = currentDate.getFullYear();

    const months = [
        { value: 1, name: 'January' },
        { value: 2, name: 'February' },
        { value: 3, name: 'March' },
        { value: 4, name: 'April' },
        { value: 5, name: 'May' },
        { value: 6, name: 'June' },
        { value: 7, name: 'July' },
        { value: 8, name: 'August' },
        { value: 9, name: 'September' },
        { value: 10, name: 'October' },
        { value: 11, name: 'November' },
        { value: 12, name: 'December' }
    ];

    months.forEach(month => {
        const option = document.createElement('option');
        option.value = month.value;
        option.textContent = month.name;
        if (month.value === currentMonth) {
            month.selected = true;
        }
        changeMonthSelect.appendChild(option);
    });

    for (let i = currentYear - 10; i <= currentYear + 10; i++) {
        const option = document.createElement('option');
        option.value = i;
        option.textContent = i;
        if (i === currentYear) {
            option.selected = true;
        }
        changeYearSelect.appendChild(option);
    }


    function getDaysInMonth(month, year) {
        return new Date(year, month, 0).getDate();
    }

    function updateDays() {
        const selectedMonth = parseInt(changeMonthSelect.value);
        const selectedYear = parseInt(changeYearSelect.value);

        if (!isNaN(selectedMonth) && !isNaN(selectedYear)) {
            const daysInMonth = getDaysInMonth(selectedMonth, selectedYear);
            changeDaySelect.innerHTML = '<option value="" disabled selected>Select a Day</option>';
            for (let i = 1; i <= daysInMonth; i++) {
                const option = document.createElement('option');
                option.value = i;
                option.textContent = i;
                changeDaySelect.appendChild(option);
            }
        }
    }


    changeMonthSelect.addEventListener('change', updateDays);
    changeYearSelect.addEventListener('change', updateDays);

    // --------+++++++++++++++++++++++++++++++++++------------------------
    function handleChangeDateFormSubmit() {
        const changeDateForm = document.getElementById('date-change-form');
        changeDateForm.addEventListener('submit', e => {
            e.preventDefault();
            const year = e.target[0].value;
            const month = e.target[1].value;
            const day = e.target[2].value;

            const url = `/${year}/${month}/${day}`;
            window.location.href = url;
        })
    }

    handleChangeDateFormSubmit();
})
