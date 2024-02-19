from __future__ import annotations

import inspect
from typing import Callable

import print_color


MAX_LENGTH = 70


def filter_parameters(func: Callable, input_parameters: dict) -> dict:
    """
    Filter input parameters to only include those that are required by the function.

    Args:
        func (Callable): The function to filter the parameters for.
        input_parameters (dict): The input parameters to filter.

    Returns:
        dict: The filtered input parameters.
    """
    parameters = inspect.signature(func).parameters

    print(parameters)

    return {key: value for key, value in input_parameters.items() if key in parameters}


def print_success(message: str, step: int | None = None, max_step: int | None = None) -> None:
    """
    Print a success message.

    Args:
        message (str): The message to print.
        step (int | None): The current step. Defaults to None.
        max_step (int | None): The maximum step. Defaults to None.
    """
    txt = _format_message(message, step, max_step, MAX_LENGTH)
    print_color.print(txt, tag="success", tag_color="green", color="white")


def print_warning(message: str, step: int | None = None, max_step: int | None = None) -> None:
    """
    Print a warning message.

    Args:
        message (str): The message to print.
        step (int | None): The current step. Defaults to None.
        max_step (int | None): The maximum step. Defaults to None.
    """
    txt = _format_message(message, step, max_step, MAX_LENGTH)
    print_color.print(txt, tag="warning", tag_color="yellow", color="white")


def print_error(message: str, step: int | None = None, max_step: int | None = None) -> None:
    """
    Print an error message.

    Args:
        message (str): The message to print.
        step (int | None): The current step. Defaults to None.
        max_step (int | None): The maximum step. Defaults to None.
    """
    txt = _format_message(message, step, max_step, MAX_LENGTH)
    print_color.print(txt, tag="failure", tag_color="red", color="magenta")


def _format_message(message: str, step: int | None, max_step: int | None, max_length: int = 70) -> str:
    """
    Format a message to include the current step and the maximum step.
    Truncate the message if it is too long.
    """
    if step is not None and max_step is not None:
        step_text = f"[{step}/{max_step}]"
        remaining_space = max_length - len(step_text)
        if len(message) > remaining_space:
            message_length = remaining_space - 3
            message = message[:message_length] + "..."

        spaces = max_length - len(message) - len(step_text)
        return f"{message}{'.' * spaces}{step_text}"

    if len(message) > max_length:
        return message[: max_length - 3] + "..."

    return message
