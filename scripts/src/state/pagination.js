export default {
  currentPage: 1,
  itemsPerPage: 10,

  get totalPages() {
    return Math.ceil(this.display.length / this.itemsPerPage);
  },

  getPaginationNumbers(currentPage, totalPages) {
    if (totalPages <= 7) {
      return Array.from({ length: totalPages }, (_, i) => i + 1);
    }

    const pages = [];
    pages.push(1);

    let startPage = Math.max(2, currentPage - 1);
    let endPage = Math.min(totalPages - 1, currentPage + 1);

    if (currentPage <= 3) {
      startPage = 2;
      endPage = 5;
    } else if (currentPage >= totalPages - 2) {
      startPage = totalPages - 4;
      endPage = totalPages - 1;
    }

    if (startPage > 2) pages.push("...");
    for (let i = startPage; i <= endPage; i++) pages.push(i);
    if (endPage < totalPages - 1) pages.push("...");
    pages.push(totalPages);

    return pages;
  },

  get paginationNumbers() {
    return this.getPaginationNumbers(this.currentPage, this.totalPages);
  },

  get paginatedDatasets() {
    const start = (this.currentPage - 1) * this.itemsPerPage;
    return this.datasetsByFilterAndSearch.slice(start, start + this.itemsPerPage);
  },

  get paginationStart() {
    return (this.currentPage - 1) * this.itemsPerPage + 1;
  },

  get paginationEnd() {
    return Math.min(this.currentPage * this.itemsPerPage, this.display.length);
  },
}