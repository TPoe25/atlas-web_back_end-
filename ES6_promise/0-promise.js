const fetchDataFromApi = () => new Promise((resolve) => {
  setTimeout(() => {
    resolve('Data from API');
  }, 1000);
});

export default fetchDataFromApi;
