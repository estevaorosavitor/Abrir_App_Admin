import ctypes
from ctypes import wintypes

# Deixa o programa chamado oculto, rodando em segundo plano
def configurar_janela():
    hwnd = ctypes.windll.kernel32.GetConsoleWindow()
    ctypes.windll.user32.ShowWindow(hwnd, 0)
    style = ctypes.windll.user32.GetWindowLongW(hwnd, -16)
    style &= ~0xC0000  # WS_MINIMIZEBOX | WS_MAXIMIZEBOX
    style &= ~0x80000  # WS_SYSMENU
    ctypes.windll.user32.SetWindowLongW(hwnd, -16, style)  # Define o novo estilo

def abrirProgramaComCredenciais(user, password, program):
    # Estrutura de dados para as credenciais
    class PROCESS_INFORMATION(ctypes.Structure):
        _fields_ = [("hProcess", wintypes.HANDLE),
                    ("hThread", wintypes.HANDLE),
                    ("dwProcessId", wintypes.DWORD),
                    ("dwThreadId", wintypes.DWORD)]

    # Estrutura de dados para as informações de inicialização
    class STARTUPINFO(ctypes.Structure):
        _fields_ = [("cb", wintypes.DWORD),
                    ("lpReserved", wintypes.LPWSTR),
                    ("lpDesktop", wintypes.LPWSTR),
                    ("lpTitle", wintypes.LPWSTR),
                    ("dwX", wintypes.DWORD),
                    ("dwY", wintypes.DWORD),
                    ("dwXSize", wintypes.DWORD),
                    ("dwYSize", wintypes.DWORD),
                    ("dwXCountChars", wintypes.DWORD),
                    ("dwYCountChars", wintypes.DWORD),
                    ("dwFillAttribute", wintypes.DWORD),
                    ("dwFlags", wintypes.DWORD),
                    ("wShowWindow", wintypes.WORD),
                    ("cbReserved2", wintypes.WORD),
                    ("lpReserved2", wintypes.LPBYTE),
                    ("hStdInput", wintypes.HANDLE),
                    ("hStdOutput", wintypes.HANDLE),
                    ("hStdError", wintypes.HANDLE)]

    pi = PROCESS_INFORMATION()
    si = STARTUPINFO()
    si.cb = ctypes.sizeof(STARTUPINFO)

    ctypes.windll.advapi32.CreateProcessWithLogonW(
        ctypes.wintypes.LPWSTR(user),
        None,
        ctypes.wintypes.LPWSTR(password),
        0,  # Logon flags
        None,
        ctypes.wintypes.LPWSTR(program),
        0,  # Creation flags
        None,
        None,
        ctypes.byref(si),
        ctypes.byref(pi)
    )

if __name__ == "__main__":
    user = "user" # Usuário administrador local
    password = "admin" # Senha do usuário admin local
    program = r"C:\Program Files\VideoLAN\VLC\vlc.exe" # Substituir pelo caminho do app.

    configurar_janela()
    abrirProgramaComCredenciais(user, password, program)