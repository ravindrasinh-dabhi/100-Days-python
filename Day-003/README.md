# Day 003 – Python List Methods

**Challenge:** 100 Days of Python  
**Day:** 03  
**Date:** 24 November 2026  
**Topic:** Python List Methods  
**Project:** Electrical Equipment Inventory Manager  
**Status:** Completed ✅

## Objective
Learn how to manipulate Python lists using built-in list methods to manage electrical equipment inventory.

## Concepts Learned

| Method | Purpose |
|---|---|
| `append()` | Adds an element at the end |
| `insert()` | Inserts an element at a specific index |
| `pop()` | Removes an element using its index |
| `remove()` | Removes the first matching element |
| `sort()` | Sorts elements in ascending order |
| `count()` | Counts occurrences of an element |
| `index()` | Finds the index of an element |
| `reverse()` | Reverses the list in place |

## Practical Project: Electrical Equipment Inventory Manager

### Problem Statement
An electrical maintenance department needs to manage its equipment inventory. The program uses Python list methods to add new equipment, remove unavailable equipment, identify duplicate IDs and organize the inventory.

### Initial Data

```python
equipment = [105, 102, 108, 102, 110, 104, 108]
```

### Tasks Completed
1. Added equipment ID `112` using `append()`.
2. Inserted equipment ID `101` at index `0`.
3. Removed the equipment at index `3` using `pop()`.
4. Removed the first occurrence of `108` using `remove()`.
5. Sorted equipment IDs using `sort()`.
6. Counted occurrences of equipment ID `102`.
7. Found the index of equipment ID `110`.
8. Reversed the sorted inventory using `reverse()`.

## Final Output

**Sorted Inventory:**
```text
[101, 102, 102, 104, 105, 110, 112]
```

**Count of equipment ID 102:**
```text
2
```

**Index of equipment ID 110:**
```text
5
```

**Reversed Inventory:**
```text
[112, 110, 105, 104, 102, 102, 101]
```

## Key Learnings
- Understood how Python list methods modify existing lists.
- Learned the difference between `pop()` and `remove()`.
- Practised sorting and reversing lists.
- Learned to identify duplicate elements using `count()`.
- Used `index()` to locate specific equipment IDs.

## Repository Structure

```text
100-Days-of-Python/
│
└── Day-003/
    ├── main.py
    └── README.md
```

## Next Challenge
**Day 004 – List Mutability and References**

Continue learning Python through practical engineering-related projects.

---
*100 Days of Python – Learn, Practise, Build.*