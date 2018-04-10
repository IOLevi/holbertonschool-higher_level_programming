#include "lists.h"
#include <stdio.h>

/**
 * check_cycle  - determines if a linked list has a cycle in it
 * @list: linked list
 * Return: 0 if no; 1 if yes
 */
int check_cycle(listint_t *list)
{
	listint_t *copy;
	listint_t *copyhead;
	listint_t *tmp;

	copy = malloc(sizeof(listint_t));
	copy->n = list->n;
	copy->next = NULL;
	copyhead = copy;

	while (list)
	{
		if (list->next == NULL)
			break;
		copy = copyhead;
		while (copy)
		{
			if (list->next->n == copy->n)
			{
				free_listint(copyhead);
				return (1);
			}

			if (copy->next == NULL)
				break;
			copy = copy->next;
		}

		list = list->next;
		/*add node to end of copy list*/
		tmp = malloc(sizeof(listint_t));
		tmp->n = list->n;
		tmp->next = NULL;
		copy->next = tmp;
	}
	free_listint(copyhead);
	return (0);
}
