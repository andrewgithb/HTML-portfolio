const textElement = document.querySelector('.animated-text');
const text = 'Drew\'s Clothing Co';
let index = 0;

function typeText() {
  textElement.textContent += text[index];
  index++;

  if (index < text.length) {
    setTimeout(typeText, 100); // Adjust the delay (in milliseconds) for typing speed
  }
}

typeText();