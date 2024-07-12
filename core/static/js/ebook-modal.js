export default function initEbookModal() {
    const modalBox = document.querySelector(".modal_box");
    const modalForm = document.getElementById("modalForm");
    const modalName = document.getElementById("modalName");
    const modalPhone = document.getElementById("modalTelefone");
    const modalEmail = document.getElementById("modalEmail");
    const downloadFinished = document.getElementById("downloadFinished");

    function closeModal(modal) {
        modal.classList.remove("active_animation");
        modal.style.display = "none";
    }

    document.querySelectorAll("[data-buttonModal]").forEach((button) => {
        button.addEventListener("click", () => {
            modalBox.classList.add("active_animation");
            modalForm.style.display = "block";
        });
    });

    document.getElementById("backModalBtn").addEventListener("click", (e) => {
        e.preventDefault();
        closeModal(modalBox);
    });

    modalBox.addEventListener("click", (e) => {
        if (e.target === modalBox) closeModal(modalBox);
    });

    function validateForm() {
        return modalName.value.length > 3 && modalPhone.value.length > 8 && modalEmail.value.length > 7;
    }

    document.getElementById("dowloadModalBtn").addEventListener("click", (e) => {
        e.preventDefault();

        if (validateForm()) {
            const formData = new FormData(modalForm);

            fetch(modalForm.action, {
                method: "POST",
                body: formData,
                headers: {
                    "X-CSRFToken": formData.get("csrfmiddlewaretoken"),
                },
            })
                .then((response) => response.json())
                .then((data) => {
                    if (data.success) {
                        closeModal(modalBox);
                        downloadFinished.classList.add("active_animation");

                        Toastify({
                            text: "Sucesso!",
                            duration: 3000,
                            close: true,
                            gravity: "top",
                            position: "right",
                            stopOnFocus: false,
                            style: { background: "white", color: "#242C12" },
                        }).showToast();

                        // Limpar os campos do formulário
                        modalName.value = "";
                        modalPhone.value = "";
                        modalEmail.value = "";

                        // Criar um link para o download e abrir em uma nova aba
                        const downloadLink = document.createElement('a');
                        downloadLink.href = data.download_url;
                        downloadLink.target = '_blank'; // Abrir em uma nova aba
                        downloadLink.download = ''; // Indica que o link é para download
                        downloadLink.click();
                    } else {
                        // Preparar mensagens de erro
                        let errorMessages = "Erro ao processar o formulário!";
                        if (data.errors) {
                            errorMessages = "";
                            for (const [field, errors] of Object.entries(data.errors)) {
                                errorMessages += `${field.charAt(0).toUpperCase() + field.slice(1)}: ${errors.join(", ")}\n`;
                            }
                        }

                        Toastify({
                            text: errorMessages,
                            duration: 3000,
                            close: true,
                            gravity: "top",
                            position: "right",
                            stopOnFocus: true,
                            style: { background: "red" },
                        }).showToast();
                    }
                })
                .catch((error) => {
                    console.error("There was a problem with the fetch operation:", error);
                    Toastify({
                        text: "Erro ao processar o formulário!",
                        duration: 3000,
                        close: true,
                        gravity: "top",
                        position: "right",
                        stopOnFocus: true,
                        style: { background: "red" },
                    }).showToast();
                });
        } else {
            Toastify({
                text: "Preencha os campos corretamente!",
                duration: 3000,
                close: true,
                gravity: "top",
                position: "right",
                stopOnFocus: true,
                style: { background: "red" },
            }).showToast();
        }
    });

    document.getElementById("CloseDowloadBtn").addEventListener("click", (e) => {
        e.preventDefault();
        closeModal(modalBox);
        closeModal(downloadFinished);
    });
}
