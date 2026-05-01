const practiceState = {
  owner: "main branch",
  message: "This message starts from main and will be changed by each branch.",
  status: "ready for practice"
};

function describePractice() {
  return `${practiceState.owner}: ${practiceState.message}`;
}

console.log(describePractice());
