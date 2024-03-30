document.addEventListener("DOMContentLoaded", function() {
    // Function to load edit form into modal
    function loadEditForm(productId) {
        fetch(`/edit/${productId}/`)
            .then(response => response.text())
            .then(data => {
                document.querySelector('.modal-body').innerHTML = data;
                $('#editModal').modal('show');
            })
            .catch(error => console.log(error));
    }

    // Add event listener to all edit buttons
    const editButtons = document.querySelectorAll('.edit-btn');
    editButtons.forEach(button => {
        button.addEventListener('click', function() {
            const productId = this.getAttribute('data-product-id');
            loadEditForm(productId);
        });
    });
});
