import smtplib
import csv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_automated_emails(csv_filename="file.csv"):
    """
    Reads a CSV file and sends personalized emails.
    Note: This script simulates sending. To actually send, uncomment the server lines
    and provide valid credentials.
    """
    
    # --- Configuration ---
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "your_email@gmail.com"
    sender_password = "your_app_password" # Use App Password, not login password
    # ---------------------

    try:
        # 1. Connect to the SMTP Server
        # In a real scenario, you would uncomment these lines:
        # server = smtplib.SMTP(smtp_server, smtp_port)
        # server.starttls() # Secure the connection
        # server.login(sender_email, sender_password)
        print(f"--- Connecting to {smtp_server} (Simulated) ---")

        # 2. Read the CSV file
        with open(csv_filename, mode='r') as f:
            # DictReader allows accessing columns by name (e.g., row['Name'])
            reader = csv.DictReader(f)
            
            for row in reader:
                name = row.get('Name')
                department = row.get('Department')
                
                # Since file.csv doesn't have an email column, we generate a fake one
                receiver_email = f"{name.lower()}@company.com"

                # 3. Create the email content
                subject = f"Monthly Update for {department}"
                body = f"Hello {name},\n\nThis is a reminder for the {department} team to submit their reports.\n\nBest,\nAutomated System"

                # 4. Setup the MIME object (Structure of the email)
                msg = MIMEMultipart()
                msg['From'] = sender_email
                msg['To'] = receiver_email
                msg['Subject'] = subject
                msg.attach(MIMEText(body, 'plain'))

                # 5. Send the email
                # server.send_message(msg)
                
                print(f"Email sent to: {name} <{receiver_email}> | Subject: {subject}")

        # server.quit()
        print("--- All emails processed successfully ---")

    except FileNotFoundError:
        print(f"Error: The file '{csv_filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    send_automated_emails()