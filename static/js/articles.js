function openArticleDeleteModal(slug, title) {
    const articleDeleteConfirm = document.getElementById('articleDeleteConfirm');
    articleDeleteConfirm.href = `/article/delete/${slug}/`;
    const modalTitle = document.getElementById('deleteModalLabel');
    modalTitle.textContent = `Delete article: "${title}"?`;
    const deleteModal = new bootstrap.Modal(document.getElementById('articleDeleteModal'));
    deleteModal.show();
}
