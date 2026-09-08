export default {
  currentPage: 1,
  itemsPerPage: 10,

  get totalPages() {
    return Math.ceil(this.display.length / this.itemsPerPage);
  },

  get paginationNumbers() {
    if (this.totalPages <= 7) {
      return Array.from({ length: this.totalPages }, (_, i) => i + 1);
    }

    const pages = [];
    pages.push(1);

    let startPage = Math.max(2, this.currentPage - 1);
    let endPage = Math.min(this.totalPages - 1, this.currentPage + 1);

    if (this.currentPage <= 3) {
      startPage = 2;
      endPage = 5;
    } else if (this.currentPage >= this.totalPages - 2) {
      startPage = this.totalPages - 4;
      endPage = this.totalPages - 1;
    }

    if (startPage > 2) pages.push("...");
    for (let i = startPage; i <= endPage; i++) pages.push(i);
    if (endPage < this.totalPages - 1) pages.push("...");
    pages.push(this.totalPages);

    return pages;
  },

  get paginationStart() {
    return (this.currentPage - 1) * this.itemsPerPage + 1;
  },

  get paginationEnd() {
    return Math.min(this.currentPage * this.itemsPerPage, this.display.length);
  },
};
