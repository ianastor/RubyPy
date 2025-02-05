import asyncio
from core.config import CONFIG

async def run_nmap(target, options="-sV"):
    nmap_path = CONFIG.get("nmap_path", "nmap")
    process = await asyncio.create_subprocess_exec(
        nmap_path, target, options,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    if stderr:
        print(f"[!] Nmap error: {stderr.decode()}")
    return stdout.decode()

# Example function usage within a plugin or adapter wrapper
if __name__ == "__main__":
    target_ip = "127.0.0.1"
    output = asyncio.run(run_nmap(target_ip))
    print(output)