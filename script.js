const chatWindow = document.getElementById("chat-window");
const form = document.getElementById("chat-form");
const input = document.getElementById("user-input");
const sendBtn = document.getElementById("send-btn");
const suggestions = document.getElementById("suggestions");

const sidebar = document.getElementById("sidebar");
const sidebarToggle = document.getElementById("sidebar-toggle");
const sidebarClose = document.getElementById("sidebar-close");
const sidebarOverlay = document.getElementById("sidebar-overlay");
const historyList = document.getElementById("history-list");

const ROBOT_ICON = `
  <svg viewBox="0 0 24 24" width="14" height="14">
    <rect x="4" y="8" width="16" height="12" rx="4" fill="#5eead4"/>
    <rect x="10" y="3" width="4" height="5" rx="1" fill="#5eead4"/>
    <circle cx="9" cy="14" r="1.7" fill="#0b0f19"/>
    <circle cx="15" cy="14" r="1.7" fill="#0b0f19"/>
    <rect x="9" y="17" width="6" height="1.4" rx="0.7" fill="#0b0f19"/>
  </svg>
`;

/* ---------- sidebar open/close (mobile slide-in) ---------- */
function openSidebar() {
  sidebar.classList.add("open");
  sidebarOverlay.classList.add("show");
}
function closeSidebar() {
  sidebar.classList.remove("open");
  sidebarOverlay.classList.remove("show");
}
sidebarToggle?.addEventListener("click", openSidebar);
sidebarClose?.addEventListener("click", closeSidebar);
sidebarOverlay?.addEventListener("click", closeSidebar);

/* ---------- history: remembers every question you've asked ---------- */
function addHistoryItem(question) {
  const emptyEl = document.getElementById("history-empty");
  if (emptyEl) emptyEl.remove();

  const li = document.createElement("li");
  const btn = document.createElement("button");
  btn.type = "button";
  btn.className = "history-item";
  btn.textContent = question;
  btn.title = question; // shows full text on hover if truncated
  btn.addEventListener("click", () => {
    sendMessage(question); // tap a past question to ask it again
    closeSidebar();
  });
  li.appendChild(btn);
  historyList.prepend(li); // newest question appears at the top
}

function scrollToBottom() {
  chatWindow.scrollTop = chatWindow.scrollHeight;
}

function addUserMessage(text) {
  const msg = document.createElement("div");
  msg.className = "msg msg-user";
  msg.innerHTML = `
    <div class="bubble-wrap">
      <div class="bubble"></div>
    </div>
  `;
  msg.querySelector(".bubble").textContent = text;
  chatWindow.appendChild(msg);
  scrollToBottom();
}

function addBotMessage({ answer, matched_question, confidence }) {
  const msg = document.createElement("div");
  msg.className = "msg msg-bot";

  const bubbleWrap = document.createElement("div");
  bubbleWrap.className = "bubble-wrap";

  const bubble = document.createElement("div");
  bubble.className = "bubble";
  bubble.textContent = answer;
  bubbleWrap.appendChild(bubble);

  if (matched_question) {
    const meta = document.createElement("div");
    meta.className = "match-meta";
    const pct = Math.round((confidence || 0) * 100);
    meta.innerHTML = `
      <span class="match-badge">${pct}% match</span>
      <span class="match-source">"${matched_question}"</span>
    `;
    bubbleWrap.appendChild(meta);
  }

  const avatar = document.createElement("div");
  avatar.className = "avatar";
  avatar.innerHTML = ROBOT_ICON;

  msg.appendChild(avatar);
  msg.appendChild(bubbleWrap);
  chatWindow.appendChild(msg);
  scrollToBottom();
}

function addTypingIndicator() {
  const msg = document.createElement("div");
  msg.className = "msg msg-bot typing";
  msg.id = "typing-indicator";
  msg.innerHTML = `
    <div class="avatar">${ROBOT_ICON}</div>
    <div class="bubble-wrap">
      <div class="bubble">
        <span class="dot"></span><span class="dot"></span><span class="dot"></span>
      </div>
    </div>
  `;
  chatWindow.appendChild(msg);
  scrollToBottom();
}

function removeTypingIndicator() {
  const el = document.getElementById("typing-indicator");
  if (el) el.remove();
}

async function sendMessage(text) {
  if (!text.trim()) return;

  addUserMessage(text);
  addHistoryItem(text);
  input.value = "";
  sendBtn.disabled = true;
  addTypingIndicator();

  try {
    const res = await fetch("/get_response", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: text }),
    });
    const data = await res.json();
    removeTypingIndicator();
    addBotMessage(data);
  } catch (err) {
    removeTypingIndicator();
    addBotMessage({
      answer: "Something went wrong reaching the server. Is the Flask app running?",
      matched_question: null,
      confidence: 0,
    });
  } finally {
    sendBtn.disabled = false;
    input.focus();
  }
}

form.addEventListener("submit", (e) => {
  e.preventDefault();
  sendMessage(input.value);
});

suggestions.addEventListener("click", (e) => {
  const chip = e.target.closest(".chip");
  if (!chip) return;
  sendMessage(chip.dataset.q);
});
