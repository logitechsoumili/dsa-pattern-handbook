# Data Structures and Algorithms Pattern Handbook

<a href="https://leetcode.com/u/logitechsoumili"><img src="https://img.shields.io/badge/Platform-LeetCode-FFA116?logo=leetcode&logoColor=white" alt="LeetCode" /></a>
<a href="https://www.geeksforgeeks.org/user/logitechsoumili"><img src="https://img.shields.io/badge/Platform-GeeksforGeeks-2F8D46?logo=geeksforgeeks&logoColor=white" alt="GeeksforGeeks" /></a>
<a href="https://isocpp.org/"><img src="https://img.shields.io/badge/Language-C++-00599C?logo=c%2B%2B&logoColor=white" alt="C++" /></a>

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

## Why Modern C++?

* **Rich STL Ecosystem** — Highly optimized data structures and algorithms (containers, iterators, sort, binary search) available out-of-the-box.
* **Strong Interview & OA Adoption** — Widely supported and preferred in industry technical evaluations and online assessments.
* **Competitive Programming Suitability** — Extremely fast execution times, efficient memory usage, and granular control.
* **Zero-Overhead Pattern Implementation** — Clean, performant translation of common DSA pattern logic without language-level overhead.


## Learning Roadmap

This handbook follows a structured DSA roadmap organized by patterns to build problem-solving intuition, online assessment (OA) speed, and competitive programming readiness. Problems are solved using Modern C++ as the primary language with a focus on standard STL containers and algorithms, documented, and organized according to the roadmap sequence. 

### Resources

* [DSA Roadmap Tracking Sheet](https://docs.google.com/spreadsheets/d/1T5-nGsJ9WNwna44e9WWRD0jlZIT5KxVOGvylcvvVrY8/edit?usp=sharing)
* [DSA Patterns 2025 Playlist (Padho with Pratyush)](https://www.youtube.com/playlist?list=PLbJhGqY-mq47k_WLUtzVjmarUm1EuXPj2)

## Repository Structure

Each pattern is organized into its own directory. Every problem contains:

* `solution files` — Final optimized implementations in Modern C++ (primary) and Python (reference).
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

## Learning Approach

Mastering algorithms requires a systematic, workflow-oriented approach. For every problem in this handbook, we follow these steps:

* **Understand the brute-force solution** — Start by conceptualizing and analyzing the most straightforward approach to establish a baseline.
* **Identify the bottleneck** — Pinpoint the specific operations or redundant steps that degrade performance.
* **Derive the optimized STL approach** — Apply Modern C++ Standard Template Library (STL) containers and optimized algorithms to eliminate the bottlenecks and minimize complexity.
* **Extract the reusable pattern** — Abstract the core strategy so it can be recognized and applied to similar challenges in interviews, OAs, and competitive programming.
* **Document observations and mistakes** — Record C++ specific memory details, type edge cases (such as unsigned index underflow), and debugging lessons.
* **Store notes for future revision** — Keep structured, lightweight documentation for efficient recall and interview preparation.

## How to Use This Handbook

To get the most out of this repository, follow this recommended progression:

1. **Read the pattern README first** — Start by reading the folder-level README to understand the pattern's core concept, classification, and templates.
2. **Learn recognition signals** — Familiarize yourself with the clues and keywords that indicate when to apply the pattern.
3. **Understand the brute-force solution** — Walk through the initial sub-optimal approach for a problem to build a clear understanding of its baseline constraints.
4. **Study the optimized C++ solution** — Analyze the primary C++ STL-based solution and compare it to the brute-force version to see how the bottleneck was solved efficiently.
5. **Review notes and common mistakes** — Read the notes file for each problem to grasp the edge cases, typical pitfalls, and C++ specific compiler or runtime gotchas.
6. **Re-solve representative problems during revision** — Re-visit the key questions periodically in C++ to build speed and accuracy for interviews, online assessments, and competitive programming.


## Technology Stack

* **C++** (Primary Language)
* **Python** (Reference Implementations)
* **Java** (Additional Learning Language)


## Support

If this handbook helps with DSA practice, interview preparation, or pattern revision, consider giving the repository a star. It helps others discover the resource and motivates continued improvements.