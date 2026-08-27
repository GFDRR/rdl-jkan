export default {
  isLoading: false,
  isLoaded: false,
  syncStateWhileLoading(loadFunction) {
    this.isLoading = true;
    loadFunction().then(() => {
      this.isLoaded = true;
      this.isLoading = false;
    }).catch((error) => {
      console.error("Error loading:", error);
      this.isLoading = false;
    })
  }
}