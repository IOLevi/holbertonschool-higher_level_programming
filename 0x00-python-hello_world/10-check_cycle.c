#include "lists.h"
#include <stdio.h>

/**
 * check_cycle  - determines if a linked list has a cycle in it
 * @list: linked list
 * Return: 0 if no; 1 if yes
 */
int check_cycle(listint_t *list)
{
	listint_t *fast;

	fast = list->next;
	while(list)
	{
		if (fast == NULL)
			return (0);

		if (fast == list)
			return (1);
		list = list->next;
		if ((fast = fast->next) == NULL)
			return (0);
		fast = fast->next;

	}
	return (0);
}
