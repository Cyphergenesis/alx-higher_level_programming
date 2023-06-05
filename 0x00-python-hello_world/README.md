# 0x00.Python-Hello, World

##### By: Guillaume
##### Weight: 1
##### Allowed editors: Vim | vi, Emacs

### Concepts
**For this project, we expect you to look at this concept:**
+ Python programming

### Resources
+ The Python tutorial
+ Whetting Your Appetite
+ Using the Python Interpreter
+ An Informal Introduction to Python 
+ Learn to Program

### lists.h file

```
#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 *
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

#endif /* LISTS_H */
```

