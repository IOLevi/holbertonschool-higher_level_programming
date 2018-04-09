#include "lists.h"
#include <stdio.h>

/**
 * check_cycle  - determines if a linked list has a cycle in it
 * Return: 0 if no; 1 if yes
 */
int check_cycle(listint_t *list)
{
	int headnum;
	
	headnum = list->n;
	while (*list)
	{
		if (list->next == NULL)
			break;
		if (list->next.n == headnum)
			return (1);

		list = list->next;
	}

	return (0);

}
