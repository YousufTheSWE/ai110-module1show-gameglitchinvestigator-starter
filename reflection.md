# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  - It had questionable text like "Something is off" and it wasn't as responsive. It also gave incorrect hints.
- List at least two concrete bugs you noticed at the start  
  - One bug is giving me GO LOWER when I should've went higher!
  - Giving me a negative score!
  - When I disabled show hint, it didn't decrement my attempts.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| 50    | Go Higher         | Go LOWER        | N/A                    |
| 50 (with show hints off) | decrement attempts | no attempts changed | N/A |
| 12    | Positive/zeo score | score of -35 | N/A |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  - Anthropic
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  - AI suggested that history/status was not updated on new game, I manually checked code and figured out it was true then fixed it.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  - AI suggested that score should be changed at new game, I figured out that score shouldn't be reset on new games.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
