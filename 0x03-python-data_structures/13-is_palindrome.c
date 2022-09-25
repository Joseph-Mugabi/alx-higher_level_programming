#include "lists.h"
#include <stddef.h>


/**
 *  is_palind - recursively moves pointer to linked list node and match
 *  @start: pointer to head (** gives different address so not same as end)
 *  @end: pointer to last node
 *  Return: 0 if not, 1 if palindrome
 */
int is_palind(listint_t **start, listint_t *end)
{
	if (end == NULL)
		return (1);
	/* use a recursion */
	if (is_palind(start, end->next) && ((*start)->n == end->n))
	{
		*start = (*start)->next;
		return (1);
	}
	return (0);
}

/**
 * is_palindrome - determine if singly linked list is palindrome
 * @head: pointer to head of singly linked list
 * Return: 0 if not, 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *start = *head;
	listint_t *end = *head;

	if (head == NULL)
		return (0);
	if (*head == NULL)
		return (1); /* a node list is a palindrome */
	return (is_palind(&start, end));
}
