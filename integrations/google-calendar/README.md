# Google Calendar integration (Python + GitHub Actions)

This integration creates recurring study sessions directly through the Google Calendar API. It does not use Google Apps Script.

## Schedule

- Monday-Friday: 19:00-20:00
- Saturday: 19:00-20:00
- Time zone: `America/Tegucigalpa`
- A popup reminder is set for 10 minutes before each session.
- The workflow can be run manually and also checks weekly on Sunday.

The sync searches upcoming events for a series marker before creating a recurring series, so repeated runs should not create duplicates.

## One-time Google setup

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

Open the repository's [Actions secrets settings](https://github.com/Jchernand3z19/cyber-data-analyst-study-plan/settings/secrets/actions) and add:

- `GOOGLE_SERVICE_ACCOUNT_JSON`: the entire contents of the downloaded service-account JSON key file.
- `GOOGLE_CALENDAR_ID`: the calendar ID for the calendar shared with the service account.

Do not put either value in repository files, issues, commits, or chat.

## Test

Open the [Sync study calendar workflow](https://github.com/Jchernand3z19/cyber-data-analyst-study-plan/actions/workflows/sync-study-calendar.yml), choose **Run workflow**, and inspect the run logs. A successful run prints whether each recurring series was created or already existed.

## Security

Keep the service-account JSON private and store it only as an Actions secret. Grant the service account access only to the calendar used for this plan. If the key is exposed, revoke it in Google Cloud Console and create a replacement.
