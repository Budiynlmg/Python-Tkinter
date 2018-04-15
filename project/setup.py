from cx_Freeze import setup, Executable

target = Executable(
    script="bar.py",
    base="Win32GUI",
    compress=False,
    copyDependentFiles=True,
    appendScriptToExe=True,
    appendScriptToLibrary=False,
    icon="jo.ico"
    )

setup(
    name="workshop",
    version="1.0",
    description="stt pelita bangsa",
    author="sas",
    options={"build_exe": {"packages":["tkinter"]}},
    executables=[target]
    )
