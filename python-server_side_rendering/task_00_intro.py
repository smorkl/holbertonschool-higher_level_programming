import os

def generate_invitations(template, attendees):
  """
  Generates personalized invitation files from a template and list of attendees.

  Args:
      template: The template string containing placeholders.
      attendees: A list of dictionaries, where each dictionary represents an attendee with keys 'name', 'event_title', 'event_date', and 'event_location'.
  """

  if not isinstance(template, str):
    print("Error: Template must be a string.")
    return
  if not isinstance(attendees, list) or not all(isinstance(d, dict) for d in attendees):
    print("Error: Attendees must be a list of dictionaries.")
    return

  if not template:
    print("Template is empty, no output files generated.")
    return
  if not attendees:
    print("No data provided, no output files generated.")
    return

  for i, attendee in enumerate(attendees):
    # Replace placeholders with attendee data
    processed_template = template.format(**attendee, **{"event_date": attendee.get("event_date", "N/A")})

    output_filename = f"output_{i+1}.txt"

    if os.path.exists(output_filename):
      print(f"Warning: File {output_filename} already exists, skipping.")
      continue

    try:
      with open(output_filename, 'w') as f:
        f.write(processed_template)
      print(f"Invitation for {attendee['name']} generated successfully!")
    except Exception as e:
      print(f"Error writing to file {output_filename}: {e}")

with open('template.txt', 'r') as file:
  template_content = file.read()

attendees = [
  {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
  {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
  {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
]

generate_invitations(template_content, attendees)