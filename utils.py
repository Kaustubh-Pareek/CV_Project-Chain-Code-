EXTENSIONS_ALLOWED = ['jpeg', 'png', 'jpg']

def allowed_file(filename):
    if '.' not in filename:
        return False
    file_extension = filename.rsplit('.', 1)[1].lower()
    if file_extension in EXTENSIONS_ALLOWED:
        return True
    else:
        return False
    

def get_file_extension(file):
    filename = file.filename 
    file_extension = filename.rsplit('.', 1)[1].lower()
    return file_extension