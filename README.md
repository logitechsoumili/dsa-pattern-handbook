# Data Structures and Algorithms Pattern Handbook

<a href="https://leetcode.com/u/logitechsoumili"><img src="https://img.shields.io/badge/Platform-LeetCode-FFA116?logo=leetcode&logoColor=white" alt="LeetCode" /></a>
<a href="https://www.geeksforgeeks.org/user/logitechsoumili"><img src="https://img.shields.io/badge/Platform-GeeksforGeeks-2F8D46?logo=geeksforgeeks&logoColor=white" alt="GeeksforGeeks" /></a>
<a href="https://www.python.org/"><img src="https://img.shields.io/badge/Language-Python-3776AB?logo=python&logoColor=white" alt="Python" /></a>
<a href="https://www.oracle.com/java/"><img src="https://img.shields.io/badge/Language-Java-ED8B00?logo=java&logoColor=white" alt="Java" /></a>
<a href="https://en.cppreference.com/w/c"><img src="https://img.shields.io/badge/Language-C-A8B9CC?logo=c&logoColor=white" alt="C" /></a>

A structured handbook of Data Structures and Algorithms patterns, containing problem solutions, detailed notes, brute-force and optimized approaches, templates, common mistakes, and interview-focused insights.

## Learning Roadmap

This handbook follows a structured DSA roadmap organized by patterns to build problem-solving intuition and interview readiness. Problems are solved, documented, and organized according to the roadmap sequence. 

The complete tracking sheet can be viewed below:
* [DSA Roadmap Tracking Sheet](https://docs.google.com/spreadsheets/d/1T5-nGsJ9WNwna44e9WWRD0jlZIT5KxVOGvylcvvVrY8/edit?usp=sharing)

## Repository Structure

Each pattern is organized into its own directory. Every problem contains:

* `solution files` — Final optimized implementations in one or more languages.
* `notes.md` — Problem summary, alternative approaches, observations, complexity analysis, common mistakes, and interview notes.

```text
DSA-Practice/
├── README.md
├── 01_Two_Pointers/
│   ├── README.md
│   ├── 01_two_sum/
│   │   ├── solution.py
│   │   └── notes.md
│   └── ...
├── 02_Sliding_Window/
│   ├── README.md
│   ├── 01_max_subarray_sum/
│   │   ├── solution.py
│   │   └── notes.md
│   └── ...
```

## Pattern Index

### [1. Two Pointers](./01_Two_Pointers/README.md)

The Two Pointers pattern uses two indices to traverse a linear data structure efficiently. It is commonly applied to sorted arrays, pair-based searches, in-place modifications, and partitioning problems.

### [2. Sliding Window](./02_Sliding_Window/README.md)

The Sliding Window pattern is used for problems involving contiguous subarrays or substrings. By maintaining a dynamic window and updating it incrementally, it avoids redundant computations and often reduces quadratic solutions to linear time.

## Learning Approach

For each problem:

1. Understand the brute-force solution.
2. Identify the bottleneck.
3. Derive the optimized approach.
4. Document key observations and pattern recognition signals.
5. Store the final implementation and notes for future revision.

## Technology Stack

* **Python** — Primary language used for solving and documenting problems.
* **Java** — Used for revision and alternative implementations.
* **C/C++** — Used for low-level implementation practice.