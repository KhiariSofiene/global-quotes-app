// Replace the value below with your deployed backend URL *without* trailing slash.
// Example: const BACKEND_URL = "https://my-quotes-app.onrender.com";
const BACKEND_URL = "https://global-quotes-app.onrender.com";

const quoteText = document.getElementById("quote-text");
const quoteAuthor = document.getElementById("quote-author");
const btn = document.getElementById("get-quote");

async function getQuote() {
  try {
    quoteText.innerText = "Loading...";
    const res = await fetch(`${BACKEND_URL}/quote`);
    if (!res.ok) throw new Error("Network response not ok");
    const data = await res.json();
    quoteText.innerText = `"${data.text}"`;
    quoteAuthor.innerText = `— ${data.author}`;
  } catch (err) {
    quoteText.innerText = "Could not fetch quote. Make sure BACKEND_URL is set correctly in script.js";
    quoteAuthor.innerText = "";
    console.error(err);
  }
}

btn.addEventListener("click", getQuote);
