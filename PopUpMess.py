from PyQt5.QtWidgets import QMessageBox


def PopUpMessage(self, error_message):
    QMessageBox.critical(self, "Error", error_message)
