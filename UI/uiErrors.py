from tkinter import messagebox

def invalidSpeakerName(name):
    messagebox.askretrycancel('Invalid name', 'The name %s is not correct!' % name)

def invalidSpeakerFamilyName(familyName):
    messagebox.askretrycancel('Invalid family name', 'The family name %s is not correct!' % familyName)

def failedDelete(file_path, e):
    messagebox.askretrycancel('Delete', 'Failed to delete %s. Reason: %s' % (file_path, e))
