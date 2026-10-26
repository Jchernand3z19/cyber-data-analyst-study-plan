/**
 * Google Apps Script endpoint for the Security Data Analyst study calendar.
 *
 * Deploy as a Web App executing as the calendar owner. Store a long random
 * token in Script Properties as STUDY_CALENDAR_TOKEN. Send the same token
 * from GitHub Actions as the STUDY_CALENDAR_TOKEN repository secret.
 */
function doPost(e) {
  const props = PropertiesService.getScriptProperties();
  const expected = props.getProperty('STUDY_CALENDAR_TOKEN');
  const supplied = e && e.parameter ? e.parameter.token : '';
  if (!expected || !supplied || !constantTimeEquals_(expected, supplied)) {
    return json_({ ok: false, error: 'Unauthorized' });
  }

  const calendar = CalendarApp.getDefaultCalendar();
  const title = 'Estudio Security Data Analyst';
  const description = [
    'Sesión de estudio de 60 minutos para el plan Security Data Analyst.',
    'Retoma el tema pendiente más antiguo del tracker de GitHub.',
    'Si no terminas, deja el tema pendiente; no saltes contenido.',
    'Reserva 10 min de repaso, 20 min de estudio, 20 min de práctica y 10 min de evidencia.',
    'Repositorio: https://github.com/Jchernand3z19/cyber-data-analyst-study-plan'
  ].join('\n');

  const tz = 'America/Tegucigalpa';
  const now = new Date();
  const startDate = new Date(now.getFullYear(), now.getMonth(), now.getDate());
  const endDate = new Date(startDate.getTime() + 400 * 24 * 60 * 60 * 1000);
  const existing = calendar.getEvents(startDate, endDate, { search: title });
  const hasWeekdaySeries = existing.some(ev =>
    ev.getTitle() === title && ev.isRecurringEvent() &&
    ev.getEventSeries().getDescription().indexOf('SDA-WEEKDAYS') >= 0
  );
  const hasSaturdaySeries = existing.some(ev =>
    ev.getTitle() === title && ev.isRecurringEvent() &&
    ev.getEventSeries().getDescription().indexOf('SDA-SATURDAY') >= 0
  );

  if (!hasWeekdaySeries) {
    const start = nextOccurrence_(1, 19, 0); // Monday-Friday
    const end = new Date(start.getTime() + 60 * 60 * 1000);
    const recurrence = CalendarApp.newRecurrence().addWeeklyRule().onlyOnWeekdays();
    calendar.createEventSeries(title, start, end, recurrence, {
      description: description + '\nSeries key: SDA-WEEKDAYS',
      location: 'Sesión personal de estudio'
    });
  }

  if (!hasSaturdaySeries) {
    const start = nextOccurrence_(6, 19, 0); // Saturday
    const end = new Date(start.getTime() + 60 * 60 * 1000);
    const recurrence = CalendarApp.newRecurrence().addWeeklyRule()
      .onlyOnDays([CalendarApp.Weekday.SATURDAY]);
    calendar.createEventSeries(title, start, end, recurrence, {
      description: description + '\nSeries key: SDA-SATURDAY',
      location: 'Sesión personal de estudio'
    });
  }

  return json_({
    ok: true,
    calendar: 'primary',
    timezone: tz,
    schedule: 'Monday-Saturday 19:00-20:00',
    weekdaySeriesCreated: !hasWeekdaySeries,
    saturdaySeriesCreated: !hasSaturdaySeries
  });
}

function nextOccurrence_(targetDay, hour, minute) {
  const now = new Date();
  const d = new Date(now.getFullYear(), now.getMonth(), now.getDate(), hour, minute, 0);
  const currentDay = d.getDay();
  let delta = (targetDay - currentDay + 7) % 7;
  if (delta === 0 && d.getTime() <= now.getTime()) delta = 7;
  d.setDate(d.getDate() + delta);
  return d;
}

function constantTimeEquals_(a, b) {
  if (a.length !== b.length) return false;
  let result = 0;
  for (let i = 0; i < a.length; i++) result |= a.charCodeAt(i) ^ b.charCodeAt(i);
  return result === 0;
}

function json_(obj) {
  return ContentService.createTextOutput(JSON.stringify(obj))
    .setMimeType(ContentService.MimeType.JSON);
}
