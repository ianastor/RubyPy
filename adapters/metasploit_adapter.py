import asyncio
from core.config import CONFIG

async def run_metasploit(command):
    metasploit_path = CONFIG.get("metasploit_path", "msfconsole")
    # This is a simplified example. In a real adapter, you may need to handle sessions, authentication, etc.
    process = await asyncio.create_subprocess_exec(
        metasploit_path, "-q", "-x", command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    if stderr:
        print(f"[!] Metasploit error: {stderr.decode()}")
    return stdout.decode()

# For testing purposes
if __name__ == "__main__":
    command = "help"
    output = asyncio.run(run_metasploit(command))
    print(output)