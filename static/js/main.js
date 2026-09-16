/**
 * NIET SMART UNIVERSITY ERP PLATFORM - JAVASCRIPT
 * Simple, vanilla, readable JS for tab switching, modals, and search.
 */

document.addEventListener('DOMContentLoaded', () => {
    // 1. Live Time Display in Header/Status
    const timeEl = document.getElementById('liveClock');
    if (timeEl) {
        const updateClock = () => {
            const now = new Date();
            timeEl.innerText = now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit', second: '2-digit' });
        };
        updateClock();
        setInterval(updateClock, 1000);
    }

    // 2. Tab Switching Logic (e.g. Student & Admin Dashboards)
    const tabButtons = document.querySelectorAll('.tab-btn');
    tabButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            const targetTab = btn.getAttribute('data-tab');
            const parent = btn.closest('.tabs-container');
            if (!parent) return;

            // Remove active from sibling buttons
            parent.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            // Hide all tab panes in this container
            parent.querySelectorAll('.tab-pane').forEach(pane => pane.classList.remove('active'));
            const activePane = parent.querySelector(`#${targetTab}`);
            if (activePane) {
                activePane.classList.add('active');
            }
        });
    });

    // 3. Quick Table Search Filter
    const searchInputs = document.querySelectorAll('.table-search-input');
    searchInputs.forEach(input => {
        input.addEventListener('keyup', () => {
            const query = input.value.toLowerCase();
            const tableId = input.getAttribute('data-target-table');
            const table = document.getElementById(tableId);
            if (!table) return;

            const rows = table.querySelectorAll('tbody tr');
            rows.forEach(row => {
                const text = row.innerText.toLowerCase();
                row.style.display = text.includes(query) ? '' : 'none';
            });
        });
    });

    // 4. Modal Helpers (Vanilla HTML/CSS Modal)
    window.openModal = function(modalId) {
        const modal = document.getElementById(modalId);
        if (modal) modal.style.display = 'flex';
    };

    window.closeModal = function(modalId) {
        const modal = document.getElementById(modalId);
        if (modal) modal.style.display = 'none';
    };

    // Close modal when clicking on overlay background
    window.addEventListener('click', (e) => {
        if (e.target.classList.contains('modal-overlay')) {
            e.target.style.display = 'none';
        }
    });

    // 5. Fee Receipt Print Helper
    window.printReceipt = function(receiptAreaId) {
        const printContent = document.getElementById(receiptAreaId).innerHTML;
        const originalContent = document.body.innerHTML;
        document.body.innerHTML = printContent;
        window.print();
        document.body.innerHTML = originalContent;
        window.location.reload();
    };
});
