document.addEventListener("DOMContentLoaded", function () {
    const addBtn = document.getElementById("addBtn");  // ID of your Add button
    const tableBody = document.querySelector("#scheduleTable tbody");  // Table to append new row

    addBtn.addEventListener("click", async function (e) {
        e.preventDefault();

        // Collect data from form inputs by name
        const data = {
            instructor: document.querySelector("[name='instructor']").value,
            room: document.querySelector("[name='room']").value,
            day: document.querySelector("[name='day']").value,
            start_time: document.querySelector("[name='start_time']").value,
            end_time: document.querySelector("[name='end_time']").value,
            course: document.querySelector("[name='course']").value,
            subject: document.querySelector("[name='subject']").value,
            year: document.querySelector("[name='year']").value,
            section: document.querySelector("[name='section']").value,
        };

        try {
            const response = await fetch("/add_class/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": getCSRFToken(),  // Get CSRF token from cookie
                },
                body: JSON.stringify(data),
            });

            const result = await response.json();

            if (result.success) {
                const classData = result.class_entry;

                const newRow = document.createElement("tr");
                newRow.innerHTML = `
                    <td>${classData.course}</td>
                    <td>${classData.subject}</td>
                    <td>${classData.instructor}</td>
                    <td>${classData.room}</td>
                    <td>${classData.day}</td>
                    <td>${classData.start_time} - ${classData.end_time}</td>
                    <td>${classData.year}</td>
                    <td>${classData.section}</td>
                `;

                tableBody.appendChild(newRow);

                alert("✅ Class added successfully!");
            } else {
                console.error(result.error);
                alert("❌ Failed to add class: " + result.error);
            }
        } catch (error) {
            console.error(error);
            alert("❌ Error adding class");
        }
    });

    // Utility to get CSRF token from cookies
    function getCSRFToken() {
        let cookieValue = null;
        const cookies = document.cookie.split(";");
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.startsWith("csrftoken=")) {
                cookieValue = cookie.substring("csrftoken=".length);
                break;
            }
        }
        return cookieValue;
    }
});
