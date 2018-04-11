#include "lists.h"

/**
 * insert_node - inserts a node into a sorted list
 * @head: head of the lsit
 * @number: number/node to insert
 * Return: address of node; or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *hptr;
    listint_t *new;
    listint_t *tmp;

    /* empty list */
    if (!*head)
        return (NULL);

    hptr = *head;

    new = malloc(sizeof(listint_t));
    new->n = number;
    new->next = NULL;

    while (hptr)
    {
        if (hptr->next == NULL)
        {
            if (number < hptr->n)
            {
                new->next = hptr;
                return (new);
            }
            else
            {
                hptr->next = new;
                return (new);
            }
        }

        if (number >= hptr->n && number <= hptr->next->n)
        {
            tmp = hptr->next;
            hptr->next = new;
            new->next = tmp;
            return (new);
        }

        if (number <= hptr->n && number <= hptr->next->n)
        {
            new->next = hptr;
            return (new);
        }

        hptr = hptr->next;
    }

    free(new);
    return (NULL);    
}