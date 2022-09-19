#include "lists.h"
#include <stdio.h>

/**
 *  check_cycle - checks if singly linked list is a cycle
 *  @list: linked list
 *  Return: 0 if there is no cycle, 1 if there is cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *head = list;
	listint_t *tail = list;

	if (!list)
		return (0);

	while (1)
	{
		if (head->next != NULL && head->next->next != NULL)
		{
			head = head->next->next;
			tail = tail->next;

			if (head == tail)
				return (1);
		}
		else
			return (0);
	}
}
