# .\write_paths.py
import os


COMMENTS = {
    '.py': '#',
    '.js': '//',
    '.ts': '//',
}


def add_comment_to_files(root_dir, format='.py', ignore_dirs=None):
    if ignore_dirs is None:
        ignore_dirs = []
    comment = COMMENTS[format]
    for subdir, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if d not in ignore_dirs]
        if not dirs:
            continue
        for file in files:
            if file.endswith(format):
                file_path = os.path.join(subdir, file)
                with open(file_path, 'r+') as f:
                    content = f.readlines()
                    if not content:
                        continue
                    print(file_path, end="."*(70 - len(file_path[:-1])))
                    first_line = content[0]
                    f.seek(0, 0)
                    if not first_line.endswith(f"{format}\n"):
                        f.write(f"{comment} {file_path}\n{''.join(content)}")
                        print('DONE')
                    elif not first_line.startswith(f"{comment} {file_path}"):
                        f.write(
                            f"{comment} {file_path}\n{''.join(content[1:])}")
                        print('UPDATED')
                    else:
                        print('ALREADY')


ignore_dirs = ('migrations')
add_comment_to_files(root_dir='.',
                     ignore_dirs=ignore_dirs)
