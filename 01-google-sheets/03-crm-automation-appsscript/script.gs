function onEdit(e) {
  if (!e) return;

  const sheet = e.source.getActiveSheet();
  const cell = e.range;

  // Працюємо лише з колонкою A (Ім’я) на аркуші clients_tracker
  if (sheet.getName() === "clients_tracker" && cell.getColumn() === 1 && cell.getRow() > 1) {
    const row = cell.getRow();

    Utilities.sleep(100); // Затримка, щоб формула в колонці B встигла порахуватись

    const name = sheet.getRange(row, 1).getValue();   // колонка A
    const status = sheet.getRange(row, 2).getValue(); // колонка B (підтягується з формули)

    if (!name || !status) return;

    const logSheet = e.source.getSheetByName("notes_log");
    logSheet.appendRow([new Date(), name, status]);
  }
}