let isLoading = true;

/* ..다른 코드들 */

const url = 'https://jsonplaceholder.typicode.com/users';
// const url = 'https://www.google.com';

fetch(url)
  .then((response) => {
    const contentType = response.headers.get('content-type');
    if (contentType.includes('application/json')) {
      return response.json();
    }
    throw new Error('response is not json data');
  })
  .then((result) => {
    // 리스폰스 처리
    console.log(result);
  })
  .catch((error) => {
    // 에러 처리
    console.log(error);
  })
  .finally(() => {
    isLoading = false;
    console.log(isLoading);
  });