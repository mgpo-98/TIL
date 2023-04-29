async function showQuiz() {
  try {
    const response = await fetch('https://learn.codeit.kr/api/quiz');
    const test = await response.json();
    const yourAnswer = prompt(test.quiz);
    if (yourAnswer.toLowerCase() === test.answer) {
      alert(`Good Job, ${test.explanation} => Let\'s learn more with Codeit!`);
    } else {
      throw new Error('wrong');
    }
  } catch (error) {
    if (error.message === 'wrong') {
      alert('You need to learn JavaScript with Codeit!');
    } else {
      alert('Error');
    }
  } finally {
    window.open('https://codeit.kr', '_blank');
  }
}

showQuiz();