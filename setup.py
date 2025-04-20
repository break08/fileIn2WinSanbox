from cx_Freeze import setup, Executable

setup(
    name="fileIn2WinSandbox",
    version="1.0",
    description="Create .wsb to put folder into Windows Sanbox",
        options={
        "build_exe": {
            "include_msvcr": True
        }
    },
    executables=[Executable("filein2winsandbox.py", base="Win32GUI", icon ="icon/icon.ico")],
)
