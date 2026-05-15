import psutil

def get_heavy_processes(limit=5):
    """
    Scans the system and returns a list of the most resource-intensive processes.
    """
    print(f"🚀 Scanning system for heavy processes (Top-{limit})...")
    processes = []
    
    # Iterate over all active processes in the system
    for proc in psutil.process_iter(['pid', 'name', 'memory_percent']):
        try:
            # Try to fetch process info
            # Skip if we don't have permission or the process is dead
            processes.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
            
    # Sort the list by memory usage (descending)
    processes = sorted(processes, key=lambda x: x['memory_percent'] if x['memory_percent'] else 0, reverse=True)
    
    return processes[:limit]

if __name__ == "__main__":
    top_procs = get_heavy_processes(10)
    
    print("-" * 50)
    print(f"{'PID':<8} | {'Process Name':<20} | {'RAM %':<10}")
    print("-" * 50)
    
    for p in top_procs:
        # Format output nicely
        name = p['name'][:18] + '..' if len(p['name']) > 20 else p['name']
        print(f"{p['pid']:<8} | {name:<20} | {p['memory_percent']:.2f}%")
    
    print("-" * 50)
