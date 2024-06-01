/**
* Opens a confirmation modal for deleting an article.
*
* Functionality:
* - Retrieves the element for the article deletion confirmation link.
* - Sets the href attribute of the confirmation link to point to 
*   the deletion endpoint for the specific article using the provided slug.
* - Retrieves the modal title element and updates its text content 
*   to display a message asking if the user wants to delete the specified article.
* - Initializes and displays the Bootstrap modal to prompt the user 
*   for confirmation before deletion.
*/
function openArticleDeleteModal(slug, title) {
    const articleDeleteConfirm = document.getElementById('articleDeleteConfirm');
    articleDeleteConfirm.href = `/article/delete/${slug}/`;
    const modalTitle = document.getElementById('ArticleDeleteModalLabel');
    modalTitle.textContent = `Delete article: "${title}"?`;
    const articleDeleteModal = new bootstrap.Modal(document.getElementById('articleDeleteModal'));
    articleDeleteModal.show();
}