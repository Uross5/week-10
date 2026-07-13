import psutil

memory_info=psutil.virtual_memory()

memory=int(memory_info[0])
print(memory)
gig_memory=memory/(1024**3)
print(f"{gig_memory:.2f}")