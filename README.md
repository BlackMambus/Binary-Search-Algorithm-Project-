# Binary-Search-Algorithm-Project-

🧮 The Binary Search Algorithm is a highly efficient method for finding an item in a sorted list. Instead of checking each element one by one (like linear search), it cleverly cuts the search space in half with each step—like guessing a number and halving the possibilities based on whether it's too high or too low.

⚙️ How It Works
Here’s a breakdown of the process:

Start with two pointers: low and high—marking the beginning and end of your list.

Find the middle: Calculate mid = (low + high) // 2

Compare the middle value with the target:

If they match: 🎯 you're done!

If the target is less than the middle: search the left half (high = mid - 1)

If the target is greater than the middle: search the right half (low = mid + 1)
