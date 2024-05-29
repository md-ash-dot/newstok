


function openDeleteModal(slug, title) {
    const deleteConfirm = document.getElementById('deleteConfirm');
    deleteConfirm.href = `/article/delete/${slug}/`;
    const modalTitle = document.getElementById('deleteModalLabel');
    modalTitle.textContent = `Delete article: "${title}"?`;
    const deleteModal = new bootstrap.Modal(document.getElementById('deleteModal'));
    deleteModal.show();
}
