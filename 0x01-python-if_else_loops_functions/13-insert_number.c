#include "lists.h"
/**
 * insert_node - function to insert node\
 * in a sorted linked list
 * @head: head of list
 * @number: number to be inserted
 * Return: head if success else NULL
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp;
	listint_t *ptr;

	ptr = *head;
	temp = malloc(sizeof(listint_t));
	temp->n = number;

	if (temp == NULL)
	{
		return (NULL);
	}
	if (!ptr || number < ptr->n)
	{
		temp = *head;
		*head = temp;
		return (*head);
	}
	else
	{
		while (ptr->next != NULL && ptr->next->n < number)
		{
		ptr = ptr->next;
		}
		temp->next = ptr->next;
		ptr->next = temp;
	}
	return (*head);
}
