#!/usr/bin/python3
"""
Task 0: Simple templating program
Generates personalized invitation files from a template and a list of attendees.
"""

import os


def generate_invitations(template, attendees):
    """
    Generates invitation files from a template for each attendee.

    Args:
        template (str): The invitation template with placeholders.
        attendees (list): List of dictionaries with attendee info.

    Behavior:
        - Validates input types.
        - Handles empty template or attendees list.
        - Replaces missing data with 'N/A'.
        - Writes each invitation to output_X.txt, starting from 1.
    """
    # Input type check
    if not isinstance(template, str):
        print(f"Error: Template must be a string, got {type(template).__name__}")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print(f"Error: Attendees must be a list of dictionaries")
        return

    # Empty template check
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    # Empty attendees list check
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Process each attendee
    for idx, attendee in enumerate(attendees, start=1):
        invitation = template
        # Replace placeholders
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            invitation = invitation.replace(f"{{{key}}}", str(value))
        
        # Generate output file
        output_filename = f"output_{idx}.txt"
        try:
            with open(output_filename, "w") as f:
                f.write(invitation)
        except Exception as e:
            print(f"Error writing to file {output_filename}: {e}")
