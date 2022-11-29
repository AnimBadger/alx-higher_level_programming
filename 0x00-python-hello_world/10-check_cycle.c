#include "lists.h"
/**
 * check_cycle - check a singly linked have a cycle
 * @list: pointer to head of the list
 * Return: 0 if there is no cycle
 * 1 if there is a cycle
*/
int check_cycle(listint_t *list)
{
	listint_t *slow;
	listint_t *fast;

	if (list == NULL)
	{
		return (0);
	}
	slow = list;
	fast = list;
	while (fast != NULL)
	{
		if (slow == fast)
		{
			return (1);
		}
		fast = fast->next->next;
		slow = slow->next;
	}
	return (0);
}
