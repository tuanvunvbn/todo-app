import zipfile

def extract_archive(sourcefile, dest_folder):
    with zipfile.ZipFile(sourcefile, "r") as archive:
        archive.extractall(dest_folder)