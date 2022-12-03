#include "lists.h"
/**
 * is_palindrome - function to check if a list is
 * a palindrome
 * @head: head of the list
 * Return: 0 if a palindrome, 1 if otherwsie
*/

int is_palindrome(listint_t **head)
{
	listint_t *slow;
	listint_t *fast;
	listint_t *prev;
	listint_t *tmp;
	listint_t *right;
	listint_t *left;

	slow = *head;
	fast = *head;

	if (!*head)
	{
		return (1);
	}

	while (fast && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	prev = NULL;
	while (slow)
	{
		tmp = slow->next;
		slow->next = prev;
		prev = slow;
		slow = tmp;
	}
	right = *head;
	left = prev;
	while (right != NULL && left != NULL)
	{
		if (right->n != left->n)
		{
			return (0);
		}
		left = left->next;
		right = right->next;
	}
	return (1);
}
