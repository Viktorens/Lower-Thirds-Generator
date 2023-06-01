from tkinter import messagebox

class Error:
    def invalidSpeakerName(self):
        return messagebox.askretrycancel('Invalid input', 'Check if name or family name is correct!')

    def failedDelete(self, file_path, e):
        return messagebox.askretrycancel('Delete Output Folder', 'Failed to delete %s. Reason: %s' % (file_path, e))
