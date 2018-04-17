#include "lists.h"

/**
 * is_palindrome - checks whether a linked list is a palindrome
 * @head: head of a single linked list
 * Return: 0 if is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *hpointer;
	int *new;
	int len;
	int i;

	hpointer = *head;

	/* empty list is a palindrome */
	if (!head || !*head)
		return (1);

	len = 0;
	while (hpointer)
	{
		len++;
		hpointer = hpointer->next;
	}

	hpointer = *head;
	new = malloc(sizeof(int) * len);

	i = 0;
	while (hpointer)
	{
		new[i] = hpointer->n;
		hpointer = hpointer->next;
		i++;
	}
	for (i = 0; i < len / 2; i++)
	{
		if (new[i] != new[len - 1 - i])
			return (0);
	}
	return (1);
}
