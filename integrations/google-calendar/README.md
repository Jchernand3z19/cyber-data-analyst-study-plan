# Google Calendar integration (Python + GitHub Actions)

This integration manages study sessions directly through the Google Calendar API using Python and GitHub Actions. It does not use Google Apps Script.

## Schedule

- Monday-Saturday: 08:00-09:30
- Time zone: `America/Tegucigalpa`
- A popup reminder is planned for 10 minutes before each session.
- The workflow is currently manual-only. Its scheduled trigger is intentionally paused until calendar access is verified and the migration is approved for execution.

The sync script is prepared to replace only the two legacy recurring series marked `[SDA-WEEKDAYS]` and `[SDA-SATURDAY]`, then create three setup events and 90 individually titled sessions. Each event includes the objective, reading resource, practice, expected evidence and a 10-minute reminder. It uses stable markers to avoid duplicates and retains the original start date on retries.\n\n**Important:** the script deletes only those two program-owned recurring series. It does not touch unrelated events. The workflow's automatic schedule is paused; do not run it until the service-account sharing and permission have been confirmed.

## Study schedule\n\n- Time zone: `America/Tegucigalpa`.\n- Time: 08:00–09:30, Monday through Saturday.\n- Each of the 90 sessions will carry its own topic, learning objective, resource link and practice summary from [`curriculum/session-plan.md`](../../curriculum/session-plan.md).\n- The three environment-preparation sessions are separate from the 90 learning sessions.\n\n## One-time Google setup

1. Open the [Google Cloud Console](https://console.cloud.google.com/).
2. Create or select a project.
3. Enable **Google Calendar API** for that project.
4. Under IAM & Admin → Service Accounts, create a service account.
5. Create a JSON key for that service account and download it. Keep it private; do not commit it to GitHub or paste it into chat.
6. In Google Calendar settings, open the target calendar's **Share with specific people or groups** section.
7. Share that calendar with the service account's email address (ending in `iam.gserviceaccount.com`) and grant **Make changes to events**.
8. Copy the calendar ID from that calendar's settings. For the primary calendar, it is often your Google account email; for another calendar, use its displayed ID.

> A service account does not automatically have access to your personal calendar. Share the target calendar explicitly with its service-account email. Events will be created on that shared calendar.

## Configure GitHub Actions secrets

Open the repository's [Actions secrets settings](https://github.com/Jchernand3z19/security-data-analyst-learning-path/settings/secrets/actions) and verify these are already configured (never paste their values into chat):

- `GOOGLE_SERVICE_ACCOUNT_JSON`: the entire contents of the downloaded service-account JSON key file.
- `GOOGLE_CALENDAR_ID`: the calendar ID for the calendar shared with the service account.

Do not put either value in repository files, issues, commits, or chat.

## Test

Open the [Sync study calendar workflow](https://github.com/Jchernand3z19/security-data-analyst-learning-path/actions/workflows/sync-study-calendar.yml), choose **Run workflow**, and inspect the run logs. Run the workflow only after the migration logic has been reviewed and the calendar has been verified. A successful run must report created, updated and skipped items without printing credentials.

## Security

Keep the service-account JSON private and store it only as an Actions secret. Grant the service account access only to the calendar used for this plan. If the key is exposed, revoke it in Google Cloud Console and create a replacement.
