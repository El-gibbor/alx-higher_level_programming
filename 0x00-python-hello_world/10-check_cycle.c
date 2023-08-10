#include "lists.h"
#include <stdio.h>
/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: the linked list to check
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *oneStep = list, *twoSteps = list;

	if (oneStep == NULL && twoSteps == NULL)
		return (0);
	while (oneStep && twoSteps && twoSteps->next)
	{
		oneStep = oneStep->next;
		twoSteps = twoSteps->next->next;
		if (twoSteps == oneStep)
			return (1);
	}
	return (0);
}
