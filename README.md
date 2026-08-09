# Data Structures and Algorithms Pattern Handbook

<a href="https://leetcode.com/u/logitechsoumili"><img src="https://img.shields.io/badge/Platform-LeetCode-FFA116?logo=leetcode&logoColor=white" alt="LeetCode" /></a>
<a href="https://www.geeksforgeeks.org/user/logitechsoumili"><img src="https://img.shields.io/badge/Platform-GeeksforGeeks-2F8D46?logo=geeksforgeeks&logoColor=white" alt="GeeksforGeeks" /></a>

A structured handbook of Data Structures and Algorithms patterns, containing problem solutions, detailed notes, brute-force and optimized approaches, templates, common mistakes, and interview-focused insights.

### Why Pattern-Based Learning?

Instead of memorizing individual solutions for hundreds of problems, the most effective way to master Data Structures and Algorithms is to focus on reusable algorithmic patterns. By learning to recognize the underlying structure of a problem, you develop the intuition needed to solve unfamiliar questions. Mastering patterns bridges the gap between seeing a problem for the first time and designing an optimal solution efficiently, which is a key skill for technical interviews.

Focusing on patterns provides:
* **Pattern recognition signals** — Clues in the problem description that suggest a specific approach.
* **Brute-force to optimized transitions** — Step-by-step guidance on how to identify bottlenecks and reduce complexity.
* **Complexity analysis** — In-depth analysis of time and space trade-offs.
* **Common mistakes** — Pitfalls, edge cases, and typical bugs to avoid.
* **Interview-focused insights** — Tips on how to structure thoughts and communicate solutions clearly.
* **Revision-friendly notes** — Summarized concepts and key takeaways for quick review.


## Learning Roadmap

This handbook follows a structured DSA roadmap organized by patterns to build problem-solving intuition, online assessment (OA) speed, and competitive programming readiness. Problems may be implemented in different languages (such as C++, Python, or Java), focusing on algorithmic reasoning, pattern recognition, data structure selection, and complexity analysis rather than language-specific features. 

### Resources

* [DSA Roadmap Tracking Sheet](https://docs.google.com/spreadsheets/d/1T5-nGsJ9WNwna44e9WWRD0jlZIT5KxVOGvylcvvVrY8/edit?usp=sharing)
* [DSA Patterns 2025 Playlist (Padho with Pratyush)](https://www.youtube.com/playlist?list=PLbJhGqY-mq47k_WLUtzVjmarUm1EuXPj2)

## Repository Structure

Each pattern is organized into its own directory. Every problem contains:

* `solution.*` — Language-specific implementation files (e.g., C++, Python, Java) for the problem.
* `notes.md` — Problem summary, alternative approaches, observations, complexity analysis, common mistakes, and interview notes.

```text
dsa-pattern-handbook/
├── README.md
├── 01_Two_Pointers/
│   ├── README.md
│   ├── 01_two_sum/
│   │   ├── solution.cpp
│   │   ├── solution.py
│   │   └── notes.md
│   └── ...
├── 02_Sliding_Window/
│   ├── README.md
│   ├── 01_max_subarray_sum/
│   │   ├── solution.cpp
│   │   ├── solution.py
│   │   └── notes.md
│   └── ...
```


## Pattern Index

### [1. Two Pointers](./01_Two_Pointers/README.md)

The Two Pointers pattern uses two indices to traverse a linear data structure efficiently. It is commonly applied to sorted arrays, pair-based searches, in-place modifications, and partitioning problems.

### [2. Sliding Window](./02_Sliding_Window/README.md)

The Sliding Window pattern is used for problems involving contiguous subarrays or substrings. By maintaining a dynamic window and updating it incrementally, it avoids redundant computations and often reduces quadratic solutions to linear time.

### [3. Slow & Fast Pointers](./03_Slow_Fast_Pointers/README.md)

The Slow & Fast Pointers pattern (also known as Floyd's Cycle Detection Algorithm) uses two pointers moving at different speeds to traverse a linear or cyclic structure. It is commonly applied to cycle detection in linked lists, finding loop entry points, determining midpoints, and solving cyclic mapping problems in arrays.

### [4. Kadane's Algorithm](./04_Kadane_Algorithm/README.md)

The Kadane's Algorithm pattern is a dynamic programming technique used to find the maximum or minimum contiguous subarray sum or product in linear time and constant space. It involves making local optimal decisions at each element to build the global optimal subarray, and is commonly applied to circular arrays, multi-state dynamic programming, and contiguous array optimization problems.

### [5. Prefix Sum](./05_Prefix_Sum/README.md)

The Prefix Sum pattern precomputes cumulative totals to answer range sum queries over contiguous subarrays in constant O(1) time. When combined with HashMaps, it efficiently tracks frequencies or earliest indices of previous prefix states, enabling linear O(n) solutions for target sum matches, divisibility constraints, and binary balance problems even in the presence of negative numbers.

## Learning Approach

Mastering algorithms requires a systematic, workflow-oriented approach. For every problem in this handbook, we follow these steps:

* **Understand the brute-force solution** — Start by conceptualizing and analyzing the most straightforward approach to establish a baseline.
* **Identify the bottleneck** — Pinpoint the specific operations or redundant steps that degrade performance.
* **Derive the optimized approach** — Select appropriate data structures and algorithmic techniques to eliminate bottlenecks and minimize time/space complexity.
* **Extract the reusable pattern** — Abstract the core strategy so it can be recognized and applied to similar challenges in interviews, OAs, and competitive programming.
* **Document observations and mistakes** — Record language-independent implementation considerations, edge cases, and debugging lessons.
* **Store notes for future revision** — Keep structured, lightweight documentation for efficient recall and interview preparation.

## How to Use This Handbook

To get the most out of this repository, follow this recommended progression:

1. **Read the pattern README first** — Start by reading the folder-level README to understand the pattern's core concept, classification, and templates.
2. **Learn recognition signals** — Familiarize yourself with the clues and keywords that indicate when to apply the pattern.
3. **Understand the brute-force solution** — Walk through the initial sub-optimal approach for a problem to build a clear understanding of its baseline constraints.
4. **Study the optimized solution** — Analyze the optimal approach and compare it to the brute-force version to see how the bottleneck was solved efficiently.
5. **Review notes and common mistakes** — Read the notes file for each problem to grasp the edge cases, implementation details, and typical pitfalls.
6. **Re-solve representative problems during revision** — Re-visit key questions periodically in the language appropriate for your current practice, interview, or OA context to build speed and accuracy.


## Languages

* **C++**
* **Python**
* **Java**


## Support

If this handbook helps with DSA practice, interview preparation, or pattern revision, consider giving the repository a star. It helps others discover the resource and motivates continued improvements.
