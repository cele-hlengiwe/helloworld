# Build python script into a stand-alone exe
- uses: Nuitka/Nuitka-Action@main
  with:
    nuitka-version: main
    script-name: hello_world.py

C:\> hello_world.exe
hello world!
