#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * run_infinite_loop - Function to create an infinite loop
 *
 * This function runs an infinite loop using sleep(1).
 *
 * Return: Always returns 0.
 */
int run_infinite_loop(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Main function
 *
 * This program creates five child processes using fork(),
 * printing information about each zombie process before entering an
 * infinite loop.
 *
 * Return: Always returns 0.
 */
int main(void)
{
	int iteration;
	pid_t zombie;

	/* Create five child processes */
	for (iteration = 0; iteration < 5; iteration++)
	{
		zombie = fork();

		/* If the process is the child, exit */
		if (!zombie)
			return (0);

		/* If the process is Parent, print info about the zombie process */
		printf("Zombie process created, PID: %d\n", zombie);
	}

	/* Enter an infinite loop */
	run_infinite_loop();

	return (0);
}
